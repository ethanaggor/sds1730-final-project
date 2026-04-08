import { readdir, readFile, stat } from "fs/promises";
import { join } from "path";

const TRACES_DIR = join(import.meta.dir, "traces");
const RUNS_DIR = join(TRACES_DIR, "runs");
const PORT = 3456;
const POLL_INTERVAL = 2000;

async function getRunDirs(): Promise<string[]> {
  try {
    const entries = await readdir(RUNS_DIR);
    const dirs: string[] = [];
    for (const e of entries) {
      const s = await stat(join(RUNS_DIR, e));
      if (s.isDirectory()) dirs.push(e);
    }
    return dirs.sort().reverse();
  } catch {
    return [];
  }
}

async function getLatestRunId(): Promise<string | null> {
  const dirs = await getRunDirs();
  return dirs[0] ?? null;
}

function runDir(id: string): string {
  return join(RUNS_DIR, id);
}

async function readEvents(id: string): Promise<object[]> {
  try {
    const raw = await readFile(join(runDir(id), "events.jsonl"), "utf-8");
    const events: object[] = [];
    for (const line of raw.trim().split("\n")) {
      if (!line) continue;
      try { events.push(JSON.parse(line)); } catch {}
    }
    return events;
  } catch {
    return [];
  }
}

async function readManifest(id: string): Promise<object | null> {
  try {
    const raw = await readFile(join(runDir(id), "manifest.json"), "utf-8");
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

async function buildRunMeta(id: string) {
  const events = await readEvents(id);
  const start = events.find((e: any) => e.type === "optimization_start") as any;
  const end = events.find((e: any) => e.type === "optimization_complete") as any;
  const manifest = await readManifest(id);
  const latestStats = events.filter((e: any) => e.type === "stats").at(-1) as any;
  const costSource = manifest ?? end ?? latestStats;
  return {
    id,
    status: end || manifest ? "complete" : "running",
    startedAt: start?.ts ?? null,
    model: start?.student_model ?? null,
    evalCount: events.filter((e: any) => e.type === "eval").length,
    costUsd: costSource?.total_cost_usd ?? null,
  };
}

async function resolveRunId(url: URL): Promise<string | null> {
  const param = url.searchParams.get("run");
  if (param) return param;
  return getLatestRunId();
}

const server = Bun.serve({
  port: PORT,
  async fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === "/" || url.pathname === "/index.html") {
      return new Response(Bun.file(join(import.meta.dir, "index.html")));
    }

    if (url.pathname === "/api/runs") {
      const dirs = await getRunDirs();
      const runs = await Promise.all(dirs.map(buildRunMeta));
      return Response.json(runs);
    }

    if (url.pathname === "/api/events") {
      const id = await resolveRunId(url);
      if (!id) return Response.json([]);
      return Response.json(await readEvents(id));
    }

    if (url.pathname === "/api/manifest") {
      const id = await resolveRunId(url);
      if (!id) return new Response("null", { status: 404 });
      const manifest = await readManifest(id);
      return manifest
        ? Response.json(manifest)
        : new Response("null", { status: 404 });
    }

    if (url.pathname === "/api/stream") {
      const stream = new ReadableStream({
        start(controller) {
          const encoder = new TextEncoder();
          const eventCounts = new Map<string, number>();
          let lastManifestJson = new Map<string, string>();
          let lastRunCount = 0;
          let aborted = false;
          let seeded = false;

          const send = (data: string) => {
            if (aborted) return;
            controller.enqueue(encoder.encode(`data: ${data}\n\n`));
          };

          send(JSON.stringify({ type: "connected" }));

          // Seed counts, then start polling
          const seed = async () => {
            const dirs = await getRunDirs();
            lastRunCount = dirs.length;
            for (const runId of dirs) {
              const events = await readEvents(runId);
              eventCounts.set(runId, events.length);
              const manifest = await readManifest(runId);
              if (manifest) lastManifestJson.set(runId, JSON.stringify(manifest));
            }
            seeded = true;
          };
          seed();

          const poll = async () => {
            if (!seeded) return;
            if (aborted) return;
            try {
              const dirs = await getRunDirs();

              // Detect new run directories
              if (dirs.length > lastRunCount) {
                lastRunCount = dirs.length;
              }

              for (const runId of dirs) {
                // Check for new events
                const events = await readEvents(runId);
                const lastCount = eventCounts.get(runId) ?? 0;
                if (events.length > lastCount) {
                  for (const ev of events.slice(lastCount)) {
                    send(JSON.stringify({ ...ev, _run: runId } as any));
                  }
                  eventCounts.set(runId, events.length);
                }

                // Check for manifest changes
                const manifest = await readManifest(runId);
                if (manifest) {
                  const json = JSON.stringify(manifest);
                  if (json !== lastManifestJson.get(runId)) {
                    lastManifestJson.set(runId, json);
                    send(JSON.stringify({ type: "manifest", _run: runId, ...manifest } as any));
                  }
                }
              }
            } catch {}
          };

          const interval = setInterval(poll, POLL_INTERVAL);

          req.signal.addEventListener("abort", () => {
            aborted = true;
            clearInterval(interval);
            controller.close();
          });
        },
      });

      return new Response(stream, {
        headers: {
          "Content-Type": "text/event-stream",
          "Cache-Control": "no-cache",
          Connection: "keep-alive",
        },
      });
    }

    return new Response("Not found", { status: 404 });
  },
});

console.log(`GEPA dashboard running at http://localhost:${PORT}`);
