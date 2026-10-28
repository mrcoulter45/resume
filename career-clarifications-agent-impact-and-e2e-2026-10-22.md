# Career clarification: engineering impact and installed-module agent tests

Recorded October 22, 2026 from Michael Coulter's direct statements in the resume chat. These facts supplement the earlier career sources, which remain intact. Michael supplied them to strengthen the Netflix resume and address feedback about impact, agent evaluation and specific engineering skills.

## 1. Harness and Jenkins repair impact

- The agent harness helps several engineers on Michael's team use Codex more efficiently and effectively.
- Michael reports that the Jenkins repair skill dramatically reduces flaky Playwright debugging effort for GUI and test engineers on his team.
- He describes the manual alternative as taking hours to days and the skill's debugging/repair process as completely autonomous.
- The existing workflow description remains relevant: after invocation, Codex investigates the actual failed cluster checkout, iterates on fixes and reruns the specific tests, then returns patches for human review and commit/push. Three consecutive clean passes are the documented repair gate.
- The autonomous scope is the diagnosis/fix/retest loop. Human invocation, patch review and the local Git commit/push are separate; do not describe these as automatic publication.
- The hours-to-days range is Michael's reported manual-effort baseline, not a timed comparative study. No exact automated elapsed time, average saving, percentage reduction, repair volume or overall success rate was provided. Do not turn the range into a guaranteed time saving for every failure.

## 2. Actual ia-mcp end-to-end test flow

Michael describes the full test flow as:

1. Install the internal tooling module with ia-mcp enabled on the Arm cluster.
2. Invoke Codex with ia-mcp registered; registration is part of module installation/ia-mcp setup.
3. Execute a Codex prompt that uses ia-mcp to create entire valid NCI and CMN configurations and verify that the configurations build successfully.

This establishes an installed-module, live Codex/tool integration test flow with configuration and build outcomes, rather than only a direct-backend API test. It does not establish a broad repeated agent benchmark, trajectory collection, model/configuration ablations, fleet-scale hosting or production reliability metrics.

The historical source separately reports 92 passing live acceptance checks and two scoped agent evaluations including exact rollback-hash restoration (Interconnect-Architect-resume.md:336-345). Do not assume every one of the 92 checks is an end-to-end Codex prompt or equate the two historical evaluations with one NCI and one CMN case. The supplied new flow has no new run count, success percentage or model/version details. Configuration builds are not relabeled as silicon tapeout, synthesis results or full hardware verification.

Current installation/use of the internal module is directly confirmed here. This does not retroactively establish module publication at the earlier September completion milestone or prove every proposed publication/acceptance lane ran.

## 3. Evidence for a more specific skills line

Michael requested using the accomplishment corpus for precise skills. Existing sources support MCP/tool integration, typed plans, semantic/execution validation, checkpointing, rollback and knowledge provenance. Relevant sources include Interconnect-Architect-resume.md:315-345 and AI-System-resume.md:43-71, 147-176, 403-430. The general root orchestrator and shared evaluation placeholders in the October 5 snapshot are not promoted into a completed general agent runtime. No new framework, tracing platform, distributed-memory implementation or production scale was asserted.
