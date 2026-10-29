# NoC safety verification — achievement and technical narrative library

Reviewed 2026-10-29 for Michael Coulter against complete locally reachable authored
history and selected current implementations. The five core themes below represent
related parts of one engineering effort; select relevant alternatives without counting
the same integration several times. The release variant is narrower maintenance work.

Bullet wording draws only on public confirmed/reported facts. Fact references,
attribution caveats and technical narratives are internal tailoring material. Remove
them from application copy and read each record’s private facts first. The safety
implementations are historical validation/testbench work, principally 2020–2021;
the 2024 changes concern configuration-tool release setup. They do not establish a
new hardware job title, current responsibility or functional-safety certification.

Read [the research scope and reconciliation](arachne-noc-research.md) for the complete
commit map, later removal of legacy top-level bindings and execution limits.

## Protocol-aware parity models

**Concise:** Built protocol-aware parity generators and checkers for AXI/ACE-Lite
and AHB safety verification, extending the testbench’s read-path error observation.

**Expanded:** Implemented strobe-aware odd-parity models and parameterized read-data
checking, coordinating request/response sidebands, validity conditions and
Python-generated bindings across interconnect testbench interfaces.

**Technical narrative:** Safety sidebands cannot be treated as arbitrary VIP user
data. Michael introduced the initial write-data models, extended an existing
request/response implementation to read paths and authored read-data generation
and checking. The read checker accounts for the offset of response bits; interface
integration supplies AXI and AHB’s different validity conditions. At the inspected
setting, each data byte carries a parity bit and a marker. He also selected random
binary values for invalid VIP read lanes to support parity computation. Existing
write request/response models and later protocol-attribute extensions include
colleague contributions. No fault-coverage percentage is established.

Evidence: [accomplishment-interconnect-safety-parity#initial-models](../knowledge/accomplishments/accomplishment-interconnect-safety-parity.json);
[accomplishment-interconnect-safety-parity#read-channel](../knowledge/accomplishments/accomplishment-interconnect-safety-parity.json);
[accomplishment-interconnect-safety-parity#validity-and-stimulus](../knowledge/accomplishments/accomplishment-interconnect-safety-parity.json).

## Write-data ECC and error classification

**Concise:** Implemented 32-bit write-data ECC generation and syndrome-based checking
for configurable interconnect testbenches.

**Expanded:** Replaced write-parity model instances with strobe-aware ECC generation
and checking across AXI/ACE-Lite and AHB interfaces, exposing error classifications
and routing aggregate failures into the safety-observation path.

**Technical narrative:** The generator masks inactive bytes, places data around
positional check bits and derives odd-parity checks from XORs of set-bit positions.
The checker reconstructs the encoded message and combines syndrome and overall
parity to expose single-bit-location and double-bit indicators. This demonstrates
bit-level algorithm implementation and protocol integration. Michael’s initial
integration consumes the aggregate error signal; later correction-bit vectors,
strobe fixes and actual correction integration belong to a colleague. Use
“ECC generation/checking,” without claiming sole authorship of current correction
behavior, exhaustive SECDED validation or shipped DUT error-correction hardware.

Evidence: [accomplishment-interconnect-write-ecc#encoding](../knowledge/accomplishments/accomplishment-interconnect-write-ecc.json);
[accomplishment-interconnect-write-ecc#syndrome-checking](../knowledge/accomplishments/accomplishment-interconnect-write-ecc.json);
[accomplishment-interconnect-write-ecc#observation-integration](../knowledge/accomplishments/accomplishment-interconnect-write-ecc.json).

## Reusable protocol progress monitors

**Concise:** Developed AHB timeout and ID-aware AXI hang monitors, then generalized
AXI tracking for both read and write transactions.

**Expanded:** Modeled outstanding AXI requests using transaction IDs, completion
handshakes and coarse timestamp aging, reusing a common monitor across AR/R and
AW/B while integrating AHB stalled-ready detection into safety verification.

**Technical narrative:** AXI may have multiple outstanding transactions sharing
IDs, so progress detection needs bookkeeping beyond a single timeout counter.
Michael’s tracker records accepted requests and age epochs, finds matching
completion candidates and flags aged entries. Parameterizing ID width, outstanding
capacity and counter width enables reuse across the two transaction directions.
AHB uses a consecutive-low-ready counter with reset/progress clearing. A later
colleague split the monitors and added read beat counting; Michael’s generic
implementation survives in the renamed write-model source. This is historical
model development, without a current-use or all-corner-case correctness claim.

**Focused debugging variant:** Corrected an incomplete combinational idle-state
assignment in an AXI hang detector to address unintended latch behavior.

The debugging variant describes a specific source correction. It does not claim a
new clean lint/synthesis run. Timeout values are configurable; the AHB introduction’s
commit subject does not match its actual selected timeout.

Evidence: [accomplishment-interconnect-hang-detection#ahb-monitor](../knowledge/accomplishments/accomplishment-interconnect-hang-detection.json);
[accomplishment-interconnect-hang-detection#axi-reuse](../knowledge/accomplishments/accomplishment-interconnect-hang-detection.json);
[accomplishment-interconnect-hang-detection#latch-correction](../knowledge/accomplishments/accomplishment-interconnect-hang-detection.json).

## Configuration-driven fault-injection integration

**Concise:** Connected Python-generated testbench bindings and SystemVerilog safety
models to existing UVM fault-injection observations.

**Expanded:** Propagated safety-mode options through configuration services and
build objects, generated protocol-sideband connections and integrated parity,
ECC and hang indications with the testbench’s shared safety-interrupt path.

**Technical narrative:** The integration crosses configuration YAML, a Python
service option, internal build state, generated SystemVerilog connections, interface
models and UVM observation. Michael connected those boundaries so generated
protection codes and modeled errors could participate in the existing fault-injection
flow. He adapted payload checking to distinguish safety sidebands from ordinary
user payload, while preserving data comparisons. The framework and scoreboard
predate his changes; his scoreboard modification adjusts the observation window.
Control-file repetitions and transaction counts describe intended campaigns rather
than successful execution. A colleague removed the legacy top-level model bindings
in 2022, and current top-level safety observation uses FMU interrupts.

Evidence: [accomplishment-interconnect-fault-injection-integration#mode-propagation](../knowledge/accomplishments/accomplishment-interconnect-fault-injection-integration.json);
[accomplishment-interconnect-fault-injection-integration#error-observation](../knowledge/accomplishments/accomplishment-interconnect-fault-injection-integration.json);
[accomplishment-interconnect-fault-injection-integration#payload-semantics](../knowledge/accomplishments/accomplishment-interconnect-fault-injection-integration.json).

## Multidimensional register enumeration

**Concise:** Generalized Tcl netlist extraction to enumerate three-dimensional
register arrays for fault-site tooling.

**Expanded:** Replaced one-/two-dimensional special cases with dimension-driven
recursive enumeration, normalizing array bounds and retaining hierarchical module
traversal to extend the register inventory available to fault-injection tooling.

**Technical narrative:** The previous extractor handled only fixed array shapes.
Michael parsed the dimensions into bound lists and used recursive index traversal
to enumerate individual elements, including three-dimensional registers. The
practical result is support for an additional class of register structures. The
configured recursion limit accommodates this strategy; it is not a performance
benchmark or proof of unrestricted scale. Initial walker creation and later filtering
of tied-off bits belong to a colleague. Prefer the concrete capability improvement
over an invented fault-coverage or runtime percentage.

Evidence: [accomplishment-interconnect-register-enumeration#generalization](../knowledge/accomplishments/accomplishment-interconnect-register-enumeration.json);
[accomplishment-interconnect-register-enumeration#bound-handling](../knowledge/accomplishments/accomplishment-interconnect-register-enumeration.json).

## Bounded release-integration variant

**Concise:** Maintained configuration-tool version selections for NoC end-to-end
validation across release histories.

**Expanded:** Updated Interconnect Architect module selections and corrected a
malformed version value in release-specific NoC validation setup.

**Technical narrative:** Seven ordinary authored commits change one environment
selection line on different histories, including repeated patches and a typo fix.
This is evidence of scoped tool/IP release integration support. It does not establish
creation of the end-to-end harness, seven independent features or passing regressions.
Use it when release maintenance is relevant; prioritize the deeper safety and
automation accomplishments for limited résumé space.

Evidence: [project-arachne-noc#release-setup](../knowledge/projects/project-arachne-noc.json);
[project-interconnect-architect#noc-release-integration](../knowledge/projects/project-interconnect-architect.json).

## Combined résumé alternative

**Concise:** Built SystemVerilog parity/ECC and protocol-progress models for
interconnect safety verification, integrating generated Python bindings with
existing UVM fault-injection observations.

**Expanded:** Combined protocol-aware safety modeling, reusable AXI/AHB progress
checks and configuration-driven testbench integration, alongside Tcl automation
that extended register extraction to three-dimensional arrays.

This is an alternative summary of the five core themes, not an additional
accomplishment. Choose it for a software résumé needing one hardware-domain bullet;
use the individual mechanisms for verification or engineering-tool roles.

Evidence: [skill-systemverilog#safety-models](../knowledge/skills/skill-systemverilog.json);
[accomplishment-interconnect-fault-injection-integration#mode-propagation](../knowledge/accomplishments/accomplishment-interconnect-fault-injection-integration.json);
[accomplishment-interconnect-fault-injection-integration#error-observation](../knowledge/accomplishments/accomplishment-interconnect-fault-injection-integration.json);
[accomplishment-interconnect-register-enumeration#generalization](../knowledge/accomplishments/accomplishment-interconnect-register-enumeration.json).

## Positioning and evidence guardrails

- **Hardware verification:** parity/ECC models, handshake/ID-aware monitors,
  source-level debugging and safety-observation integration.
- **Systems and engineering tools:** Python-to-SystemVerilog configuration
  propagation, generated bindings, semantic consistency and Tcl netlist traversal.
- **Cross-domain software:** connect this earlier hardware/verification context
  to later Interconnect Architect GUI, migration and typed automation work without
  implying that the later software features are hardware-IP inventions.
- **Useful quantities:** 32-bit ECC chunks, eight-bit read-data parity groups at
  the inspected setting and support beyond one-/two-dimensional register arrays.
  These describe design scope, not measured performance or coverage.

No bullet draws delivered-work credit from the 2026 stash. No new simulator pass,
formal proof, silicon PPA result, functional-safety certification, fault-coverage
percentage, customer outcome or measured time saving is established by this review.
