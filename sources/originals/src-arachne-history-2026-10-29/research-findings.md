# NoC contribution findings — Michael Coulter — 2026-10-29

PRIVATE analyst findings from read-only local Git/source inspection. These are reported source interpretations, not new owner confirmations, independent employer verification, or new simulation results. Public application language belongs in normalized public facts and the achievement library. Internal names, paths, emails and raw code remain research context.

## scope

The inspected repository is `/Users/miccou01/GitProjects/sysip_shared_ai/workspaces/arachne-noc/slot_01/checkout/arachne_noc`, branch `dev`, HEAD `c13c1beb89b07b46afd963706bb5d941ea4d36d0`. The repository is non-shallow and initially clean. All 2,316 locally available refs were inventoried; no fetch, checkout change, product edit, build, simulator, formal tool, environment/module activation, publication or outside upload was performed. Entire-history coverage here means all locally reachable Git history, not deleted/unreachable objects or a claim of remote freshness.

The 101,139 locally reachable commit objects include 89,162 in selected HEAD ancestry. Searching author names/emails for Coulter and the miccou account finds 22 objects: 21 with `Michael Coulter <michael.coulter@arm.com>` and one with the same author name and a local account email. Thirteen ordinary authored commits are ancestors of HEAD; seven ordinary commits are on other locally available release histories; two objects are a stash and its empty index snapshot. No other-author objects match Michael as committer. Author dates span November 3, 2020–August 13, 2026, but ordinary authored commits end December 17, 2024. These dates do not establish rotation boundaries, title tenure, or shipment dates.

All 20 ordinary authored diffs were inspected, including the one-line maintenance commits, repeated/reapplied patches and source/generated YAML collateral. The two stash objects were separately inspected and excluded from delivered-work claims. All nonempty ordinary patches have 17 distinct stable patch IDs: January's reapplication repeats one patch, and two pairs of release-branch version edits repeat two others. These are patch identities, not accomplishments. The seven release objects are absent from HEAD ancestry, and their five patch identities do not match any of the 49 nonmerge HEAD changes to the same loader path; this does not rule out differently shaped or squashed equivalents.

## architecture

This is a configurable SystemVerilog interconnect IP repository with Python parameter/configuration generation, stitched RTL and generated testbench bindings, shared UVM/VIP simulation components, formal/fault-site tooling and implementation/release collateral. Relevant use cases are configuring requester/subordinate interfaces, exercising protocol traffic, injecting faults into a design, observing corruption or stalled transactions and selecting a configuration-tool version for end-to-end validation. Reading those components establishes context, not Michael's authorship of the entire IP, parameter engine, UVM infrastructure or simulation environment.

The contribution path crosses input/generated configuration YAML, an Arm Engine service option, internal Python build objects, Python-generated `wrapper_connect.svh`, SystemVerilog generators/checkers at interface boundaries, testbench-level error aggregation and an existing UVM fault-injection scoreboard. Netlist traversal provides an adjacent fault-site inventory capability. The modules added by Michael live under `logical/noc_arachne/validation/dynamic/top/components/chariot/`; their location and connections establish testbench-side safety verification mechanisms, not shipment of DUT datapath RTL.

## preserved-owner-evidence

The existing `project-arm-rtl-vip-rotations#safety-rtl` fact is owner-confirmed, and `src-clarifications:L53-L61` identifies the older lightweight non-coherent interconnect and waveform-debugging experience. Retain those facts and their original citations. This repository adds concrete implementation evidence for the validation-side part of that work; it does not disprove broader owner-confirmed design experience or establish undisclosed production RTL work. Waveform viewers remain tools used, not tools authored. Exact rotation dates and public product mapping remain unestablished.

## parity-origin

Michael's `492593a8f1b7a15c8f12174cda9bcf7cfd7f6c8b` (December 9, 2020) adds the initial `chariot_parity_generation.sv`, `chariot_parity_checker.sv` and package, instantiates generation/checking in `testbench.sv`, routes write-user error-detection bits through `noc_testbench_wrapper.py`, and connects the checker result to the existing safety-interrupt interface. The generator masks unstrobed data bytes and forms odd parity; the checker gates mismatch reporting with validity. The source configuration and expanded generated YAML belong to the same integration, not separate personal feature inventions.

## request-protection

In `8452bb85684afd82d80cdc2e90a7d3296dacaf4c` (January 25, 2021), Michael extends an existing write request/response model to AXI/ACE-Lite read address/response paths and AHB request validity, including generated ARUSER/RUSER binding changes. Sean Steel authored the earlier write request/response support in `2d1718066b9a38b5f333bf08106716ff9aa10b94`; do not attribute those entire modules to Michael. Sean's `99937b8c02a02511fba7c67e602dce610aca453e` reverts Michael's change, and Michael reapplies the same patch in `41d2221e7973c21437e040d51dbe75cbf73ed3c0`. Reapplication is evolution of the same work, not another achievement.

Michael adjusts protected-address slicing in `0061d5b19fa53c919287bfa6ccc9150edba032df` and `d8e7d9edefe1c18d2cb15669cc682d7375d6c900`. The actual source range evolves to `addr_i[ADDR_WIDTH-1:15]` at that milestone. Earlier subjects mentioning a protected-bit count do not establish universal address coverage across widths; later colleagues further extend protection to protocol attributes.

## read-parity

`ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012` (January 29 author date; February 6 commit date, 2021) introduces `chariot_rdat_parity_generator.sv` and `chariot_rdat_parity_checker.sv`. With the integration's two safety bits, each eight data bits has a parity bit and a marker bit in the user sideband. The checker accounts for response-sideband offset and reports only when valid; AXI and AHB integrations supply their different transaction-validity conditions. Python wrapper generation concatenates read-data and response codes for AXI and provides the AHB read sideband. These two module blobs survive in the captured HEAD, while the surrounding testbench is collaborative.

## invalid-lanes

The same `ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012` changes `amba5_slave_controller_component.svh` to request `INVALID_BYTE_LANES_RANDOM`, supplying random zero/one values instead of Xs on invalid read-data lanes. This is an actual stimulus-model decision supporting meaningful parity computation in this context. It is not a measured X-propagation improvement, proof of complete X-safety, or authorship of the full slave controller.

## ecc-design

`2cb79d4081f5d79cd0aba93217e2c121b4e6348f` (February 24 author date; March 4 commit date, 2021) introduces `chariot_wdat_ecc_generator.sv` and `chariot_wdat_ecc_checker.sv` and replaces write-data parity instances in AXI/ACE-Lite and AHB interface branches. Each 32-bit data chunk receives six positional check bits and overall odd parity, plus the then-marker bit in an eight-bit user field. The generator masks inactive bytes, places data/check bits in a Hamming-style arrangement and XORs set-bit positions to derive the check values. The checker reconstructs the codeword and uses syndrome/overall parity to expose error, single-bit-location and double-bit indicators. This is stronger technical depth than merely listing ECC as a skill.

## ecc-integration

Michael's ECC introduction adds per-interface ECC aggregation through `interface_block.sv` and `testbench.sv`, combining ECC with parity and hang errors at the shared safety interrupt. The initial interface instances leave the detailed single-/double-bit outputs unconnected and consume the aggregate error output. The evidence therefore supports write-data ECC stimulus/checking and error observability in the testbench, without claiming that Michael delivered live data correction or consumed every diagnostic output.

## ecc-collaboration

Current ECC checking is collaborative. Sean's `e1382ca03cf1858b5d74e8fd472dcdadc4f59098` changes strobe indexing, and `f2603804d15af6e69ba074c082ed08639c0d6195` introduces correctable/uncorrectable outputs, a correction-bit vector, strobe-parity encoding and correction integration. Additional Sean fixes include `44793ed9c17389e739907a2e90c0fb8f0cf5d7a1` and `8e334abdefabadf66d4bf72040ca3c16ebfde876`. Michael authored the original ECC generator/checker pair, not every current correction behavior. No simulator, synthesis, formal proof, diagnostic coverage or certification result was recovered or rerun to establish exhaustive ECC correctness.

## ahb-hang

Michael's `3ba56bea53a1b7e239c7f609ef88bf8b60e83829` (February 19 author date; February 25 commit date, 2021) adds a parameterized AHB hang detector that counts consecutive low-ready cycles, clears on ready/reset and exposes a timeout error. Interface and top-level changes aggregate that error into the existing safety interrupt. This extends the verification path to non-progress as well as data corruption.

The commit subject says 1,000 cycles, but its actual interface macro is 100,000; `5d88abb380368baa73f3e9e2b8b6f4d2033aa398` later changes it to 400,000. Treat the timeout as configurable. Do not publish a 1,000-cycle latency or derive a detection-speed improvement from the subject. The scoreboard delay changes from 1,000 to 5,000 in the February commit; it is a configured observation/reporting window, not a measured saving or achieved detection latency.

## axi-hang

Michael introduces `chariot_axi_read_hang_detector.sv` in `5d88abb380368baa73f3e9e2b8b6f4d2033aa398` (March 26 author date; April 1 commit date, 2021), then generalizes it to `chariot_axi_hang_detector.sv` in `c22154dd2c2f91d60d1f15c6b83053be63a708eb` (April 7). The parameterized tracker records accepted address requests, IDs, validity and coarse timestamps. Completion handshakes remove a matching outstanding entry; cyclic two-bit epoch comparisons select older matching candidates and flag aged entries. Generalized address/completion ports let the same model serve AR/R and AW/B, with RLAST on read completion and a constant terminal condition for B responses. This demonstrates protocol modeling, outstanding-transaction bookkeeping, state-machine reasoning and reuse, not the invention of AXI.

## latch-fix

In `996cb7d4e7b7ab29b5478dd39bffaf0fe802495a` (April 8, 2021), Michael supplies the missing `hang_detection_state = IDLE` assignment in the combinational idle branch. This addresses the specific incomplete-assignment latch problem identified in the commit. Credit the concrete state-machine correction; do not turn it into an unobserved clean lint/synthesis result or claim every tracker corner case is proven correct.

## hang-evolution

Jordon Kashanchi's `cde13afb3503f64717b468bdd38ca846f8465063` (August 2021) renames Michael's generic monitor to `chariot_axi_hang_detector_write.sv` (98% similarity in Git's rename view) and introduces a separate read monitor with beat-counting behavior. The current write implementation retains Michael's tracker and idle-state correction, with later collaboration visible through blame. The current read beat-counter implementation and later full integration are not solely his. Inspect historical additions and the explicit rename diff; automatic `--follow` can infer spurious unrelated predecessors for small/deleted files.

## current-top-lifecycle

Ariel Paling's `cb3d526eb8f49e7ed3e09fcb146aea535587417a` (August 2022) removes the legacy safety-model instances and conditional interrupt aggregation from `interface_block.sv` and `testbench.sv`, with a change toward fault-injection use when an FMU is present. At captured HEAD, those legacy model files and package survive as source, while the selected top-level safety interrupt observes `fmu_fault_int | fmu_err_int | fmu_cri_int`. Thus survival of Michael's model blobs and current blame do not establish active use by this top-level simulation path. Describe the work as historical implementation/integration, without claiming current regression execution, retirement of every possible use, or authorship of later FMU infrastructure.

## generated-integration

The December 2020 implementation propagates a safety-mode option through `arm_engine/services/param_engine/param_engine.sm`, `noc_core_build.py`, `noc_internal_build.py` and `noc_external_bindings/noc_testbench_wrapper.py`. The result selects generated error-code bindings instead of ordinary VIP USER connections. January read-path work extends those bindings for AXI/ACE-Lite and AHB. This is configuration-driven cross-language integration between Python generation and SystemVerilog verification models; it is not authorship of the entire parameter engine or a standalone new RTL-generation framework.

## payload-checking

The December integration adds safety-mode conditional handling and a `check_user` guard in `amba5_payload_checker_component.svh`. Ordinary payload comparisons cannot treat generated safety bits as arbitrary user payload; the change selects whether user comparisons apply while retaining data checking. This is a protocol/testbench consistency decision. The same commit also changes simulation-summary waiver strings for UVM report summaries; do not treat broader message suppression as proven error-detection quality or coverage improvement.

## fault-scoreboard

The fault-injection scripts and scoreboard predate Michael's major integration: Sean's `bce47a50cf9fee013517d4bb33f71c70d4f730f1` introduces fault-injection scripts, and `c53d65457f8e62c88e46411fd533cf491782caeb` adds the scoreboard. Michael connects newly observed parity, hang and ECC errors to its virtual interrupt interface and changes its wait/report window. Credit integration and the bounded modification, not creation of the complete fault-injection framework, random fault selection, report catcher or UVM itself.

## test-definitions

`492593a8f1b7a15c8f12174cda9bcf7cfd7f6c8b` changes the control-file configuration and adds simulator full-access selection for fault injection; it defines a parameter-engine → flop-list → scenario-generation → simulation path. Current control files reflect later collaborators' changes, including fault-site naming and mode flags. `--repeat=100`, `--uvm=num_txs=1000`, phase limits and run-time settings are definitions, not evidence of 100 successful campaigns, 1,000 completed transactions or a passing regression. No raw run logs or pass-rate outcomes were found in Michael's inspected commit evidence.

## register-enumeration

Michael's `4df3354cc2c16df21f6cfeddf2cb3bcef3efac32` (November 5, 2020) refactors the preexisting `logical/shared/scripts/fusa/qverify_get_flops.tcl`. It replaces separate one-/two-dimensional cases with dimension-driven bound parsing and recursive index enumeration, enabling registers in three-dimensional arrays to be listed. Per-dimension min/max normalization handles either bound direction; recursive module descent remains. Raising the interpreter recursion limit to 64,000 accommodates the chosen recursive strategy. The practical capability is a more complete candidate register inventory for fault injection; no fault-coverage percentage, runtime/memory improvement or unbounded-dimension guarantee is established.

## register-collaboration

The Tcl file originated with Sean's `bce47a50cf9fee013517d4bb33f71c70d4f730f1`. Sean later adds per-bit register checks to avoid tied-off array bits in `132198680b02ca12a89c8127c412dd48d36bd338`, followed by further targeting/list changes. Michael's generalized enumeration remains recognizable in HEAD; current filtering and full tooling architecture are collaborative. The original refactor also normalizes many line endings, so its 106 additions/116 removals do not measure semantic work or a performance gain.

## release-branches

Seven December 2024 authored commits modify only `logical/shared/scripts/end_to_end/load_brunel.sh`: `81dabe34f1c49adf6fd00e1ad5456c801f8f50b9`, `ce7563ed91e6b163872d4b642b9d5a85298456cf`, `5047992d67b81c6d7098cac6e32ab96373847985`, `4ecbc240850052ce6105a7bcde2745438539c0d1`, `2971e359debd42c9831b7bc1b9aff08b650a36ee`, `c4454008e9b44b2045a71003484cc9d61d18c51a`, `25e56dce89fd5bc49da9dc16a2ebad22b3c56246`. They select the `2024.rtl.0` Interconnect Architect module on older release histories; the first malformed prefixed value is corrected in the next patch. This supports scoped release-validation environment maintenance and tool/IP integration support, not creation of the end-to-end flow, seven distinct features, proof that regressions passed, or a selected-HEAD version claim. The loader existed before this work and currently selects a later version.

## minor-maintenance

`16654dee97f714a69586f4b1aac4fb7630cc7fb8` (November 3, 2020) adds Michael's email to a report-distribution script. It is retained in the history inventory for completeness, not elevated into a separate reporting-system accomplishment or Perl proficiency claim.

## stashed-debugging

`2ffec6bd4c8180b5089cc542fe4a195bcabbbb87` is a stash working-tree object from August 13, 2026 with first parent `9e3dd54486e`; `d9cbdcbc1751740ece9dd329bd5487f5423d4e75` is its empty index snapshot. The five-file working patch guards absent unblock/ack routes in ASNI/DSNI decoders, derives a consistent OWO interface subset from access maps with credits, and converts clock-frequency values before SDC comparisons. It is useful private debugging context connecting configuration semantics to generation, but it is not an ordinary landed commit, no tests were recovered, and neither object is in selected HEAD ancestry. Keep it out of public delivered-accomplishment facts and résumé bullets. Similar later source is not automatically Michael's work.

## metric-and-outcome-boundaries

Verifiable quantities describe implementation scope: eight data bits per read-parity group at the inspected setting; 32-bit write-ECC chunks; extension beyond the old one-/two-dimensional register enumeration; separate read/write AXI use of a generalized tracker. Repository/ref/patch counts measure research coverage. None is a measured silicon PPA result, throughput/latency improvement, diagnostic coverage, functional-safety certification, customer adoption or business impact. Do not conflate configured repetitions/timeouts/recursion limits with achieved outcomes. No product tests, builds, formal runs, coverage reports or current end-to-end execution were performed in this investigation.

## reconciliation

Expand the existing RTL/VIP rotation project and skill relationships rather than recreating its owner-confirmed experience. Use a separate NoC project context to connect the safety work, later release integration and private stash limits; create granular records only for independently useful parity, ECC, hang-detection, generated fault-injection integration and register-enumeration work. SystemVerilog now has direct implementation context beyond the older private skills list; Tcl gains a demonstrated automation context. Preserve all previous IA, Pelion, internship, education and owner evidence. Earlier UVM coverage-model uncertainty concerns a different internship and remains unresolved by this repository.

## remaining-evidence

Useful follow-up evidence includes original simulator/fault-campaign logs and criteria; measured fault-detection/coverage outcomes; synthesis/lint/formal acceptance for any separately claimed production RTL; disclosable product/customer outcomes; measured register-extraction time or missed-site reduction; exact rotation dates; and original end-to-end results for the 2024 version selections. A separately preserved, reviewed landed change and validation would be needed to promote the 2026 stash into delivered work. Missing evidence does not establish missing experience and does not reopen existing owner confirmations.
