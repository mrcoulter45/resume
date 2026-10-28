# Historical results and attribution supplement

PRIVATE local Git evidence captured 2026-10-27 at e24d80378096cb8d7a0ad87c20929cb520fa49d7. Historical reports below were read, not executed. Commit author dates do not imply shipment dates.

## guided-results
```text
commit 32939448d1a9a1f084701f320870daa4e0aa408e
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Thu Oct 1 15:48:19 2026 -0500
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Thu Oct 1 15:56:12 2026 -0500

    consolidate Guided Flow coverage across supported IPs
    
    Consolidate nine Guided Flow specs into four focused suites covering
    launcher, import, policy, and lifecycle behavior.
    
    - Run common scenarios on nitwain_r1p0 and towernci_r0p0/r1p3/r1p5
      using matching starters, metadata, and applicable policy controls.
    - Keep complex recovery permutations on representative Nitwain fixtures
      and route NIC400 scenarios according to supported migration choices.
    - Exclude unsupported IP revisions and mismatched scenarios during
      collection to avoid unnecessary Electron launches.
    - Move GUI interactions and lock assertions into reusable POM methods.
    - Validate metadata reactivation, accessible unlock state, and Canvas
      refresh through each IP's supported controls.
    - Derive the vertical runner's default projects from CE policy and the
      Playwright matrix, preserving explicit project overrides.
    - Update coverage documentation and capability-routing validation.
    
    Validation:
    - Complete NoC-Lite vertical runner passed.
    - All 79 Guided executions passed across the four supported IPs.
    - Overall Playwright: 132 passed, seven existing competing-load skips.
    - CE: 105 passed, nine missing-fixture skips; nine NIC400 fixtures audited.
    - Angular: 522 passed; both renderer builds passed.
    - Focused lint, formatting, capability, and shell checks passed.
    
    Change-Id: I3c8f5ab3b48a8dd3b74a6bff6aabc93ae0630a57
```

## migration-results
```text
commit f0e5bb3195676179948595be567624c872686134
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Fri May 8 22:51:19 2026 -0500
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Tue May 12 14:08:14 2026 -0500

    feat(nic400): reconstruct NCI uArch and close DRCs
    
    Add an integrated NIC400 XML/CCXML conversion flow that builds NCI-base IYML in memory, reconstructs source-derived uArch, preserves physical placement, and applies deterministic state-preserving DRC fixes before export.
    
    Map NIC bus matrices to routers, CDC-capable IBs to PCDCs, width-converting IBs to SERDES, reconstruct routes from NIC architecture/connect topology, and log unsupported features plus every DRC-driven IYML mutation in nic400-to-nci.log.
    
    Replace the legacy Tower wrapper with nic400_to_nci_iyml.py, remove obsolete helper scripts, and wire supported raw configs through CE import_design without mutating the source XML/CCXML.
    
    Add the NIC400 pytest package, corpus audit/collection tools, curated 10 valid plus 5 invalid fixtures, standalone wrapper coverage, route/DRC diagnostics, and source-fidelity assertions for endpoint/uArch/path counts.
    
    Validation: PYTHONPATH=CE CE/venv_3_13/bin/python -m pytest CE/pytests/nic400 -q; standalone wrapper pytest; full valid corpus audit 4130/4130 DRC-clean; invalid lane rejected 5/5 curated invalid configs.
    Change-Id: I15aa3911678a2cbd8813735600b24e174c106989
```

## deadlock-origin
```text
commit 4c1307f3aa52cd86cbe46ba7c9b14d866a122f81
Author:     lingao01 <lingao01@arm.com>
AuthorDate: Wed Feb 24 14:16:47 2021 -0600
Commit:     lingao01 <lingao01@arm.com>
CommitDate: Wed Feb 24 14:16:47 2021 -0600

    Move flow implementations to flow_helper directory.
```

## report-resource-pruning
```text
commit 5d3af6fe4d952b8e1ff7a0bef205696436e82a1c
Author:     Tanushi Ahuja <tanushi.ahuja@arm.com>
AuthorDate: Thu Mar 5 14:16:26 2026 -0600
Commit:     Tanushi Ahuja <tanushi.ahuja@arm.com>
CommitDate: Thu Mar 5 14:18:51 2026 -0600

    Prune resources/scripts/reports dir
    
    Change-Id: Ibea6f720de0530d77ce0f15fc093ce6731d0ab2f
```

## completion-baseline
Source: HEAD:ai/docs/agentic-v1-completion.md; SHA-256 21b4b437c9cf172d6b7393a25fec11dc3f86adfcf1cedf35aec90998130fe07d.
```text
# IA MCP Agentic V1 Completion Record

Agentic V1 was completed on 2026-09-04. The implementation is preserved by
`fb6764542de61d70ff7606846e5ad53e77736c31` (`Deliver bounded IA MCP Agentic
V1`), with the final completion record in
`ee717f4711324e81bb8c78717680042035402a01`.

This page is a frozen point-in-time completion record. Its API counts, support
counts, test totals, and evaluation status describe the 2026-09-04 baseline,
not the current working tree. Use the live generated disposition, current
support resource, and current validation reports for present behavior.

The product boundary is defined by
[`agentic-v1-scope.md`](agentic-v1-scope.md). The machine-readable execution
authority is
[`agentic_v1_support.yaml`](../ia-mcp-pack/src/ia_mcp_pack/policy_pack/agentic_v1_support.yaml),
not an API or operation count.

## Delivered Boundary

- Two certified end-to-end workflows: blank-session `nitwain_r1p0` NCI and
  blank-session `cmns4_r1p0` CMN construction.
- Ten exact certified operation profiles, 115 assisted-only operations, and
  fourteen fail-closed operations.
- Forty-five compiler routes classified as five certified-operation routes,
  37 assisted-only routes, two fail-closed routes, and one provider-gated
  route.
- Typed intent, live capability binding, strict operation schemas,
  deterministic plans, transactional execution, checkpoints, rollback,
  semantic evidence, applicable DRC, explicit CE Python, derived iYML, and
  replay for the exact certified profiles.
- Broad bounded assistance for API, schema, metadata, source, example, DRC,
  Python, and iYML work without turning unproved capabilities into unrestricted
  mutation.

The live CE disposition inventory closed at 450 APIs: 354 mapped, 96 unmapped,
139 reviewed direct operations, and zero API-level fully-supported claims.
That zero is intentional: certification belongs to exact workflow and
operation profiles.

## Final Validation

The final deterministic tiers passed on the completion source:

| Tier | Result |
| --- | --- |
| `fast` | 136 passed |
| `contract` | 2,013 passed; one intentional tamper warning |
| `security` | 733 passed |
| `packaging` | 279 passed; one expected platform skip |
| `full` | 5,063 passed; one expected platform skip and one intentional warning |
| `certified-live` | 92 passed with Python 3.13.9 and Ruby 3.2.2 |

The corresponding run IDs were
`fast/20260904T004504Z`, `contract/20260904T004636Z`,
`security/20260904T005045Z`, `packaging/20260904T005115Z`,
`full/20260904T005705Z`, and `certified-live/20260904T011522Z`.
Source confinement, import provenance, disposition freshness, shell syntax,
skill installation, packaging, security, consolidation compatibility,
checkout boundaries, and temporary-state hygiene also passed.

## Agent Evaluations

The two user-authorized bounded evaluations run during V1 completion used the
configured OpenAI backend through Arm's proxy and passed:

- `nci-certified-create-20260903T230002Z` completed all seven server-owned
  phases, final DRC, CE Python and iYML export, session close, and zero-owner
  checks. Report SHA-256:
  `e7f712d27c71addcc05a6d282ddbafa61e464fe85d2c16a32336bc8445531175`.
- `nci-import-modify-diagnose-20260904T003410Z` imported the first run's iYML,
  proved a clean baseline, attempted the exact `nonPosted=true` mutation,
  diagnosed `HLS_60_1`, rolled back, passed restored final DRC, exported iYML,
  closed, and reached zero owners. Report SHA-256:
  `f102cd6a0332473361fce8568d28a790f8ee27a3f3d09b12482b4727f8c8ac39`.

The restored iYML SHA-256,
`504eea50849f405a6d7ee013974ed9f9f8315f37b576757ba42d59ee0f3b25a2`,
exactly matched the imported input. Imported sessions intentionally do not
claim CE Python replay because they lack server-owned blank-session
construction history.

The first evaluation exposed a checkpoint-restore defect involving an already
restored CTB/interface association. The fix now uses exact public
`get_instance_interfaces()` readback, skips satisfied associations, applies
only missing associations, verifies the result, and fails closed on malformed
evidence. Its focused restore tests passed 8, the worker suite passed 270, and
the affected regression shard passed 543.

The evaluation catalog now also contains `cmn-certified-create`, which drives
the exact five-phase `cmn-cmns4-r1p0-m6` construction workflow and requires
managed CE Python, iYML, and CMN topology evidence. This later-added scenario
has not yet been authorized or executed against a model provider, so it has no
passing real-agent result in this completion record.

## Ownership And Remaining Work

The Ideas checkout owns the IA MCP runtime, product configuration,
documentation, acceptance assets, release payload, general configuration
skills and workflow, and tests under `ai/`. Among IA MCP-specific assets, the
shared AI system owns only the explicit module-publication and rehearsal
skills and publication tool; those consume checkout-owned assets through
`IDEAS_REPO_ROOT`.

No implementation blocker remained at completion. Module publication was not
performed and remains an explicit-only external workflow. Future expansion,
upstream reconciliation, and maintainability work require a separate goal
that explicitly invokes [`post-v1-roadmap.md`](post-v1-roadmap.md).
```

## committer-is-not-author
Local --all committer-name search: 1271 objects committed by Michael Coulter, including 39 authored by others. The latter are integration metadata, not automatically personal implementation. Michael-authored objects committed by somebody else remain in the authored inventory.
```text
b90e3777088add409f64c98c33dbc249b2540b0e | Pawan Kakarla | pawan.kakarla@arm.com | BRUNEL-4532 Include prune_dsign before running NoC-SE and BE
cd280cb2072f32e936fad4726f8e590ac3a086ee | Liza Dayoub | liza.dayoub@arm.com | More display name fixes
2d8bc2ad36ee66c64bf60f97b22feebbf38eda67 | Liza Dayoub | liza.dayoub@arm.com | Update display names
688146f578cb084503081e604cd4cb67d4f8b385 | Liza Dayoub | liza.dayoub@arm.com | Update display names
ef4beddc7c23e0158acfb22d2f962c9b6312860b | Tanushi Ahuja | tanushi.ahuja@arm.com | BRUNEL-4317 Sub-section & SB for - Config network
3bfb7f9efdc385f849b37cb1d7eeeea1a8db2a2e | Pawan Kakarla | pawan.kakarla@arm.com | BRUNEL-4532 Include prune_dsign before running NoC-SE and BE
a7c2a26e15bcdde81ca098e8202d0c1048577bbe | Liza Dayoub | liza.dayoub@arm.com | More display name fixes
385d4e51dc28b9156ea9e321506a2f7870b982aa | Liza Dayoub | liza.dayoub@arm.com | Update display names
03dc2c2fc28789941a5c50eb232130acc78e8087 | Liza Dayoub | liza.dayoub@arm.com | Update display names
e05fd7f2d0f92ab02384e8831d6b757543f1e162 | Tanushi Ahuja | tanushi.ahuja@arm.com | BRUNEL-4317 Sub-section & SB for - Config network
317aa9f71605ca5756f21546a367736083343a63 | Pawan Kakarla | pawan.kakarla@arm.com | fix search e2e tests
7f63df3ce3c1e4d9b7ddbcec13cda1404e9e585b | Christopher Alvarez | christopher.alvarez@arm.com | change basename of output cmn topology file from export method
ad38a136d201b68a3c9d33c73f1bff2f06445604 | Christopher Alvarez | christopher.alvarez@arm.com | cmn export now will export botha brunel iyml and a cmn topology yaml
c6dfec74e953311a3af89a66fb827a6302299ad7 | lingao01 | lingao01@arm.com | Fix report area script
d2256468c1de40917bca45abe54ffe65fa53f9b2 | lingao01 | lingao01@arm.com | Update a retiming bit description
0bb531b0432216e72bec33b5c60bf3c6af059aff | lingao01 | lingao01@arm.com | If FMU is not required but present, it's now a DRC error
07523d3746af787ca0c8fd44f2a29a43b96807bf | Your Name | email.addr@arm.com | Added optional output path to script for consistency with other report scripts
4662cd8a2234d32e72d335ec17495dbaf614d9d1 | Your Name | email.addr@arm.com | Updates for reporting, re: BRUNEL-803
e0f4389b790086546f15f27c1a4017c166ef5060 | Chris Styles | chris.styles@arm.com | updated Domains, Memory maps, and utils for FuSa testing
a29aac01ad5489e140e27a7bb46fab0b3c02394d | lingao01 | lin.gao@arm.com | Update examples
2232ce62f14573acd70c68f9c7c03c81b790f7ae | lingao01 | lingao01@arm.com | Update docs
4af0932847aecc326785b64ebc845d0066534ea2 | lingao01 | lingao01@arm.com | Change MCI protocol to DMC and SLC
7794e13ca5b4408dbcd19b5a55b47278fc3f7ba8 | lingao01 | lingao01@arm.com | Fix a broken pytest
0d4be158362466f7e6d08759b9cace78311ff5bf | Kelly Alvarez | kelly.alvarez@arm.com | 48 Hour Bug Fixes Interface table serperated delete to end of table Updated Text to DRC modal , shows rule broken Memory Region Editor Sync Fix, ngOnInit was being called twice Test And Report Config Logger responsivness improved Can Changed Memory Map Name now Checkpoint Updated to have support for config_file_path launch
940dd9c86f5c7ee7f5313d905abb9040d65f93b7 | Dustin Divis | dustin.divis@arm.com | [GUI] Canvas: Adding button to toggle sidebar to sidebar
1aff2c634cb334a0558bb638d2d60c09e87d52b9 | lingao01 | lingao01@arm.com | Add adaptor/mbistPipeDepth
81e5fa82df4d8123a192485646b30b1f69eaad10 | Victor Benarbia | victor.benarbia@arm.com | add CMN configuration space into Brunel start implementing CMN topology import $ pytest -v pytests/cmn
19b964d2a8266b42baeb86cca6822f855cc7639b | Victor Benarbia | victor.benarbia@arm.com | cmn device/bridge classification
950ddb9e3bb64de3cfb381d346aa202fb7062e6a | Victor Benarbia | victor.benarbia@arm.com | improve default_params_cmn.yaml - update display name. e.g.  display: CHIX_REQ_ADDR_WIDTH  desc: Width of ADDR field in REQ flit - remove interfaces section
c0d5d08426f5bce132746e35bd09583ba1e41233 | Victor Benarbia | victor.benarbia@arm.com | add CMN configuration space into Brunel start implementing CMN topology import $ pytest -v pytests/cmn
1c3aee589733ece6f600da71736ff89c7dd369af | Victor Benarbia | victor.benarbia@arm.com | basic parameter and busdef import from CMN configuration into Brunel configuration files
4c2897d3cc67d3dc4f3a2f23c8d6c38a4ff7f117 | Victor Benarbia | victor.benarbia@arm.com | first commit to add CMN support
6b4523b181e375fed536fbd038507a8fdc96fa97 | Kelly Alvarez | kelly.alvarez@arm.com | Fixing Inspect Modal Bugs Interface And Stripe inspect modals now correctly update name
bd7567fbcaeb9d909a73cc8dd0b822d5ccf1b57d | lingao01 | lin.gao@arm.com | Change synth command to work with the latest SE
b1496bfd2e05aa0fedec2add7e5b74c2c6576d34 | lingao01 | lingao01@arm.com | Add a check in rename_instance to disallow renaming of implicit units
b067911931cd39b555c62ece8d4731dd1bd934a1 | Kelly Alvarez | kelly.alvarez@arm.com | Updating installer creation Now copy resources directory to root level
dedda3e3cf96fc198ea85f0812949cd4d635441c | lingao01 | lin.gao@arm.com | Fix configs with too small config space
76111a066c58888ac5d88fcc854e1ea469848c58 | lingao01 | lingao01@arm.com | Add pcdc upstream mux support
80f9eec1b3087634870c0de49ac36d36bdad0482 | Kelly Alvarez | kelly.alvarez@arm.com | Adding Features Memory Map Create Default Button Min Stripe Size Hiding master selection from Stripe Groups if no stripes exist.
```
