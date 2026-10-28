# Interconnect Architect contribution research — 2026-10-27

PRIVATE analyst findings. Public application wording belongs in eligible normalized facts and the reviewed bullet collection. Internal paths, codenames, author emails and raw excerpts remain research context.

Product checkout: `/Users/miccou01/GitProjects/sysip_shared_ai/workspaces/ideas/slot_04/checkout`. Selected `master` HEAD: `e24d80378096cb8d7a0ad87c20929cb520fa49d7`. Non-shallow local repository; product worktree clean at capture. No fetch, checkout mutation, product builds/tests, Jenkins calls, publication or outside uploads.

## Method and scope

Reviewed the full locally reachable authored-history metadata and changed-path catalog, grouped recurring work, traced representative introduction/refinement/current-state implementations, and compared surviving-line authorship with original diffs and explicit collaborator credits. Git author/committer identities were inspected; Michael’s matched identity is Michael Coulter <michael.coulter@arm.com>. This is attributable Git work, not proof of unaided implementation, merge approval, sole ownership or external employer audit.

All local refs contain 11,987 total reachable commits. Michael has 1,309 authored commits (1,261 nonmerge, 48 merge); selected HEAD contains 1,029 (986 nonmerge, 43 merge). Nonmerge Change-Ids: 988 distinct across all refs, 947 in HEAD, with 20/18 nonmerge commits lacking one. Author dates span 2021-11-04 through 2026-10-05; dates are commit evidence, not role/project starts.

Stable patch-ID analysis: 1,259 nonempty authored patches, 1,025 distinct stable patch identities, 968 represented in selected HEAD and 57 absent. Patch IDs, Change-Ids and commit counts are different measures; alternate revisions, reapplications, squash differences and stash objects are not independent delivered accomplishments. Two stash-related nonmerge objects are excluded from delivery claims. No remote freshness or unreachable-object completeness is asserted.

Implementation evidence captures 105 selected authored commits across 28 overlapping topics and 73 current-path snapshots (some paths recur), plus focused function-range review. Full selected patches were captured in disposable local scratch; key implementation hunks were reviewed. This is broad history coverage with representative deep investigation, not a manual audit of every changed line.

Commands: `git --no-optional-locks log --all --author=... --fixed-strings`; `rev-list --all`; `for-each-ref`; per-commit `show --numstat --no-renames` and `show --format= --unified=3`; `git patch-id --stable` over authored nonmerge patches; `git show HEAD:path`; `git log HEAD --follow --diff-filter=A -- path`; `git blame --line-porcelain HEAD -- path`. Current excerpts preserve source line numbers and SHA-256 fingerprints. No line-count ownership percentage is used.

## Architecture and engineering context

The application combines Angular/TypeScript forms, services and graph canvases; Electron/Node desktop integration and Python command transport; a Python Configuration Engine owning topology/parameters/rules; YAML/XML interchange and reports; and unit, CE, renderer-build and Electron/Playwright qualification. Internal MCP tooling adds a typed capability/planning boundary over the engine and a separate legacy runtime route. Michael’s changes cross these layers; shared graphics foundations, backend algorithms, catalog infrastructure and later fixture changes include other engineers.

Use cases include configuring coherent meshes and NoCs; inspecting/editing groups, ports, routes and physical placement; migrating legacy configurations; diagnosing DRC/deadlock/latency issues; comparing saved designs; qualifying desktop workflows; and bounded agent-assisted engineering configuration.

## Evolution

- 2021–2022: command translation, IP-catalog interchange, metadata-driven controls, report execution, headless E2E and CMN UI scaffolding/API-backed mesh rendering.
- 2023–2024: editable CMN hierarchy/canvas, legacy conversion, vector exports, structured diagnostics, metadata-driven latency reports and event/memory fixes.
- 2025: original NCI logical canvas and connectors, tile/combined-mesh views, route/deadlock investigation, semantic diff, Playwright check-in coverage and source-aware documentation.
- 2026: integrated graph-based migration, shared rendering semantics, auto-placement, guided/OWO workflows, test/runtime reliability, typed MCP plans and compatibility-aware packaging.

These are implementation milestones, not formal-title transitions, exhaustive release dates or claims that all features shipped on commit author dates.

## integration: Catalog integration and configuration interchange

Challenge: An IP-catalog workflow and the desktop configuration engine represented domains, interfaces and build data differently.
Personal action and engineering decisions: Michael introduced Python adapters converting CCXML into engine YAML and JSON build data back into catalog structures. The converter rebuilds voltage/power/clock hierarchy, assigns interface protocols/directions and clock references, supplies required defaults and supports an existing YAML input. The reverse adapter hashes datasets to avoid unnecessary imports. Launcher subprocess output and failure reporting connect the workflow.
Practical outcome: Enabled configuration interchange between the catalog and desktop tool without requiring the user to reconstruct the same interface/domain data manually.
Attribution and evidence limits: This is historical integration work from 2022. The old launcher was explicitly deprecated in 2024; surviving converters do not establish that every old launch path remains supported. An authored change explicitly credits supplied changes to a colleague; no exclusive authorship of the catalog platform is claimed.
Supporting authored milestones:
- `bde8578f4858ffe38b25dfc814bd3cb777e4819d` | author 2022-01-24 | in selected HEAD: True | Adding files for Socrates integration:
- `9a9a6e9964ce5f3abebeee2463d4c290cdf615f0` | author 2022-02-04 | in selected HEAD: True | Update CcxmlToIyml.py to allow for an IYML to be specified as part of IPCatalog creation wizard in Socrates
- `81689f1799fc07e1ce845cb7b8c8a211790b7187` | author 2024-05-22 | in selected HEAD: True | IPTOOLING-14229: Display import error messages from Brunel (project_init.py) in Socrates
- `a08ab38bc571d160441c0593f5d68a7c4ca5a411` | author 2024-05-22 | in selected HEAD: True | deprecate scripts/socrates_integration/BrunelLauncher.py
Current source anchors (existence checked at captured HEAD):
- `HEAD:scripts/socrates_integration/CcxmlToIyml.py`
- `HEAD:scripts/socrates_integration/JsonToCcxml.py`
- `HEAD:scripts/socrates_integration/BrunelLauncherDeprecated.py`
Reviewed fact `accomplishment-catalog-configuration-interchange#adapters` (public): Built Python adapters translating IP-catalog CCXML and engine YAML/JSON, reconstructing domain hierarchies, protocol mappings and interface clock relationships.
Reviewed fact `accomplishment-catalog-configuration-interchange#incremental-import` (public): Used content hashes to avoid reimporting unchanged build datasets and added subprocess/error reporting for the historical catalog-to-desktop workflow.
Reviewed fact `accomplishment-catalog-configuration-interchange#historical-scope` (private): Integration adapters date to 2022; the legacy launcher was deprecated in May 2024, so historical launcher functionality is not asserted as current supported architecture.

## bitfields: Reusable metadata-driven parameter controls

Challenge: Hardware parameters encode boolean and multi-bit fields whose valid masks vary by wire mode.
Personal action and engineering decisions: Michael introduced an Angular ControlValueAccessor registered through NG_VALUE_ACCESSOR, deriving bit labels, groups and masks from Configuration Engine metadata and propagating values/disabled state through Angular forms. Later changes support multi-bit segments and wiremode-dependent masks, rather than one checkbox for every raw numeric bit.
Practical outcome: A reusable control allows hardware bitfields to be edited within existing parameter forms while retaining numeric engine values and mode-specific constraints.
Attribution and evidence limits: The later branch-only mask iteration is an alternate revision, not independent landed delivery evidence. No claim of bug-free masks for arbitrary JavaScript numeric widths or a measured productivity saving.
Supporting authored milestones:
- `5cebeb111cf2f7fa49bba4c08b354e1c5a882a10` | author 2022-03-29 | in selected HEAD: True | Add/integrate bitfield-input component for parameters that have a "bits" constraint
- `759c72f0ec74fc97432265d66019ed3662d74fb3` | author 2024-10-11 | in selected HEAD: True | BRUNEL-2536: Update GUI bitfield inputs to handle new retiming param format
- `e2e685fb7e666d29b22982d370751c5cd7d9e8ae` | author 2024-12-06 | in selected HEAD: False | update/fix IP-specific bits constraint in default-params and CE
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/shared/components/bitfield-input/bitfield-input.component.ts`
- `HEAD:GUI/src/app/shared/components/bitfield-input/bitfield-input.component.spec.ts`
Reviewed fact `accomplishment-metadata-parameter-controls#reusable-control` (public): Built a reusable Angular form control for engine-defined bitfields, mapping hardware metadata and grouped labels to editable numeric values with disabled-state propagation.
Reviewed fact `accomplishment-metadata-parameter-controls#mode-sensitive-fields` (public): Extended bitfield editing to multi-bit segments and wiremode-dependent masks, integrating the control across parameter-editing surfaces.
Reviewed fact `accomplishment-metadata-parameter-controls#pattern` (private): Used ControlValueAccessor and NG_VALUE_ACCESSOR to integrate domain-specific numeric editing with Angular forms rather than maintaining an unrelated value model.
Reviewed fact `skill-angular#demonstrated-patterns` (public): Applied Angular form adapters, metadata-driven validation, Material/CDK trees, change-detection control and service/facade composition in shipped interconnect tooling.

## cmn-editor: Coherent-mesh hierarchy editing

Challenge: A coherent mesh has crosspoints, device/CAL representations, groups, ports and domains that need consistent inspection and editing.
Personal action and engineering decisions: Michael progressed from a 2022 node-configuration scaffold to API-backed mesh rendering, real-data parameter inspection, group add/delete/rename/parameter workflows and canvas group editing in 2023. Components coordinate CE service calls, metadata and validation; a scaffold commit is distinguished from later functioning editing.
Practical outcome: Hardware hierarchy became an interactive configuration workflow in the production desktop application.
Attribution and evidence limits: Owner confirmation establishes CMN GUI functional responsibility; Git alone does not establish sole authorship of all current shared rendering, infrastructure or hardware algorithms. Formal title remains Senior Software Engineer since April 2023.
Supporting authored milestones:
- `7996d5bb3a4bd9a7ed5836c8acb4013acc722c2c` | author 2022-06-14 | in selected HEAD: True | Add node-configuration component
- `1ff7b26ffd816acc1fbfabe4bb2b7e06d213f7fb` | author 2022-12-08 | in selected HEAD: True | Rendering all devices/cal devices on logical canvas from API data
- `122a9594cf683d1f0cec7a856e5fe6dbbf0bc796` | author 2023-05-22 | in selected HEAD: True | CMN: bulk GUI set-functionality updates
- `d951e149f26fc6349582361130bfa0906669ad77` | author 2023-11-14 | in selected HEAD: True | BRUNEL-1283: Logical canvas group editing features
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/node-configuration/node-configuration.component.ts`
- `HEAD:GUI/src/app/shared/components/group-attributes-modal/group-attributes-modal.component.ts`
- `HEAD:GUI/src/app/canvas/renderers/svg/logical-mesh/svg-logical-mesh-renderer.base.ts`
Reviewed fact `accomplishment-cmn-configuration-editor#evolution` (public): Evolved CMN GUI tooling from API-backed mesh and device inspection into editable groups, port assignments, tile definitions and combined-mesh views.
Reviewed fact `accomplishment-cmn-configuration-editor#tile-integration` (public): Integrated tile service APIs, tile editor/viewer components and navigation with mesh visualization to support tile-definition and combined-mesh workflows.
Reviewed fact `accomplishment-cmn-configuration-editor#multiport-model` (public): Implemented multiport and super-device group-member configuration, preserving distinctions between logical devices, physical ports and group assignments.
Reviewed fact `accomplishment-cmn-configuration-editor#metadata-tests` (public): Drove user-defined-group regression inputs from live engine metadata and hardened duplicate-name handling in group creation.
Reviewed fact `project-interconnect-architect#verified-history` (private): Locally reachable Git history attributes changes to Michael Coulter from November 2021 through October 2026 across configuration UX, graph visualization, migration, diagnostics, desktop lifecycle, testing and internal AI tooling.
Reviewed fact `project-interconnect-architect#cross-layer-delivery` (public): Delivered interconnect engineering workflows across Angular/TypeScript components, Electron/Node integration, Python engine APIs and product-aware regression infrastructure.

## cmn-tiles: Tile definition and combined-mesh views

Challenge: Tile-level designs need both local editing context and an integrated view across repeated mesh structure.
Personal action and engineering decisions: Michael added tile-definition rendering, tile editor/viewer components, tile service APIs and navigation/metadata integration in May 2025, then added the combined-mesh view. This connects tile definitions and group configuration to the broader canvas workflow.
Practical outcome: Extended CMN editing from individual mesh/group inspection to tile-definition and combined-mesh visualization.
Attribution and evidence limits: This is software tooling for describing and visualizing designs, not hardware tile-architecture invention or a measured silicon outcome.
Supporting authored milestones:
- `dbcfdb561663d19eb96c6225ecde625f47da57b6` | author 2025-05-22 | in selected HEAD: True | BRUNEL-2904 BRUNEL-3247: Tile Definition for CMN
- `ffad4a69dc271816dfeedc2b927d71990cbafee1` | author 2025-05-30 | in selected HEAD: True | BRUNEL-2905: Combined mesh view
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/tiling-configuration/tiling-configuration.component.ts`
- `HEAD:GUI/src/app/canvas/renderers/svg/tile-definition/svg-tile-definition-renderer.base.ts`
- `HEAD:GUI/src/app/mesh/mesh.component.ts`

## cmn-multiport: Multiport and super-device group configuration

Challenge: One logical hardware device can expose multiple physical ports; GUI names and group assignments must preserve that distinction.
Personal action and engineering decisions: Michael implemented multiport/super-device member-port dialogs and group workflows, hardened duplicate-name handling and drove UDG regression inputs from live CE metadata rather than a fixed device list.
Practical outcome: Configuration forms and tests track supported member/port capabilities and reduce dependence on stale hardcoded product assumptions.
Attribution and evidence limits: Sole CMN GUI responsibility remains owner-confirmed; backend topology and other contributors to shared components retain separate attribution. Current metadata-driven test definitions were inspected, not executed.
Supporting authored milestones:
- `5236c96147b0e3211477d33c461a4a1420e11d5a` | author 2026-07-01 | in selected HEAD: True | Support super-device ports in group editing
- `d98d6c2f9058186885304249cbcffcd51d46de3a` | author 2026-07-08 | in selected HEAD: True | Delphi R1 updates: add Multi-CHI Port and advanced settings UI
- `55885d15452b3f8af975d724a94ad52095dc1784` | author 2026-07-07 | in selected HEAD: True | Drive UDG Playwright coverage from live CE metadata
- `ac9d282c943590a48a40a9c791531935f2eb6a44` | author 2026-07-28 | in selected HEAD: True | Prevent duplicate user-defined group names
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/shared/components/group-member-port-modal/group-member-port-modal.component.ts`
- `HEAD:GUI/src/app/shared/components/add-group-modal/add-group-modal.component.ts`
- `HEAD:GUI/tests/ui/user-defined-groups/user-defined-groups.spec.ts`

## nci-canvas: Original NoC logical canvas and editing

Challenge: Engine topology needed a logical presentation that supports connection creation, route inspection and hardware-specific layout.
Personal action and engineering decisions: Michael introduced the original NCI logical canvas in January 2025, extended logical connectors and route interaction, then rebuilt layout classification and logical route-editor state handling. Current layout uses explicit classifiers and connectivity/grouping rules rather than only physical coordinates.
Practical outcome: Provided a graph-oriented design workflow connecting topology visualization to editing and engine state.
Attribution and evidence limits: Original canvas creation is owner-confirmed. Later common scene builders, renderer drivers and interactions are collaborative; no sole authorship of the entire modern graphics architecture.
Supporting authored milestones:
- `e0a9fdd0159f724fcbf6988cfead60a55a282fed` | author 2025-01-14 | in selected HEAD: True | BRUNEL-1816, BRUNEL-2779: Logical canvas for NCI
- `82ff7cdeea292d5f48f6b335a937e449a8bc1eeb` | author 2026-05-18 | in selected HEAD: True | Rebuild logical canvas render model
- `155fd4ed9db7abd727c72c91db65472bc2180d73` | author 2026-05-18 | in selected HEAD: True | Fix Route Editor candidate routing state
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/canvas/core/services/canvas-logical-layout.service.ts`
- `HEAD:GUI/src/app/canvas/core/utils/canvas-logical-layout-classifier.util.ts`
Reviewed fact `accomplishment-nci-original-canvas#logical-editing` (public): Extended the original NoC logical canvas with connection creation, transformed connector gestures and route-editing state tied to backend topology.
Reviewed fact `accomplishment-nci-original-canvas#layout-model` (public): Implemented hardware-aware logical layout classification and connectivity grouping so the graph view reflects design structure rather than only physical coordinates.

## renderers: Shared hardware semantics across renderers

Challenge: SVG and Pixi views can disagree when label, visibility, cursor or hardware-classification rules are duplicated.
Personal action and engineering decisions: Michael centralized renderer metadata and behavior and implemented route-aware classification, CAL connector semantics and MCN/CAL persistence/readback repairs. Selected changes separate logical grouping from persisted backing connectivity and expose metadata to shared interactions.
Practical outcome: Aligns hardware meaning and interaction behavior across CPU/SVG and GPU/Pixi paths while retaining persisted topology semantics.
Attribution and evidence limits: Current input and rendering infrastructure contains substantive contributions from other engineers. Surviving-line blame is context, not an ownership percentage or a measure of lifetime work.
Supporting authored milestones:
- `35d9937af5473b8cdc558edb68611e304ddbbe8d` | author 2026-06-22 | in selected HEAD: True | Centralize canvas renderer metadata and behavior
- `b1361c9f775374129b1b98fa709f148bf10a9d83` | author 2026-08-18 | in selected HEAD: True | Fix CAL connector and route editor behavior
- `b2bdbf984870ee6846f4231644e4ab3e24c81cf4` | author 2026-10-03 | in selected HEAD: True | BRUNEL-4855: Fix CAL/MCN connectivity and route rendering across SVG and Pixi
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/canvas/core/services/canvas-input-interpreter.service.ts`
- `HEAD:GUI/src/app/canvas/core/utils/canvas-logical-layout-classifier.util.ts`
Reviewed fact `accomplishment-shared-renderer-semantics#persistence` (public): Repaired route, CAL and multi-chip connectivity presentation and export/re-import behavior while preserving backend connection and placement semantics.
Reviewed fact `accomplishment-shared-renderer-semantics#shared-boundary` (private): Current shared input and renderer infrastructure includes substantive contributions by multiple engineers; Michael authored selected metadata, classification and persistence changes rather than the entire shared architecture.

## performance: Interactive graphics performance and memory lifecycle

Challenge: Pointer-rate work, repeated geometry reads, change detection and retained observers/subscriptions can degrade an interactive canvas.
Personal action and engineering decisions: Michael made frame-batched pan updates, shared zoom/pan handling, geometry caching and work outside Angular change detection, and repaired interface/ResizeObserver lifecycle leaks. He extended coherent-mesh coordinates/identifiers to 64 by 64 and worked on no-GPU/CPU execution paths. Owner evidence separately confirms introducing Pixi.js.
Practical outcome: Concrete rendering/event-path and memory-lifecycle improvements, plus larger representable mesh dimensions and compatibility work for CPU/headless environments.
Attribution and evidence limits: No benchmark establishes a speedup ratio, latency reduction, memory percentage or tested full 4096-node workload. 64 by 64 describes coordinate/identifier support. No-GPU branch alternatives are not separate accomplishments.
Supporting authored milestones:
- `e93183095a43d3607cbe8bf6e2337edb7fc4c68e` | author 2024-08-28 | in selected HEAD: True | BRUNEL-2503, BRUNEL-2020
- `6946d58aec43e7d2e9d77ca7aaacf830da2dff15` | author 2024-12-20 | in selected HEAD: True | BRUNEL-2756: optimize panning for logical canvas
- `a6e5a6486e4a6be8c43e12f4245b872557c5c043` | author 2025-02-19 | in selected HEAD: True | centralize all canvas zoom/pan logic in canvas-interaction.util.ts
- `9d505f90c7dc30ccb87e9c0be2784d5522adb26d` | author 2025-09-25 | in selected HEAD: True | BRUNEL-2729: GUI - 64x64 Mesh support
- `9126ab49b5795b74f8bb61638c303f2d36e332d7` | author 2025-08-15 | in selected HEAD: True | BRUNEL-3468: Address interface tab memory leaks
- `f922795c315a0ee4816e39bbc0c2efdd6a1b36bc` | author 2025-10-01 | in selected HEAD: True | Fix Access Maps tab memory leaks due to resize observer, implement flex layout css
- `63b5c1f13b94724541a9556695fa272a20524313` | author 2025-10-14 | in selected HEAD: True | Pixi working on cluster (no GPU)
- `cd3602f944118c7c6abb91506a8072cf698e46da` | author 2025-11-11 | in selected HEAD: False | BRUNEL-3727: Improve PIXI performance on no-GPU machines
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/canvas/core/services/canvas-input-interpreter.service.ts`
- `HEAD:GUI/src/app/canvas/core/utils/canvas-transform.util.ts`
- `HEAD:GUI/src/app/memory-maps/memory-map-regions/memory-map-regions.component.ts`
Reviewed fact `accomplishment-canvas-performance#optimization-mechanism` (public): Reduced repeated canvas event-path work through cached geometry, animation-frame batching and processing outside Angular change detection; repaired retained observer/subscription lifecycles.
Reviewed fact `accomplishment-canvas-performance#scale-boundary` (private): The 64×64 change establishes coordinate and identifier support, not a measured full-scale rendering benchmark or a claim of 4,096 independently tested nodes.
Reviewed fact `accomplishment-canvas-performance#cpu-compatibility` (public): Improved desktop rendering compatibility for CPU/headless environments and configurations without an available GPU.

## placement: Physical auto-placement with engine persistence

Challenge: Unplaced design objects need coherent placement without overlaps, while an incremental mode must account for existing design state.
Personal action and engineering decisions: Michael implemented a deferred per-project auto-placement operation with an active-run guard, generation/context checks, model reconciliation, grid/collision allocation, interface/blockage grouping, route/bridge adjacency, die sizing and CE persistence. Full and missing-only modes use different reservations.
Practical outcome: Automates physical-canvas population and persists the resulting layout; regression definitions exercise geometry/model properties for SVG and Pixi.
Attribution and evidence limits: Missing-only reserves valid existing placements; this is not unconditional preservation of invalid/overlapping locations. No measured placement-time reduction or physical-design PPA improvement. Test definitions are not passes in this investigation.
Supporting authored milestones:
- `8043ff80857818dfd48a591f6f0de794dc906c13` | author 2026-07-01 | in selected HEAD: True | BRUNEL-1475: Physical auto-placement, remove HLS Floorplan
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/canvas/core/services/canvas-physical-auto-place.service.ts`
- `HEAD:GUI/tests/ui/noc-se/physical-auto-place-layout.spec.ts`
Reviewed fact `accomplishment-physical-autoplacement#project-operation` (public): Designed auto-placement as a deferred, project-bound operation with active-run and generation guards, reconciling live model state before allocating and persisting locations.
Reviewed fact `accomplishment-physical-autoplacement#incremental-layout` (public): Implemented full and missing-only layout modes with grid/collision allocation, interface/bridge adjacency, blockage grouping and die sizing; missing-only reserves valid existing placements.
Reviewed fact `accomplishment-physical-autoplacement#preservation-limit` (private): Missing-only placement does not promise to preserve invalid or overlapping locations; no elapsed-time or silicon PPA improvement has been established.

## conversion: Source-aware NIC-400 migration and bounded DRC closure

Challenge: Legacy XML describes source microarchitecture that must be reconstructed, mapped and validated in a different target topology.
Personal action and engineering decisions: Michael evolved 2023 conversion scripts through 2024 source-microarchitecture derivation into an integrated 2026 engine. Graph node/edge records represent source paths; bus matrices map to routers, clock crossings to PCDC helpers and width conversions to SERDES. Repairs record rule, action and fidelity impact, with initial/iteration/final DRC results and a maximum of six closure iterations. Later assertions reject unresolved connectivity and check source-path fidelity.
Practical outcome: The introduction commit reports 4130/4130 valid corpus configurations DRC-clean and 5/5 curated invalid inputs rejected; audit scripts and fixtures make the corpus checks inspectable.
Attribution and evidence limits: These counts are historical commit-reported results; raw logs were not recovered and no tests were rerun. DRC-clean does not establish RTL equivalence. Repairs can add helpers or change target mappings/endpoints. Later fixes by colleagues do not erase Michael primary implementation attribution.
Supporting authored milestones:
- `12c14eb478040a280bb5f8373bc296d748048b7c` | author 2023-05-04 | in selected HEAD: True | Add first edition of nic400_to_tower_iyml.py script
- `6ba68516e28599638b3447891a50876d6a59602e` | author 2024-04-08 | in selected HEAD: True | BRUNEL-1648: NIC-400 Migration
- `429a76b7e0e98b720b61065b8216e6ab2b96504a` | author 2024-04-29 | in selected HEAD: True | BRUNEL-1974: Add NIC-400 migration regresssion tests in Pytest
- `f0e5bb3195676179948595be567624c872686134` | author 2026-05-08 | in selected HEAD: True | feat(nic400): reconstruct NCI uArch and close DRCs
- `d8e09fbe489d822f1e7841797f595b83ed7dc8b3` | author 2026-08-04 | in selected HEAD: True | Preserve NIC400 topology during conversion
- `0ec8ee6bddb3815016daf76faa8d38193d94cbc6` | author 2026-09-25 | in selected HEAD: True | Update NIC-400 tests for channel-aware deadlock repair
Current source anchors (existence checked at captured HEAD):
- `HEAD:CE/ideas/base/nic400_conversion.py`
- `HEAD:CE/pytests/nic400/audit_nic400_corpus.py`
Reviewed fact `accomplishment-nic400-migration#graph-model` (public): Modeled legacy source microarchitecture as nodes, edges and paths, mapping bus matrices, clock crossings and width conversion into target routers and helper blocks.
Reviewed fact `accomplishment-nic400-migration#bounded-repair` (public): Built bounded DRC closure with at most six iterations, per-fix fidelity-impact records, initial/iteration/final results and a stop when no further repair progress is possible.
Reviewed fact `accomplishment-nic400-migration#equivalence-limit` (private): DRC-clean migration is not proof of RTL or functional equivalence: target repairs may introduce helpers or adjust mappings, endpoints and memory maps.
Reviewed fact `skill-python#engineering-tools` (public): Implemented Python topology reconstruction, bounded rule-driven repair, semantic comparison, typed planning and modern/legacy runtime integration.

## guided: Policy-backed Guided Flow and lifecycle persistence

Challenge: An accessible configuration workflow must enforce product constraints while preventing stale asynchronous work or retired state from reactivating.
Personal action and engineering decisions: Michael implemented backend guided policy and GUI integration in July 2026, supported by explicit product-revision policy, starting/active/retired states, queued mutations, project-context guards, source hashes and atomic temporary-file metadata replacement. Backend compliance evaluates retiming minima, PMU and other supported constraints, with structured violations; later work strengthens retirement and test routing.
Practical outcome: A guided editing lifecycle connects engine-authoritative constraints, persistence/export checkpoints and a durable transition into advanced editing.
Attribution and evidence limits: The policy integrates an existing area-reduction capability, not authorship of that algorithm or measured area savings. Supported revisions must be read from the frozen policy, not extrapolated to every family. The October 1 commit separately reports 79 Guided executions, 132 Playwright passes/7 competing-load skips, 105 CE passes/9 fixture skips, 522 Angular passes and two renderer builds; these tiers are historical, overlapping in purpose and must not be summed.
Supporting authored milestones:
- `0567531987d35ff866e312c510795b5b634707b1` | author 2026-07-29 | in selected HEAD: True | Add NoC-Lite guided policy APIs
- `3287440c76c2ab24aceaee5b73ebcc42cda052dc` | author 2026-07-29 | in selected HEAD: True | Implement the NoC-Lite guided GUI flow
- `9f385e8b0fc6b8bbb2b9bef9170a43ce33d5146f` | author 2026-07-29 | in selected HEAD: True | Make Guided Flow retirement atomic
- `18dc7270ca6f155cd2774eef6a4d222ad2451551` | author 2026-08-04 | in selected HEAD: True | Harden Guided Flow metadata and project lifecycle
- `32939448d1a9a1f084701f320870daa4e0aa408e` | author 2026-10-01 | in selected HEAD: True | consolidate Guided Flow coverage across supported IPs
- `badc593694d2ba52c12722ac5da52a934101dabc` | author 2026-10-03 | in selected HEAD: True | Generate Nitwain NoC-Lite starter as a Guided Flow resource
Current source anchors (existence checked at captured HEAD):
- `HEAD:CE/ideas/flow_impl/guided_policy.py`
- `HEAD:GUI/src/app/shared/services/guided-flow-policy.service.ts`
- `HEAD:GUI/src/app/shared/services/guided-flow-metadata.ts`
- `HEAD:CE/ideas/guided-flow-features.yaml`
Reviewed fact `accomplishment-guided-noc-flow#lifecycle-persistence` (public): Implemented a persistent Guided Flow lifecycle with starting, active and retired states, queued policy mutations, project-context checks and atomic metadata replacement.
Reviewed fact `accomplishment-guided-noc-flow#engine-authority` (public): Connected product-specific guided editing to backend compliance checks for supported constraints, structured violations and persistence/export preflight.
Reviewed fact `accomplishment-guided-noc-flow#historical-qualification` (private): An October 1, 2026 commit separately reports 79 Guided Flow executions, 132 Playwright passes with seven competing-load skips, 105 CE passes with nine missing-fixture skips, 522 Angular passes and two renderer builds; these are historical reports, not newly rerun results.

## owo: Ordered Write Observation setup wizard

Challenge: OWO setup crosses source/target topology, protocol prerequisites, resource planes, credits, buffering, striping and memory-address rules.
Personal action and engineering decisions: Michael introduced a component/facade/models/utilities/topology-matrix design with plan/review/apply/recovery stages, sparse topology validation, source-dependent target-capacity multipliers, reserved/shared credits and memory-range alignment. Feedback changes add project-bound opening checkpoints, fingerprint validation, stale-state detection and recovery. The introduction changes 12 Angular source spec files and five Playwright UI spec files.
Practical outcome: Brings interacting hardware constraints into one guided configuration and diagnostic workflow with inspectable recovery behavior.
Attribution and evidence limits: Owner confirmation covers wizard creation, not OWO hardware invention. Current restore logic contains colleague refinements: six lines in the inspected opening-checkpoint range, including full CE-copy restoration, are from Dustin Divis. Attribute project-bound checkpoint/fingerprint work to Michael and describe full current recovery as collaborative. File counts are changed files, not cases, coverage percentages or passes.
Supporting authored milestones:
- `9851f748f2450a96ad59aab5521b3bc157ba79db` | author 2026-09-29 | in selected HEAD: True | BRUNEL-4829: OWO Streaming Wizard
- `e19a7b5a8db40056f8c3ac002504a39d3fe65383` | author 2026-10-01 | in selected HEAD: True | OWO Streaming Wizard feedback updates
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/interfaces/owo-setup/owo-setup.facade.ts`
- `HEAD:GUI/src/app/interfaces/owo-setup/owo-memory-ranges.ts`
- `HEAD:GUI/tests/ui/feature-flows/owo-setup-wizard.spec.ts`
Reviewed fact `accomplishment-owo-wizard#constraint-design` (public): Implemented sparse source/target topology checks, source-dependent credit-capacity calculations and memory-range alignment within the OWO plan/review/apply workflow.
Reviewed fact `accomplishment-owo-wizard#checkpoint-validation` (public): Added project-bound opening checkpoints, content-fingerprint validation and stale-design detection to support safe wizard recovery.
Reviewed fact `accomplishment-owo-wizard#recovery-collaboration` (private): The current opening-checkpoint restore includes later colleague changes to full Configuration Engine state/undo restoration; attribute wizard and checkpoint/fingerprint work to Michael without claiming every current recovery line.
Reviewed fact `skill-interconnect#applied-domain` (public): Translated routing, clock crossings, width conversion, resource-plane/credit constraints and memory alignment into validated configuration and migration workflows.

## deadlock: Mesh routing and deadlock investigation

Challenge: Deadlock diagnosis needs a way to locate loops within channel/subchannel routing and relate them to editable mesh turns.
Personal action and engineering decisions: Michael added global/scoped deadlock checks, loop/turn/crosspoint summaries, route selection/highlights and custom-route integration in late 2025. The earlier route viewer flattens nested source/target/channel/subchannel/hop data with filters; routing dialogs validate selected subchannels and show permissible turn patterns. These evolved into the current route editor/deadlock sidebar.
Practical outcome: Engine analysis becomes an interactive investigation and route-correction workflow.
Attribution and evidence limits: The underlying CE deadlock-analysis algorithm predates this work; its history includes a 2021 introduction/relocation by another engineer. No claim of inventing the core detection algorithm or a measured diagnostic-time saving.
Supporting authored milestones:
- `5d7183cf554c64341e5b7e1c4adfa3857ee4cac8` | author 2025-10-28 | in selected HEAD: True | BRUNEL-2900: Deadlock detection (Part 1)
- `a6053261023e4d20f77231c8faac995dd829a5e9` | author 2025-11-03 | in selected HEAD: True | BRUNEL-2900: Deadlock detection (Part 2)
- `c46b9c3ca90a63169ce3ae61eaa7a7746e04658c` | author 2025-11-08 | in selected HEAD: True | BRUNEL-2900: Deadlock detection (Part 3)
- `28ed79a29c52ff893ee9894357de071123c7e92e` | author 2025-11-09 | in selected HEAD: True | BRUNEL-2900: Deadlock detection (Part 4)
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/canvas/ui/sidebar/mesh-deadlock/mesh-deadlock.component.ts`
- `HEAD:CE/ideas/flow_impl/deadlock_analysis.py`
Reviewed fact `accomplishment-mesh-deadlock-investigation#channel-navigation` (public): Connected channel/subchannel route filtering and permissible-turn selection to scoped deadlock loops, crosspoint summaries and editable mesh routes.
Reviewed fact `accomplishment-mesh-deadlock-investigation#algorithm-boundary` (private): The engine deadlock-analysis algorithm predates Michael’s investigation GUI; contribution evidence supports routing/diagnostic integration and visualization, not original authorship of the detector.

## latency: Metadata-driven static latency reporting

Challenge: An existing report encoded extensive type-specific rules and needed minimum/configured latency to follow actual parameter and wire-mode metadata.
Personal action and engineering decisions: Michael added default-latency attribute/API exposure and refactored the standalone report toward CE metadata in October 2024. Subsequent corrections address retiming, clock-domain crossing, wire modes and SERDES. The active CE report still reads DefaultLatency and supported retiming parameters.
Practical outcome: Improved maintainability and hardware-condition coverage of an existing engineering report.
Attribution and evidence limits: Supplied default values are explicitly credited to a colleague. The old resource script was pruned in March 2026; an active CE report remains. Historical resource cleanup is not the disappearance of the reporting capability; no measured silicon latency improvement.
Supporting authored milestones:
- `519cf31c6c2c4f7cad86550de47b313f29cb7a5e` | author 2024-10-07 | in selected HEAD: True | BRUNEL-2535: Create API to get 'default_latency' from instance attributes
- `4c2bce6ad1f3ce33dd870f14d4e6122d256acf77` | author 2024-10-11 | in selected HEAD: True | BRUNEL-2537: Update static latency report to use new attribute API and report new min latency info - part 1
- `6e276c22916434f742b5c2c8bfe47c862af6d09a` | author 2024-10-21 | in selected HEAD: True | BRUNEL-2537: Update static latency report to use new attribute API and report new min latency info - part 2
- `2f222a1d3099f6fc092656440d256e2e4931e489` | author 2026-01-16 | in selected HEAD: True | BRUNEL-3749: Static latency report is not accounting for SERDES
Current source anchors (existence checked at captured HEAD):
- `HEAD:CE/ideas/api/interconnect_config.py`
- `HEAD:CE/ideas/instance/instances.py`
- `HEAD:CE/ideas/report_impl/static_latency.py`
Reviewed fact `accomplishment-static-latency-reporting#attribute-contract` (public): Exposed default-latency attributes through the engine API and replaced extensive report-specific conditionals with metadata-backed minimum/configured latency handling.
Reviewed fact `accomplishment-static-latency-reporting#active-lineage` (private): The historical standalone resource script was pruned in March 2026, while an active CE static-latency report still reads DefaultLatency and retiming metadata; resource cleanup did not remove the entire reporting capability.

## diff: Semantic and textual configuration comparison

Challenge: Raw YAML changes do not directly explain which design entities, connections or routes differ.
Personal action and engineering decisions: Michael introduced logical diff overlays in October 2025 and report/highlight improvements in 2026. Python loads two isolated temporary CE sessions, captures instance/interface/connection/route/attribute views and computes nested differences alongside raw YAML differences. HTML output escapes text, aligns lines and highlights changed spans using common prefix/suffix and SequenceMatcher logic.
Practical outcome: Connects configuration-file changes to hardware entities in the canvas and a shareable HTML report.
Attribution and evidence limits: Temporary directory cleanup appears in the successful paired-load path; no blanket claim of fault-proof cleanup on every exception. Current report/GUI components include later collaboration. No quantified review-time or correctness uplift.
Supporting authored milestones:
- `30b70cb283e509fed0d584ba8c206a31f46c9b1b` | author 2025-10-13 | in selected HEAD: True | BRUNEL-3314: Present diffs on logical canvas
- `76bb561f94f32624d9494b4d95c3f040807144bb` | author 2026-01-08 | in selected HEAD: True | BRUNEL-539: Add configuration Diff report
- `c23851428ffcbc041fee920acca72dc4e7ce24ca` | author 2026-07-17 | in selected HEAD: True | Highlight exact YAML diff changes
Current source anchors (existence checked at captured HEAD):
- `HEAD:resources/scripts/iyml_diff.py`
- `HEAD:GUI/src/app/canvas/core/services/canvas-diff-overlay.service.ts`
- `HEAD:CE/pytests/report/test_iyml_diff.py`
Reviewed fact `accomplishment-semantic-configuration-diff#semantic-snapshots` (public): Compared two isolated engine snapshots across hardware entities, routes and parameters alongside recursive raw YAML differences, linking changes to logical-canvas overlays.
Reviewed fact `accomplishment-semantic-configuration-diff#precise-highlights` (public): Implemented escaped, line-aligned HTML configuration reports with changed-span highlighting to expose precise differences in nested design data.

## testing: Product-aware GUI test infrastructure

Challenge: Desktop regression flows depend on product capabilities, application lifecycle and reliable renderer/engine state.
Personal action and engineering decisions: Michael expanded 2022 E2E/headless Xvfb CI, introduced a 2025 Playwright check-in gate, added reporting/utilities and migrated CMN coverage. Later tests derive supported group types/parameters from live engine metadata and check persistence, rich feature interactions and build-output behavior. A June 2026 change modifies 51 Angular source .spec.ts files; two tsconfig.spec JSON files are excluded from that count.
Practical outcome: Established and expanded repeatable, hardware-aware desktop regression coverage across unit and UI layers.
Attribution and evidence limits: Owner evidence confirms Playwright creation; shared fixtures and later work are collaborative. Changed spec-file counts are scope, not coverage percentage or pass totals. Tests were not executed here.
Supporting authored milestones:
- `4985c20cf3c226569c19d4f980bb883864a15512` | author 2022-04-29 | in selected HEAD: True | Add interfaces e2e test
- `ca950bd508ee634fd6270dd96573b88733b7ca84` | author 2022-05-05 | in selected HEAD: True | Run e2e tests with xvfb
- `499876145fceb3ced61d0c11d179808094dfb9f5` | author 2025-09-04 | in selected HEAD: True | BRUNEL-3411: Set up a simple GUI end2end test and make it a gate for check-in
- `75eb348e988e2139a8c3057937bf54dfc23cd885` | author 2025-09-05 | in selected HEAD: True | extract gui test boilerplate code into electronTestUtil.js, created playwright-reporter.js for custom test reporting/logging
- `e53836bfd7e883a4f43df292a25fc69b777b5262` | author 2026-01-30 | in selected HEAD: True | BRUNEL-3847: Migrate CMN e2e user defined group tests to playwright
- `fff32ba2a4b6f0f5a1018df771e2ba0a6ef19439` | author 2026-06-22 | in selected HEAD: True | Expand GUI unit test coverage and Karma harness
- `55885d15452b3f8af975d724a94ad52095dc1784` | author 2026-07-07 | in selected HEAD: True | Drive UDG Playwright coverage from live CE metadata
- `c8120b3bc450ea5097d736bc4b746aa996826323` | author 2026-08-18 | in selected HEAD: True | Add feature-rich Nitwain end-to-end regression
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/tests/fixtures/index.ts`
- `HEAD:GUI/tests/config/ip-capabilities.ts`
- `HEAD:GUI/tests/ui/project/project.guided-flow-lifecycle.spec.ts`
Reviewed fact `accomplishment-playwright-infrastructure#capability-fixtures` (public): Replaced fixed assumptions in group-regression inputs with live engine capability metadata and added persistence, renderer and rich-workflow assertions.
Reviewed fact `accomplishment-playwright-infrastructure#coverage-count-boundary` (private): The June 2026 expansion changed 51 Angular source .spec.ts files; spec-file counts describe change scope and exclude two tsconfig.spec JSON files, not case totals, coverage percentages or newly executed passes.
Reviewed fact `skill-playwright#desktop-qualification` (public): Built Electron/Playwright regression tooling with product-aware fixtures, engine-metadata-driven inputs and renderer/persistence assertions.

## electron-karma: Electron-hosted unit testing and vertical runners

Challenge: A generic browser unit environment can differ from the deployed Electron renderer and headless execution stack.
Personal action and engineering decisions: Michael implemented Electron-hosted Karma with dynamically allocated loopback ports, isolated temporary state and logs, runtime coordination and Playwright proof steps. Focused vertical scripts select related CE/unit/build/UI checks and renderer modes.
Practical outcome: Aligns unit and UI checks with the desktop runtime and provides focused cross-layer qualification entry points.
Attribution and evidence limits: Only source definitions inspected here. Historical results recorded elsewhere do not establish fresh success; environment-specific port restrictions and skipped checks must remain visible.
Supporting authored milestones:
- `fa16f0019d05f3e0514f94594db9190f9fc0cbb0` | author 2026-05-18 | in selected HEAD: True | Add Electron-bound Karma runtime workflow
- `fff32ba2a4b6f0f5a1018df771e2ba0a6ef19439` | author 2026-06-22 | in selected HEAD: True | Expand GUI unit test coverage and Karma harness
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/tests/scripts/electron-karma-runtime.ts`
- `HEAD:GUI/tests/scripts/run-electron-karma-playwright.ts`
- `HEAD:scripts/vertical-tests/test-owo-streaming.sh`
Reviewed fact `accomplishment-electron-karma#runtime-isolation` (public): Coordinated Electron-hosted unit tests with dynamic loopback ports, temporary run state/logs and Playwright verification in the same desktop/headless runtime.
Reviewed fact `accomplishment-electron-karma#vertical-selection` (public): Created focused vertical runners selecting related backend, unit, renderer-build and UI checks so feature qualification can span application layers.

## lifecycle: Asynchronous desktop correctness

Challenge: Overlapping loads and late engine replies can let one project overwrite another or repopulate stale dialogs.
Personal action and engineering decisions: Michael repaired corrupt-startup handling and project loading, then added per-load snapshots and revision/request identity, cancellation of superseded subscriptions and callback ownership guards. DRC work gives module loads and results separate request sequences, attaches listeners before dispatch and resets warning state. Stale Guided Flow operations are similarly guarded.
Practical outcome: Addresses cross-project state contamination, missed synchronous responses and stale-dialog updates through explicit request ownership.
Attribution and evidence limits: Current common data/project infrastructure includes other authors. No concurrency benchmark or universal race-freedom claim; targeted regression definitions were inspected without execution.
Supporting authored milestones:
- `c5250faae7ab861de53a6416406ad0708dfcbaee` | author 2024-04-17 | in selected HEAD: True | BRUNEL-2072: Brunel GUI hangs if input config is corrupted
- `7bed6f651e4d8aca0850cac94deafe55e9ee1c33` | author 2025-04-08 | in selected HEAD: True | BRUNEL-2634, BRUNEL-2799, BRUNEL-2801
- `f5881ff4e50ebf29740a2227ea34d430ca4ffe16` | author 2025-06-12 | in selected HEAD: True | BRUNEL-3223: Create a 'Pre-build check' API that will run lite BE/Build tab button
- `1aa44baff56d6b49bc9b39cf2b874ba3d8d22ea1` | author 2026-04-14 | in selected HEAD: True | Project tab rework
- `12eb8c808c4743cc394118f0e66e8569cf1dfdc7` | author 2026-07-29 | in selected HEAD: True | Isolate competing project load pipelines
- `c7d43253081940a2d599647f2820bf5837ab882a` | author 2026-08-06 | in selected HEAD: True | BRUNEL-4632: Fix stale HLS and uArch DRC result handling
- `1ad1c93d466261afe48ee9441c42471c3fafde2e` | author 2026-08-18 | in selected HEAD: True | Prevent stale guided flow work across project loads
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/project/project-launcher.service.ts`
- `HEAD:GUI/src/app/status-bar/drc-results/drc-results.component.ts`
- `HEAD:GUI/tests/ui/project/project.competing-loads.spec.ts`
Reviewed fact `accomplishment-desktop-async-correctness#load-ownership` (public): Prevented superseded project loads from applying late state through per-load snapshots, revision/request identities, subscription cancellation and callback ownership checks.
Reviewed fact `accomplishment-desktop-async-correctness#drc-ownership` (public): Hardened DRC dialogs with separate module/result request sequences, response listeners attached before dispatch and corrected warning initialization.
Reviewed fact `skill-typescript#stateful-systems` (public): Used TypeScript and RxJS to implement graph interactions, request ownership, cancellation, project lifecycle guards and renderer-independent hardware semantics.
Reviewed fact `skill-electron-desktop#implementation` (public): Engineered Electron/Node desktop workflows spanning Python backend commands, asynchronous project loading, platform close/quit behavior, graphics compatibility and runtime-aligned tests.

## console: Console, executable command streams and backend observability

Challenge: Engine actions and report subprocesses need understandable logs and commands that remain valid when replayed in Python.
Personal action and engineering decisions: Michael integrated GUI report execution and stdout/stderr/status handling in 2022, CE logfile capture in 2024 and command-stream behavior in 2025. A 2026 JavaScript serializer emits Python None/True/False, nested containers, escaped strings and numeric special values instead of JSON literals. Circular/unsupported values deliberately fall back to None.
Practical outcome: Connects user-visible console diagnostics with backend operations and fixes cross-language command-text serialization.
Attribution and evidence limits: The serializer is not a general arbitrary-object or lossless cyclic-graph serializer. Owner evidence establishes console creation independently of the earliest inspected report-runner date.
Supporting authored milestones:
- `5b307cd1717f72d851f7807c67782659f53a05f8` | author 2022-03-30 | in selected HEAD: True | Add ability for users to run report scripts from the GUI
- `13108e12760abcc1f4d310ac1685901e7ba93c5b` | author 2024-11-01 | in selected HEAD: True | BRUNEL-2580: Capture all CE output in a logfile
- `d99d886cb31239c71ebaa5cba2b9b12155259e8a` | author 2025-10-16 | in selected HEAD: True | BRUNEL-3662: Add command stream in brunel console
- `30a56c92475007426f3404182da48c428a745957` | author 2025-11-15 | in selected HEAD: True | Console command stream improvements
- `5547a60f51c4fc6b3a6ea04e004f0ffc53c2701d` | author 2026-08-26 | in selected HEAD: True | BRUNEL-4702: fix cmd stream output to be correct Python and stabilize Pixi blockage resize tool cursors
Current source anchors (existence checked at captured HEAD):
- `HEAD:brunel/python-command.js`
- `HEAD:GUI/src/app/shared/services/data.service.ts`
- `HEAD:brunel/test.py`
Reviewed fact `accomplishment-configuration-console#command-replay` (public): Fixed executable Python command generation across the JavaScript/Python boundary, serializing nulls, booleans, nested containers, strings and numeric special values as Python literals.
Reviewed fact `accomplishment-configuration-console#stream-observability` (public): Extended console/report integration with engine log capture, command-stream reporting and subprocess stdout/stderr/status handling.
Reviewed fact `accomplishment-configuration-console#literal-limit` (private): Command serialization deliberately substitutes None for circular/unsupported values; it is not a general lossless object-graph serializer.

## exports: Canvas vector export

Challenge: Engine configuration exports do not provide a reusable image of an interactive design view.
Personal action and engineering decisions: Michael added SVG canvas serialization and Blob/object-URL download in November 2023, with export-dialog improvements in 2025. The original change selected the then-existing canvas container, serialized it through XMLSerializer and revoked the temporary URL after download.
Practical outcome: Enabled vector snapshots of a rendered design for external viewing and engineering communication.
Attribution and evidence limits: At captured HEAD, vector export is conditional on the logical mesh having an SVG element; other canvases use available PNG paths. Later clone/PNG compatibility logic is current-state context, not all attributed to the original author. No universal SVG/Pixi vector export guarantee or visual QA performed.
Supporting authored milestones:
- `23f8742b677fd300b070a0209fc83cf6a7728c8b` | author 2023-11-15 | in selected HEAD: True | BRUNEL-1288: Export SVG of Logical/Physical canvas
- `1a1ffed4dafa2ab389ec95a52eea19567ef1f7cd` | author 2025-09-19 | in selected HEAD: True | export dialog modal improvements
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/status-bar/export-dialog/export-dialog.component.ts`
Reviewed fact `accomplishment-canvas-vector-export#svg-export` (public): Added SVG export of the rendered design canvas through XML serialization and downloadable Blob/object URLs, enabling vector snapshots of engineering views.
Reviewed fact `accomplishment-canvas-vector-export#export-integration` (public): Integrated canvas-image export into the configuration export dialog and subsequently refined dialog behavior.
Reviewed fact `accomplishment-canvas-vector-export#current-limit` (private): At the captured HEAD, SVG export is conditional on a logical-mesh SVG element; PNG paths serve other available canvases. Historical SVG work does not establish universal Pixi vector export support.

## docs: Source-aware developer documentation

Challenge: GUI navigation and component knowledge can drift when manually maintained separately from source.
Personal action and engineering decisions: Michael introduced TypeScript metadata collection, Python documentation rendering, curated overrides, source indexing and task-to-code navigation. Generated documents and manual narrative sources have distinct roles.
Practical outcome: Provides reproducible documentation inputs and engineering navigation tied to real application structure.
Attribution and evidence limits: Surrounding agent/orchestration code includes scaffolding; the inspected doc_guard returns an empty finding list. Do not portray that placeholder as enforced autonomous documentation parity or claim authorship of a general execution loop.
Supporting authored milestones:
- `31a0f63e2ae554ce1afb122a2886d345c1302306` | author 2025-09-26 | in selected HEAD: True | This change introduces and integrates a comprehensive orchestration framework under
- `4244a7676653076be51535e15e0f2e617c38edac` | author 2025-09-29 | in selected HEAD: True | Move nav bar to menu-bar. Extended the agent’s navigation awareness: added menu-bar keywords so the planner now picks up menu-bar.component.{ts,html,css} alongside the existing nav artifacts, and registered the menu-bar doc as a tracked nav resource (GUI/agent/runtime/action_planner.py, GUI/agent/runtime/bootloader.py). Rebuilt the agent context index so downstream tooling immediately sees the new assets and guidance (GUI/agent/context/index.json).
- `fd0f07d1913dc6628280755f280a3ab6b62952d9` | author 2025-10-08 | in selected HEAD: True | Create `GUI/agent/lessons-learned` and integrate it into the GUI agent context framework and runtime workflows
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/agent/collect-app-docs-data.js`
- `HEAD:GUI/agent/render-app-docs.py`
- `HEAD:GUI/agent/runtime/tools/doc_guard.py`
Reviewed fact `accomplishment-ia-source-aware-documentation#source-pipeline` (public): Built a source-aware GUI documentation pipeline using TypeScript metadata collection, Python rendering, curated narrative overrides and navigation/source indexes.
Reviewed fact `accomplishment-ia-source-aware-documentation#guard-limit` (private): The inspected documentation guard returns no findings; surrounding orchestration scaffolding does not establish fully enforced automated documentation parity.

## ai-planning: Typed capability-bound engineering plans

Challenge: Agent intent needs a deterministic boundary between supported interconnect operations, ambiguous requirements and backend mutations.
Personal action and engineering decisions: Michael introduced the MCP pack and developed typed intent/strict schemas, live capability binding, product-aware operation lowering, dependency ordering, semantic readback and planned artifacts. The execution registry owns canonical plans; durable phase receipts must match authority, form a consecutive committed prefix and preserve semantic continuity. Exact committed retries return receipt evidence without repeating mutations. Checkpoints/postconditions support rollback and replay.
Practical outcome: Turns bounded engineering intent into inspectable, reproducible engine operations with explicit capability and continuation checks.
Attribution and evidence limits: Not a new foundation model, Codex executor, general orchestrator or hosted agent fleet. The September completion report records 5063 non-live passes, 92 real-engine contract/integration cases, two bounded agent evaluations and rollback hash equality as distinct historical evidence categories.
Supporting authored milestones:
- `0ab6800995f1cbf36129653ccea400b713c8d8ae` | author 2026-04-21 | in selected HEAD: True | IA MCP capability pack initial implementation
- `7319af553f5601a0a4365cd952f08c91fba3dd6f` | author 2026-08-28 | in selected HEAD: True | Harden IA MCP transactional execution
- `7ba22c61f75afb5228694245af4de75f00b5fb78` | author 2026-08-29 | in selected HEAD: True | Bind IA MCP capabilities to live CE
- `67b621ef6f366c852550ef07ee1122d336f2985e` | author 2026-08-30 | in selected HEAD: True | Compile typed IA MCP design plans
- `ad62f9ccb1382a153997636f24a9e6cd35cb096d` | author 2026-08-31 | in selected HEAD: True | Prove IA MCP NCI construction vertical
- `f1867d608f03207757d61e06a5abe6a35b0ac432` | author 2026-09-01 | in selected HEAD: True | Prove IA MCP CMN construction vertical
- `fb6764542de61d70ff7606846e5ad53e77736c31` | author 2026-09-03 | in selected HEAD: True | Deliver bounded IA MCP Agentic V1
- `e2415aae9c4951362cabb1d0607a2bf74cc9e869` | author 2026-09-16 | in selected HEAD: True | Expand IA MCP configuration execution
Current source anchors (existence checked at captured HEAD):
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/plan_compiler.py`
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/plan_execution.py`
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/direct_ce_fallback.py`
- `HEAD:ai/docs/agentic-v1-completion.md`
Reviewed fact `accomplishment-ia-mcp-typed-planning#compilation-boundary` (public): Compiled validated design intent against live product capabilities and strict operation schemas, explicitly rejecting mismatched families or incomplete source identity before authorizing native plans.
Reviewed fact `accomplishment-ia-mcp-typed-planning#engineering-lowering` (public): Implemented domain-specific plan lowering for interconnect instances, interfaces, routing, domains, memory configuration and planned artifacts, with explicit dependencies and semantic postconditions.
Reviewed fact `accomplishment-ia-mcp-checkpoint-replay#phase-receipts` (public): Validated durable plan receipts against canonical authority, consecutive mutation batches and semantic continuity, rejecting phase gaps or stale continuation evidence.
Reviewed fact `accomplishment-ia-mcp-checkpoint-replay#idempotent-retry` (public): Implemented exact committed-phase retries that return validated receipt evidence without repeating Configuration Engine mutations.
Reviewed fact `accomplishment-ia-mcp-backend-fallback#script-admission` (public): Added content-bound fallback script admission using AST checks, protected-harness fingerprints, public API inventories and explicit rejection of unresolved gaps or prohibited dynamic calls.
Reviewed fact `accomplishment-ia-mcp-backend-fallback#authority-distinction` (private): Controlled backend fallback is distinct from checkpoint rollback and runtime routing; script admission is not a claim of a general secure Python sandbox.
Reviewed fact `accomplishment-ia-mcp-real-engine-qualification#result-provenance` (private): The repository completion report preserves the September 2026 baseline as separate non-live suite, real-engine contract/integration, bounded agent evaluation and rollback evidence; this research inspected records and definitions without rerunning employer tests.
Reviewed fact `accomplishment-ia-mcp-agent-evaluations#evaluation-boundary` (private): The two historical bounded agent evaluations remain separate from the 92 real-engine contract/integration cases and later scenario definitions; none is a newly executed agent campaign in this research.
Reviewed fact `project-ia-mcp#source-history` (private): Introduced the internal MCP capability pack in April 2026 and developed transactional planning, compatibility and packaging through later 2026 changes; the inspected code supports bounded engineering automation rather than a new model execution loop.

## ai-runtime: Modern/legacy runtime routing

Challenge: Modern MCP dependencies and older product engines require incompatible Python environments.
Personal action and engineering decisions: Michael kept control/planning in Python 3.13 and isolated the legacy engine in an authenticated Python 3.7 sidecar. Admission checks exact runtime versions, selected product/session identity and CE import origin; allowlisted public methods and path roots limit dispatch. Token/sequence checks, bounded messaging, timeout/parent-lifetime monitoring and cleanup maintain a distinct subprocess boundary.
Practical outcome: Provides product-aware current/legacy routes without moving modern dependencies into the old interpreter.
Attribution and evidence limits: Runtime compatibility is distinct from backend fallback and checkpoint restoration. Exact qualified runtime versions and supported routes matter; no arbitrary 3.7 compatibility, isolation-security certification or deployment acceptance claimed from static inspection.
Supporting authored milestones:
- `be568b8bdac01df3762f96a5d3e62dc9fa532e7b` | author 2026-09-19 | in selected HEAD: True | Route IA MCP CE execution through qualified runtimes
- `5560c7c340a808c9b9683fe5431a795b4fbc43b4` | author 2026-09-19 | in selected HEAD: True | Qualify IA MCP toolchains in setup and release gates
Current source anchors (existence checked at captured HEAD):
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/legacy_ce_sidecar.py`
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/ce_backends.py`
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/runtime_router.py`
Reviewed fact `accomplishment-ia-mcp-dual-runtime#dispatch-boundary` (public): Restricted legacy dispatch to packaged public-method inventories and approved path roots while verifying exact interpreter, selected product and Configuration Engine import origin.
Reviewed fact `accomplishment-ia-mcp-dual-runtime#direct-source-review` (private): Current local source for runtime routing, backend adapters and the legacy sidecar was inspected at the recorded Git HEAD; this supplements earlier supplied correspondence without asserting fresh runtime execution.

## release: Isolated release staging and contract-aware packaging

Challenge: Installer changes and an optional internal AI payload need rehearsal without overwriting normal release outputs or granting stale API authority.
Personal action and engineering decisions: Michael introduced a manual nonconcurrent staging pipeline selecting an exact Gerrit patchset, later a validated branch override. It isolates buildenv/releases/archive outputs, omits synthesis-engine collateral, packages checked-in examples and performs post-installer rehearsal. Optional MCP packaging uses a checkout-owned wrapper. Deployment binding compares live CE reflection with reviewed API contracts, preserves reviewed bytes and disables native support only for affected drifted operations while retaining controlled-fallback inventory.
Practical outcome: Created a reviewable installer rehearsal path and explicit staged deployment authority for API-sensitive tooling.
Attribution and evidence limits: Pipeline and packaging code were inspected; no Jenkins job, installer, module publication or remote environment was executed here. Isolated staging is not a claim of sole release ownership. Internal credentials/host paths remain private evidence and never enter résumé copy.
Supporting authored milestones:
- `65e2d9081e5f6aa94b20bbbbce281999df31b713` | author 2026-09-13 | in selected HEAD: True | Add isolated daily staging pipeline
- `c3335efecbb32729a04404b795725a998c0d42e1` | author 2026-09-17 | in selected HEAD: True | Add a dedicated, conditional IA MCP packaging stage to installer-staging.
- `142665a60206f1034954bc00eb649a52be2de601` | author 2026-09-17 | in selected HEAD: True | Allow installer-staging.Jenkinsfile to use both branches and gerrit refs
- `2f0f548b67be00bfaa78d481474666356a1a4131` | author 2026-09-21 | in selected HEAD: True | Make CE API disposition staging contract-aware
Current source anchors (existence checked at captured HEAD):
- `HEAD:jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`
- `HEAD:ai/ia-mcp-pack/src/ia_mcp_pack/api_disposition_deployment.py`
- `HEAD:ai/scripts/stage-ia-mcp-runtime.sh`
Reviewed fact `accomplishment-isolated-installer-staging#isolated-rehearsal` (public): Built a manual, nonconcurrent installer-staging pipeline selecting exact review patchsets or validated branches, with isolated release/archive outputs and post-installer rehearsal.
Reviewed fact `accomplishment-isolated-installer-staging#optional-payload` (public): Added optional internal MCP packaging through a checkout-owned wrapper while keeping API-sensitive release gates explicit.
Reviewed fact `accomplishment-isolated-installer-staging#contract-binding` (public): Implemented staged API contract binding that preserves reviewed authority and limits native support for drifted operations while retaining controlled-fallback discovery.
Reviewed fact `accomplishment-isolated-installer-staging#execution-limit` (private): This investigation inspected staging and deployment-binding code; no installer build, Jenkins execution, module publication or remote acceptance was performed.

## ip-policy: Version policy and lifecycle-aware UX

Challenge: Supported/retired product versions and subsection constraints should follow explicit policy rather than scattered UI assumptions.
Personal action and engineering decisions: Michael added configurable IP version policy, import/retirement behavior and subsection gates. Current policy parsing and normalization provide a common basis for availability decisions; shared data-service integration later gained additional lifecycle/epoch changes by others.
Practical outcome: Makes product availability and compatibility decisions explicit and easier to update across application flows.
Attribution and evidence limits: Do not attribute every current epoch/context guard to Michael. Policy support is not proof of exercising every revision or deploying every migration.
Supporting authored milestones:
- `4fb049b5c92bedb7192e7db8780eaa5b4218fa15` | author 2026-07-17 | in selected HEAD: True | Add configurable IP version policy
- `fc81777f4faabd7a84b0bbe8ff58785298f0da90` | author 2026-09-08 | in selected HEAD: True | Retire cmns4_r0p0 from GUI support
- `48b5e3a43642b65ef99c0363937ac17d3d93c20d` | author 2026-08-13 | in selected HEAD: True | BRUNEL-4683, BRUNEL-4684, BRUNEL-4693: Gate GT ports and subsections to niTwain R1
Current source anchors (existence checked at captured HEAD):
- `HEAD:brunel/ip-version-policy.js`
- `HEAD:GUI/src/app/shared/services/data.service.ts`
Reviewed fact `accomplishment-product-version-policy#configurable-policy` (public): Centralized supported/retired product-version decisions in configurable policy and integrated import/retirement behavior and subsection availability gates.
Reviewed fact `accomplishment-product-version-policy#maintenance-outcome` (public): Made compatibility rules explicit across application flows, reducing dependence on scattered hardcoded product assumptions.
Reviewed fact `accomplishment-product-version-policy#collaboration-limit` (private): Later lifecycle/epoch guards in the shared data service include other authors; static policy inspection does not prove every product revision was exercised.

## diagnostics: Structured design-rule diagnostics

Challenge: Flat or paged log strings made it difficult to relate a rule violation to its severity, components and detailed engine output.
Personal action and engineering decisions: Michael introduced a reusable Angular Material/CDK tree and DRC result integration in May 2024, converting rule metadata and matching log messages into expandable rule/issue nodes. Typed DRC categories and RxJS teardown coordinate the status-bar viewer and report flows.
Practical outcome: Presents rule description, severity, affected components and issue details in a structured diagnostic workflow.
Attribution and evidence limits: This is diagnostic presentation/integration, not authorship of the engine rule library or a measured reduction in debugging time. Later request-race hardening belongs to the separate lifecycle record.
Supporting authored milestones:
- `44d2ae68c761b8be51a3956cab45519545eaca74` | author 2024-05-20 | in selected HEAD: True | BRUNEL-1999: Add DRC violation tree viewer
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/shared/components/info-tree/info-tree.component.ts`
- `HEAD:GUI/src/app/status-bar/drc-results/drc-results.component.ts`
Reviewed fact `accomplishment-structured-drc-diagnostics#diagnostic-tree` (public): Replaced flat/paged DRC result presentation with expandable rule and issue trees showing descriptions, severity, affected components and matching engine logs.
Reviewed fact `accomplishment-structured-drc-diagnostics#reusable-tree` (public): Created a reusable Angular Material/CDK diagnostic tree and integrated typed DRC categories and RxJS lifecycle teardown across status-bar and report flows.
Reviewed fact `accomplishment-structured-drc-diagnostics#scope-limit` (private): Work covers diagnostic presentation and application integration; it does not establish authorship of the underlying design-rule library or a measured debugging-time reduction.

## routing-editors: Interactive route editing evolution

Challenge: Connection gestures and nested channel/subchannel route data must coordinate canvas interaction and engine state.
Personal action and engineering decisions: The February 2025 logical connector change adds view transforms, connector selection/preview and create-connection interaction. August mesh-routing work adds route rows, channel/subchannel filtering and validated routing-scheme selection. Later route/deadlock changes reorganize these pieces into the current sidebar.
Practical outcome: Extends a visual topology from inspection into connection and route editing.
Attribution and evidence limits: Domain-specific routing UI is not authorship of the core engine routing/deadlock algorithm. Historical component paths can be removed or relocated; full commit paths remain retrievable.
Supporting authored milestones:
- `4d97de903fd55a58857fb69fefff10cc1909dbd6` | author 2025-02-28 | in selected HEAD: True | BRUNEL-2863: Enable connector tool in logical canvas
- `7389f6a0958aecb9e01f7708bd71fa95caa2d584` | author 2025-08-28 | in selected HEAD: True | delphi routing
Current source anchors (existence checked at captured HEAD):
- `HEAD:GUI/src/app/canvas/ui/sidebar/mesh-route-editor/mesh-route-editor.component.ts`
- `HEAD:GUI/src/app/shared/components/routing-scheme-modal/routing-scheme-modal.component.ts`

## desktop-dev: Desktop development and platform lifecycle

Challenge: Developer setup, GPU availability and platform close behavior affect a local engineering application.
Personal action and engineering decisions: Michael added macOS setup support in 2022, adjusted Electron rendering/runtime configuration in 2025 and corrected unsaved-change close/quit handling in 2026, preserving macOS window-close versus application-quit semantics.
Practical outcome: Demonstrates ongoing maintenance across development setup, desktop runtime and platform-specific application lifecycle.
Attribution and evidence limits: Performance settings alone do not establish measured gains; no claim that every GPU flag remains optimal or every OS path was tested here.
Supporting authored milestones:
- `91f84a5f7c53f21ede6eee30274358d3b6c5abbb` | author 2022-09-06 | in selected HEAD: True | Add gui_setup_mac.sh script
- `1c5488ad4df90b335e39fe987368c519d5c9cac3` | author 2025-01-30 | in selected HEAD: True | Update main.js with various GPU/rendering/JavaScript settings to increase app performance
- `cbf07500fb644e609f85b386cdba9adfe8d295ae` | author 2026-03-02 | in selected HEAD: True | BRUNEL-3756, BRUNEL-4050: GUI quit issues
Current source anchors (existence checked at captured HEAD):
- `HEAD:gui_setup_mac.sh`

## Evidence reconciliation and application boundaries

Existing owner statements and registered analyses remain intact. Direct Git/source findings supplement them; they do not overwrite role title, qualitative adoption/licensing context, sole CMN GUI functional responsibility, original NCI canvas/Pixi/Playwright/console creation, earlier work, education or unrelated employment. Newly inferred code facts use reported status; explicit owner confirmations retain confirmed status.

The old latency resource-script deletion is now distinguished from the still-active CE report. Earlier runtime notes saying source had not been inspected are revised to identify this direct local source review. Existing OWO changed-spec counts (12 Angular, five Playwright) and 51-file Angular expansion were recalculated, retaining their original scope. Historical 4130/5 migration counts and 5063/92/two MCP figures remain reported baselines, never fresh executions.

Application selection: omit private implementation paths/codenames/customer details; formal title is Senior Software Engineer, with CMN GUI Lead as a functional responsibility. No measured graphics speedup, time saving, revenue, silicon result, number of agent tasks from 92 integration cases or large-scale hosted-fleet experience is established. Preserve private caveats before selecting public facts.

Open gaps: raw historical corpus/result logs; measured rendering/placement/debugging improvements; attributable customer/business outcomes that can be disclosed; exact lead-role start; adoption counts and repeated agent evaluation statistics. Local commits establish engineering milestones and technical mechanisms, not those missing outcomes.
