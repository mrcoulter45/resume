# Complete example

The end-to-end example is stored in
`applications/example-labs/staff-ai-developer-tools/2026-10-27/`, following the same
company/role/date layout used for real opportunities. The company and posting are
fictional. Its career facts are drawn from the documented real knowledge base.

Read `job.md` → `job.json` → `selection.json` → `resume.md` and
`match-analysis.md`. `claims.json` maps every factual résumé line to facts and
evidence. `build-manifest.json` fingerprints inputs and outputs. Run `match` to
retrieve candidates and `audit` to verify the build. No paid service is needed.

Synthetic career data used by regression tests is explicitly labeled under
`tests/fixtures/`; it is never included in the authoritative records or this résumé.
