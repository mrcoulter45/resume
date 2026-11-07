# 24-hour job and resume campaign

This branch hosts the cumulative ranking, job database and tailored application documents. Preserve earlier results and expired jobs. Run fresh official-job searches hourly. Strict geography: Austin metro, Tampa metro, or fully US remote. Only pursue credible total annual compensation above $286,000, distinguishing public RSUs, private equity, cash bonus and guaranteed salary.

Read `AGENTS.md`, `docs/evidence.md`, `docs/workflows.md` and `knowledge/`. Use only public confirmed/reported career facts. Do not invent scope, percentages, revenue, or training of AI models; do not submit applications or contact recruiters. Deduplicate by company/requisition/URL, and revise resumes only when evidence shows meaningful improvement.

The first cycle creates researched Markdown drafts with evidence references and a cumulative ranking. The local `scripts/career.py validate/build/audit` workflow and PDF/DOCX export checks still need execution in an environment with a full checkout. Do not claim they passed. Track each hourly iteration in `runs/`. The final run should add `final-summary.md`.
