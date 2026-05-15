#!/usr/bin/env node
/**
 * Extract the `topics = [...]` JS array literal from agent_rl_papers.html
 * and dump it as JSON for the Python importer.
 *
 *   node scripts/extract_archive.js <path-to-html> [out.json]
 *
 * The HTML embeds the full archive as a plain JS object literal — no SPA
 * runtime needed. We grab the source range and eval it in this sandbox.
 */
const fs = require("fs");
const path = require("path");

const srcPath = process.argv[2];
const outPath = process.argv[3] || ".cache/archive_topics.json";
if (!srcPath) {
  console.error("usage: node extract_archive.js <html> [out.json]");
  process.exit(2);
}

const html = fs.readFileSync(srcPath, "utf8");

// Capture `const topics = [` ... matching `];` at the corresponding depth.
// The literal includes nested objects/strings, so we can't lazy-regex it.
// Walk the braces from the opening `[` instead.
const start = html.indexOf("const topics");
if (start < 0) {
  console.error("could not find `const topics` in source");
  process.exit(3);
}
const bracketStart = html.indexOf("[", start);
if (bracketStart < 0) {
  console.error("no opening `[` after `const topics`");
  process.exit(3);
}

let depth = 0;
let i = bracketStart;
let inStr = null;     // "'" | '"' | "`"
let escape = false;
let inLineComment = false;
let inBlockComment = false;

for (; i < html.length; i++) {
  const c = html[i];
  const n = html[i + 1];
  if (escape) { escape = false; continue; }
  if (inLineComment) {
    if (c === "\n") inLineComment = false;
    continue;
  }
  if (inBlockComment) {
    if (c === "*" && n === "/") { inBlockComment = false; i++; }
    continue;
  }
  if (inStr) {
    if (c === "\\") escape = true;
    else if (c === inStr) inStr = null;
    continue;
  }
  if (c === "/" && n === "/") { inLineComment = true; i++; continue; }
  if (c === "/" && n === "*") { inBlockComment = true; i++; continue; }
  if (c === '"' || c === "'" || c === "`") { inStr = c; continue; }
  if (c === "[" || c === "{") depth++;
  else if (c === "]" || c === "}") {
    depth--;
    if (depth === 0) { i++; break; }
  }
}

const literal = html.slice(bracketStart, i);
let topics;
try {
  // eslint-disable-next-line no-eval
  topics = eval(`(${literal})`);
} catch (e) {
  console.error("eval failed:", e.message);
  process.exit(4);
}

if (!Array.isArray(topics)) {
  console.error("extracted value is not an array");
  process.exit(5);
}

fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(topics, null, 2), "utf8");

const totalPapers = topics.reduce((s, t) => s + (t.papers || []).length, 0);
console.log(`extracted ${topics.length} topics, ${totalPapers} papers → ${outPath}`);
for (const t of topics) {
  console.log(`  [${t.id}] ${t.name}: ${(t.papers || []).length} papers`);
}
