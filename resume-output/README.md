# Resume artifacts

The application default is **resume.pdf**, a one-page resume. All documents stay local. The original Word/LinkedIn/image/AI evidence is preserved. Two explicitly authorized Markdown source corrections have untouched before-edit copies in source-archive/ and an audit record in qa/source-update-audit.json. No commit, push or publication was performed.

The current Netflix edition incorporates the supplied ia-mcp testing correspondence: 92 real Configuration Engine contract/integration cases are separate from Codex-driven configuration builds and historical rollback validation. See [the current Netflix review](netflix-resume-review.md) and `qa/netflix-testing-accuracy-2026-10-22.json`. Dated sections below describe earlier editorial passes where explicitly identified.

The latest compatibility correction also specifies Python 3.13 control/direct current-backend execution and product-aware routing to an isolated authenticated Python 3.7 subprocess. Current artifact and visual QA is `qa/netflix-runtime-architecture-2026-10-22.json`; the earlier testing/typography records retain their historical hashes.

## Current Netflix edition

The qualification-focused version now states customer-shipped production delivery, operation of the shared Codex harness, automatic persistent engineering memory, stakeholder-driven feature/API work, qualitative licensing value and user-scoped cluster/LSF policies. It preserves the exact ia-mcp testing/runtime distinctions, both monospace identifiers and the one-page 11 pt layout. See [the current Netflix review](netflix-resume-review.md) for every qualification's evidence and limits. Current QA is `qa/netflix-role-fit-2026-10-22.json`. Older dated records retain historical artifact hashes.

## Files

| File | Purpose |
| --- | --- |
| `resume-netflix-agent-platform.pdf` / `.md` | Netflix Agent Platform: production software, shared Codex harness and persistent memory, ia-mcp outcomes, stakeholder/API delivery, cluster safeguards and software/hardware breadth. |
| `resume-openai-codex-agents.pdf` / `.md` | OpenAI Codex Agents: execution/evaluation, clean Codex verification, failure replay, Rust/context tools and stateful product workflows. |
| `resume-anthropic-claude-code.pdf` / `.md` | Anthropic Claude Code: React/Rust desktop/CLI architecture, agent tools, UI performance, VS Code and test infrastructure. |
| `resume-google-agent-architecture.pdf` / `.md` | Google Enterprise AI Platforms and Agent Architecture: platform decomposition, topology migration, state, compatibility and semantic comparison. |
| `netflix-resume-review.md` | Netflix-only adoption revision: claim provenance, editorial tradeoffs, hiring-manager review and remaining operating/measurement gaps. |
| `application-resumes-review.md` | Exact job links, hiring-manager assessments, claim provenance, editorial changes and remaining evidence gaps for the four company-specific versions. |
| `resume.pdf` / `resume.md` | Primary application resume and matching plain Markdown. |
| `resume-ai-systems.pdf` / `.md` | AI platform architecture, bounded MCP validation, concurrent workspaces, CI repair, release integrity and isolated agent verification. |
| `resume-systems-engineering.pdf` / `.md` | Complete CMN GUI ownership, original NCI/NoC canvas/console, migration, OWO constraints, placement, Pixi.js/Playwright creation and FPGA background. |
| `resume-senior-software.pdf` / `.md` | Rust/Tauri/React architecture, concurrent workspaces, Python migration, original NoC canvas/console, Pixi.js/Playwright creation and async correctness. |
| `resume-two-page.pdf` / `.md` | Technical alternative with CMN ownership, original NoC tools, platform/release architecture, MCP validation, advanced NoC workflows and earlier history. |
| `resume-content.json` | Canonical content, common employment history, bullet/source mapping and version selections. Edit here. |
| `build_resume.py` | Complete editable PDF/Markdown generation source, equivalent to a TeX source deliverable. |
| `../career-clarifications-netflix-fit-2026-10-22.md` | Direct qualification clarifications (`ROLE_FIT`, source 21): production delivery, shared Codex workflows, APIs, stakeholders, automatic memory and cluster policies. |
| `master-career-profile.md` | Comprehensive career inventory, evidence register, historical context and uncertainties. |
| `resume-review.md` | Editorial assessment, track fit, provenance and evidence gaps. |
| `../source-archive/ia-mcp-testing-correspondence-2026-10-22.txt` | Verbatim user-supplied work-agent correspondence (`TESTING`): exact 92-case classification, historical passing baseline and current testing inventory. Registered source 19; no employer tests rerun. |
| `../source-archive/ia-mcp-runtime-correspondence-2026-10-22.txt` | Supplied work-agent correspondence (`DUAL_RUNTIME`): Python 3.13.9 control/current-engine runtime and isolated legacy Python 3.7.15 execution. Registered source 20; truncated final link retained as supplied. |
| `../career-clarifications-agent-impact-and-e2e-2026-10-22.md` | Reported hours-to-days manual debug baseline, autonomous repair loop, actual module-install/Codex/NCI/CMN build tests, and limits of the supplied impact/evaluation evidence. |
| `../career-clarifications-grouping-and-runtime-2026-10-22.md` | Direct evidence for the accompanying workbench, backend fallback emphasis, and Python 3.13/3.7 backend compatibility; requested grouping. |
| `../career-clarifications-workflows-and-embedded.md` | Direct evidence for Angular, $repair-jenkins/Codex workflow and reuse, Kubernetes/EFS persistence, Verilog modules and C++ shield firmware. |
| `../career-clarifications-2026-10-21.md` | New direct evidence: shared harness and ia-mcp adoption, harness features, about six years of external product shipping, twice-monthly internal releases and qualitative licensing value. |
| `../career-clarifications.md` | Direct user evidence; authoritative product naming, ongoing CMN GUI Lead ownership and Tower/Twain feature mapping. |
| `qa/source-update-audit.json` / `../source-archive/` | Authorized source corrections and preserved original Markdown snapshots. |
| `claim-manifest.json` | Generated claim provenance for each resume. |
| `validate_resume.py` | PDF integrity, extraction, reading order, geometry, font/link and source-protection checks. |
| `qa/` | Extracted PDF text, rendered page previews, source extraction, validation results and visual-review record. |
| `qa/linkedin-source-review.md` / `qa/linkedin-profile-extracted.txt` | Supplied export reconciliation, visual certificate observations and complete exact three-page text extraction; linkedin-profile-normalized.txt separately applies the corrected application name. |

## Generation approach

No `pdflatex`, `xelatex`, `lualatex` or `tectonic` was installed; the normal macOS TeX installation paths were also absent. ReportLab provides a working, reproducible local generation route without an uncompiled TeX dependency. Body fonts are the Bitstream Vera family bundled with ReportLab, embedded with Unicode mappings. Inline code uses the included `fonts/DejaVuSansMono.ttf`, with its license in `fonts/LICENSE-DejaVu.txt`. No system font files need to be copied or redistributed.

To style an identifier in monospace, add a `code_spans` list to its canonical claim, for example `"code_spans": ["repair-jenkins"]`. Each entry must appear exactly once in the claim text. The builder embeds the monospace font at the existing body size and exports Markdown backticks; the validator verifies the PDF font and matching Markdown formatting. The identifier-only typography edition is recorded in `qa/netflix-ia-mcp-monospace-2026-10-22.json`; the testing-accuracy review below still describes the unchanged factual content.

The PDFs use US Letter, a single column, a 10.5 pt accomplishment font with 13.6 pt leading (11 pt with 15.4 pt leading in the two-page alternative), half-inch side/top margins and right-aligned dates drawn as normal text. Contact/skills/education metadata is approximately 10 pt; the long URL row is 8.6 pt. There are no tables, images, text boxes, logos or icon fonts in the resumes. Section rules are simple vector lines. Tables in the supporting Markdown documents do not affect the resumes.

## Exact commands in this workspace

From the repository root:

```sh
cd /Users/michael/Documents/resume
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/build_resume.py
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/validate_resume.py
```

Build one version after editing its content:

```sh
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/build_resume.py --version resume-ai-systems
```

Build only the four company-specific application versions, then validate all available resumes:

```sh
cd /Users/michael/Documents/resume
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/build_resume.py --applications
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/validate_resume.py
```

For example, regenerate just the Netflix application with `--version resume-netflix-agent-platform`, or OpenAI with `--version resume-openai-codex-agents`. Each application's `versions` entry controls its claim selection, skill groups, scope, preparation date, recognition placement, optional `summary` / `summary_sources`, optional `skill_sources`, font/leading and omitted portfolio/capstone links or content. Netflix-only claims use `netflix_` IDs so editing them does not rewrite bullets shared by the other applications. The common identity, role history and full degree/focus remain shared. Do not change the global preparation date solely to revise one application; use that version's `prepared_date`.

Render every final page for visual review, using the installed Poppler tools:

```sh
cd /Users/michael/Documents/resume/resume-output
mkdir -p qa
pdftoppm -scale-to 1800 -png -singlefile resume.pdf qa/resume
pdftoppm -scale-to 1800 -png -singlefile resume-ai-systems.pdf qa/resume-ai-systems
pdftoppm -scale-to 1800 -png -singlefile resume-systems-engineering.pdf qa/resume-systems-engineering
pdftoppm -scale-to 1800 -png -singlefile resume-senior-software.pdf qa/resume-senior-software
pdftoppm -scale-to 1800 -png resume-two-page.pdf qa/resume-two-page
pdfinfo resume.pdf
```

For a separate machine with Python 3.10 or later:

```sh
cd /path/to/resume-output
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build_resume.py
.venv/bin/python validate_resume.py
```

The validator expects the five earlier career documents, all six LinkedIn export files, career-clarifications.md, career-clarifications-2026-10-21.md, career-clarifications-workflows-and-embedded.md, career-clarifications-grouping-and-runtime-2026-10-22.md, career-clarifications-agent-impact-and-e2e-2026-10-22.md, the two source-archive snapshots and qa/source-update-audit.json; copy the full repository if rerunning source-protection checks elsewhere. Eighteen evidence files, including the October 21 workflow and October 22 runtime/grouping and impact/test-flow clarification sources, have registered fingerprints; unrelated .DS_Store metadata is excluded. `build_resume.py` itself needs only ReportLab, the script and the JSON file. Poppler is only needed for rendering (`brew install poppler` on macOS). Package versions are pinned to the versions actually used.

## Editing and safety against layout regressions

1. Edit `resume-content.json`, preserving evidence references and common role dates. Update `prepared_date` when preparing a new edition; it sets deterministic PDF metadata. Do not hand-edit generated Markdown/PDF files.
2. Run the builder and validator. An overflowing paragraph stops generation; the script never silently shrinks the body font or truncates content.
3. Render the changed PDFs and inspect the actual PNGs. Fix wrapping/content before delivery. Automated extraction checks alone do not validate appearance.
4. Reconcile any new claim with the master inventory and review. Change source fingerprint baselines only after deliberately updating original sources and recording why.

Validation checks annotation targets, not email deliverability, ownership of profiles, or a proprietary ATS's ranking. Destination availability observations, if any, are recorded separately in `qa/link-checks.json`.

## Which version to submit

Use the primary for general applications. Choose the corresponding one-page targeted version when the role's work aligns with that track. Use the two-page alternative when a systems/EDA or tooling hiring manager requests more technical context. It preserves worthwhile breadth but is not the default. See `resume-review.md` for the evidence and limits behind these choices.

For agentic systems applications, read the [October 21 career and resume audit](agentic-career-audit-2026-10-21.md). The AI version is the closest starting point, but the audit recommends surfacing actual agent execution/evaluation and choosing product or infrastructure evidence for the specific role. It includes current employer-posted compensation examples, portfolio findings and an evidence-gathering checklist; it does not change the current resumes.

The four company-specific versions now implement those editorial recommendations for their named postings. **Use the matching company-specific PDF for these four applications.** Each is one page with 11 pt accomplishment text and a 9.4 pt professional-link row, omits the portfolio and older capstone award, and preserves the 2025 AI recognition. Netflix now places its award before the current-role accomplishments and adds a two-line summary; the other three keep the award after the accomplishments. The five earlier general/track versions retain their existing content and PDF bytes. The [application review](application-resumes-review.md) and `qa/application-resumes-reproducibility.json` record the new selection, visual QA and factual limits; the older `qa/visual-review.md` and `qa/reproducibility.json` refer to the five general versions.

## Product-context revision of the four application resumes

The current four open with Interconnect Architect, its Python/TypeScript stack, SoC interconnect configuration and internal/external users. Role-specific AI achievements remain prominent, with larger product ownership and correctness accomplishments supporting the transition into agent engineering. CMN ownership appears earlier; the Anthropic version also includes original NoC topology-editor/console creation and combines related UI quality work.

The workspace allocator is omitted from all four application selections following Michael's annotation. Its source evidence remains in the career inventory and earlier general versions. CI repair is a separate supported accomplishment that uses Git worktrees. No design-defect conclusion was recorded.

All four retain 11 pt accomplishment text, the existing margins, one-page layouts and unchanged contact/history/education. The previous application edition's QA record is preserved in `qa/application-resumes-before-context-revision.json`; `qa/application-resumes-reproducibility.json` describes the current edition.

## October 20 AI System revision (before ownership clarification)

The new source is integrated into the existing Arm Senior Software Engineer role. The primary replaces physical-placement, Electron/Karma and request-reload bullets with modular AI platform architecture, Jenkins/LSF repair and Rust/Tauri workbench implementation. Existing application and hardware contributions remain available in targeted versions, the two-page alternative or the master profile. Each selected new claim uses `AI:start-end` provenance in the generated manifest. Four packs mean configuration scope, three clean replays mean a finalization gate, and 56 cells mean a regression fixture; none is silently converted into adoption or live-pass counts. New test-definition counts are preserved in the master profile rather than used as execution results in the resumes.

## LinkedIn export incorporation (before ownership clarification)

All three profile pages and all five images were reviewed. Each version now includes the December 2025 Engineering AI Showcase Most Innovative Award and its multi-agent/context-system topic, PCB contributions and explicit team-award wording, plus the capstone award's exact Industry category. The scope names Interconnect Architect's internal engineers/external customers; AMBA/SoC knowledge is selected where relevant. That initial export pass retained the existing dates and degree wording; the direct education clarification below subsequently corrects the degree and adds both focus areas. The one-page font/margins remain unchanged. At that stage product-release photos were context without an individual role; the direct ownership clarification below resolves that gap. The award is a separately documented 2025 recognition, not proof that all 2026 platform features existed at that date. Provenance uses `LI:p1-3` for PDF pages and named image IDs with `:visual` for certificate observations.

## October 20 direct ownership and product clarification - current edition

Michael's direct statements are saved in `../career-clarifications.md`, which takes precedence over older assistant interpretations. The primary now leads with all CMN GUI tooling from CMN-800 onward and shows **CMN GUI Lead** beneath the unchanged Senior Software Engineer title. This covers Multi-CHI port devices, MCS groups, custom routing and deadlock detection interfaces. Original NCI/NoC logical canvas and configuration/DRC console creation now replaces the generic editor description. The primary's CI-repair bullet moves to the AI/two-page alternatives to make room. Body sizes, margins and page counts remain unchanged.

The systems/software alternatives emphasize the confirmed original canvas/console, Pixi.js introduction and Playwright infrastructure creation; the systems version retains OWO and placement depth. The AI version retains its six focused platform accomplishments plus the common CMN GUI Lead responsibility. The two-page alternative adds fuller NoC workflow evidence. Qualification fixtures and packaged-agent details remain in the master profile and selectable canonical claims when omitted from a page.

The private inventory maps Cyprus to CMN-800; Delphi to subsequent CMN features; Tower to original NCI/NoC tooling and AMBA-to-GT bridges; and Twain to newer NoC configuration, placement, diff, rendering and test infrastructure. Application PDFs omit the internal codenames. Product-family mappings do not backdate 2026 features to 2023 commemorative dates.

Use **Interconnect Architect** consistently in future updates. The working README and interconnect analysis were corrected under Michael's explicit authorization; their prior versions are preserved in source-archive/ and audited by hash. The original LinkedIn PDF/raw extraction are historical evidence, while the labeled normalized text applies the corrected application name. Earlier application-name and release-role uncertainties are resolved. Measured adoption/performance and individual rotation dates remain separate open evidence questions. Waveform-viewer use is resolved: Michael debugged Verilog testbenches, RTL designs and IP source code using existing viewers during RTL/VIP rotations and the Mbed OS FPGA test shield work. The root README line 44 is corrected; the systems and two-page resumes now include the debugging detail, and it has been removed from unresolved-question lists.

## Waveform debugging and rotation context

`../career-clarifications.md` sections 1 and 5 are authoritative: waveform viewers were used for debugging, not created. The private master profile records Chariot as the older/lightweight interconnect safety-mechanism RTL context, and VIP as virtual Arm IP / bus functional models used in large testbench simulations. Internal Chariot naming does not appear in application PDFs. Existing compact one-page FPGA bullets retain their module/firmware/PCB/award emphasis; the two-page version expands that bullet with waveform debugging. Historical snapshot wording is explicitly rejected in `../source-archive/README.md`; it is not an unresolved career question.

## Education clarification - current credential

All versions use **Bachelor of Science, Electrical and Computer Engineering**, **The University of Texas at Austin**, **December 2018**, with **Primary focus: Computer Architecture and Embedded Systems** and **Secondary focus: Integrated Circuits**. This direct confirmation in `../career-clarifications.md` section 6 supersedes the shorter historical Computer Engineering degree wording and the earlier LinkedIn interpretation. Focus areas are not described as separate degrees or minors. The shared `education.degree` and `education.focus` fields in resume-content.json generate the same facts in every PDF/Markdown; the validator checks both. The additional education line fits without changing body fonts, margins or page counts.

## Netflix-only adoption and product-impact update

The latest Netflix version leads with the shared coding-agent harness used by several Arm engineers, then the separate internal ia-mcp interface and its bounded evaluation results. The scope states about six years of external Interconnect Architect shipping and twice-monthly internal releases; CMN ownership includes qualitative licensing-business value. It keeps authenticated backend compatibility, CI repair and Rust/Tauri/React architecture. Migration and release automation remain in the inventory and other versions rather than this application.

The [October 21 clarification source](/Users/michael/Documents/resume/career-clarifications-2026-10-21.md:1) is registered as `CURRENT`; the master profile and reviews reconcile it with the older repository snapshots. Only Netflix content was revised. All other eight PDF/Markdown resume pairs retain their prior bytes. The role summary's "nearly 8 years" refers to full-time engineering beginning January 2019 as of October 2026; update that phrasing when preparing future applications.

Edit `versions.resume-netflix-agent-platform` for its summary, scope, recognition and skills. Edit its `netflix_` claim texts for the newly tailored accomplishments. Existing `app_` claims can be shared across applications: check their selections before editing them. Rebuild and validate:

```sh
cd /Users/michael/Documents/resume
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/build_resume.py --version resume-netflix-agent-platform
/Users/michael/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 resume-output/validate_resume.py
pdftoppm -scale-to 1800 -png -singlefile resume-output/resume-netflix-agent-platform.pdf resume-output/qa/resume-netflix-agent-platform
```

Open the resulting PNG after every layout/content change. The existing `regen-resumes` shell alias still rebuilds all four applications and runs validation. [The Netflix review](netflix-resume-review.md) explains current choices; `qa/netflix-testing-accuracy-2026-10-22.json` records the current final checks and unchanged-artifact comparisons. `qa/netflix-impact-e2e-revision-2026-10-22.json` and `qa/netflix-adoption-revision.json` document preceding editions. The prior application QA is preserved as `qa/application-resumes-before-netflix-adoption-revision.json`.

## Netflix workflow and embedded clarification

The latest Netflix PDF names Angular, promotes the team-used $repair-jenkins Codex skill immediately after the shared-harness accomplishment, and explains the legacy backend bridge in plain language. It describes Kubernetes persistence backed by AWS EFS and identifies the Arm Mbed OS FPGA Test Shield with Verilog master/slave test modules and C++ firmware. C++ is also in the Netflix skills list; the job lists Python plus one of several languages, including C/C++ or Rust, rather than requiring both. Kubernetes is named in the posting's preferred stack.

The two reported bounded evaluations are phrased as two scoped configuration workflows; the 92 live acceptance checks remain a separate result. Full prompts and trajectories are not in this resume repository. Supporting facts and interpretation are in `../career-clarifications-workflows-and-embedded.md` (`WORKFLOW` evidence ID). Only Netflix resume content changed; the other eight PDF/Markdown pairs are unchanged. Its source is still the canonical JSON plus build_resume.py, and the same rebuild commands apply.

## Netflix grouping and Python compatibility - October 22

Netflix now presents the shared harness as a main bullet with the agentic tools/$repair-jenkins and accompanying Rust/Tauri workbench as indented sub-bullets. A separate ia-mcp main bullet has indented verification and Python 3.13/3.7 compatibility details. CMN ownership remains a main bullet. The verification wording emphasizes backend fallback; historical rollback hashes, two scoped evaluations and 92 live checks remain in the career inventory rather than the current Netflix text.

`versions.resume-netflix-agent-platform.senior` remains an ordered list of claim IDs. Its `claim_parents` map assigns each supporting claim to a main claim; keep children immediately after their parent, with no intervening main claim. The builder indents child markers/text by 18 pt and writes ordinary four-space Markdown sub-lists. The validator checks contiguous grouping, manifest agreement, Markdown indentation and actual PDF marker coordinates. Every bullet keeps the same 11 pt font and 14.2 pt leading.

The source ID `RUNTIME` points to `../career-clarifications-grouping-and-runtime-2026-10-22.md`. Only Netflix content changed; the other eight resume pairs retain their prior bytes. Current verification is `qa/netflix-grouping-revision-2026-10-22.json`; earlier QA files describe their dated editions. Rebuild commands and the existing shell alias are unchanged.

## Netflix focused refinement - October 22

The latest Netflix version restores 92 live acceptance checks and exact rollback-hash restoration alongside two scoped agent evaluations, keeping those results separate. It sharpens the harness around shared/project boundaries and source-verified knowledge capture, displays the skill name as repair-jenkins, names direct CMN ownership/capabilities, and distinguishes the product's roughly six-year release history from current-role tenure. Notebook persistence is described through Kubernetes storage backed by AWS EFS.

This is a content-only revision: the same canonical JSON, builder, grouped selection, regeneration commands and fonts apply. No new source facts, production operating claims or framework keywords were added. All 17 career evidence files are preserved. Current review/QA: `netflix-resume-review.md` and `qa/netflix-surgical-revision-2026-10-22.json`. The preceding grouped edition is preserved in `qa/netflix-before-surgical-revision-2026-10-22.json` and `qa/application-resumes-before-surgical-revision-2026-10-22.json`.

## Preceding Netflix edition: impact and end-to-end testing

The latest Netflix resume incorporates `../career-clarifications-agent-impact-and-e2e-2026-10-22.md` as source `IMPACT`. It describes autonomous flaky-test diagnosis/fix/retest against a reported hours-to-days manual baseline, retaining three consecutive passes and manual patch review. No automated elapsed time or percentage reduction is invented.

The ia-mcp verification bullet now explicitly installs the tooling module on Arm's cluster, invokes Codex with ia-mcp registered, and generates/builds valid NCI/CMN configurations. The separately reported 92 acceptance checks and two scoped evaluations remain distinct; 92 is not a count of Codex tasks. The skills line names MCP, typed plans, semantic validation, checkpointing, rollback and knowledge provenance, grounded in the accomplishment corpus. It avoids unsupported general-orchestrator or tracing-platform claims.

The older FPGA bullet is shortened to Verilog I/O test modules, C++ firmware and the proper shield name. Full PCB/master-slave/compatibility and team-award details remain in the master profile and other resume versions. The one-page format, 11 pt body, margins and project grouping remain intact. Only Netflix resume content changes; all other eight resume pairs retain their bytes. That edition's QA is `qa/netflix-impact-e2e-revision-2026-10-22.json`.

## Netflix testing-accuracy edition

The user-supplied work-repository correspondence is preserved verbatim at `../source-archive/ia-mcp-testing-correspondence-2026-10-22.txt` and registered as `TESTING`. All 18 previous evidence files retain their fingerprints; validation now checks 19 registered sources.

The 92 cases are automated contract/integration qualification against the real Configuration Engine, recorded passing on September 4, 2026. Codex-driven evaluations and installed-module configuration builds are separate. The reporting agent inspected source and the historical baseline without rerunning tests. This resume update also makes no new employer-test execution claim.

The Netflix testing bullet retains the 92 result, actual Codex-driven cluster-module builds and exact configuration-hash restoration from a rollback evaluation. It drops the fixed evaluation count because the older two successful evaluations and the current three scenario definitions are different evidence; the latter does not prove three current passes. The full overlapping-tier inventory, manual campaigns, deferred agent flows and local/cluster distinction are preserved in the master profile, not added as larger resume metrics.

Edit `claims.netflix_evals` in the canonical JSON to change this bullet. The same build, validate and render commands above apply. The final PDF remains one page with 11 pt body text, unchanged margins and the same grouped bullets; the other eight resume pairs retain their bytes. Current review is `netflix-resume-review.md`; current QA is `qa/netflix-testing-accuracy-2026-10-22.json`. Its before-state is `qa/netflix-before-testing-audit-2026-10-22.json`.

## Preceding Netflix edition: ia-mcp runtime architecture

Edit `claims.netflix_backend_bridge` for the runtime accomplishment. The Python 3.13 server/control layer runs current engines directly; product metadata routes legacy engines to an isolated authenticated Python 3.7 subprocess. Exact-version checks constrain supported runtimes: the supplied correspondence qualifies Python 3.13.9 and legacy Python 3.7.15 specifically. Patch versions, dependency isolation, import/product/session checks and process-lifecycle controls are preserved in the master profile; the resume keeps a readable two-line architecture statement.

The `DUAL_RUNTIME` source is preserved separately; all 19 earlier evidence files remain unchanged. This revision retains both `ia-mcp` monospace spans, `repair-jenkins` monospace, the testing distinction, one-page format, 11 pt body and grouped hierarchy. The other eight resume pairs remain unchanged. The existing regeneration commands apply. Current QA is `qa/netflix-runtime-architecture-2026-10-22.json`, with before-state in `qa/netflix-before-runtime-architecture-2026-10-22.json`.

## Editing the Netflix qualification-focused version

The canonical source remains `resume-content.json` plus `build_resume.py`; generated Markdown and PDF are rebuilt. Edit `versions.resume-netflix-agent-platform` for the summary/scope/skills, and its selected `netflix_` claim entries for accomplishments. Keep source references and `code_spans` metadata. The existing `regen-resumes` alias still works; the exact Netflix-only build/validate/render commands above also apply.

ROLE_FIT is the newest evidence source; all 20 previous registered source files retain their bytes. Workbench detail and the MCP introduction were shortened to fund cluster policies and stakeholder/API evidence; the older backend and C++ accomplishments remain. Body font, leading, margins and grouped hierarchy are unchanged. All other eight resume pairs remain unchanged. Current review is `netflix-resume-review.md`; current QA is `qa/netflix-role-fit-2026-10-22.json`, with before-state in `qa/netflix-before-role-fit-2026-10-22.json`.
