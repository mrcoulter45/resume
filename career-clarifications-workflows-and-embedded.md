# Career clarifications: agent repair workflow, notebook storage and FPGA shield

Recorded October 21, 2026 from Michael Coulter's direct statements in the resume chat. These facts supplement the earlier clarification sources and the supplied employer-repository analyses. Michael requested incorporating them into the Netflix application. The original evidence files are preserved.

## 1. Interconnect Architect application stack

Interconnect Architect is an Angular/TypeScript application with a Python backend for SoC interconnect tooling. Angular is also documented in the earlier career sources.

## 2. $repair-jenkins agent-harness skill

- The Jenkins/LSF replay and repair accomplishment describes Michael's $repair-jenkins skill within his agentic coding harness/system.
- After a Jenkins job for headless Interconnect Architect GUI Playwright tests finishes and fails on Arm cluster machines, Codex uses this skill to log into the cluster on Michael's behalf.
- It examines the failing tests in the actual Jenkins checkout, implements fixes and iterates until those specific failing tests pass three times.
- The existing implementation analysis additionally documents the requirement for three consecutive clean replays, recorded-revision checks, isolated repair worktrees, patch/evidence identity and guarded synchronization.
- Changes return to the local checkout for manual review and Git commit/push. The skill is not described as autonomously committing, pushing or publishing a fix.
- Michael uses it frequently and finds it useful. Other GUI developers/testers on his team also use it; their frequency and exact number are unspecified.
- This confirms a real, reused agentic repair workflow. No percentage reduction in failures, measured time saving, patch volume or general autonomous repair success rate was supplied.

## 3. Pelion Jupyter notebook storage

Michael used Kubernetes persistent-storage features together with AWS EFS for Jupyter notebook storage. This supplements the Flask notebook-lifecycle services, PostgreSQL schema design and end-to-end testing already documented in the older resume. Kubernetes storage is direct implementation experience here, not an inferred large-scale Kubernetes operations role.

## 4. Arm Mbed OS FPGA Test Shield

- The project's name was Arm Mbed OS FPGA Test Shield.
- The FPGA contained master/slave testing modules for Mbed board I/O and was integrated into a physical PCB compatible with any Mbed OS board, according to Michael's clarification.
- The FPGA code was Verilog; the Mbed firmware was C++.
- Michael's implementation contributions and contribution to test-shield PCBs are documented in the earlier sources. This clarification does not change the team nature of the 2020 Arm Quality Award or claim sole design of every PCB component.
- This is concrete professional C++ firmware experience from the earlier FPGA work. It does not establish recent C++ specialization, GPU-kernel programming or an unverified performance result.

## 5. Explanation of earlier technical shorthand

Interconnect-Architect-resume.md lines 336-345 reports two successful scoped agent evaluations covering configuration creation and import/modify/diagnose/rollback, plus exact restored-iYML hash equality in the rollback case. It separately reports 92 passing certified-live checks. This resume repository contains that supplied analysis, not the full prompts, trajectories or raw completion record. Do not interpret two scoped exercises as a broad agent-success benchmark, or 92 acceptance checks as 92 agent tasks.

The same analysis, lines 315-333, describes current/legacy Configuration Engine runtime routing and an authenticated legacy Python sidecar with API allowlisting, path restrictions, import-provenance checks and parent-lifetime handling. In plain language, this is a separate helper process allowing ia-mcp to call legacy configuration engines while controlling permitted operations/paths and checking the loaded backend's origin. It is not evidence of a separate company-wide identity platform.
