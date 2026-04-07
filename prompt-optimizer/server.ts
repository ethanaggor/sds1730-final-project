import { watch } from "fs";
import { readFile } from "fs/promises";
import { join } from "path";

const TRACES_DIR = join(import.meta.dir, "traces");
const PORT = 3456;

async function readEvents(): Promise<object[]> {
  try {
    const raw = await readFile(join(TRACES_DIR, "events.jsonl"), "utf-8");
    return raw
      .trim()
      .split("\n")
      .filter(Boolean)
      .map((line) => JSON.parse(line));
  } catch {
    return [];
  }
}

async function readManifest(): Promise<object | null> {
  try {
    const raw = await readFile(join(TRACES_DIR, "manifest.json"), "utf-8");
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

async function readGepaLogs(): Promise<object[]> {
  // GEPA writes its own log files to traces/; collect any JSON files it creates
  const { readdir } = await import("fs/promises");
  const logs: object[] = [];
  try {
    const files = await readdir(TRACES_DIR);
    for (const f of files) {
      if (f.endsWith(".json") && f !== "manifest.json") {
        const raw = await readFile(join(TRACES_DIR, f), "utf-8");
        try {
          logs.push({ file: f, data: JSON.parse(raw) });
        } catch {
          // skip non-JSON
        }
      }
    }
  } catch {
    // traces dir may not exist yet
  }
  return logs;
}

const server = Bun.serve({
  port: PORT,
  async fetch(req) {
    const url = new URL(req.url);

    if (url.pathname === "/" || url.pathname === "/index.html") {
      return new Response(Bun.file(join(import.meta.dir, "index.html")));
    }

    if (url.pathname === "/api/events") {
      return Response.json(await readEvents());
    }

    if (url.pathname === "/api/manifest") {
      const manifest = await readManifest();
      return manifest
        ? Response.json(manifest)
        : new Response("null", { status: 404 });
    }

    if (url.pathname === "/api/logs") {
      return Response.json(await readGepaLogs());
    }

    if (url.pathname === "/api/stream") {
      // SSE endpoint: watches traces/ for changes
      const stream = new ReadableStream({
        start(controller) {
          const encoder = new TextEncoder();
          let lastSize = 0;

          const send = (data: string) => {
            controller.enqueue(encoder.encode(`data: ${data}\n\n`));
          };

          // Initial ping
          send(JSON.stringify({ type: "connected" }));

          const watcher = watch(TRACES_DIR, async (eventType, filename) => {
            if (filename === "events.jsonl") {
              const events = await readEvents();
              if (events.length > lastSize) {
                const newEvents = events.slice(lastSize);
                lastSize = events.length;
                for (const ev of newEvents) {
                  send(JSON.stringify(ev));
                }
              }
            } else if (filename === "manifest.json") {
              const manifest = await readManifest();
              if (manifest) send(JSON.stringify({ type: "manifest", ...manifest }));
            }
          });

          req.signal.addEventListener("abort", () => {
            watcher.close();
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
