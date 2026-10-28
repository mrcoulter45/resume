# Architecture

Authoritative data is UTF-8 JSON plus original evidence. JSON gives strict schemas,
readable Git diffs and structured metadata without parser dependencies. Narratives
remain prose fields and Markdown. Search reads records directly; no database is needed.

A project records scope; accomplishments capture distinct technical challenges,
actions and outcomes; experience records establish employment; skill records link
technologies to demonstrated contexts. Education, leadership, additional experience
and identity share the same record contract. Every independently claimable fact has
a stable ID, status, visibility and evidence. References use `record-id#fact-id`.
Do not cite a navigation summary as if it were independently evidenced.

Record metadata includes title, context, role, organization, date precision,
technologies, competencies, tags, relationships and notes. Preserve challenges,
personal actions, engineering complexity, results and metric context in specific
facts. Separate statements whose status, evidence or sensitivity differs.

`schemas/*.schema.json` documents the contracts. The standard-library validator
implements the exact subset used there (listed in `schema_check`) plus source hash,
relationship, date and locator checks. Unknown fields fail. Extend contracts and
code together; increment schema versions for incompatible changes and document the
migration. Do not relax checks to conceal incomplete data.

The source registry preserves original paths, identity hashes, origin, revisions
and extraction relationships. Existing sources stay in place to preserve links;
new imports use `sources/originals/<source-id>/`. Only the previous root README moved
to an identical immutable copy, with explicit legacy reference mapping.

Applications store captured jobs, requirements, authored text/coverage decisions,
résumé Markdown, match analysis, per-line claims and build manifests. The manifest
fingerprints records, sources, contracts, tooling, job and selection. Explicit
preparation dates make builds deterministic. `audit` regenerates in memory and
detects drift. Use the corresponding Git revision for historical reproduction;
registry or tooling changes intentionally invalidate earlier manifest snapshots.

Search ranks eligible fact text using weighted token overlap, evidence, and visible
heuristic ownership/impact/recency signals. Those signals are not measurements or
proof of semantic coverage. Alias normalization covers equivalent spellings, not
equivalent qualifications. Unknown work dates receive no recency bonus; ongoing
work uses its evidence as-of date. Agents handle transferable experience and scope.

`index` exports eligible facts, stable references and evidence as disposable JSONL
under ignored `build/`. A future local semantic index can consume it; authoritative
records remain file-based. Rebuild caches when source/record hashes change. No
specialized infrastructure is necessary, and no external model is called.
