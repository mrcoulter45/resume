# Migration — October 27, 2026

The starting repository already contained career résumés, detailed AI/interconnect
contribution analyses, direct owner corrections, original Word/LinkedIn materials,
award/release images, prior QA and a curated PDF/Markdown builder. These were used
as evidence rather than replaced with synthetic career history.

The initial normalized inventory has 88 records and 226 individually cited facts:
7 employment records, granular project/accomplishment/leadership entries, 18 skills,
education/awards, additional experience and city-level application identity. The
26 registered source files retain their source classifications and limitations.
New imports and future corrections can extend this without reorganizing directories.

Existing evidence stayed in place because many prior artifacts use its paths and
line numbers. The old root README was a career résumé; its exact bytes are preserved
at `sources/originals/README-before-knowledge-base.md`. The new README is navigation.
Its source ID is `src-legacy-profile`, and old `README:line` references mean this
immutable copy. The earlier October 20 snapshots remain separate historical evidence
containing superseded wording; they are never new current career claims.

Only two existing files changed: the root README and
`resume-output/validate_resume.py`. The validator has a small evidence-path adapter
so its old README source keys, hashes and correction audit still resolve the
preserved profile. Its checks and the existing résumé builder/content/output files
remain intact. No existing PDF or generated résumé content was rebuilt or edited.

`sources/migration-inventory-2026-10-27.json` records the initial file fingerprints,
the preserved README mapping and the deliberate validator adapter. It is historical
audit data, not an evidence source for career claims. The current source registry
performs ongoing integrity checks. Prior QA reports describe their own dated work,
not tests or visual review performed during this migration.

The example application pairs real documented career facts with an explicitly
fictional job opening. All automated-test career data lives under `tests/fixtures/`
and temporary test repositories, never in authoritative `knowledge/`. No API, model
provider, external database, subscription, publication or Git commit was introduced.

Normalized records are a granular first pass over the supplied evidence, not a
claim that every career detail is known or independently verified. Original detail
remains retrievable. Open questions document missing measurements, dates and context.
