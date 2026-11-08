# Comprehensive job-specific résumé review — 2026-11-08

This review covers **all six live-employer job-specific résumés** found on `main` at audit time (commit `b026223e4ca2911c4ebfd8b16712bb7b81e1e2e2`). Each now has a separate preserved, manually reviewed revision in `2026-11-08-reviewed/`: `resume.md` (candidate-facing), `job.md` (condensed target) and `review.md` (critique, mapped evidence and remaining gaps).

The older revisions, generated `selection.json` files, source records and campaign tracking have **not** been modified. A real posting was not available for `applications/example-labs/` because it is explicitly fictional; that example is excluded from candidate competitiveness claims.

| Employer / position | Reviewed version | Hiring competitiveness, evidence-based |
| --- | --- | --- |
| Hightouch — Software Engineer, AI Agents | [resume](hightouch/software-engineer-ai-agents/2026-11-08-reviewed/resume.md) · [review](hightouch/software-engineer-ai-agents/2026-11-08-reviewed/review.md) | Good technical agent/backend fit; less proven customer-facing LLM marketing-data product experience |
| Hightouch — Staff Engineer, AI Productivity | [resume](hightouch/staff-engineer-ai-productivity/2026-11-08-reviewed/resume.md) · [review](hightouch/staff-engineer-ai-productivity/2026-11-08-reviewed/review.md) | Very strong direct AI-developer-tooling alignment; cloud-agent fleet and staff-scale rollout gaps |
| Netflix — Senior Software Engineer L5, N-Tech (JR43443) | [resume](netflix/n-tech-productivity-experience/2026-11-08-reviewed/resume.md) · [review](netflix/n-tech-productivity-experience/2026-11-08-reviewed/review.md) | Strong app, backend and shared-AI tools; AWS/GCP operations and enterprise SaaS integration unproven |
| Netflix — TV Developer Lifecycle Test Infrastructure (JR42270) | [resume](netflix/tv-developer-lifecycle-test-infrastructure/2026-11-08-reviewed/resume.md) · [review](netflix/tv-developer-lifecycle-test-infrastructure/2026-11-08-reviewed/review.md) | Strong CI reliability/Playwright; production device-fleet and distributed orchestration gaps |
| Netflix — Visualization Engineer 5, AI Infrastructure (JR41877) | [resume](netflix/visualization-engineer-ai-infrastructure/2026-11-08-reviewed/resume.md) · [review](netflix/visualization-engineer-ai-infrastructure/2026-11-08-reviewed/review.md) | Strong complex visualization and full-stack delivery; GraphQL/cloud-cost analytics gaps |
| NVIDIA — Distributed Systems / EDA Infrastructure (JR2024825) | [resume](nvidia/eda-infrastructure-senior-software-engineer/2026-11-08-reviewed/resume.md) · [review](nvidia/eda-infrastructure-senior-software-engineer/2026-11-08-reviewed/review.md) | Excellent EDA user-domain connection; production fleet operations not demonstrated |

## Common high-impact findings

1. Earlier drafts often gave equal weight to different AI tools and omitted useful differentiated backend/product or infrastructure detail. Revisions order and distinguish contributions according to each employer's actual responsibilities.
2. The Netflix N-Tech draft omitted the full April 2020–April 2023 software-engineering role, losing years of real React, Flask, SQL, data modeling and services evidence. This has been repaired.
3. Several draft bullets recited mechanisms without conveying why the design was difficult. New bullets emphasize safety gates, typed plan compilation, isolation, failure provenance, data-model complexity and explicit scope.
4. Functional CMN GUI leadership is clearly represented without promoting the formal job title to Staff or assigning ownership of Arm's entire application.
5. All quantitative statements are tied to their correct meaning: three clean repair replays are a gate; 56 is a defined 28×2 fixture matrix, not 56 passing tests; 35 is a configured host advisor pool, not a managed compute fleet.
6. No unsupported employer-wide adoption, revenue, LLM production fleet, speedup or cloud platform operations were invented.

## Audit boundaries

These new revisions are human-authored Markdown rather than output of the `career.py build` command; the predecessor source selections and manifests were deliberately not overwritten. Manual claim maps document factual support. No automated `validate`, `audit`, PDF/DOCX export, visual QA or external ATS acceptance test was run in this environment. Do not mistake Markdown review for those checks.

Live job listings were researched using employer URLs and indexed copies on 2026-11-08. Compensation and vacancy status are not offers or guaranteed open headcount. In particular, Hightouch's $180k–$400k base range spans below the current $286k benchmark; NVIDIA's cited $184k–$287.5k L4 base needs equity/level verification. Netflix's cited $388k–$558k ranges vary by location and compensation election.

Prior to application, verify contact information and actual submission format. When a checkout is available, migrate revisions into `selection.json` with every claim cited, run `career.py validate/build/audit`, then export and visually review a single-column DOCX/PDF. Do not substitute keyword volume for hiring qualifications.
