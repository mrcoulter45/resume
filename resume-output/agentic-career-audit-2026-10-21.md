# Agentic systems career and resume audit

Reviewed October 20–21, 2026. Recommendations reflect the career evidence available in this repository and the employer postings inspected during this review. Posting availability and compensation can change.

## Later clarification and implementation

This audit preserves its original evidence assessment. Subsequent direct evidence in [career-clarifications-2026-10-21.md](/Users/michael/Documents/resume/career-clarifications-2026-10-21.md:1) confirms several engineers use both the shared coding-agent harness and ia-mcp, plus harness agents/tools/skills/memory/context, roughly six years of customer-facing product shipping, twice-monthly internal releases and qualitative licensing value. The Netflix application now incorporates these facts; see [the updated review](netflix-resume-review.md). Earlier statements below about missing adoption or business evidence should be read as the pre-clarification assessment. Exact measurements and large-scale agent operations remain separate gaps. Other application PDFs are unchanged in this revision.

## Assessment

The record supports a credible senior engineer specializing in **developer tools, agent-facing execution systems, validation and reliable engineering automation**. The strongest differentiator is the combination of substantial engineering-product ownership with typed MCP execution, checkpointing, rollback, isolated workspaces and reproducible CI repair. This is a stronger, more specific story than either “hardware GUI developer interested in AI” or an undifferentiated “AI platform architect.”

The current resumes undersell that story. The AI version is the closest starting point, but its opening emphasizes repository organization and test totals over what agents actually accomplished. The general software version demonstrates product engineering while omitting the strongest agent contribution. The main work is selecting and ordering existing evidence, followed by documenting adoption, operating outcomes and empirical agent quality.

Senior engineering applications are justified. Staff-level applications should be selective: sole ownership and difficult implementation are valuable, while the corpus provides less evidence of sustained cross-team adoption, organization-wide technical influence or operating large production agent services. This is an evidence assessment, not a finding that those experiences did not occur. Employer levels are not interchangeable, and a posted pay ceiling is not an expected offer.

## Scope and limits

Reviewed the working README, 2020 Word resume and extraction, links, complete AI System and Interconnect Architect analyses, career clarifications, LinkedIn PDF/export evidence and reconciliation, source-archive context, master career profile, editorial review, canonical content, all five generated Markdown resumes and all five PDFs. All six PDF pages were freshly rendered and visually inspected; the local validator passed. Reviewed the public portfolio homepage and current employer job descriptions. This was a resume/career audit, not a new audit or execution of Arm source code.

The supplied engineering analyses are evidence about source snapshots; their linked employer checkout paths are not present in this resume repository. Their limitations remain attached to their claims. In particular, the AI inventory explicitly treats the documented implementations as completed and working. Missing adoption or deployment measurements must not be reinterpreted as “the work was merely a personal prototype.” See [AI evidence scope](/Users/michael/Documents/resume/AI-System-resume.md:4).

## Findings, in priority order

### 1. High priority: the first scan routes the reader toward EDA GUI work

Every version opens the current role with “Interconnect Architect | CMN GUI Lead,” followed by a two-line award statement. The primary then leads with coherent-mesh GUI functionality. These are truthful differentiators, but the first visible identity is not the target function for agent tooling roles. The AI version's first accomplishment is a modular platform with four project packs. That describes architecture without immediately demonstrating useful agent behavior.

For agent applications, keep the formal Senior Software Engineer title, lead with agent execution and validation, and use a factual scope line such as “AI engineering tools, MCP execution and developer platforms.” Retain a compact CMN ownership accomplishment as proof of deep product responsibility. Move or shorten recognition so implementation earns the first scan. The 2025 award is useful corroboration, not a substitute for explaining the system.

Evidence: [AI resume opening](/Users/michael/Documents/resume/resume-output/resume-ai-systems.md:10), [primary opening](/Users/michael/Documents/resume/resume-output/resume.md:12), [confirmed CMN responsibility](/Users/michael/Documents/resume/career-clarifications.md:19).

### 2. High priority: the AI resume omits its most direct agent-outcome evidence

Its MCP bullet mentions planning, rollback, 5,063 full-suite passes and 92 live checks. The underlying record is more distinctive: typed intent becomes a dependency-ordered plan, execution is checkpointed, semantic readback checks postconditions, and two bounded agent evaluations exercised creation and import/modify/diagnose/rollback. The rollback evaluation restored the exact configuration hash. The current AI bullet omits those agent tasks and the deterministic execution architecture. The two-page version includes more evaluation detail, but places it near the end of page one.

Lead with the mechanism and observed agent tasks. Keep one well-labeled validation figure if it earns space. Two recorded evaluations are useful case evidence; they are not a representative success-rate benchmark or evidence of unrestricted autonomous design.

Evidence: [execution architecture](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:309), [recorded results and boundaries](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:336), [current AI bullet](/Users/michael/Documents/resume/resume-output/resume-ai-systems.md:17).

### 3. High priority: engineering mechanisms are clearer than adoption and impact

The corpus is unusually detailed about locks, leases, hashes, runtime boundaries, Git preservation and acceptance gates. It does not establish how many engineers use the AI system, how many teams adopted it, how often it completes useful work, or the measured change in task completion time, cost or failure rate. The source explicitly acknowledges these missing measurements. That leaves a hiring manager able to judge implementation sophistication but unable to judge practical leverage.

Preserve qualitative achievements now. Add verified scope and outcomes later: actual users/teams, shipped workflows, runs per week, repeated task results, reduced investigation time, eliminated manual steps, or incidents prevented with a documented comparison. A small, precise internal adoption result is more useful than a large configuration or test count presented as impact.

Keep these distinctions intact:

| Existing number | What it supports | What it does not establish |
| --- | --- | --- |
| Four project packs | Declared configuration/integration scope | Four teams or four deployed users of the platform |
| 5,063 passing full-suite tests; 92 passing live checks | Recorded validation of the bounded MCP implementation | All tests personally authored, current rerun results, or general agent reliability |
| Two successful bounded agent evaluations | Demonstrated completion of the recorded agent tasks | A broad benchmark or a general 100% success rate |
| Three clean replays | A CI-repair finalization requirement | Three incidents repaired, a reliability increase, or measured time savings |
| 4,130 valid / five curated invalid migration cases | Strong recorded migration correctness evidence | Customer adoption or performance improvement |
| Other test-definition counts and the 56-cell fixture | Implemented regression scope | Executed/passing runs unless separately documented |

Evidence: [AI analysis limitations](/Users/michael/Documents/resume/AI-System-resume.md:16), [project manifests](/Users/michael/Documents/resume/AI-System-resume.md:28), [CI finalization](/Users/michael/Documents/resume/AI-System-resume.md:239), [MCP results](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:336), [migration](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:115).

### 4. High priority: distinguish the agent tools you built from the model loop and cloud service

The delivered MCP compiler/executor, isolation, registration, packaging and verification are substantial professional work. The evidence does not document ownership of every part of a general-purpose agent: provider/model invocation, the iterative model–tool loop, durable multi-tenant scheduling, production memory, or a large hosted service with on-call ownership. The shared root orchestrator, executable agent registry and shared evaluation suite are explicitly placeholders; authored knowledge-capture procedures are not an implemented autonomous memory runtime.

The current modular-platform claim is supported. The risk is allowing that phrase or the separate 2025 orchestration award to imply that every later runtime component was implemented and deployed. Be prepared to diagram exactly what you built, what existing agents supplied, and how an agent invoked your tools. Local workspace separation and process cleanup also do not establish a security boundary for hostile multi-tenant code execution.

Evidence: [platform maturity](/Users/michael/Documents/resume/AI-System-resume.md:22), [knowledge workflow versus executable enforcement](/Users/michael/Documents/resume/AI-System-resume.md:403), [working MCP execution](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:315), [context helper boundary](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:363).

### 5. High priority: the linked portfolio does not reinforce the application

The live [portfolio homepage](https://mrcoulter45.github.io/portfolio/) introduces a “Computer Engineer & Creator,” broad interests, phone-control hardware, a web code editor, a three-bit counter, and creator media. It does not explain the professional MCP execution, agent evaluations, isolated workspaces or CI repair that distinguish the resume. A recruiter following that link receives a different emphasis.

For agent applications, link a focused engineering landing page or omit the portfolio link until its first screen reinforces the professional story. A permitted, sanitized architecture case study or independent reproducible agent-tool demonstration would help. Do not publish employer code or internal details to accomplish this. Creative projects can remain elsewhere. The GitHub search view available during review was stale, so this audit makes no claim that the current GitHub account lacks relevant work; review its current pinned repositories before using it as primary evidence.

### 6. Medium priority: older bullets consume space needed for current evidence

Across the one-page versions, approximately 38–41% of accomplishment-bullet words describe the two earlier full-time roles. This excludes headers, skills, awards and education. Their Flask/cloud, sensor and FPGA work establishes breadth, but four older bullets crowd out stronger current agent and product evidence. Meanwhile, interconnect contributions began in 2021 and CMN GUI work in 2022, before the April 2023 promotion, yet the 2020–2023 role lists only the other earlier work.

For an AI application, consider one strong bullet per earlier title, retaining dates and progression. Keep the corrected degree and focus areas. The 2018 capstone award is a lower-priority use of space than current agent execution. Attribute ongoing CMN work as work begun in the earlier role and continued after promotion where space permits; its placement under the current role is not proof that the work started in 2023.

Evidence: [role allocation](/Users/michael/Documents/resume/resume-output/resume-ai-systems.md:23), [contribution window](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:13), [CMN start](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:26).

### 7. Medium priority: product-oriented agent roles need a different blend

The AI version lists Rust, React and Tauri but omits the workbench accomplishment. The software version demonstrates that workbench and asynchronous correctness but omits MCP execution. For a coding-agent product, IDE or developer-experience team, a hybrid is stronger than either current selection: MCP execution/evaluation plus the Rust desktop/CLI core, React/TypeScript UI, workspace isolation and CI repair.

Do not infer expert React specialization merely because React appears in two projects. The source supports concrete application work; a UI-specialist role needs additional evidence of component architecture, accessibility, performance decisions and user feedback.

Evidence: [AI selection and skills](/Users/michael/Documents/resume/resume-output/resume-ai-systems.md:16), [software selection](/Users/michael/Documents/resume/resume-output/resume-senior-software.md:16), [workbench depth](/Users/michael/Documents/resume/AI-System-resume.md:110).

### 8. Medium priority: wording and ordering can become more direct

“Recorded validation lists” and “historical validation recorded” are careful provenance language but read awkwardly in application bullets. Normal past-tense claims can describe recorded results without implying a fresh rerun; retain exact campaign dates and limitations in the evidence register. Expand domain terms when needed, especially before presenting CHI/MCS/NCI/LSF detail to an unfamiliar AI recruiter. Avoid replacing precise mechanisms with generic “AI-powered” adjectives.

The two-page resume offers useful depth but starts with several hardware-tooling bullets and puts MCP execution/evaluation late on page one. It needs reordering before use for agent positions. Its extra length does not solve relevance by itself.

### 9. No new blocking layout or core-fact defect found

All five PDFs passed extraction, reading-order, font, link-annotation, geometry and source-protection checks. Four are one page and the detailed alternative is two; all are US Letter. Fresh inspection of all six rendered pages found no overlap, clipping or missing text. One-page accomplishment text remains 10.5 pt. The URL row is smaller, but not the main obstacle to competitiveness. These checks do not certify proprietary ATS ranking or guarantee that a linked profile's content is persuasive.

The direct corrections remain resolved: Interconnect Architect naming; ongoing CMN GUI Lead ownership; Tower/Twain/CMN feature associations; waveform-viewer **use**, not creation; and UT Austin B.S. Electrical and Computer Engineering with both confirmed focus areas. Do not reopen them as unsupported leadership, viewer authorship or uncertain education. Internal codenames stay out of application PDFs. Evidence: [authoritative clarifications](/Users/michael/Documents/resume/career-clarifications.md), [validation results](/Users/michael/Documents/resume/resume-output/qa/validation.json).

## Recommended use of the existing versions

| Version | Best use | Change for the present goal |
| --- | --- | --- |
| `resume-ai-systems` | Starting point for agent tools, execution/evaluation and developer infrastructure | Put typed execution and actual agent evaluations first; add product UI evidence when relevant; replace lower-value release/configuration detail as needed. |
| `resume-senior-software` | Complex applications, IDEs and developer products | Add MCP/evaluation evidence for agent teams while retaining workbench and async correctness. |
| `resume` | Broad engineering software, EDA and hardware-adjacent applications | Do not treat it as the automatic default for agent positions; its first-scan story is different. |
| `resume-systems-engineering` | EDA, SoC configuration and hardware/software tooling | Strong domain fit; does not by itself establish distributed agent-service or inference-runtime expertise. |
| `resume-two-page` | Requested technical detail or a highly tailored technical application | Move agent execution/evaluation to the top for agent roles; trim older detail before adding more. |

### Source-grounded replacement language to consider

These are editorial proposals, not changes to the current PDFs. They would still need to be selected for a specific job and rendered after editing the canonical JSON.

- Built Python MCP tooling that compiled typed design intent into dependency-ordered plans, with checkpointed execution, semantic readback and rollback for two interconnect workflows.
- Validated agent-driven creation and import/modify/diagnose/rollback in two bounded evaluations; rollback restored the exact configuration hash.
- Built isolated engineering workspaces with dedicated ports, caches and editor state, using atomic allocation locks, tokenized leases and ownership-checked recovery.
- Built Jenkins/LSF repair tooling that replayed failures at the original revision and transferred cumulative binary patches without staging the user's checkout; gated flaky-test fixes on three clean replays.
- Built a Rust/Tauri workbench with a React/TypeScript UI and shared desktop/CLI core, bounded asynchronous Git inspection and process-identity checks.

Provenance, in order: [MCP architecture/results](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:315), [agent evaluations](/Users/michael/Documents/resume/Interconnect-Architect-resume.md:336), [workspace allocation](/Users/michael/Documents/resume/AI-System-resume.md:74), [CI repair](/Users/michael/Documents/resume/AI-System-resume.md:216), [workbench](/Users/michael/Documents/resume/AI-System-resume.md:110). Select rather than concatenate. Retain a compact professional ownership accomplishment and the 2025 recognition where relevant.

## Current role and compensation examples

These are specific postings, not company-wide compensation bands. “Closer fit” means stronger overlap with the documented work, not a prediction of an interview or offer. Quoted ranges are advertised ranges, not independent compensation estimates. Employer wording controls the compensation category.

| Employer and inspected posting | Advertised compensation and location | Assessment against this corpus |
| --- | --- | --- |
| [OpenAI — Software Engineer, Codex Enterprise](https://openai.com/careers/software-engineer-codex-enterprise-san-francisco/) | $230k–$385k base; equity; performance bonuses for eligible employees. San Francisco. | A priority role family: technical product ownership, extensibility, skills and developer workflows. The posting also expects deep production backend/distributed-systems experience; describe that evidence explicitly if available. |
| [OpenAI — AI Systems Engineer, Codex Agents](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/) | $230k–$385k base; equity; eligible performance bonuses. San Francisco. | Strong overlap in tools, execution, isolation and debugging. A selective stretch where model/harness experiments, production observability, latency/cost and inference-stack depth are expected beyond the current record. |
| [OpenAI — Software Engineer, Cloud Agents](https://openai.com/careers/software-engineer-cloud-agents-san-francisco/) | $347k–$445k base; equity; eligible performance bonuses. San Francisco. | Lower priority as documented: posting explicitly requests 9+ professional years excluding internships and large-scale production backend/platform ownership. |
| [Anthropic — Staff Software Engineer, Claude Code](https://job-boards.greenhouse.io/anthropic/jobs/5383610008) | Annual salary $320k–$625k. The post does not quantify an equity grant or bonus. SF/NYC/Seattle; hybrid, generally at least 25% in office. | Strong developer-tool theme; use the AI/product hybrid. This particular opening specifically requests expert React and UX specialization, hands-on LLM work and 6+ years. Verify that specialization rather than treating it as a generic backend-agent role. |
| [Anthropic — Staff+ Software Engineer, Claude Managed Agents](https://job-boards.greenhouse.io/anthropic/jobs/5395767008) | Annual salary $405k–$485k. SF/NYC; hybrid policy. | Stretch: 8+ years of backend/distributed/infrastructure work and operating durable, stateful production systems. Workspace/tool isolation transfers conceptually, but does not prove hosted multi-tenant sessions, streaming or durable scheduling. |
| [Google — Software Engineer, Enterprise AI Platforms and Agent Architecture](https://www.google.com/about/careers/applications/jobs/results/91999936312156870-software-engineer-enterprise-ai-platforms-and-agent-architecture?q=agent) | $207k–$300k US base + 20% target bonus + equity. Sunnyvale. | Selective stretch: 8 years of programming experience, enterprise agent-platform architecture and integration. Knowledge graphs/ontologies and enterprise runtime scope are not established here. |
| [Netflix — Software Engineer 5, Agent Platform, AI Platform, JR41100](https://explore.jobs.netflix.net/careers/job/790316292023) | $466k–$750k advertised compensation range, location dependent. Remote US; posting dated October 19, 2026. Annual salary/options allocation; no bonuses. | Worth investigating for the exact work, but a stretch on present evidence: production tool-using agents, evals/tracing, distributed operations and measured outcomes; typically 8+ years. The gap is production scope more than a few months of tenure. |
| [Meta — Software Engineer, Multimedia & Multimodal AI](https://www.linkedin.com/jobs/view/software-engineer-multimedia-multimodal-ai-at-meta-4473441079) | $183,997–$257k base + bonus + equity + benefits. Menlo Park. Employer-authored LinkedIn listing. | Not a priority match: significant media-modality and training/evaluation-pipeline depth is central. Its agentic-workflow wording alone does not make it a good fit. This is not a conclusion about all Meta teams. |

OpenAI and Anthropic descriptions were read on their employer pages. Google's detailed posting and Netflix's JavaScript-rendered description were read in the live browser; a text-only fetch did not expose their complete content. The Meta example is Meta's own advertisement on LinkedIn; a corresponding direct Meta application page was not independently verified. The cached Google Applied AI Agent Studio full-stack result was **not** retained as an active target because its live page said the job was unavailable. Do not assume a search snippet proves an opening is still live.

For Meta, prioritize team-specific searches in developer infrastructure, AI product engineering, coding tools and agent evaluation rather than using the multimodal example as the target. This review did not establish a currently open, closely matched Meta role with a verified comparable pay band. For Google, agent developer tools and platform/product teams are a better starting category than automatically choosing ML-training or research roles. Evaluate each actual requirement list.

### Compensation strategy

Netflix specifies annual salary with an annual choice of salary versus stock options and no bonuses. Treat its range as that compensation arrangement, rather than adding options and bonus to a presumed $750k base. Confirm allocation terms during recruiting. [Netflix posting](https://explore.jobs.netflix.net/careers/job/790316292023)

Compare offers using separate fields: guaranteed annual cash; target and actual bonus terms; annual vesting of equity and its instrument; vesting/cliff and refreshers; one-time sign-on; work location; and liquidity/exercise terms. “Equity,” RSUs and options are not interchangeable. Keep private-company equity separate from spendable cash rather than assuming a future valuation. A high base is a legitimate goal, but salary maxima across different locations and levels are not an apples-to-apples ranking.

As of October 2026, the recorded January 2019 full-time start gives approximately **7 years 9 months**, plus the separately labeled internships. Do not combine internships into a claim of 12 years of full-time engineering experience. Do not exclude yourself automatically from every 8-year posting, but honor explicit minimums and application questions. The stronger argument for a high offer is demonstrable ownership and useful outcomes at the offered level, not stretching dates or assigning a staff title to yourself.

## Highest-value evidence to add

These are follow-up opportunities, not unresolved corrections to the already confirmed degree, ownership or product names. Record dates, measurement method and a source for each answer; use qualitative wording when a reliable number does not exist.

1. **Real use:** Which AI tools/workflows are used today, by whom, how frequently, and on what real engineering tasks? Separate personal use, colleague trials, team adoption and external customer availability. Identify the actual release/rollout date where there is one.
2. **Agent boundary:** Which model/provider and agent client were used? Which loop, context-building, tool-selection and retry components did you implement? Which were supplied by Codex or other existing tooling? Record the 2025 award system separately from the later components and their dates.
3. **Evaluation:** Preserve the two bounded evaluations with task definitions, initial state, model/client/version, expected outcomes, traces and failure cases. Add repeated representative tasks and measure success, manual interventions, rollback correctness, latency and cost where appropriate. Do not turn unit-test totals into model-quality metrics.
4. **Operational responsibility:** If applicable, document API/service deployments, users, durable state, concurrency, identity/permissions, monitoring, incident response and reliability objectives. State which were local tools, cluster jobs or hosted services. Do not add Kubernetes, Temporal, RAG or a framework just to match a posting.
5. **Engineering value:** Before/after CI-investigation time, setup time, reproducible failures, release effort or configuration errors. Existing logs and issue records may support a retrospective measurement; identify any sample limitations.
6. **Influence:** Who adopted your interfaces, designs or standards? What technical decisions did you drive across teams? What did you teach, review or enable others to deliver? CMN GUI Lead is already confirmed; additional evidence should describe its engineering effect rather than inventing people-management duties.

## Recommended next sequence

1. Tailor the one-page AI selection around execution/evaluation, workspace/CI reliability and the product evidence demanded by one real opening. Preserve the common employment history and corrected education. Keep one strong hardware-domain ownership signal.
2. Gather existing usage and operating evidence before adding more architecture bullets or new project names. This is the largest opportunity to strengthen senior/staff and high-compensation positioning.
3. Align the linked public materials with that narrative, using only publishable material. A clean-room independent demonstration is an option if work examples cannot be shared; it supplements professional work rather than replacing it.
4. Prepare interview explanations for typed planning versus model planning, failure recovery, ownership validation, rollback semantics, evaluation design, and desktop/CLI architecture. Practice general coding and system design alongside the specialist story.
5. Apply across a mix of developer-tool/product roles and a smaller set of ambitious harness/platform roles. Reassess openings by actual scope and level rather than company name or headline pay alone.

## Audit artifact and QA record

This audit adds this report and a discovery link in the artifact README. It does not alter resume claims, canonical content, source evidence, PDFs or generated resume Markdown. The existing edition's PDF hashes still match `qa/reproducibility.json`; the validator passed for all five. All six pages were freshly rendered to temporary images and opened for visual inspection. No proprietary ATS was tested. No commit, push, application submission or public publication was performed.
