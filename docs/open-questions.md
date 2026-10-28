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
