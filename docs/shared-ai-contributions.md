# Shared-AI achievement and technical narrative library

Application wording for Michael Coulter, reviewed 2026-10-29. This library augments
the granular records and the preserved `AI-System-resume.md` analysis. Read
[research scope, evolution and limits](shared-ai-research.md) and each fact’s notes
before selecting copy. Options are alternatives, not a list to paste into one
résumé. Use the existing Arm formal title; functional ownership does not establish
a promotion. Public phrasing below avoids private paths, hosts and product codenames.

References pair a record ID with a fact ID to identify the normalized facts and their
immutable evidence. Short options favor résumé density; expanded options and
technical narratives support interviews, portfolios and job-specific synthesis.
Mechanism wording describes implemented code, including captured working-tree
work; do not turn it into a new deployment or successful-execution assertion.

## Platform architecture and AI engineering

### 1. Shared engineering harness

**Concise:** Designed and built a modular Codex engineering harness used by several
engineers, combining reusable tools, project-specific workflows and persistent
engineering knowledge.

**Expanded:** Built a shared coding-agent platform that separates reusable
workspace, cluster and release infrastructure from project-owned runtimes, with
discoverable capabilities and source-verified engineering context across four
declared project integrations.

**Technical narrative:** Repeated engineering work spans repositories, runtime
environments and tool interfaces. The architecture makes ownership explicit:
shared infrastructure handles discovery and environment/tool operations, while
project packs own domain contracts and product runtimes. Skills and knowledge
guide Codex’s existing execution loop. Root scheduler/agent/evaluation placeholders
are excluded from delivered functionality; four manifests do not imply four fully
implemented products.

Evidence: `project-ai-harness#design-adoption`, `#modular-boundaries`, `#codex-scope`;
read private `#owner-attribution-scope` and `#placeholder-boundary`.

### 2. Deterministic capability discovery

**Concise:** Built deterministic capability catalogs with SHA-256 freshness checks
and rollback-safe skill registration for shared engineering tools.

**Expanded:** Implemented coordinated human/machine capability catalogs with
metadata/prerequisite validation, alias resolution and path/permission/content
fingerprints; added preflight and rollback to protect existing skill registrations.

**Technical narrative:** Documentation, invocation metadata and installed links
can drift independently. The implementation validates structured contracts,
compares generated JSON/Markdown and distinguishes discovery from registration or
live health. A Ruby/Psych fallback supports YAML discovery when PyYAML is absent.
Transactional link installation refuses unrelated paths and removes newly created
links if a later step fails.

Evidence: `accomp-ai-capability-discovery#catalogs`, `#freshness`, `#registration`,
`#metadata-and-fallback`.

### 3. Typed MCP integration and ownership consolidation

**Concise:** Implemented a typed Python MCP host with dynamic capability
registration, compatibility checks and traceable tool execution.

**Expanded:** Built a Pydantic-based MCP runtime adapting SDK interfaces and
model-derived call signatures, routing synchronous/asynchronous handlers through
descriptor-controlled approval and structured request/evidence traces.

**Technical narrative:** The historical host integrates tools, resources and
prompts through capability-pack manifests and runtime compatibility contracts.
It handles SDK constructor differences and records success, blocked approval and
failure states. Later consolidation moves the runtime to product ownership,
avoiding two competing implementations. The workflow bridge and general scheduler
remain procedural/planned boundaries; approval fields do not authenticate a human.

Evidence: `accomp-ai-historical-mcp-host#typed-host`, `#controls`,
`#sdk-and-trace-adaptation`; `project-ai-harness#ownership-consolidation`.

### 4. Durable engineering context

**Concise:** Built source-verified engineering memory and reusable agent workflows
that preserve decisions, technical lessons and authoritative subsystem guidance.

**Expanded:** Designed knowledge capture that follows complete available task
history, recognizes superseded decisions, validates lessons against owning sources
and routes reusable guidance while excluding secrets and transient artifacts.

**Technical narrative:** The contribution includes operational capture/retrieval
and authored standards for source ownership, GUI/RTL/configuration boundaries,
testing, review and logical commits. It also documents bounded read-only
Jira/Confluence retrieval. These are mechanisms and engineering practices around
Codex; they do not establish a distributed memory service or authorship of those
external connectors and product algorithms.

Evidence: `lead-ai-engineering-memory#dynamic-memory`, `#source-verification`,
`#standards`, `#integration-contracts`, `#domain-context-curation`.

## Concurrent development and native tooling

### 5. Isolated workspace lifecycle

**Concise:** Built manifest-driven workspaces isolating ports, caches, editor state
and runtime data for parallel engineering sessions.

**Expanded:** Automated checkout/task binding, guarded branch preparation,
project-specific session environments and archive/restore workflows, separating
durable task context from disposable runtime state.

**Technical narrative:** Sharing a checkout or browser/cache/port configuration
can make concurrent sessions interfere. Slot-derived settings isolate these
resources. Git guards reject unsafe ahead/diverged reconciliation; stale-binding
warnings and refusal to archive bound tasks protect task lifecycle. Metadata
archival is not a checkout snapshot or an all-or-nothing filesystem transaction.

Evidence: `accomp-ai-workspace-isolation#manager`, `#isolation`, `#git-guards`,
`#task-lifecycle`.

### 6. Concurrent checkout allocation

**Concise:** Engineered concurrency-safe checkout allocation using atomic locks,
tokenized leases and ownership-aware recovery.

**Expanded:** Made reservations visible to ordinary Git cleanliness checks and
paired them with refreshable lease records, preserving ambiguous state and limiting
failed-creation cleanup to allocator-owned resources.

**Technical narrative:** Checking that a checkout is clean is insufficient when
two agents race to acquire it. A project-wide lock serializes allocation; lease
tokens and Git-visible markers carry ownership beyond the critical section.
Tracked/ignored-marker checks ensure the reservation actually affects cleanliness.
Refresh/release require matching tokens; acquisition can reclaim recognized,
expired untracked markers. That reclamation does not prove the original session
has stopped, and unrecognized state remains preserved.

Evidence: `accomp-ai-checkout-allocation#allocator`, `#reservations`, `#recovery`,
`#lease-identity`.

### 7. Native engineering Workbench

**Concise:** Built a Tauri desktop engineering workbench with a React/TypeScript
interface and a shared Rust core serving both desktop and JSON CLI users.

**Expanded:** Combined asynchronous repository inspection, independent CPU/GPU
actions and packaged-build/process views behind a shared Rust/Tokio application
core, using targeted query updates and native events to keep status responsive.

**Technical narrative:** The shared core avoids separate desktop/CLI rules for
Git inspection and actions. Repository inspection bounds concurrency to four
tasks and restores stable ordering; process updates avoid repeating expensive Git
refreshes. TanStack Query manages independent frontend state. This is an explicit
concurrency/responsiveness design, with no measured speedup claimed.

Evidence: `project-ai-workbench#architecture`, `#inspection-concurrency`,
`#independent-ui-state`, `#action-validation`.

### 8. Native renderer controls

**Concise:** Developed a SwiftUI workspace manager with independent CPU/GPU build,
run, focus and termination controls.

**Expanded:** Exposed workspace/task status, editor launch and eight renderer
operations in a native macOS interface, reusing shared workspace backends across
the Swift launcher and later Workbench.

**Technical narrative:** Native UI work includes status/warning presentation and
process lifecycle controls. The backend checks actual build assets instead of
treating a running watcher as build completion. The two interfaces are related
surfaces over shared capabilities, not duplicate implementation credit.

Evidence: `accomp-ai-swift-workspace-manager#native-ui`, `#renderer-actions`;
`project-ai-workbench#runtime-delegation`; `accomp-ai-process-controls#identity`.

### 9. Reliable Git state and guarded actions

**Concise:** Implemented robust Git-state inspection and guarded repository actions
covering renames, conflicts, Unicode paths and stale upstream evidence.

**Expanded:** Parsed NUL-delimited porcelain-v2 status and labeled remote
comparisons by freshness; reset operations recheck branch identity, cleanliness
and ahead counts after fetch before changing repository state.

**Technical narrative:** Whitespace-based parsing breaks on real filenames and
rename records. Structured parsing preserves boundaries and conflict states.
Fresh/cached/missing remote states prevent absence of evidence from appearing as
synchronization. Post-fetch checks address changes that occur while remote work
runs; they are guards, not a claim of a filesystem-wide transaction.

Evidence: `accomp-ai-git-inspection#state-model`, `#remote-evidence`,
`#reset-guards`, `#parser-design`.

### 10. Recoverable build/process orchestration

**Concise:** Built recoverable packaged-build orchestration with persistent job
state, independent completion events and process-identity checks.

**Expanded:** Managed concurrent builds and packaged applications through an
atomic registry, restoring monitoring of recorded jobs after restart and
revalidating PID, start time and executable identity before process-control actions.

**Technical narrative:** Long-lived builds must outlast UI refreshes without
becoming untracked. The implementation persists jobs before monitoring them and
terminates a newly spawned build if persistence fails. Restart recovery monitors
recorded jobs and checks their resulting payloads; it does not restart build commands
or recover their original child exit status. Events update each build independently.
Identity checks reduce PID-reuse errors; they do not establish an
OS security boundary or eliminate every process race.

Evidence: `accomp-ai-process-controls#controls`, `#identity`,
`#registry-failure-recovery`.

## CI reliability, release integrity and packaged verification

### 11. Autonomous CI repair with reviewable patches

**Concise:** Built a team-used Codex workflow that diagnoses Jenkins GUI failures,
implements targeted fixes and replays affected tests in the captured cluster
environment before human patch review.

**Expanded:** Automated matrix-specific failure reconstruction from Jenkins,
JUnit and logs, preserving source revisions and LSF constraints while iterating
on flaky-test and application defects and returning synchronized, reviewable fixes.

**Technical narrative:** Local reproduction alone can miss environment-specific
failures. The workflow reconstructs the failed cell and works from its revision.
The diagnosis/fix/retest loop is autonomous after invocation; human review and
commit/push remain separate. Three consecutive clean passes are the documented
repair gate for flaky-test work. Existing owner-reported effort reduction is
qualitative; hours-to-days describes the manual alternative, not a timed saving.

Evidence: `accomp-ai-jenkins-repair#workflow`, `#repair-scope`, `#review-gate`,
`#environment`, `#impact`; read private `#gate-semantics`.

### 12. Patch and validation identity

**Concise:** Bound CI repair evidence to exact patches using cumulative binary
diffs and content, mode, symlink and deletion inventories.

**Expanded:** Used isolated repair worktrees and an alternate Git index to create
cumulative patches, then verified synchronized contents and required updated-matrix
cluster validation when changes affected test selection.

**Technical narrative:** A passing replay of an older patch or old matrix cannot
certify a new fix. The tooling records patch identity and file inventories and
applies classification-specific gates before finalization. Legacy timestamp
matching remains a weaker historical compatibility path. Retained records show
bounded successful replays and skipped-test distinctions; no overall repair rate
is inferred.

Evidence: `accomp-ai-jenkins-repair#patch-identity`,
`#selection-sensitive-validation`; private `#gate-semantics`, `#retained-run-evidence`.

### 13. Resumable cluster publication

**Concise:** Engineered resumable module publication spanning artifact validation,
verified transfer, cluster build/install, propagation and packaged acceptance.

**Expanded:** Persisted release phase/attempt state and immutable identities,
validating archive paths/links, payloads, source/dependency provenance and capability
hashes while preserving validated bytes and permission modes.

**Technical narrative:** Release work crosses filesystem, transport, scheduler
and installation boundaries. Explicit phase records allow safe reuse of completed
work while refusing identity-changing resumes. Retained manifests establish
historical complete runs and later failures under their respective contracts;
publication alone is not acceptance and current acceptance was not rerun.

Evidence: `accomp-ai-module-publication#workflow`, `#state-machine`, `#validation`,
`#payload-integrity`; private `#operational-history`.

### 14. Immutable host-native modules

**Concise:** Built macOS and Windows local-module tooling with verified payload
inventories, dependency provenance and atomic no-overwrite installation.

**Expanded:** Created lightweight-runtime and full-application profiles from
disposable source copies, recording dirty/untracked input context, validating
archive round trips and rejecting source-checkout leakage into installed payloads.

**Technical narrative:** Local success can depend on undeclared source paths or
mutable dependencies. Canonical inventories, dependency fingerprints, relocation
checks and unique module identities make these assumptions inspectable. Host/profile
preflight rejects incompatible builds before expensive packaging. Integrity controls
do not prove bit-for-bit rebuild reproducibility or cross-host/cluster acceptance.

Evidence: `accomp-ai-immutable-local-modules#builders`, `#immutability`,
`#relocation`, `#profile-preflight`.

### 15. Isolated packaged-agent verification

**Concise:** Built isolated agent-verification sessions that check packaged MCP
registration, provider identity, module integrity and protocol startup.

**Expanded:** Created blank agent workspaces with session-local state and narrowly
projected provider/authentication inputs, validating exact packaged launch settings,
health/proof output, JSON-RPC handshake and runtime-owner cleanup.

**Technical narrative:** Ordinary development sessions can hide packaging defects
through inherited tools, registrations and context. Session isolation excludes those
normal inputs while deliberately retaining selected authentication and system tools.
Verification rejects source leakage and unexpected links. The gates are implemented;
this research did not execute them or demonstrate air-gapped operation.

Evidence: `accomp-ai-isolated-agent-verification#sessions`, `#verification`,
`#provider-projection`.

### 16. Packaged-documentation integration checks

**Concise:** Automated isolated macOS builds and packaged-documentation smoke
checks through the application’s real Electron IPC path.

**Expanded:** Combined selective checkout copying, Doxygen regeneration, desktop
packaging and CDP/WebSocket evaluation to verify that documentation opens from
packaged assets, with slot-specific debug ports and bounded readiness waits.

**Technical narrative:** Source-tree documentation can work while packaged assets
are missing or misrouted. The helper invokes the existing builder, opens the real
application documentation action and checks the resulting page URL. It replaces its
selected build target and uses process-pattern cleanup; keep it distinct from the
modern immutable-module and stronger process-identity controls.

Evidence: `accomp-ai-packaged-docs-smoke#pipeline`, `#electron-contract`,
`#slot-and-failure-controls`; private `#implementation-boundary`.

### 17. Evidence-aware GUI qualification

**Concise:** Built resumable GUI qualification tooling tying renderer/test/coverage
evidence to source and dependency fingerprints.

**Expanded:** Orchestrated static checks, renderer builds, unit coverage and a
28-project/two-renderer fixture, preserving raw diagnostics and making missing,
skipped, synthetic or interrupted evidence explicitly non-qualifying.

**Technical narrative:** Shared output directories and resumed runs can silently
mix incompatible evidence. The runner preserves artifacts before cleanup and binds
reuse to source, matrix, tool and dependency identities. Complete, incomplete and
interrupted states remain distinct. The 56-cell fixture is configured scope; the
retained historical run is incomplete and supports no full-pass/coverage claim.

Evidence: `accomp-ai-gui-qualification#runner`, `#scope`, `#resumption`,
`#nonqualifying`, `#evidence-state-machine`; private `#retained-interruption`.

## Developer experience and infrastructure integration

### 18. Exact editor-driven test selection

**Concise:** Built editor-driven Playwright selection that verifies the exact test
ID before execution and cancels ambiguous or failed discovery.

**Expanded:** Generated workspace launch inputs from live test discovery, escaped
and anchored full-title filters, then collected again to prove the selection still
identifies exactly the chosen test.

**Technical narrative:** Parsed source names and loose regexes can broaden a
selection, especially with parameterized tests, punctuation and tags. Public
Playwright discovery and a second ID check provide a stronger contract. EOF and
collection errors cancel; selecting all remains an explicit separate choice.

Evidence: `accomp-ai-precise-test-selection#selection`, `#ambiguity`, `#editor`.

### 19. Robust editor navigation

**Concise:** Developed a VS Code navigation extension supporting multi-root and
remote workspaces, symbol lookup and stale-result-safe asynchronous search.

**Expanded:** Combined Git-aware file indexing, URI-preserving path operations,
frecency ranking and location/symbol queries, using query-revision and picker
identity checks to prevent late results from replacing current selections.

**Technical narrative:** Navigation has both path-semantics and asynchronous-state
problems. The implementation avoids assuming every URI is a local path, falls back
to editor discovery for remote contexts and serializes usage-history writes.
Query identity checks handle rapid user edits without conflating old and new work.

Evidence: `accomp-ai-vscode-navigation#extension`, `#asynchronous-query-identity`.

### 20. Native display automation

**Concise:** Built native macOS editor-window placement with display-coordinate
conversion and verified bounds updates.

**Expanded:** Reconciled AppKit and Accessibility coordinate systems, handled
ambiguous display names and fullscreen/transient windows, and retried placement
after re-enumerating windows to accommodate application reflow.

**Technical narrative:** A single position write does not guarantee the editor
ends at the intended size/location. The utility targets the usable viewport and
checks actual bounds across retries. Test definitions target shell arguments and
configuration using stubbed native automation; source assertions check for retry
constructs. They do not execute the native coordinate/bounds algorithm or establish
live multi-monitor behavior or granted Accessibility access.

Evidence: `accomp-ai-native-window-placement#coordinate-model`,
`#verification-loop`; private `#test-boundary`.

### 21. Reusable cluster access

**Concise:** Developed reusable cluster-access tooling with compatibility/load-aware
host advice and credentials kept out of command arguments.

**Expanded:** Integrated noninteractive SSH, optional terminal sessions and guarded
macOS storage operations with bounded OS/load probes across configured cluster
environments and user-scoped execution rules.

**Technical narrative:** Tooling separates transport configuration, authentication
helpers, host compatibility and workload placement. The configured 35-host pool
describes orchestration scope, not tested throughput. Account-owned paths and LSF
policies protect shared resources through workflows rather than a new security
platform or universal write sandbox.

Evidence: `accomp-ai-cluster-access#access`, `#host-advice`, `#storage`;
`lead-ai-cluster-execution-policies#policies`, `#implementation-controls`.

### 22. Integrity-checked cross-site transfer

**Concise:** Implemented idempotent cross-site artifact transfer using SHA-256
verification, run-owned partials and conflict-preserving finalization.

**Expanded:** Reused matching destinations, refused conflicting files and limited
retry cleanup to the current run’s partial path before no-clobber finalization of
verified content.

**Technical narrative:** Interrupted transfers and existing destinations need
different handling. Unique partials isolate incomplete data; content hashes make
matching-file reuse explicit. Verification precedes finalization, and retries
restart transfers instead of claiming byte-level resume or measured speed gains.

Evidence: `accomp-ai-verified-transfer#transfer`, `#conflicts`; private `#retry-scope`.

## Suggested positioning

For AI developer tooling, lead with the adopted harness, autonomous CI repair,
capability discovery and packaged-agent verification. For native/platform roles,
lead with the Rust/Tauri shared core, Git/process state models and concurrency-safe
workspace allocation. For quality/release roles, emphasize exact patch identity,
resumable publication, packaging integrity and evidence-aware qualification.

Do not combine every option or repeat a shared mechanism under several bullets.
Use stronger quantified outcomes only when separately sourced: configured counts
and test definitions demonstrate scope, while adoption, measured savings and
completed qualification require their own evidence.
