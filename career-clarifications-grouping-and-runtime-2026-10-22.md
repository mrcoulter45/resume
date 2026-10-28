# Career clarification: project grouping, backend fallback and Python runtimes

Recorded October 22, 2026 from Michael Coulter's direct wording and explanation in the resume chat. This supplements the earlier career sources without rewriting them. Michael requested these refinements to the Netflix resume and asked for related accomplishments to be grouped with indentation.

## 1. Shared coding-agent harness and accompanying workbench

- The shared coding-agent harness is used by several Arm engineers and combines agents, tools, skills and memory with shared and project-specific knowledge and conventions.
- Michael described building many agentic tools and skills, notably $repair-jenkins: a Codex skill teammates use to iteratively fix cluster Playwright failures, verify three consecutive passes and return patches for manual review.
- The Rust/Tauri 2 workbench accompanies that harness. It provides repository, build and process control, a React/TypeScript UI, a shared desktop/CLI core and bounded asynchronous Git inspection.
- The repair-skill accomplishment and accompanying workbench should be indented under the main harness accomplishment. The supplied AI-System-resume.md provides the broader tools/skills and workbench implementation evidence.

## 2. ia-mcp and Python-version compatibility

- Michael's preferred main accomplishment describes ia-mcp as an internal Python Model Context Protocol (MCP) interface used by several engineers, translating interconnect intent into backend API calls with typed plans, checkpoints, semantic validation and backend fallback.
- He described verified agent-led configuration creation and import/modify/diagnose/backend fallback, and requested that this appear as a supporting accomplishment under ia-mcp.
- The Interconnect Architect Python backend must be compliant with both Python 3.13 and Python 3.7, so ia-mcp needed to support both Python versions.
- The authenticated Python helper/sidecar enables ia-mcp to use legacy configuration-engine Python versions when needed. It restricts APIs/file paths and verifies the backend code's origin, as also described in the earlier interconnect analysis.
- The Python runtime compatibility accomplishment should be indented under ia-mcp, together with the verification accomplishment.

## 3. Editorial and evidence boundaries

This clarification establishes the accompanying relationship, preferred grouping, fallback emphasis and exact required Python versions. It supplies no new adoption counts, performance figures, availability targets or broad agent-success rates. Backend fallback, runtime compatibility and rollback are different mechanisms; do not relabel the earlier rollback hash result as a fallback benchmark. The previously documented two scoped evaluations, 92 live acceptance checks and exact rollback-hash restoration remain historical evidence in the master inventory, even though Michael's new preferred resume wording omits those details. Earlier source files remain intact.
