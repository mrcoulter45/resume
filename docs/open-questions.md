# Information worth collecting

These are evidence gaps, not claims that the experience does not exist. No invented
values should fill them. Add dated owner notes or suitable supporting documents,
register them, and update the related facts. Do not reopen resolved corrections.

| Area | Useful evidence | Related records |
| --- | --- | --- |
| Current employment and contacts | Confirm currency when preparing later applications | `exp-arm-senior`, `profile-michael` |
| Harness and ia-mcp adoption | Active users/teams, usage periods, representative completed tasks, responsibility boundaries | `project-ai-harness`, `project-ia-mcp` |
| Repair impact | Measured manual/automated elapsed time, interventions, attempts, success rates, patch volume and baseline methodology | `accomp-ai-jenkins-repair` |
| Agent evaluation | Dated actual runs with model/configuration, criteria, success/failure distributions, latency/cost and attributable improvements | `accomplishment-ia-mcp-agent-evaluations` |
| Production operations | Actual hosted-service/SLO/incident/operating responsibilities if present; distinguish desktop delivery and internal tools | `project-interconnect-architect`, `project-ai-harness` |
| Rendering/layout impact | Before/after benchmark conditions and results; real user/device scale | `accomplishment-canvas-performance`, `accomplishment-physical-autoplacement` |
| Business value | Attributable customer outcomes, engineering effort or licensing contributions that may be disclosed | `project-interconnect-architect` |
| Leadership and mentoring | Specific architecture decisions adopted beyond own work, collaboration, mentoring actions and outcomes | `leadership-cmn-gui` |
| Individual project dates | Precise starts/releases/role transitions; avoid inferring rotations from employment dates | Experience records and earlier project records |
| UVM coverage models | Resolve authored-model vs debugging/testing attribution in earlier internship evidence | `project-embedded-logic-analyzer`, `skill-uvm` |
| Academic/personal work | Personal capstone contribution, hobby/open-source/entrepreneurial projects, code and outcomes | `additional-ut-capstone`, additional experience records |
| Credentials/development | Any certifications, formal learning or credentials beyond the documented degree; do not assume any exist | Education records |

Resolved: application name is Interconnect Architect; CMN GUI ownership and product
family mapping are owner-confirmed; waveform viewers were used, not created; the
degree is BS Electrical and Computer Engineering with the documented primary and
secondary focuses; repair scope includes test and application defects; the 92 cases
are historical real-engine contract/integration cases, separate from agent tasks.


## Gaps after direct Interconnect Architect history review

The 2026-10-27 [research capture](interconnect-architect-research.md) establishes
implementation mechanisms and commit milestones. The following evidence would
strengthen outcome or attribution claims without reopening resolved owner statements:

| Area | Focused follow-up evidence | Record/source reference |
| --- | --- | --- |
| Migration corpus | Retain original dated audit output, corpus identity and validity criteria; distinguish DRC repairs from semantic/RTL equivalence | `accomplishment-nic400-migration#corpus`; `src-ia-results-attribution-2026-10-27` |
| Performance/layout | Before/after workload, renderer/hardware, repeated timings and memory measurements; distinguish 64×64 identifier support from actual rendered scale | `accomplishment-canvas-performance#mesh-scale`; `accomplishment-physical-autoplacement` |
| Guided/OWO outcome | Disclosable user adoption and configuration/debugging effort; preserve product-revision scope and original pass/skip logs | `accomplishment-guided-noc-flow`; `accomplishment-owo-wizard` |
| Diagnostics/export | Representative user outcomes; whether vector export beyond current logical-mesh SVG is intended | `accomplishment-structured-drc-diagnostics`; `accomplishment-canvas-vector-export#current-limit` |
| Release rehearsal | Actual dated staging/installer results and deployment acceptance, if needed for a delivery claim | `accomplishment-isolated-installer-staging#execution-limit` |
| MCP qualification | Retain raw historical runs and repeated bounded-agent evaluations; never relabel 92 integration cases as agent tasks | `accomplishment-ia-mcp-real-engine-qualification`; `accomplishment-ia-mcp-agent-evaluations` |
| Leadership timing | Exact start of CMN GUI lead responsibility, separate from 2022 code milestones and April 2023 formal promotion | `leadership-cmn-gui`; `exp-arm-senior` |

Local history coverage includes every reachable ref available at the captured HEAD,
with representative deep implementation review. Additional remote/unreachable history
would require a separately authorized source collection; it is not silently assumed.

## Gaps after direct NoC history review

The 2026-10-29 [NoC research](arachne-noc-research.md) establishes historical model
implementation and integration. It preserves earlier owner confirmations and keeps
these narrower outcome questions separate:

| Area | Useful follow-up evidence | Record/source reference |
| --- | --- | --- |
| Safety-model outcomes | Original fault-campaign/simulator logs, criteria, detected/missed fault categories and measured coverage; configured repetitions are not completed runs | `accomplishment-interconnect-safety-parity`; `accomplishment-interconnect-write-ecc`; `accomplishment-interconnect-fault-injection-integration` |
| Production RTL acceptance | Source and acceptance evidence for any separately claimed DUT implementation, synthesis/lint/formal results or certification; do not erase existing owner-confirmed RTL experience | `project-arm-rtl-vip-rotations#safety-rtl`; `project-arachne-noc#ownership-boundary` |
| Monitor correctness | Historical tests for IDs, ordering, tracker capacity, timestamp rollover and reset/backpressure; no clean-tool or all-corner-case guarantee from a source fix | `accomplishment-interconnect-hang-detection` |
| Enumeration impact | Original extraction/site inventories and measured omitted-site or time improvement; recursion limits are not benchmarks | `accomplishment-interconnect-register-enumeration` |
| Rotation dates and outcomes | Exact individual rotation boundaries, later deployment/use and disclosable product/customer impact; current source retention does not establish active use | `project-arm-rtl-vip-rotations`; `project-arachne-noc#current-use-boundary` |
| Release validation | Actual end-to-end result logs for December 2024 module selections, distinct from commits titled Testing | `project-arachne-noc#release-setup`; `project-interconnect-architect#noc-release-integration` |
| Stashed debugging | Separately preserved landed change, ownership and actual validation before treating the August 2026 candidate patch as delivered | `project-arachne-noc#stashed-work-boundary`; `src-arachne-history-2026-10-29` |

The older internship question about authored UVM coverage models remains distinct
from this verified NoC safety-integration work. Formal titles, waveform-viewer use
and the internal/public product-naming boundary remain as previously confirmed.

## Gaps after direct shared-AI review

The 2026-10-29 [shared-AI research](shared-ai-research.md) adds direct implementation
and local-history evidence with Michael’s explicit repository-wide attribution.
These remaining gaps concern outcomes/currency, not an unresolved author filter:

| Area | Useful follow-up evidence | Record/source reference |
| --- | --- | --- |
| Release state of working-tree features | Dated landed/released versions and representative completed uses of current local-module, packaged-process, qualification and editor changes | `project-ai-harness#direct-review-scope`; `src-shared-ai-working-tree-2026-10-29` |
| Current acceptance | Actual host-native and cluster/provider acceptance against current source/dependency/contract identities; four older complete publication manifests do not certify it | `accomp-ai-module-publication#operational-history`; `accomp-ai-isolated-agent-verification` |
| Qualification completion | Complete current renderer/unit/matrix artifacts and consistent terminal manifests; retain September 21 interrupted evidence | `accomp-ai-gui-qualification#retained-interruption` |
| Repair outcomes | More distinct patch-bound runs, skipped/retried/failed cases, intervention/time measurements and denominator; do not sum duplicate replay records | `accomp-ai-jenkins-repair#retained-run-evidence`, `#gate-semantics` |
| Adoption and measured benefit | Dated user/team/workflow usage and measured before/after effort or latency; several engineers is already confirmed qualitatively | `project-ai-harness#design-adoption`; `project-ai-workbench#inspection-concurrency` |
| Predecessor history | Authorized original umbrella/subtree history if needed; migration-doc hashes are absent locally and the initial publication is squashed | `src-shared-ai-history-2026-10-29`; `src-shared-ai-history-patches-2026-10-29` |
| Native helpers | Dated live packaged-docs and multi-monitor checks; source/test definitions alone do not establish executed outcomes | `accomp-ai-packaged-docs-smoke`; `accomp-ai-native-window-placement` |
| Evidence portability | Back up and restore ignored private source captures with their registered hashes before relying on another clone | `sources/private/shared-ai-review-2026-10-29/`; `sources/registry.json` |

The explicit exclusion of the shared-AI root workspaces directory remains in force.
This review does not reopen earlier IA/NoC attribution, degree/title corrections,
Codex ownership boundaries or the separate historical 92-case integration baseline.
