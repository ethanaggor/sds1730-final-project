import { readdir, readFile, stat } from "fs/promises";
import { join } from "path";

const RUNS_DIR = join(import.meta.dir, "traces", "runs");
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

async function readEvents(runId: string): Promise<object[]> {
  try {
    const raw = await readFile(join(RUNS_DIR, runId, "events.jsonl"), "utf-8");
    const events: object[] = [];
    for (const line of raw.trim().split("\n")) {
      if (line) try { events.push(JSON.parse(line)); } catch {}
    }
    return events;
  } catch {
    return [];
  }
}

async function readManifest(runId: string): Promise<object | null> {
  try {
    return JSON.parse(await readFile(join(RUNS_DIR, runId, "manifest.json"), "utf-8"));
  } catch {
    return null;
  }
}

async function buildRunMeta(id: string) {
  const events = await readEvents(id);
  const start = events.find((e: any) => e.type === "optimization_start") as any;
  const end = events.find((e: any) => e.type === "optimization_complete") as any;
  const manifest = await readManifest(id);
  const costSource = manifest ?? end ?? (events.filter((e: any) => e.type === "stats").at(-1) as any);
  return {
    id,
    status: end || manifest ? "complete" : "running",
    startedAt: start?.ts ?? null,
    profile: start?.profile ?? null,
    student: start?.student_model ?? null,
    teacher: start?.teacher_model ?? null,
    sub: start?.sub_model ?? null,
    reasoningEffort: start?.reasoning_effort ?? null,
    evalCount: events.filter((e: any) => e.type === "eval").length,
    costUsd: costSource?.total_cost_usd ?? null,
  };
}

async function resolveRunId(url: URL): Promise<string | null> {
  return url.searchParams.get("run") ?? (await getRunDirs())[0] ?? null;
}

Bun.serve({
  port: PORT,
  async fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === "/" || url.pathname === "/index.html") {
      return new Response(Bun.file(join(import.meta.dir, "index.html")));
    }

    if (url.pathname === "/api/runs") {
      const dirs = await getRunDirs();
      return Response.json(await Promise.all(dirs.map(buildRunMeta)));
    }

    if (url.pathname === "/api/events") {
      const id = await resolveRunId(url);
      return Response.json(id ? await readEvents(id) : []);
    }

    if (url.pathname === "/api/manifest") {
      const id = await resolveRunId(url);
      if (!id) return new Response("null", { status: 404 });
      const manifest = await readManifest(id);
      return manifest ? Response.json(manifest) : new Response("null", { status: 404 });
    }

    if (url.pathname === "/api/stream") {
      const stream = new ReadableStream({
        async start(controller) {
          const encoder = new TextEncoder();
          const eventCounts = new Map<string, number>();
          const lastManifestJson = new Map<string, string>();

          const send = (data: string) => {
            if (req.signal.aborted) return;
            controller.enqueue(encoder.encode(`data: ${data}\n\n`));
          };

          send(JSON.stringify({ type: "connected" }));

          for (const runId of await getRunDirs()) {
            eventCounts.set(runId, (await readEvents(runId)).length);
            const manifest = await readManifest(runId);
            if (manifest) lastManifestJson.set(runId, JSON.stringify(manifest));
          }

          const completedRuns = new Set(lastManifestJson.keys());

          const interval = setInterval(async () => {
            if (req.signal.aborted) return;
            try {
              for (const runId of await getRunDirs()) {
                if (completedRuns.has(runId)) continue;

                const events = await readEvents(runId);
                const lastCount = eventCounts.get(runId) ?? 0;
                if (events.length > lastCount) {
                  for (const ev of events.slice(lastCount))
                    send(JSON.stringify({ ...ev, _run: runId } as any));
                  eventCounts.set(runId, events.length);
                }

                const manifest = await readManifest(runId);
                if (manifest) {
                  const json = JSON.stringify(manifest);
                  if (json !== lastManifestJson.get(runId)) {
                    lastManifestJson.set(runId, json);
                    send(JSON.stringify({ type: "manifest", _run: runId, ...manifest } as any));
                    completedRuns.add(runId);
                  }
                }
              }
            } catch {}
          }, POLL_INTERVAL);

          req.signal.addEventListener("abort", () => {
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
