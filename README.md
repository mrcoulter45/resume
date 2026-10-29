# Michael Coulter — Career Knowledge Base

This repository separates original evidence, granular career knowledge, and tailored
applications. Codex or another agent can analyze a job, retrieve evidence, choose a
positioning, and write a résumé with a claim-by-claim audit trail. The core workflow
requires only Python 3.9+: no API, database, subscription, or Python packages.

Start with [AGENTS.md](AGENTS.md) and [the workflows](docs/workflows.md).

The October 27 Interconnect Architect research adds direct local Git/source evidence,
expanded contribution records and [27 achievement/narrative options](docs/interconnect-architect-contributions.md).
Read [the research scope and reconciliation](docs/interconnect-architect-research.md)
for attribution, historical metrics and validation limits.

The October 29 NoC history review adds [safety-verification and tooling achievements](docs/arachne-noc-contributions.md)
covering parity/ECC models, protocol-progress monitors, generated fault-injection
integration and register enumeration. Read [its research scope and attribution](docs/arachne-noc-research.md)
for complete local-history coverage, collaborative evolution and evidence gaps.

| Location | Purpose |
| --- | --- |
| `sources/registry.json` | Evidence paths, SHA-256 fingerprints, authority, revisions and extraction relationships |
| `sources/originals/` | Immutable imports, including the previous root README résumé |
| `sources/inbox/`, `sources/private/` | Ignored staging and optional private evidence; back up private files separately |
| `knowledge/` | Independent JSON records for experience, projects, accomplishments, skills, credentials, leadership and additional experience |
| `applications/<company>/<role>/<date>/` | Job description, requirements, selection, résumé, match analysis and trace manifests |
| `schemas/`, `templates/`, `prompts/` | Data contracts and reusable authoring workflows |
| `scripts/career.py`, `tests/` | Validation, ingestion, retrieval, assembly and regression checks |
| `docs/` | Architecture, evidence rules, workflows, migration and open questions |
| `resume-output/` | Preserved earlier résumé builder and PDF/Markdown outputs |
| Root career documents, `source-archive/`, `LinkedIn-Profile-Export/` | Registered legacy evidence retained in place |

```sh
python3 scripts/career.py validate
python3 scripts/career.py search "Python MCP checkpoint rollback" --limit 5
python3 -m unittest discover -s tests -v
```

The preserved example uses a **fictional opening and documented real career facts**.
Its prior claim trace now has expected drift after the evidence expansion; review
and deliberately refresh it before treating the audit as current:

```sh
python3 scripts/career.py match applications/example-labs/staff-ai-developer-tools/2026-10-27
python3 scripts/career.py audit applications/example-labs/staff-ai-developer-tools/2026-10-27
```

Read its [résumé](applications/example-labs/staff-ai-developer-tools/2026-10-27/resume.md),
[match analysis](applications/example-labs/staff-ai-developer-tools/2026-10-27/match-analysis.md)
and [claim trace](applications/example-labs/staff-ai-developer-tools/2026-10-27/claims.json).

To add information, say: “Ingest this project description into my career knowledge
base. Preserve the source, reconcile existing records, and flag unknowns.”

For a job, say: “Use my complete career knowledge base to create a tailored résumé
for this job description. Include a job-match analysis and trace every claim.”

The agent does the semantic analysis and writing. The CLI retrieves candidates and
assembles reviewed text; its ranking is not an ATS score or hiring probability.
Markdown is canonical. [Export instructions](docs/workflows.md#exports) cover optional
DOCX/PDF tools and the existing professional PDF pipeline.

These files include personal data and private employer context. Nothing uploads or
publishes them. Review access and diffs before committing. Source hashes establish
identity, not independent career verification. See [evidence rules](docs/evidence.md)
and [migration notes](docs/migration.md).
