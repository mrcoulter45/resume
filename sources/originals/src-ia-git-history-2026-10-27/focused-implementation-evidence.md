# Focused source inspection supplement

PRIVATE research evidence. All excerpts below are from the captured HEAD e24d80378096cb8d7a0ad87c20929cb520fa49d7. Numeric prefixes are original source lines; surrounding prose is analyst interpretation. No code executed.

## command-literals
Path: `brunel/python-command.js`; SHA-256: `55a933bf905d45dd2378c95309be8392886c47cbafda85051c895c89e99d9051`.
Lines 18-85; surviving authors: {'Michael Coulter': 67}.
```text
18: function toPythonLiteral(value) {
19:   return serializePythonLiteral(value, new Set());
20: }
21: 
22: function serializePythonLiteral(value, ancestors) {
23:   if (value === null || value === undefined) {
24:     return 'None';
25:   }
26: 
27:   if (typeof value === 'string') {
28:     return JSON.stringify(value);
29:   }
30: 
31:   if (typeof value === 'boolean') {
32:     return value ? 'True' : 'False';
33:   }
34: 
35:   if (typeof value === 'number') {
36:     if (Number.isNaN(value)) {
37:       return 'float("nan")';
38:     }
39:     if (value === Number.POSITIVE_INFINITY) {
40:       return 'float("inf")';
41:     }
42:     if (value === Number.NEGATIVE_INFINITY) {
43:       return 'float("-inf")';
44:     }
45:     return String(value);
46:   }
47: 
48:   if (typeof value === 'bigint') {
49:     return value.toString();
50:   }
51: 
52:   if (Array.isArray(value)) {
53:     if (ancestors.has(value)) {
54:       return 'None';
55:     }
56:     ancestors.add(value);
57:     const items = Array.from(value, item => serializePythonLiteral(item, ancestors));
58:     ancestors.delete(value);
59:     return `[${items.join(', ')}]`;
60:   }
61: 
62:   if (typeof value === 'object') {
63:     if (ancestors.has(value)) {
64:       return 'None';
65:     }
66:     ancestors.add(value);
67:     const entries = Object.entries(value).map(([key, entryValue]) =>
68:       `${serializePythonLiteral(key, ancestors)}: ${serializePythonLiteral(entryValue, ancestors)}`
69:     );
70:     ancestors.delete(value);
71:     return `{${entries.join(', ')}}`;
72:   }
73: 
74:   return 'None';
75: }
76: 
77: function formatPythonCall(callable, args = []) {
78:   return `${callable}(${args.map(toPythonLiteral).join(', ')})`;
79: }
80: 
81: module.exports = {
82:   formatPythonCall,
83:   toPythonLiteral,
84: };
```

## export-current
Path: `GUI/src/app/status-bar/export-dialog/export-dialog.component.ts`; SHA-256: `52dd7c04004cbaf06d34220aad409e33cfc1e8c540c70d1fcc57f027089200ca`.
Lines 110-151; surviving authors: {'Michael Coulter': 35, 'Dustin Divis': 3, 'Kelly Alvarez': 2, 'Pawan Kakarla': 2}.
```text
110:     }
111: 
112:     this.currentFloorplanType = this.canvasViewStateService.currentFloorplanType;
113: 
114:     const logicalCanvasElement = document.getElementById('logical-canvas-container');
115:     const physicalCanvasElement = document.getElementById('canvas-container');
116:     const logicalMeshElement = document.getElementById('logical-mesh-canvas-container');
117: 
118:     if (logicalMeshElement instanceof SVGSVGElement) {
119:       this.logicalMeshSvgElement = logicalMeshElement;
120:     }
121: 
122:     const activeFloorplanElement = this.resolveActiveFloorplanElement(
123:       logicalCanvasElement,
124:       physicalCanvasElement,
125:       logicalMeshElement,
126:     );
127:     if (activeFloorplanElement instanceof HTMLCanvasElement) {
128:       this.canvasElement = activeFloorplanElement;
129:     } else if (activeFloorplanElement instanceof SVGSVGElement) {
130:       this.svgCanvasElement = activeFloorplanElement;
131:     }
132: 
133:     if (this.canvasElement || this.svgCanvasElement) {
134:       this.fileTypes.push('.png (Canvas export)');
135:     }
136:     if (this.currentFloorplanType === 'logicalMesh' && this.logicalMeshSvgElement) {
137:       this.fileTypes.push('.svg (Canvas export)');
138:     }
139: 
140:     this.dirPath = path.join(this.dirPath, 'checkpoint');
141:     const controls = {};
142:     const defaultFileType = this.fileTypes[0];
143:     controls['fileType'] = new UntypedFormControl(
144:       { value: defaultFileType, disabled: this.dialogMode === 'checkpoint' },
145:       [ Validators.required]
146:     );
147:     controls['exportName'] = new UntypedFormControl(this.fileName, [Validators.pattern('^[A-Za-z][a-zA-Z0-9_]*$'), Validators.required]);
148:     this.projectForm = new UntypedFormGroup(controls);
149:     /* Get project name */
150:     // TODO: Manage project name in project service
151:     // this.dataService.brunelCEApi('app-export-dialog_get-project-name', 'get_project_name', []);
```
Lines 403-430; surviving authors: {'Michael Coulter': 26, 'Pawan Kakarla': 2}.
```text
403:   private createCanvasSVG(): void {
404:     try {
405:       const svgElement = this.logicalMeshSvgElement;
406:       if (!svgElement) {
407:         console.error('SVG element not found for export');
408:         showAppNotification('Failed to export SVG!');
409:         return;
410:       }
411: 
412:       const serializer = new XMLSerializer();
413:       let source = serializer.serializeToString(svgElement);
414: 
415:       if (!source.match(/^<svg[^>]+xmlns="http:\/\/www\.w3\.org\/2000\/svg"/)) {
416:         source = source.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
417:       }
418:       if (!source.match(/^<svg[^>]+xmlns:xlink="http:\/\/www\.w3\.org\/1999\/xlink"/)) {
419:         source = source.replace('<svg', '<svg xmlns:xlink="http://www.w3.org/1999/xlink"');
420:       }
421: 
422:       const svgContent = `<?xml version="1.0" encoding="UTF-8"?>\n${source}`;
423:       const blob = new Blob([svgContent], { type: 'image/svg+xml;charset=utf-8' });
424: 
425:       this.saveBlob(blob);
426:     } catch (e) {
427:       console.error('Failed to save SVG:', e);
428:       showAppNotification('Failed to export SVG!');
429:     }
430:   }
```
Lines 490-521; surviving authors: {'Michael Coulter': 32}.
```text
490: 
491:   private resolveSvgExportSize(svgElement: SVGSVGElement): { width: number; height: number } {
492:     const rect = svgElement.getBoundingClientRect();
493:     const viewBox = svgElement.viewBox?.baseVal;
494:     const width = Math.max(1, Math.round(rect.width || viewBox?.width || 1));
495:     const height = Math.max(1, Math.round(rect.height || viewBox?.height || 1));
496:     return { width, height };
497:   }
498: 
499:   private serializeSvgElement(svgElement: SVGSVGElement, width?: number, height?: number): string {
500:     const clone = svgElement.cloneNode(true) as SVGSVGElement;
501:     if (width) {
502:       clone.setAttribute('width', `${width}`);
503:     }
504:     if (height) {
505:       clone.setAttribute('height', `${height}`);
506:     }
507: 
508:     const serializer = new XMLSerializer();
509:     let source = serializer.serializeToString(clone);
510: 
511:     if (!source.match(/^<svg[^>]+xmlns="http:\/\/www\.w3\.org\/2000\/svg"/)) {
512:       source = source.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
513:     }
514:     if (!source.match(/^<svg[^>]+xmlns:xlink="http:\/\/www\.w3\.org\/1999\/xlink"/)) {
515:       source = source.replace('<svg', '<svg xmlns:xlink="http://www.w3.org/1999/xlink"');
516:     }
517: 
518:     return `<?xml version="1.0" encoding="UTF-8"?>\n${source}`;
519:   }
520: 
521:   private saveBlob(blob: Blob): void {
```

## semantic-diff
Path: `resources/scripts/iyml_diff.py`; SHA-256: `6f7969bb6e40190e9d66566e43b25c74acc4332afa1cf69b3511a6255b2ca5e7`.
Lines 498-533; surviving authors: {'Michael Coulter': 36}.
```text
498: def load_design(iyml_path: Path) -> Tuple[Any, str]:
499:     """Import an iYML file into an isolated NCI session."""
500:     temp_dir = tempfile.mkdtemp(prefix="iyml_diff_")
501:     session = Nci(output_dir=temp_dir)
502:     if not session.import_design(str(iyml_path)):
503:         shutil.rmtree(temp_dir)
504:         raise ValueError(f"Unable to import design from {iyml_path}")
505:     ip_version = session.get_ip_version()
506:     if not isinstance(ip_version, str) or not is_nci_ip_version(ip_version):
507:         shutil.rmtree(temp_dir)
508:         raise ValueError(
509:             f"Canvas diff only supports NCI configurations. Received IP version '{ip_version}'."
510:         )
511:     return session, temp_dir
512: 
513: 
514: def collect_view(session: Any) -> Dict[str, Any]:
515:     """Capture the logical canvas data required by the GUI."""
516:     connections_info = session.connections.get_connections_info("gui_data")
517:     data = {
518:         "ip_version": session.get_ip_version(),
519:         "instance_attributes": session.get_instance_attributes(),
520:         "instances_gui": session.instances.get_instances_info("gui_data"),
521:         "interfaces_gui": session.interfaces.get_interfaces_info("gui_data"),
522:         "route_attributes": session.get_route_attributes(),
523:         "connections": connections_info.get("network_connections", {}),
524:         "connections_per_instance": connections_info.get("connections_per_instance", {}),
525:         "routes": session.get_routes(),
526:         "pulse_routes": session.get_pulse_routes(),
527:         "remote_routes": session.get_remote_routes(),
528:         "connection_parameters": collect_connection_parameters(session, connections_info.get("network_connections", {})),
529:     }
530:     return data
531: 
532: 
533: def collect_connection_parameters(session: Any, network_connections: Mapping[str, Any]) -> Dict[str, Any]:
```
Lines 715-770; surviving authors: {'Michael Coulter': 56}.
```text
715: def build_payload(
716:     base_path: Path,
717:     compare_path: Path,
718:     original_compare_path: Optional[Path] = None,
719: ) -> Dict[str, Any]:
720:     logging.info("Starting iYML diff payload build current=%s comparison=%s", base_path, compare_path)
721:     # Load raw YAML for a procedural diff across all sections.
722:     base_yaml = load_yaml_data(base_path)
723:     compare_yaml = load_yaml_data(compare_path)
724:     yaml_base_diff, yaml_compare_diff = deep_diff_mappings(base_yaml, compare_yaml)
725: 
726:     base_session, base_tmp = load_design(base_path)
727:     compare_session, compare_tmp = load_design(compare_path)
728:     try:
729:         base_view = collect_view(base_session)
730:         compare_view = collect_view(compare_session)
731:     finally:
732:         shutil.rmtree(base_tmp, ignore_errors=True)
733:         shutil.rmtree(compare_tmp, ignore_errors=True)
734: 
735:     diff_summary = {
736:         "instances": diff_instances(
737:             base_view.get("instances_gui") or {},
738:             compare_view.get("instances_gui") or {},
739:         ),
740:         "interfaces": diff_interfaces(
741:             base_view.get("interfaces_gui") or {},
742:             compare_view.get("interfaces_gui") or {},
743:         ),
744:         "connections": diff_connections(
745:             base_view,
746:             compare_view,
747:         ),
748:     }
749: 
750:     payload = {
751:         "current_project_path": str(base_path),
752:         "comparison_project_path": str(compare_path),
753:         "comparison_project_original_path": str(original_compare_path) if original_compare_path else str(compare_path),
754:         "base_path": str(base_path),
755:         "compare_path": str(compare_path),
756:         "base": base_view,
757:         "compare": compare_view,
758:         "yaml_current": base_yaml,
759:         "yaml_comparison": compare_yaml,
760:         "diff": diff_summary,
761:         "diff_yaml": {"base": yaml_base_diff, "compare": yaml_compare_diff},
762:     }
763:     # Generic, future-proof diff across the entire view structures.
764:     base_full_diff, compare_full_diff = deep_diff_mappings(base_view, compare_view)
765:     payload["diff_all"] = {
766:         "view": {"base": base_full_diff, "compare": compare_full_diff},
767:         "yaml": {"base": yaml_base_diff, "compare": yaml_compare_diff},
768:     }
769:     return payload
770: 
```
Lines 865-910; surviving authors: {'Michael Coulter': 46}.
```text
865: def render_changed_line(
866:     comparison_line: str,
867:     current_line: str,
868: ) -> Tuple[str, str]:
869:     """Escape two changed lines and highlight only their differing text."""
870:     if is_structural_line(comparison_line) or is_structural_line(current_line):
871:         return escape(comparison_line), escape(current_line)
872: 
873:     prefix_len = 0
874:     max_prefix_len = min(len(comparison_line), len(current_line))
875:     while (
876:         prefix_len < max_prefix_len
877:         and comparison_line[prefix_len] == current_line[prefix_len]
878:     ):
879:         prefix_len += 1
880: 
881:     suffix_len = 0
882:     max_suffix_len = min(
883:         len(comparison_line) - prefix_len,
884:         len(current_line) - prefix_len,
885:     )
886:     while (
887:         suffix_len < max_suffix_len
888:         and comparison_line[len(comparison_line) - suffix_len - 1]
889:         == current_line[len(current_line) - suffix_len - 1]
890:     ):
891:         suffix_len += 1
892: 
893:     comparison_end = len(comparison_line) - suffix_len
894:     current_end = len(current_line) - suffix_len
895: 
896:     def render_line(line: str, end: int, css_class: str) -> str:
897:         prefix = escape(line[:prefix_len])
898:         changed = escape(line[prefix_len:end])
899:         suffix = escape(line[end:])
900:         if changed:
901:             changed = f'<span class="{css_class}">{changed}</span>'
902:         return f"{prefix}{changed}{suffix}"
903: 
904:     return (
905:         render_line(comparison_line, comparison_end, "yaml-char-diff-compare"),
906:         render_line(current_line, current_end, "yaml-char-diff-current"),
907:     )
908: 
909: 
910: def render_one_sided_line(line: str, css_class: str) -> str:
```
Lines 930-967; surviving authors: {'Michael Coulter': 38}.
```text
930: def render_yaml_text_diff(
931:     comparison_text: str,
932:     current_text: str,
933: ) -> Tuple[str, str]:
934:     """Render escaped, line-aligned text with intraline change highlights."""
935:     comparison_lines = comparison_text.split("\n")
936:     current_lines = current_text.split("\n")
937:     comparison_html: List[str] = []
938:     current_html: List[str] = []
939: 
940:     matcher = SequenceMatcher(None, comparison_lines, current_lines, autojunk=False)
941:     for (
942:         tag,
943:         comparison_start,
944:         comparison_end,
945:         current_start,
946:         current_end,
947:     ) in matcher.get_opcodes():
948:         if tag == "equal":
949:             comparison_html.extend(
950:                 escape(line)
951:                 for line in comparison_lines[comparison_start:comparison_end]
952:             )
953:             current_html.extend(
954:                 escape(line) for line in current_lines[current_start:current_end]
955:             )
956:             continue
957: 
958:         if tag == "replace":
959:             comparison_block = comparison_lines[comparison_start:comparison_end]
960:             current_block = current_lines[current_start:current_end]
961:             paired_lines = min(len(comparison_block), len(current_block))
962:             for index in range(paired_lines):
963:                 comparison_line, current_line = render_changed_line(
964:                     comparison_block[index],
965:                     current_block[index],
966:                 )
967:                 comparison_html.append(comparison_line)
```

## plan-compilation
Path: `ai/ia-mcp-pack/src/ia_mcp_pack/plan_compiler.py`; SHA-256: `d1eaee1c463b3973c8735be90ce397d9708c7a51a06afea598cd79197a4c3940`.
Lines 8032-8067; surviving authors: {'Michael Coulter': 36}.
```text
8032: def compile_design_plan(
8033:     intent: DesignIntentV1 | Mapping[str, Any] | str | bytes,
8034:     planning_state: PlanningStateV1 | Mapping[str, Any],
8035:     live_operation_schemas: (
8036:         Mapping[str, Mapping[str, Any]]
8037:         | Iterable[Mapping[str, Any]]
8038:         | LiveSchemaProvider
8039:     ),
8040:     *,
8041:     capability_snapshot: Mapping[str, Any] | BaseModel,
8042:     provider_requirements: Iterable[Mapping[str, Any]] = (),
8043:     native_operation_statuses: Mapping[str, str] | None = None,
8044: ) -> CompiledPlanV1:
8045:     """Compile untrusted caller intent into an exact, immutable plan DAG."""
8046: 
8047:     try:
8048:         trusted_intent = normalize_design_intent(intent)
8049:         state = verify_planning_state(planning_state)
8050:         validation = validate_design_intent(
8051:             trusted_intent,
8052:             capability_snapshot,
8053:             planning_state=state,
8054:         )
8055:     except Exception as exc:
8056:         raise PlanCompilationError(f"compiler input verification failed: {exc}") from exc
8057:     return _compile_design_plan_core(
8058:         trusted_intent,
8059:         state,
8060:         validation,
8061:         live_operation_schemas,
8062:         capability_snapshot=capability_snapshot,
8063:         provider_requirements=provider_requirements,
8064:         native_operation_statuses=native_operation_statuses,
8065:     )
8066: 
8067: 
```
Lines 8202-8305; surviving authors: {'Michael Coulter': 104}.
```text
8202: def _compile_design_plan_core(
8203:     trusted_intent: DesignIntentV1,
8204:     state: PlanningStateV1,
8205:     validation: IntentValidationResultV1,
8206:     live_operation_schemas: (
8207:         Mapping[str, Mapping[str, Any]]
8208:         | Iterable[Mapping[str, Any]]
8209:         | LiveSchemaProvider
8210:     ),
8211:     *,
8212:     capability_snapshot: Mapping[str, Any] | BaseModel,
8213:     provider_requirements: Iterable[Mapping[str, Any]],
8214:     controlled_fallback_partial: bool = False,
8215:     native_operation_statuses: Mapping[str, str] | None = None,
8216: ) -> CompiledPlanV1:
8217:     """Compile inputs that already crossed their appropriate trust boundary."""
8218: 
8219:     mcs_evidence, _mcs_error = _qualified_live_mcs_modes(capability_snapshot)
8220:     builder = _Builder(
8221:         trusted_intent,
8222:         state,
8223:         nci_product_lineage=(
8224:             _nci_product_lineage_for_compilation(capability_snapshot)
8225:             if state.product_family == "nci"
8226:             else None
8227:         ),
8228:         nci_resource_plane_capability=(
8229:             _nci_resource_plane_capability_for_compilation(capability_snapshot)
8230:             if state.product_family == "nci"
8231:             else None
8232:         ),
8233:         cmn_group_contract=(
8234:             _cmn_group_contract_for_compilation(capability_snapshot)
8235:             if state.product_family == "cmn"
8236:             else None
8237:         ),
8238:         cmn_native_mcs_public_types=(
8239:             mcs_evidence.get("public_device_type_evidence", ())
8240:             if state.product_family == "cmn" and isinstance(mcs_evidence, Mapping)
8241:             else ()
8242:         ),
8243:     )
8244:     builder.tradeoffs = list(validation.product_evaluation.tradeoffs)
8245:     if validation.valid_for_planning is not True or validation.executable is not True:
8246:         for item in validation.issues:
8247:             status = {
8248:                 # The native compiler cannot execute preservation-only input,
8249:                 # but that absence is not positive evidence that a controlled
8250:                 # CE implementation is unsafe or incompatible.
8251:                 "preservation_only": "unresolved",
8252:                 "ambiguous": "ambiguous",
8253:             }.get(item.status, item.status)
8254:             builder.issue(
8255:                 item.code,
8256:                 "/" + "/".join(str(component) for component in item.path),
8257:                 item.message,
8258:                 status=status,
8259:                 alternatives=[str(_primitive_value(value)) for value in item.alternatives],
8260:             )
8261:         if validation.issues_truncated:
8262:             builder.issue(
8263:                 "validation-issues-truncated",
8264:                 "/",
8265:                 "capability-aware intent validation exceeded its retained issue limit",
8266:                 status="blocked",
8267:             )
8268:     if trusted_intent.fabric.kind != state.product_family:
8269:         builder.issue(
8270:             "fabric-family-mismatch",
8271:             "/fabric/kind",
8272:             f"intent fabric {trusted_intent.fabric.kind!r} does not match live product family {state.product_family!r}",
8273:         )
8274:     if state.source_current is not True or state.source_identity_complete is not True:
8275:         builder.issue(
8276:             "unqualified-capability-source",
8277:             "/",
8278:             "planning requires current, complete CE source identity evidence",
8279:         )
8280:     if state.design_state_status not in {"complete", "partial"}:
8281:         builder.issue(
8282:             "incomplete-current-state",
8283:             "/",
8284:             "deterministic mutation planning requires available bounded current-state evidence",
8285:             remediation="Refresh capability discovery until the required design-state section is complete.",
8286:         )
8287:     requirements = _intent_requirements(trusted_intent)
8288:     if not requirements:
8289:         builder.issue("empty-intent", "/", "design intent contains no requirements")
8290:     compilable_requirements = requirements
8291:     if controlled_fallback_partial:
8292:         matched_requirement_ids = set(
8293:             validation.product_evaluation.matched_requirement_ids
8294:         )
8295:         compilable_requirements = [
8296:             (path, requirement)
8297:             for path, requirement in requirements
8298:             if requirement.requirement_id in matched_requirement_ids
8299:         ]
8300:     requested_gate_provenance = _requested_validation_gate_provenance(
8301:         trusted_intent,
8302:         compilable_requirements,
8303:     )
8304:     for validation_id, provenance in requested_gate_provenance.items():
8305:         if len(provenance) > _MAX_REQUESTED_GATE_PROVENANCE:
```

## plan-execution
Path: `ai/ia-mcp-pack/src/ia_mcp_pack/plan_execution.py`; SHA-256: `720631942e251330f43b137980baff12e731ba3c0dcd110b40d728d9eca0b2aa`.
Lines 1094-1157; surviving authors: {'Michael Coulter': 64}.
```text
1094: 
1095: 
1096: def _committed_prefix(
1097:     plan: CompiledPlanV1,
1098:     receipts: list[dict[str, Any] | None],
1099: ) -> tuple[int, str | None]:
1100:     """Validate an exact consecutive committed phase prefix.
1101: 
1102:     The returned integer is the first uncommitted phase index.  Any durable
1103:     receipt after that index, nonconsecutive mutation batch, authority drift,
1104:     semantic discontinuity, or non-current prefix head fails closed.
1105:     """
1106: 
1107:     first_missing = len(receipts)
1108:     for index, receipt in enumerate(receipts):
1109:         if receipt is None:
1110:             first_missing = index
1111:             break
1112:         error = _receipt_contract_error(plan, plan.phases[index], receipt)
1113:         if error is not None:
1114:             return index, error
1115:         disposition = receipt.get("disposition")
1116:         if disposition not in {"committed_active", "committed_historical"}:
1117:             return index, None
1118:     if any(receipt is not None for receipt in receipts[first_missing + 1 :]):
1119:         return first_missing, "durable plan history contains a phase gap"
1120:     committed = receipts[:first_missing]
1121:     previous_batch_index: int | None = None
1122:     previous_final: dict[str, Any] | None = None
1123:     for index, receipt in enumerate(committed):
1124:         assert receipt is not None
1125:         record = receipt["record"]
1126:         batch_index = record.get("committed_mutation_batch_index")
1127:         if type(batch_index) is not int or batch_index < 0:
1128:             return index, "committed phase receipt lacks an exact mutation-batch index"
1129:         if previous_batch_index is not None and batch_index != previous_batch_index + 1:
1130:             return index, "compiled plan phase mutation batches are not consecutive"
1131:         expected_states = _PLAN_COMPLETE_VALIDATION_STATES
1132:         if record.get("validation_state") not in expected_states:
1133:             return index, (
1134:                 f"compiled plan phase {plan.phases[index].phase_id} has "
1135:                 f"validation state {record.get('validation_state')!r}, expected "
1136:                 "a policy-complete state"
1137:             )
1138:         checkpoint = record.get("checkpoint_semantic_evidence")
1139:         final = record.get("final_semantic_evidence")
1140:         if not isinstance(checkpoint, dict) or not isinstance(final, dict):
1141:             return index, "committed phase receipt lacks its semantic proof chain"
1142:         if previous_final is not None and (
1143:             previous_final.get("configuration_sha256")
1144:             != checkpoint.get("before_semantic_sha256")
1145:             or previous_final.get("source_fingerprint")
1146:             != checkpoint.get("source_fingerprint")
1147:         ):
1148:             return index, "compiled plan semantic continuity breaks between phases"
1149:         previous_batch_index = batch_index
1150:         previous_final = final
1151:     if committed:
1152:         latest = committed[-1]
1153:         assert latest is not None
1154:         if latest.get("disposition") != "committed_active":
1155:             return first_missing, (
1156:                 "the committed plan prefix is no longer the current mutation-history head"
1157:             )
```
Lines 2062-2112; surviving authors: {'Michael Coulter': 51}.
```text
2062: 
2063:     record = receipt["record"]
2064:     provenance = record.get("commit_provenance", {})
2065:     data = {
2066:         "session_id": request.session_id,
2067:         "plan_id": request.plan_id,
2068:         "phase_id": request.phase_id,
2069:         "execution_state": "already_committed",
2070:         "transaction_id": record.get("transaction_id"),
2071:         "transaction_state": record.get("state"),
2072:         "rollback_checkpoint": record.get("rollback_checkpoint"),
2073:         "committed_mutation_batch_index": record.get(
2074:             "committed_mutation_batch_index"
2075:         ),
2076:         "committed_mutation_batch_sha256": record.get(
2077:             "committed_mutation_batch_sha256"
2078:         ),
2079:         "transaction_provenance_sha256": provenance.get(
2080:             "transaction_provenance_sha256"
2081:         ),
2082:         "next_phase_id": next_phase_id,
2083:         "plan_complete": complete,
2084:         "plan_authority_consumed": complete,
2085:         "idempotent_retry": True,
2086:         "mutation_performed": False,
2087:     }
2088:     return GenericStatusResult(
2089:         success=True,
2090:         data=data,
2091:         validations=[
2092:             ValidationRecord(
2093:                 name="compiled-plan-idempotent-retry",
2094:                 status="passed",
2095:                 summary=(
2096:                     "Returned an exact manifest-validated committed plan phase "
2097:                     "without repeating any CE mutation."
2098:                 ),
2099:             )
2100:         ],
2101:         authority_type="runtime_verified",
2102:         confidence=1.0,
2103:         validation_state=str(record.get("validation_state", "unvalidated")),
2104:         message="This exact compiled plan phase was already committed.",
2105:     )
2106: 
2107: 
2108: def _handle_execute_compiled_plan_unbounded(
2109:     runtime_context: Any,
2110:     request: ExecuteCompiledPlanRequest,
2111:     *,
2112:     enforce_agentic_v1: bool = False,
```
Lines 2118-2175; surviving authors: {'Michael Coulter': 58}.
```text
2118:         registry = server_plan_registry(runtime_context)
2119:         with adapter.transaction_lock(request.session_id):
2120:             if enforce_agentic_v1:
2121:                 plan, _support_binding = registry.resolve_agentic_v1_support(
2122:                     request.session_id,
2123:                     request.plan_id,
2124:                 )
2125:             else:
2126:                 try:
2127:                     plan = registry.resolve_owned(request.session_id, request.plan_id)
2128:                 except Exception:
2129:                     # Durable history can still prevent replay after process-owned
2130:                     # authority has been lost, but it can never authorize a later
2131:                     # phase. Preserve the prior exact retry behavior for terminal
2132:                     # phase receipts while withholding every new mutation.
2133:                     receipt = adapter.compiled_plan_execution_receipt(
2134:                         request.session_id,
2135:                         request.plan_id,
2136:                         request.phase_id,
2137:                     )
2138:                     if receipt is not None:
2139:                         if (
2140:                             receipt.get("disposition") == "committed_active"
2141:                             and receipt.get("semantic_current") is True
2142:                             and receipt.get("record", {}).get("validation_state")
2143:                             in _PLAN_COMPLETE_VALIDATION_STATES
2144:                             and receipt.get("artifacts_expected")
2145:                         ):
2146:                             try:
2147:                                 receipt = _reconcile_planned_artifacts(
2148:                                     runtime_context,
2149:                                     adapter,
2150:                                     request,
2151:                                     receipt,
2152:                                 )
2153:                             except PlannedArtifactError as exc:
2154:                                 return _artifact_failure_result(request, exc)
2155:                             except Exception as exc:
2156:                                 return _artifact_failure_result(
2157:                                     request,
2158:                                     PlannedArtifactError(str(exc)),
2159:                                 )
2160:                         return _durable_receipt_result(request, receipt)
2161:                     snapshot, _cache = adapter.capability_snapshot(
2162:                         request.session_id,
2163:                         refresh=True,
2164:                     )
2165:                     state = build_planning_state(snapshot)
2166:                     plan = registry.resolve(request.session_id, request.plan_id, state)
2167: 
2168:             phase_index = _phase_index(plan, request.phase_id)
2169:             phase_requests = _preflight_plan(plan)
2170:             phase = plan.phases[phase_index]
2171: 
2172:             if plan.provider_requirements:
2173:                 registry.discard_session(request.session_id)
2174:                 raise ValueError(
2175:                     "provider-bound compiled plans cannot execute until provider identity "
```

## fallback-admission
Path: `ai/ia-mcp-pack/src/ia_mcp_pack/direct_ce_fallback.py`; SHA-256: `5a7741c625680fde5aa6e3ba00e2034c4267c18144d4824279e5e35b18fcfdb9`.
Lines 831-932; surviving authors: {'Michael Coulter': 102}.
```text
831: def admit_script(
832:     base_script: str,
833:     revised_script: str,
834:     inventory: Mapping[str, Any],
835: ) -> dict[str, Any]:
836:     """Apply structural default-allow admission to Codex-added CE calls."""
837: 
838:     try:
839:         revised_tree = ast.parse(revised_script)
840:     except SyntaxError as exc:
841:         return {
842:             "admitted": False,
843:             "blocks": [{"category": "invalid_syntax", "evidence": str(exc)}],
844:             "admitted_calls": [],
845:         }
846:     unresolved = [
847:         gap_id
848:         for gap_id, block in extract_gap_blocks(revised_script).items()
849:         if not block["resolved"]
850:     ]
851:     sentinel_calls = [
852:         node.lineno
853:         for node in ast.walk(revised_tree)
854:         if isinstance(node, ast.Call)
855:         and isinstance(node.func, ast.Name)
856:         and node.func.id == SENTINEL_NAME
857:     ]
858:     if unresolved or sentinel_calls:
859:         return {
860:             "admitted": False,
861:             "blocks": [
862:                 {
863:                     "category": "unresolved_gap",
864:                     "evidence": {
865:                         "gap_ids": unresolved,
866:                         "sentinel_lines": sentinel_calls,
867:                     },
868:                 }
869:             ],
870:             "admitted_calls": [],
871:         }
872:     try:
873:         if not protected_harness_preserved(base_script, revised_script):
874:             return {
875:                 "admitted": False,
876:                 "blocks": [{"category": "protected_harness_modified", "evidence": "AST fingerprint"}],
877:                 "admitted_calls": [],
878:             }
879:     except (SyntaxError, DirectCEError) as exc:
880:         return {
881:             "admitted": False,
882:             "blocks": [{"category": "protected_harness_invalid", "evidence": str(exc)}],
883:             "admitted_calls": [],
884:         }
885: 
886:     blocks = _structural_violations(base_script, revised_script)
887:     records = _inventory_by_name(inventory)
888:     public_receivers = _public_receiver_names(revised_script)
889:     admitted_calls: list[dict[str, Any]] = []
890:     for call in _added_calls(base_script, revised_script):
891:         receiver, method = _call_name(call)
892:         if method in PROHIBITED_CALL_NAMES or method == "<dynamic>":
893:             blocks.append(
894:                 {"category": "dynamic_code_or_reflection", "line": call.lineno, "evidence": method}
895:             )
896:             continue
897:         if receiver is None and method in ALLOWED_SIMPLE_CALLS | ALLOWED_HARNESS_CALLS:
898:             continue
899:         if receiver is not None and receiver.split(".")[0] in FORBIDDEN_RUNTIME_NAMES:
900:             blocks.append(
901:                 {"category": "process_network_environment_or_filesystem", "line": call.lineno, "evidence": f"{receiver}.{method}"}
902:             )
903:             continue
904:         if receiver not in public_receivers:
905:             blocks.append(
906:                 {"category": "receiver_outside_verified_ce_surface", "line": call.lineno, "evidence": f"{receiver}.{method}"}
907:             )
908:             continue
909:         if method.startswith("_"):
910:             blocks.append(
911:                 {"category": "private_api", "line": call.lineno, "evidence": method}
912:             )
913:             continue
914:         record = records.get(method)
915:         if record is None:
916:             blocks.append(
917:                 {"category": "unverifiable_ownership", "line": call.lineno, "evidence": method}
918:             )
919:             continue
920:         module = str(record.get("module") or "")
921:         source = record.get("source")
922:         source_path = str(source.get("path") or "") if isinstance(source, Mapping) else ""
923:         if not module.startswith("ideas.") or not source_path.startswith("CE/ideas/"):
924:             blocks.append(
925:                 {
926:                     "category": "outside_verified_ce_installation",
927:                     "line": call.lineno,
928:                     "evidence": {"module": module, "source": source_path},
929:                 }
930:             )
931:             continue
932:         signature_error = _signature_error(call, record)
```

## legacy-sidecar
Path: `ai/ia-mcp-pack/src/ia_mcp_pack/legacy_ce_sidecar.py`; SHA-256: `db0c8f82bab151314e9e027154700c3abb1cda487c201b9314fac7ca92002695`.
Lines 263-374; surviving authors: {'Michael Coulter': 112}.
```text
263:     return route
264: 
265: 
266: def _load_public_allowlist(path):
267:     with open(str(path), "r", encoding="utf-8") as stream:
268:         payload = json.load(stream)
269:     if not isinstance(payload, dict) or payload.get("schema_version") != 1:
270:         raise ValueError("sidecar public API inventory has an unsupported schema")
271:     names = set()
272:     for entry in payload.get("apis", []):
273:         if not isinstance(entry, dict):
274:             continue
275:         name = entry.get("name")
276:         if (
277:             isinstance(name, str)
278:             and name
279:             and not name.startswith("_")
280:             and entry.get("declaring_class", "").startswith("Interconnect")
281:         ):
282:             names.add(name)
283:     required = {"get_products_list", "get_ip_version"}
284:     if not required.issubset(names):
285:         raise ValueError("sidecar public API inventory lacks required identity methods")
286:     return frozenset(names)
287: 
288: 
289: class LegacyCESidecar(object):
290:     def __init__(self, args):
291:         actual = ".".join(str(value) for value in sys.version_info[:3])
292:         if actual != EXPECTED_PYTHON:
293:             raise RuntimeError(
294:                 "legacy CE sidecar requires exact Python %s, found %s"
295:                 % (EXPECTED_PYTHON, actual)
296:             )
297:         self.session_id = args.session_id
298:         self.parent_pid = args.parent_pid
299:         self.product_version = args.product_version
300:         self.release_mode = args.release_mode == "true"
301:         self.ideas_root = Path(args.ideas_root).resolve()
302:         self.output_dir = Path(args.output_dir).resolve()
303:         self.allowed_roots = (self.ideas_root, self.output_dir)
304:         self.token = os.environ.pop(TOKEN_ENV, "")
305:         self.last_sequence = 0
306:         if len(self.token) != 64:
307:             raise RuntimeError("legacy CE sidecar authentication token is unavailable")
308:         ce_root = (self.ideas_root / "CE").resolve()
309:         sys.path.insert(0, str(ce_root))
310:         with contextlib.redirect_stdout(sys.stderr):
311:             import ideas
312:             from ideas import Interconnect
313: 
314:             imported = Path(ideas.__file__).resolve()
315:             if not _is_under(ce_root, imported):
316:                 raise RuntimeError("legacy CE import escaped the selected Ideas root")
317:             self.import_origin = str(imported)
318:             self.interconnect = Interconnect(
319:                 str(self.output_dir), release_mode=self.release_mode
320:             )
321:             self.product_bootstrap_route = _select_product_safely(
322:                 self.interconnect, self.product_version
323:             )
324:         self.public_methods = _load_public_allowlist(args.api_allowlist)
325: 
326:     def evidence(self):
327:         return {
328:             "schema_version": 1,
329:             "session_id": self.session_id,
330:             "product_version": self.interconnect.get_ip_version(),
331:             "release_mode": self.release_mode,
332:             "pid": os.getpid(),
333:             "parent_pid": self.parent_pid,
334:             "python_executable": os.path.realpath(sys.executable),
335:             "python_version": ".".join(str(value) for value in sys.version_info[:3]),
336:             "ideas_import_origin": self.import_origin,
337:             "product_bootstrap_route": self.product_bootstrap_route,
338:         }
339: 
340:     def dispatch(self, command, payload):
341:         _validate_paths(payload, self.allowed_roots)
342:         if command == "health":
343:             return self.evidence()
344:         if command == "select_product":
345:             product_version = payload.get("product_version")
346:             if product_version != self.product_version:
347:                 raise ValueError(
348:                     "session_product_identity_mismatch: legacy CE sidecar product "
349:                     "transitions are not permitted"
350:                 )
351:             self.product_bootstrap_route = _select_product_safely(
352:                 self.interconnect, product_version
353:             )
354:             return {
355:                 "accepted": True,
356:                 "product_bootstrap_route": self.product_bootstrap_route,
357:             }
358:         if command == "call_public_method":
359:             method_name = payload.get("method")
360:             args = payload.get("args", [])
361:             kwargs = payload.get("kwargs", {})
362:             if method_name not in self.public_methods:
363:                 raise ValueError("public CE method is not in the packaged allowlist")
364:             if not isinstance(args, list) or not isinstance(kwargs, dict):
365:                 raise ValueError("public CE call arguments are malformed")
366:             _validate_paths(args, self.allowed_roots)
367:             _validate_paths(kwargs, self.allowed_roots)
368:             method = getattr(self.interconnect, method_name, None)
369:             if not callable(method):
370:                 raise ValueError("allowlisted CE method is unavailable in this product")
371:             return method(*args, **kwargs)
372:         if command == "state_manager_call":
373:             method_name = payload.get("method")
374:             if method_name not in STATE_MANAGER_METHODS:
```

## release-contract
Path: `ai/ia-mcp-pack/src/ia_mcp_pack/api_disposition_deployment.py`; SHA-256: `0e11d0318653d9190681b8e901e75397e0418b6755e776d8d5f86aeaf957d6cb`.
Lines 53-125; surviving authors: {'Michael Coulter': 73}.
```text
53: def check_or_bind_deployment(
54:     *,
55:     ideas_root: str | Path,
56:     pack_root: str | Path,
57:     ce_python: str | Path,
58:     temporary_root: str | Path,
59:     bind: bool,
60: ) -> dict[str, Any]:
61:     root = Path(ideas_root).resolve(strict=True)
62:     pack = Path(pack_root).resolve(strict=True)
63:     source_pack = (root / "ai" / "ia-mcp-pack").resolve(strict=True)
64:     if bind and pack == source_pack:
65:         raise APIDispositionError(
66:             "deployment binding must target a staged pack, never the tracked source pack"
67:         )
68:     canonical = pack / "generated" / API_DISPOSITION_RELATIVE_PATH.name
69:     reviewed_bytes = read_bounded_regular_file(
70:         canonical,
71:         max_bytes=API_DISPOSITION_MAX_BYTES,
72:         description="reviewed CE API disposition artifact",
73:     )
74:     dependency_root = pack.parent / "ia-mcp-runtime" / "site-packages"
75:     live_inventory, runtime_identity = generate_live_api_inventory(
76:         root,
77:         ce_python,
78:         temporary_root=temporary_root,
79:         additional_python_paths=([dependency_root] if dependency_root.is_dir() else []),
80:     )
81:     payload, binding = build_deployment_bound_api_disposition(
82:         root,
83:         canonical,
84:         live_inventory,
85:         runtime_identity=runtime_identity,
86:     )
87:     result = {
88:         "status": (
89:             "contract_equivalent"
90:             if binding["type"] == "reviewed_contract_equivalent_deployment"
91:             else "contract_drift_tolerated"
92:         ),
93:         "mode": "bind" if bind else "check",
94:         "reviewed_authority": binding["reviewed_authority"],
95:         "deployment_authority": binding["deployment_authority"],
96:         "comparison": binding["comparison"],
97:     }
98:     if not bind:
99:         return result
100: 
101:     reviewed = pack / "generated" / API_DISPOSITION_REVIEWED_RELATIVE_PATH.name
102:     if reviewed.exists() or reviewed.is_symlink():
103:         raise APIDispositionError(
104:             "staged reviewed CE API disposition authority already exists"
105:         )
106:     _atomic_write_bytes(reviewed, reviewed_bytes)
107:     write_api_disposition_artifact(payload, canonical)
108:     load_validated_api_disposition_artifact(root, canonical)
109:     result["status"] = "deployment_bound"
110:     if binding["type"] != "reviewed_contract_equivalent_deployment":
111:         result["status"] = "deployment_bound_with_api_drift"
112:         comparison = binding["comparison"]
113:         print(
114:             "WARNING: IA MCP packaged against CE API drift; native support was "
115:             "disabled only for affected operations and controlled fallback retains "
116:             "the complete live inventory: added={}, removed={}, signature_changed={}".format(
117:                 comparison["added_api_ids"],
118:                 comparison["removed_api_ids"],
119:                 comparison["signature_changed_api_ids"],
120:             ),
121:             file=sys.stderr,
122:         )
123:     result["deployment_artifact"] = API_DISPOSITION_RELATIVE_PATH.as_posix()
124:     return result
125: 
```

## owo-restore-attribution
Path: `GUI/src/app/interfaces/owo-setup/owo-setup.facade.ts`; SHA-256: `9cb3399712a9f7c46d06788872ce0d5ab3d14678a39e986ff4effe41e878e13e`.
Lines 169-215; surviving authors: {'Michael Coulter': 41, 'Dustin divis': 6}.
```text
169:   async createOpeningCheckpoint(): Promise<OwoOpeningCheckpoint> {
170:     const projectDirectory = this.projectService.projectDirectory;
171:     const projectLoadRevision = this.projectService.projectLoadRevision;
172:     if (!projectDirectory) throw new Error('No loaded project directory is available.');
173:     const context = { projectDirectory, projectLoadRevision };
174:     const checkpointPath = join(
175:       projectDirectory,
176:       'checkpoint',
177:       `owo_opening_${Date.now()}_${Math.random().toString(36).slice(2)}.yaml`,
178:     );
179:     // Independent of the Undo slot, which resource creation and Apply replace
180:     // during this session. Live mutations remain gated until this file is ready.
181:     await this.writeOpeningCheckpoint(checkpointPath, context, true);
182:     const fingerprint = await this.checkpointFingerprint(checkpointPath);
183:     this.assertCheckpointProjectCurrent(context);
184:     // Explicit checkpoint retry may establish the new project generation, but
185:     // cannot revive a destroyed view or any already-running operation.
186:     if (this.sessionCurrent()) this.sessionProject = context;
187:     return { path: checkpointPath, fingerprint, projectDirectory, projectLoadRevision };
188:   }
189: 
190:   async restoreOpeningCheckpoint(checkpoint: OwoOpeningCheckpoint): Promise<void> {
191:     this.assertCheckpointProjectCurrent(checkpoint);
192:     const fingerprint = await this.checkpointFingerprint(checkpoint.path);
193:     this.assertCheckpointProjectCurrent(checkpoint);
194:     if (fingerprint !== checkpoint.fingerprint) {
195:       throw new Error('The opening checkpoint changed; its design was not restored.');
196:     }
197:     // Reuse Undo's full CE copy semantics, independently of its bounded stack.
198:     // YAML import cannot faithfully restore all automatic CCG RP states: CE
199:     // exports DSNIs without resourcePlane and rejects them on re-import.
200:     await this.checkpointTerminal(
201:       `get_ip_version() and ((getattr(self, '_owo_opening_checkpoint', None) or (None,))[0] == ${JSON.stringify(checkpoint.path)} and (setattr(self, 'ic', copy.deepcopy(self._owo_opening_checkpoint[1])) or setattr(self, 'ic_stack', copy.deepcopy(self._owo_opening_checkpoint[2])) or self.ic.paths.invalidate_network_paths_cache() or True))`,
202:       'CE could not restore the opening project snapshot.',
203:     );
204:     this.assertCheckpointProjectCurrent(checkpoint);
205:     const verificationPath = checkpoint.path.replace(/\.yaml$/, '_restored.yaml');
206:     await this.writeOpeningCheckpoint(verificationPath, checkpoint);
207:     const restoredFingerprint = await this.checkpointFingerprint(verificationPath);
208:     this.assertCheckpointProjectCurrent(checkpoint);
209:     if (restoredFingerprint !== checkpoint.fingerprint) {
210:       throw new Error(
211:         'Checkpoint restoration completed, but the restored design could not be verified.',
212:       );
213:     }
214:     await this.keepPartialChanges();
215:     this.assertCheckpointProjectCurrent(checkpoint);
```

## latency-current
Path: `CE/ideas/report_impl/static_latency.py`; SHA-256: `9e020aa596bd889f5ae34b16b0a27d4ed0caa869af403c63f9c4ae8c7bc5460d`.
Lines 165-250; surviving authors: {'Tanushi Ahuja': 64, 'Kyan Kornfeld': 6, 'Michael Coulter': 12, 'Lin Gao': 4}.
```text
165:         'total_cycles': cycles
166:     }
167: 
168:     if include_metadata:
169:         route_data['total_min_cycles'] = min_cycles
170:         route_data['hop_sequence'] = hop_sequence
171: 
172:     return route_data
173: 
174: 
175: def calc_inst_latency(ic, inst, ch, next_hop, prev_hop):
176:     """Calculate latency for specific instance in the route."""
177:     default_lookup = ic.get_instance_attributes()['DefaultLatency']
178:     valid_retiming_params = [
179:         'adaptor/readRetimingStages', 'adaptor/writeRetimingStages',
180:         'adaptor/retimingStages'
181:     ]
182:     l = []
183:     # Instance type
184:     t = ic.get_instance_type(inst)
185:     # Instance clock
186:     clock = 'REVISIT'
187:     if t not in ('pcdcs', 'adbs', 'cdbs'):
188:         clock = ic.get_instance_clock(inst)
189:     else:
190:         clock = ic.get_upstream_downstream_clocks(inst)
191:         clock = f'{clock["upstream"]} -> {clock["downstream"]}'
192: 
193:     # Add default latency to the list
194:     assert t in default_lookup, ('Unexpected type', t)
195:     wm = ic.get_instance_wiremode(inst)
196:     if wm is None:
197:         wm = 'none'
198:     assert wm in default_lookup[t], ('Unexpected wire mode', wm, 'for type', t)
199:     assert ch in default_lookup[t][wm], ('Unexpected channel', ch, 'for type',
200:                                          t, 'and wire mode', wm)
201: 
202:     # default latency
203:     # dependent on wire mode and bypass for serdes
204:     bypass_enabled = False
205:     if t == 'serdes':
206:         try:
207:             wm_ch = channel_string_convert(ch) if ic.get_instance_wiremode(
208:                 inst) == 'high' else high_to_low_convert(ch)
209:             params = ic.get_channel_parameters(inst)
210:             bypass_enabled = params.get(f"{wm_ch}/bypass") == 'Enabled'
211:         except (KeyError, ValueError, AttributeError):
212:             bypass_enabled = False
213: 
214:     if default_lookup[t][wm][ch] > 0 and not (t == 'serdes' and bypass_enabled):
215:         if t == 'serdes':
216:             l.append({
217:                 'name': inst,
218:                 'type': t,
219:                 'wiremode': wm,
220:                 'clock': clock,
221:                 'reason': (
222:                     'Minimum latency through instance. This latency cycle does not occur when the SERDES '
223:                     'is bypassed by enabling Bypass, or when the input and output flit sizes are equal.'
224:                 ),
225:                 'min_cycles': default_lookup[t][wm][ch],
226:                 'cycles': default_lookup[t][wm][ch]
227:             })
228:         else:
229:             l.append({
230:                 'name': inst,
231:                 'type': t,
232:                 'wiremode': wm,
233:                 'clock': clock,
234:                 'reason': 'Minimum latency through instance',
235:                 'min_cycles': default_lookup[t][wm][ch],
236:                 'cycles': default_lookup[t][wm][ch]
237:             })
238: 
239:     # Caluclate latency from retiming stages
240:     params = ic.get_instance_parameters(inst)
241:     info = ic.get_instance_parameters_info(inst)
242:     wm = ic.get_instance_wiremode(inst)
243:     for p in info:
244:         if p not in valid_retiming_params:
245:             continue  # skip non-retiming params
246:         assert p in params, ('Unexpected parameter', p, 'in instance', inst,
247:                              ' of type', t)
248:         # bitcount = info[p]['constraints']['bitcount']
249:         value = params[p]
250:         for bit_index, bit_info in info[p]['constraints']['bits'].items():
```

## Static change-scope counts
Counts obtained from the captured numstat inventory, filtering changed source spec paths, not executing tests.
Commit `fff32ba2a4b6f0f5a1018df771e2ba0a6ef19439`: 51 changed Angular source spec files, 0 changed Playwright UI spec files. Configuration JSON filenames containing `.spec.` are excluded.
Commit `9851f748f2450a96ad59aab5521b3bc157ba79db`: 12 changed Angular source spec files, 5 changed Playwright UI spec files. Configuration JSON filenames containing `.spec.` are excluded.

## Historical path resolution
The tile-definition renderer moved under `GUI/src/app/canvas/renderers/svg/tile-definition/`; the tiling component is directly under `GUI/src/app/tiling-configuration/`. UDG regressions are under `GUI/tests/ui/user-defined-groups/` and `GUI/tests/ui/node-configuration/`. Fixture entry is `GUI/tests/fixtures/index.ts`.
The staging pipeline introduced as `jenkins/BuildReleases/Installer/daily-staging.Jenkinsfile` is now `jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`.
The old `resources/scripts/reports/report_static_latency.py` was pruned by Tanushi Ahuja in commit `5d3af6fe4` on 2026-03-05. The active report implementation is `CE/ideas/report_impl/static_latency.py`; pruning the standalone resource is not removal of all latency-reporting capability.
The historical mesh-route-viewer component was removed in Michael's `5d7183cf554c64341e5b7e1c4adfa3857ee4cac8` deadlock-workflow change; current custom route editing is in `GUI/src/app/canvas/ui/sidebar/mesh-route-editor/mesh-route-editor.component.ts`.
