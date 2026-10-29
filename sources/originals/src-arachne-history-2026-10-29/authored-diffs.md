# Complete Michael Coulter authored-object diff capture

PRIVATE local evidence captured 2026-10-29. Product code was not executed. All 20 ordinary authored commits and both stash-related objects are included. Stash changes are not delivered work.

Diffs use first-parent comparison, --no-renames and no external diff. Original Git command-output SHA-256 values are in history-inventory.json. Text uses UTF-8 with non-UTF-8 bytes escaped and line endings normalized. Line numbers here locate the extraction; hunk headers retain original source coordinates.

## 16654dee97f714a69586f4b1aac4fb7630cc7fb8

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 16654dee97f714a69586f4b1aac4fb7630cc7fb8
Author:     Michael Coulter <miccou01@login7.euhpc2.arm.com>
AuthorDate: Tue Nov 3 16:31:07 2020 +0000
Commit:     Michael Coulter <miccou01@login7.euhpc2.arm.com>
CommitDate: Tue Nov 3 16:31:07 2020 +0000

    Added Michael Coulter email to generate_top_summary.pl
    
    Change-Id: I7a89c649fa53c86bbb2bbd11312e4d2c35b63964

diff --git a/logical/shared/scripts/tooling_scripts/generate_top_summary.pl b/logical/shared/scripts/tooling_scripts/generate_top_summary.pl
index aafe2dd37d8..b3f004724d9 100755
--- a/logical/shared/scripts/tooling_scripts/generate_top_summary.pl
+++ b/logical/shared/scripts/tooling_scripts/generate_top_summary.pl
@@ -603,7 +603,7 @@ if ($perf_run) {
 } else {
   $to = 'Naveen.Anumalla@arm.com';
   $cc = 'Sean.Steel@arm.com, Hui.Zeng@arm.com, Alex.Kong@arm.com, ';
-  $cc = $cc . ' Chandan.Singh@arm.com, Pragya.Shukla@arm.com, Hardik.Makhaniya@arm.com';
+  $cc = $cc . ' Chandan.Singh@arm.com, Pragya.Shukla@arm.com, Hardik.Makhaniya@arm.com, Michael.Coulter@arm.com';
   if ($regr_root_custom ne "") {
     $subject = 'Booker NCI TOP: ' . $regr_name[-6] . " - " . $cfg . ' Regression Summary';
   } else {
```

## 4df3354cc2c16df21f6cfeddf2cb3bcef3efac32

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 4df3354cc2c16df21f6cfeddf2cb3bcef3efac32
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Thu Nov 5 16:57:56 2020 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Fri Nov 6 22:01:04 2020 +0000

    Update qverify_get_flops.tcl to list regs in 3D arrays
    
    Change-Id: I507a56d860880cb3dcfb37bf8b39805b5ff4a8e6

diff --git a/logical/shared/scripts/fusa/qverify_get_flops.tcl b/logical/shared/scripts/fusa/qverify_get_flops.tcl
index dce5a952fd5..9c5384bbdbe 100755
--- a/logical/shared/scripts/fusa/qverify_get_flops.tcl
+++ b/logical/shared/scripts/fusa/qverify_get_flops.tcl
@@ -1,116 +1,106 @@
-proc dumpFlops { module outputFile} {
-    namespace import -force Netlist::*
-    set nets [GetNets $module]
-    while { [set net [GetNext $nets]] != "" } {
-    # Get flipflops - scan all nets in this instance and only dump the register nets
-    if {[Query $net isInternal] || ![Query $net isReg] } { continue }
-    # Get wires - scan all the nets in this instance and dump only the "wires"
-    set reg [GetHdlPath $net]
-    set width [GetNetWidth $net]
-    set type [GetNetDataTypeName $net]
-    if {[string first "logic" $type] == -1} {
-      if {[string first "scalar" $type] == -1} {
-        echo "reg is $reg, width is $width, type is $type"
-        exit
-      }
-    }
-    set type_array [split $type \[]
-    set type_array_length [llength $type_array]
-    #echo "reg is $reg, width is $width, type is $type, type_array_length = $type_array_length"
-
-    # Single bit wires, etc
-    if {$type_array_length == 1 || $width == 1} {
-      puts $outputFile $reg
-
-    # One-Dimensional Arrays
-    } elseif {$type_array_length == 2} {
-
-      # get dimensions of the array
-      set type [string trim [lindex $type_array 1]]
-      set type [string trim $type \]]
-      set register_index [split $type :]
-      set register_1st_index [lindex $register_index 0]
-      set register_2nd_index [lindex $register_index 1]
-      set register_max_index [expr max($register_1st_index, $register_2nd_index)]
-      set register_min_index [expr min($register_1st_index, $register_2nd_index)]
-      if {$width != [expr $register_max_index - $register_min_index + 1]} {
-        echo "width = $width, but max = $register_max_index and min = $register_min_index"
-        exit
-      }
-
-      #print to file
-      set i $register_min_index
-      while  {$i <= $register_max_index} {
-        puts $outputFile "$reg\($i\)"
-        set i [expr $i + 1]
-      }
-    # Two dimensional arrays
-    } elseif {$type_array_length == 3} {
-
-      # get dimensions of the first array
-      set first_array_dimensions [string trim [lindex $type_array 1]]
-      set first_array_dimensions [string trim $first_array_dimensions \]]
-      set first_array_dimensions [split $first_array_dimensions :]
-      set first_array_1st_index  [lindex $first_array_dimensions 0]
-      set first_array_2nd_index  [lindex $first_array_dimensions 1]
-      set first_array_max_index   [expr max($first_array_1st_index, $first_array_2nd_index)]
-      set first_array_min_index   [expr min($first_array_1st_index, $first_array_2nd_index)]
-
-      # get dimensions of the 2nd array
-      set second_array_dimensions [string trim [lindex $type_array 2]]
-      set second_array_dimensions [string trim $second_array_dimensions \]]
-      set second_array_dimensions [split $second_array_dimensions :]
-      set second_array_1st_index  [lindex $second_array_dimensions 0]
-      set second_array_2nd_index  [lindex $second_array_dimensions 1]
-      set second_array_max_index  [expr max($second_array_1st_index, $second_array_2nd_index)]
-      set second_array_min_index  [expr min($second_array_1st_index, $second_array_2nd_index)]
-
-      # print to file
-      set i $first_array_min_index
-      while  {$i <= $first_array_max_index} {
-        set j $second_array_min_index
-        while {$j <= $second_array_max_index} {
-          puts $outputFile "$reg\($i\)\($j\)"
-          set j [expr $j + 1]
-        }
-        set i [expr $i + 1]
-      }
-
-
-    } else {
-      echo "error - length too long $type"
-      echo "net is: $reg"
-      continue
-#      exit
-    }
-
-    #echo "reg is $reg, width is $width, type is $type, type_array_length = $type_array_length"
-    }
-    set insts [GetInstances $module]
-    while { [set inst [GetNext $insts]] != "" } {
-      set downModule [GetMasterModule $inst]
-      # descend recursively through the instance hierarchy
-      dumpFlops $downModule $outputFile
-    }
-}
-
-# start from the -d top module and descend down through the design
-# finding all the register nets
-set topMod [Netlist::GetTopModule]
-set outputFile [open "chariot_register_file.txt" w]
-dumpFlops $topMod $outputFile
-close $outputFile
-
-
-#set topInstance [Netlist::GetInstance testbench.dut_inst]
-#set topInstance [Netlist::GetInstance porter.u_sbsx_nid8]
-#set topMod [Netlist::GetMasterModule $topInstance]
-
-  # if { [Query $net isInternal] || [Query $net isReg] || [Query $net isLatch] || [Query $net isMem]} { continue }
-    #if {[GetNetWidth $net] > 1} {
-      #set left [GetNetLeft $net]
-      #set right [GetNetRight $net]
-      #echo "$reg\[$left:$right\]"
-    #} else {
-      #echo "$reg $width $type"
-    #}
+proc printArray { outputFile reg_name array_size max_array_index min_array_index current_array_index } {
+
+  #create the flop name
+  set index 0
+  set flop_name $reg_name
+  while { $index < $array_size } {
+    set flop_name "$flop_name\([lindex $current_array_index $index]\)"
+    set index [expr $index + 1]
+  }
+  puts $outputFile $flop_name
+
+  # pick the next entry to write
+  set next_index $current_array_index
+  set index 0
+  while { $index < $array_size } {
+    if {[lindex $current_array_index $index] == [lindex $max_array_index $index]} {
+      lset next_index $index [lindex $min_array_index $index]
+      set index [expr $index + 1] 
+    } else {
+      lset next_index $index [expr [lindex $current_array_index $index] + 1]
+      printArray $outputFile $reg_name $array_size $max_array_index $min_array_index $next_index
+      break
+    }
+  }
+}
+
+proc dumpFlops { module outputFile } {
+  namespace import -force Netlist::*
+  set nets [GetNets $module]
+  while { [set net [GetNext $nets]] != "" } {
+    # Get flipflops - scan all nets in this instance and only dump the register nets
+    if {[Query $net isInternal] || ![Query $net isReg] } { continue }
+    # Get wires - scan all the nets in this instance and dump only the "wires"
+    set reg [GetHdlPath $net]
+    set width [GetNetWidth $net]
+    set type [GetNetDataTypeName $net]
+    if {[string first "logic" $type] == -1} {
+      if {[string first "scalar" $type] == -1} {
+        echo "reg is $reg, width is $width, type is $type"
+        exit
+      }
+    }
+    set type_array [split $type \[]
+    set type_array_length [llength $type_array]
+    #echo "reg is $reg, width is $width, type is $type, type_array_length = $type_array_length"
+
+    # Single bit wires, etc
+    if {$type_array_length == 1 || $width == 1} {
+      puts $outputFile $reg
+
+    # Arrays
+    } else {
+      set max_index ""
+      set min_index ""
+      set index 1
+     # set full_reg_string $reg
+      while {$index < $type_array_length} {
+        set array_dimensions [string trim [lindex $type_array $index]]
+        set array_dimensions [string trim $array_dimensions \]]
+        set array_dimensions [split $array_dimensions :]
+        set array_1st_index  [lindex $array_dimensions 0]
+        set array_2nd_index  [lindex $array_dimensions 1]
+        set array_max_index   [expr max($array_1st_index, $array_2nd_index)]
+        set array_min_index   [expr min($array_1st_index, $array_2nd_index)]
+        lappend max_index $array_max_index
+        lappend min_index $array_min_index
+        set index [expr $index + 1]
+      }
+
+      # print to file
+      printArray $outputFile $reg [expr $type_array_length - 1] $max_index $min_index $min_index
+    }
+
+  #echo "reg is $reg, width is $width, type is $type, type_array_length = $type_array_length"
+  }
+  set insts [GetInstances $module]
+  while { [set inst [GetNext $insts]] != "" } {
+    set downModule [GetMasterModule $inst]
+    # descend recursively through the instance hierarchy
+    dumpFlops $downModule $outputFile
+  }
+}
+
+# start from the -d top module and descend down through the design
+# finding all the register nets
+set topMod [Netlist::GetTopModule]
+set outputFile [open "chariot_register_file.txt" w]
+# increase recursion limit - tcl 8.6 has no limit, and some multi-dimensional arrays are > 1000, which is the default tcl limit
+interp recursionlimit {} 64000
+dumpFlops $topMod $outputFile
+close $outputFile
+echo "Successfully wrote flops to [pwd]/chariot_register_file.txt"
+
+
+#set topInstance [Netlist::GetInstance testbench.dut_inst]
+#set topInstance [Netlist::GetInstance porter.u_sbsx_nid8]
+#set topMod [Netlist::GetMasterModule $topInstance]
+
+  # if { [Query $net isInternal] || [Query $net isReg] || [Query $net isLatch] || [Query $net isMem]} { continue }
+    #if {[GetNetWidth $net] > 1} {
+      #set left [GetNetLeft $net]
+      #set right [GetNetRight $net]
+      #echo "$reg\[$left:$right\]"
+    #} else {
+      #echo "$reg $width $type"
+    #}
```

## 492593a8f1b7a15c8f12174cda9bcf7cfd7f6c8b

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 492593a8f1b7a15c8f12174cda9bcf7cfd7f6c8b
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Wed Dec 9 10:34:44 2020 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Wed Dec 9 10:42:22 2020 +0000

    Add chariot package that includes the chariot_parity_generation and the chariot_parity_checker modules
    Add brunel_1x1_ACE5Lite_AXI5_chariot iyaml and corresponding generated syaml, and update chariot_fault_injection.ctrl to use new config
    Add --fullacc arg to ae simulate command in chariot_fault_injection.ctrl
    Add CHARIOT_ASIL_B defines and check_user condition to amba5_payload_checker_component.svh
    Modify testbench to instantiate parity read modules and associated signals
    Modify noc_testbench_wrapper.py to connect err_detection_code to ACELITE_SLAVE_S0_IF_WUSER
    Modify param_engine scripts to conditionally modify noc_testbench_wrapper.py for chariot by supplying the ae param_engine command with the '--chariot_b' flag
    large commit
    
    Change-Id: I0e9110c81797aafd0a0737f931cf64dd16a51478

diff --git a/configs/brunel_1x1_ACE5Lite_AXI5_chariot/brunel_1x1_ACE5Lite_AXI5_chariot.yaml b/configs/brunel_1x1_ACE5Lite_AXI5_chariot/brunel_1x1_ACE5Lite_AXI5_chariot.yaml
new file mode 100644
index 00000000000..ba858f2e469
--- /dev/null
+++ b/configs/brunel_1x1_ACE5Lite_AXI5_chariot/brunel_1x1_ACE5Lite_AXI5_chariot.yaml
@@ -0,0 +1,1358 @@
+---
+AddressRegions:
+  mm0_cfg:
+    endAddress: 0xffff
+    startAddress: 0x0
+    targets:
+      default: ARACHNE_CONFIGURATION_SPACE
+  mm0_m0_if:
+    endAddress: 0x1ffff
+    startAddress: 0x10000
+    targets:
+      default: m0_if
+ClockDomains:
+  clk0:
+    frequency: 1000
+    frequencyUnit: MHz
+    powerDomain: pd0
+    type: managed
+  clk1:
+    frequency: 2000
+    frequencyUnit: MHz
+    powerDomain: pd0
+    type: managed
+ClockRelations:
+- ClockRelation:
+    clockOne: clk0
+    clockTwo: clk1
+    relationType: synchronous
+ConfigurationSpaces:
+  ARACHNE_CONFIGURATION_SPACE:
+    baseAddress: 0x0
+Connections:
+  link__u_cfgni_pd0__u_router_0__readResponse__0:
+    Protocol:
+    - MemDevRRESP
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: readResponse
+    TargetNode:
+      instanceName: u_router_0
+      interface: core(2)/input(0)
+  link__u_cfgni_pd0__u_router_0__writeResponse__0:
+    Protocol:
+    - MemDevWRESP
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: writeResponse
+    TargetNode:
+      instanceName: u_router_0
+      interface: core(3)/input(0)
+  link__u_cfgni_pd0__u_router_cfg_clk0__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceRequest
+    TargetNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(0)/input(0)
+  link__u_m0__u_router_0__readResponse__0:
+    Protocol:
+    - MemDevRRESP
+    SourceNode:
+      instanceName: u_m0
+      interface: readResponse
+    TargetNode:
+      instanceName: u_router_0
+      interface: core(2)/input(1)
+  link__u_m0__u_router_0__writeResponse__0:
+    Protocol:
+    - MemDevWRESP
+    SourceNode:
+      instanceName: u_m0
+      interface: writeResponse
+    TargetNode:
+      instanceName: u_router_0
+      interface: core(3)/input(1)
+  link__u_m0__u_router_cfg_clk0__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_m0
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(1)/input(0)
+  link__u_pcdc_0_downstream__u_pcdc_0_upstream__readResponse__0:
+    Protocol:
+    - MemDevRRESP
+    SourceNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(2)/output
+    TargetNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(2)/input
+  link__u_pcdc_0_downstream__u_pcdc_0_upstream__writeResponse__0:
+    Protocol:
+    - MemDevWRESP
+    SourceNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(3)/output
+    TargetNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(3)/input
+  link__u_pcdc_0_downstream__u_router_0__readRequest__0:
+    Protocol:
+    - MemDevRREQ
+    SourceNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(0)/output
+    TargetNode:
+      instanceName: u_router_0
+      interface: core(0)/input(0)
+  link__u_pcdc_0_downstream__u_router_0__writeRequest__0:
+    Protocol:
+    - MemDevWREQ
+    SourceNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(1)/output
+    TargetNode:
+      instanceName: u_router_0
+      interface: core(1)/input(0)
+  link__u_pcdc_0_upstream__u_pcdc_0_downstream__readRequest__0:
+    Protocol:
+    - MemDevRREQ
+    SourceNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(0)/output
+    TargetNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(0)/input
+  link__u_pcdc_0_upstream__u_pcdc_0_downstream__writeRequest__0:
+    Protocol:
+    - MemDevWREQ
+    SourceNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(1)/output
+    TargetNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(1)/input
+  link__u_pcdc_0_upstream__u_s0__readResponse__0:
+    Protocol:
+    - MemDevRRESP
+    SourceNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(2)/output
+    TargetNode:
+      instanceName: u_s0
+      interface: readResponse
+  link__u_pcdc_0_upstream__u_s0__writeResponse__0:
+    Protocol:
+    - MemDevWRESP
+    SourceNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(3)/output
+    TargetNode:
+      instanceName: u_s0
+      interface: writeResponse
+  link__u_pcdc_cfgni_clk1_downstream__u_pcdc_cfgni_clk1_upstream__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_pcdc_cfgni_clk1_downstream
+      interface: core(1)/output
+    TargetNode:
+      instanceName: u_pcdc_cfgni_clk1_upstream
+      interface: core(1)/input
+  link__u_pcdc_cfgni_clk1_downstream__u_router_cfg_clk1__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_pcdc_cfgni_clk1_downstream
+      interface: core(0)/output
+    TargetNode:
+      instanceName: u_router_cfg_clk1
+      interface: core(0)/input(0)
+  link__u_pcdc_cfgni_clk1_upstream__u_pcdc_cfgni_clk1_downstream__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_pcdc_cfgni_clk1_upstream
+      interface: core(0)/output
+    TargetNode:
+      instanceName: u_pcdc_cfgni_clk1_downstream
+      interface: core(0)/input
+  link__u_pcdc_cfgni_clk1_upstream__u_router_cfg_clk0__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_pcdc_cfgni_clk1_upstream
+      interface: core(1)/output
+    TargetNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(1)/input(2)
+  link__u_pmu_clk0__u_router_cfg_clk0__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_pmu_clk0
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(1)/input(1)
+  link__u_pmu_clk1__u_router_cfg_clk1__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_pmu_clk1
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_router_cfg_clk1
+      interface: core(1)/input(0)
+  link__u_router_0__u_cfgni_pd0__readRequest__0:
+    Protocol:
+    - MemDevRREQ
+    SourceNode:
+      instanceName: u_router_0
+      interface: core(0)/output(0)
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: readRequest
+  link__u_router_0__u_cfgni_pd0__writeRequest__0:
+    Protocol:
+    - MemDevWREQ
+    SourceNode:
+      instanceName: u_router_0
+      interface: core(1)/output(0)
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: writeRequest
+  link__u_router_0__u_m0__readRequest__0:
+    Protocol:
+    - MemDevRREQ
+    SourceNode:
+      instanceName: u_router_0
+      interface: core(0)/output(1)
+    TargetNode:
+      instanceName: u_m0
+      interface: readRequest
+  link__u_router_0__u_m0__writeRequest__0:
+    Protocol:
+    - MemDevWREQ
+    SourceNode:
+      instanceName: u_router_0
+      interface: core(1)/output(1)
+    TargetNode:
+      instanceName: u_m0
+      interface: writeRequest
+  link__u_router_0__u_pcdc_0_downstream__readResponse__0:
+    Protocol:
+    - MemDevRRESP
+    SourceNode:
+      instanceName: u_router_0
+      interface: core(2)/output(0)
+    TargetNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(2)/input
+  link__u_router_0__u_pcdc_0_downstream__writeResponse__0:
+    Protocol:
+    - MemDevWRESP
+    SourceNode:
+      instanceName: u_router_0
+      interface: core(3)/output(0)
+    TargetNode:
+      instanceName: u_pcdc_0_downstream
+      interface: core(3)/input
+  link__u_router_cfg_clk0__u_cfgni_pd0__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(1)/output(0)
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceResponse
+  link__u_router_cfg_clk0__u_m0__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(0)/output(0)
+    TargetNode:
+      instanceName: u_m0
+      interface: utilityBusRequest
+  link__u_router_cfg_clk0__u_pcdc_cfgni_clk1_upstream__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(0)/output(2)
+    TargetNode:
+      instanceName: u_pcdc_cfgni_clk1_upstream
+      interface: core(0)/input
+  link__u_router_cfg_clk0__u_pmu_clk0__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_router_cfg_clk0
+      interface: core(0)/output(1)
+    TargetNode:
+      instanceName: u_pmu_clk0
+      interface: utilityBusRequest
+  link__u_router_cfg_clk1__u_pcdc_cfgni_clk1_downstream__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_router_cfg_clk1
+      interface: core(1)/output(0)
+    TargetNode:
+      instanceName: u_pcdc_cfgni_clk1_downstream
+      interface: core(1)/input
+  link__u_router_cfg_clk1__u_pmu_clk1__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_router_cfg_clk1
+      interface: core(0)/output(0)
+    TargetNode:
+      instanceName: u_pmu_clk1
+      interface: utilityBusRequest
+  link__u_router_cfg_clk1__u_s0__aubRequest__0:
+    Protocol:
+    - AubREQ
+    SourceNode:
+      instanceName: u_router_cfg_clk1
+      interface: core(0)/output(1)
+    TargetNode:
+      instanceName: u_s0
+      interface: utilityBusRequest
+  link__u_s0__u_pcdc_0_upstream__readRequest__0:
+    Protocol:
+    - MemDevRREQ
+    SourceNode:
+      instanceName: u_s0
+      interface: readRequest
+    TargetNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(0)/input
+  link__u_s0__u_pcdc_0_upstream__writeRequest__0:
+    Protocol:
+    - MemDevWREQ
+    SourceNode:
+      instanceName: u_s0
+      interface: writeRequest
+    TargetNode:
+      instanceName: u_pcdc_0_upstream
+      interface: core(1)/input
+  link__u_s0__u_router_cfg_clk1__aubResponse__0:
+    Protocol:
+    - AubRESP
+    SourceNode:
+      instanceName: u_s0
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_router_cfg_clk1
+      interface: core(1)/input(1)
+Instances:
+  u_cfgni_pd0:
+    LocalAccessMap:
+      u_m0:
+        req: route_AubREQ_u_cfgni_pd0_localSourceRequest_u_m0_utilityBusRequest
+      u_pmu_clk0:
+        req: route_AubREQ_u_cfgni_pd0_localSourceRequest_u_pmu_clk0_utilityBusRequest
+      u_pmu_clk1:
+        req: route_AubREQ_u_cfgni_pd0_localSourceRequest_u_pmu_clk1_utilityBusRequest
+      u_s0:
+        req: route_AubREQ_u_cfgni_pd0_localSourceRequest_u_s0_utilityBusRequest
+    Parameters:
+      configNetworkNodeID: 0
+      gateway/mergedReadWriteRequest: Disabled
+      localSourceRequest/all.resourcePlanesPresent: 1
+      localSourceRequest/rp(0)/all.rp.flitSize: 1
+      localSourceRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      localSourceRequest/rp(0)/genericParameters: aubInterfaceParameters
+      localSourceResponse/all.resourcePlanesPresent: 1
+      localSourceResponse/rp(0)/all.rp.flitSize: 1
+      localSourceResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      localSourceResponse/rp(0)/genericParameters: aubInterfaceParameters
+      readRequest/all.resourcePlanesPresent: 1
+      readRequest/rp(0)/all.rp.flitSize: 3
+      readRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      readRequest/rp(0)/genericParameters: ambaInterfaceParameters
+      readResponse/all.resourcePlanesPresent: 1
+      readResponse/rp(0)/all.rp.flitSize: 3
+      readResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      readResponse/rp(0)/genericParameters: ambaInterfaceParameters
+      writeRequest/all.resourcePlanesPresent: 1
+      writeRequest/rp(0)/all.rp.flitSize: 5
+      writeRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      writeRequest/rp(0)/genericParameters: ambaInterfaceParameters
+      writeResponse/all.resourcePlanesPresent: 1
+      writeResponse/rp(0)/all.rp.flitSize: 1
+      writeResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      writeResponse/rp(0)/genericParameters: ambaInterfaceParameters
+    RemoteAccessMap: {}
+    ReturnRoutes:
+      u_s0:
+        rresp: route_MemDevRRESP_u_cfgni_pd0_readResponse_u_s0_readResponse
+        wresp: route_MemDevWRESP_u_cfgni_pd0_writeResponse_u_s0_writeResponse
+    clockDomain: clk0
+    componentName: cfgni_pd0
+    instanceName: u_cfgni_pd0
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: CFGNI
+      version: r0p0
+    voltageDomain: vd0
+  u_clock_ctrl_clk0:
+    Parameters:
+      numberOfExtSynchroniserStages: 2
+      numberOfPowerSynchroniserStages: 2
+      retimingDepth: 4
+    clockDomain: clk0
+    componentName: clock_ctrl_clk0
+    instanceName: u_clock_ctrl_clk0
+    interface:
+    - clock_ctrl_clk0_if
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: CLKCTRL
+      version: r0p0
+    voltageDomain: vd0
+  u_clock_ctrl_clk1:
+    Parameters:
+      numberOfExtSynchroniserStages: 2
+      numberOfPowerSynchroniserStages: 2
+      retimingDepth: 4
+    clockDomain: clk1
+    componentName: clock_ctrl_clk1
+    instanceName: u_clock_ctrl_clk1
+    interface:
+    - clock_ctrl_clk1_if
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: CLKCTRL
+      version: r0p0
+    voltageDomain: vd0
+  u_m0:
+    ConfigReturnRoutes:
+      u_cfgni_pd0:
+        resp: route_AubRESP_u_m0_utilityBusResponse_u_cfgni_pd0_localSourceResponse
+    Parameters:
+      adaptor/burstSplitting: Enabled
+      adaptor/idm: Disabled
+      adaptor/idmDeviceId: 0
+      adaptor/protocol: AXI5
+      adaptor/readRetimingStages: 3
+      adaptor/starvationAvoidancePeriod: 12
+      adaptor/writeRetimingStages: 6
+      configNetworkNodeID: 1
+      eventRetimingStages: 0
+      gateway/mergedReadWriteRequest: Disabled
+      nodeID: 0
+      readRequest/all.resourcePlanesPresent: 1
+      readRequest/rp(0)/all.rp.flitSize: 3
+      readRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      readRequest/rp(0)/genericParameters: ambaInterfaceParameters
+      readResponse/all.resourcePlanesPresent: 1
+      readResponse/rp(0)/all.rp.flitSize: 3
+      readResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      readResponse/rp(0)/genericParameters: ambaInterfaceParameters
+      utilityBusRequest/all.resourcePlanesPresent: 1
+      utilityBusRequest/rp(0)/all.rp.flitSize: 1
+      utilityBusRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusRequest/rp(0)/genericParameters: aubInterfaceParameters
+      utilityBusResponse/all.resourcePlanesPresent: 1
+      utilityBusResponse/rp(0)/all.rp.flitSize: 1
+      utilityBusResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusResponse/rp(0)/genericParameters: aubInterfaceParameters
+      writeRequest/all.resourcePlanesPresent: 1
+      writeRequest/rp(0)/all.rp.flitSize: 5
+      writeRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      writeRequest/rp(0)/genericParameters: ambaInterfaceParameters
+      writeResponse/all.resourcePlanesPresent: 1
+      writeResponse/rp(0)/all.rp.flitSize: 1
+      writeResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      writeResponse/rp(0)/genericParameters: ambaInterfaceParameters
+    ReturnRoutes:
+      u_s0:
+        rresp: route_MemDevRRESP_u_m0_readResponse_u_s0_readResponse
+        wresp: route_MemDevWRESP_u_m0_writeResponse_u_s0_writeResponse
+    clockDomain: clk0
+    componentName: m0
+    instanceName: u_m0
+    interface:
+    - m0_if
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: AMNI
+      version: r0p0
+    voltageDomain: vd0
+  u_pcdc_0_downstream:
+    Parameters:
+      core(0)/all.resourcePlanesPresent: 1
+      core(0)/clockCrossingType: MToOne
+      core(0)/coreType: downstream
+      core(0)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/fifoBypass: Disabled
+      core(0)/multicycleDelay: 0
+      core(0)/registeredOutputs: Disabled
+      core(0)/rp(0)/all.rp.flitSize: 3
+      core(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(1)/all.resourcePlanesPresent: 1
+      core(1)/clockCrossingType: MToOne
+      core(1)/coreType: downstream
+      core(1)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/fifoBypass: Disabled
+      core(1)/multicycleDelay: 0
+      core(1)/registeredOutputs: Disabled
+      core(1)/rp(0)/all.rp.flitSize: 5
+      core(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(2)/all.resourcePlanesPresent: 1
+      core(2)/clockCrossingType: OneToN
+      core(2)/coreType: upstream
+      core(2)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/fifoBypass: Disabled
+      core(2)/multicycleDelay: 0
+      core(2)/registeredInputs: Disabled
+      core(2)/rp(0)/all.rp.flitSize: 3
+      core(2)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(3)/all.resourcePlanesPresent: 1
+      core(3)/clockCrossingType: OneToN
+      core(3)/coreType: upstream
+      core(3)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/fifoBypass: Disabled
+      core(3)/multicycleDelay: 0
+      core(3)/registeredInputs: Disabled
+      core(3)/rp(0)/all.rp.flitSize: 1
+      core(3)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/rp(0)/genericParameters: ambaInterfaceParameters
+      crossesPowerDomain: Disabled
+      numberOfCores: 4
+      siblingComponent: u_pcdc_0_upstream
+    clockDomain: clk0
+    componentName: pcdc_0_downstream
+    instanceName: u_pcdc_0_downstream
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: PCDC
+      version: r0p0
+    voltageDomain: vd0
+  u_pcdc_0_upstream:
+    Parameters:
+      core(0)/all.resourcePlanesPresent: 1
+      core(0)/clockCrossingType: MToOne
+      core(0)/coreType: upstream
+      core(0)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/fifoBypass: Disabled
+      core(0)/multicycleDelay: 0
+      core(0)/registeredInputs: Disabled
+      core(0)/rp(0)/all.rp.flitSize: 3
+      core(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(1)/all.resourcePlanesPresent: 1
+      core(1)/clockCrossingType: MToOne
+      core(1)/coreType: upstream
+      core(1)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/fifoBypass: Disabled
+      core(1)/multicycleDelay: 0
+      core(1)/registeredInputs: Disabled
+      core(1)/rp(0)/all.rp.flitSize: 5
+      core(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(2)/all.resourcePlanesPresent: 1
+      core(2)/clockCrossingType: OneToN
+      core(2)/coreType: downstream
+      core(2)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/fifoBypass: Disabled
+      core(2)/multicycleDelay: 0
+      core(2)/registeredOutputs: Disabled
+      core(2)/rp(0)/all.rp.flitSize: 3
+      core(2)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(3)/all.resourcePlanesPresent: 1
+      core(3)/clockCrossingType: OneToN
+      core(3)/coreType: downstream
+      core(3)/crossing/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/fifoBypass: Disabled
+      core(3)/multicycleDelay: 0
+      core(3)/registeredOutputs: Disabled
+      core(3)/rp(0)/all.rp.flitSize: 1
+      core(3)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/rp(0)/genericParameters: ambaInterfaceParameters
+      crossesPowerDomain: Disabled
+      numberOfCores: 4
+      siblingComponent: u_pcdc_0_downstream
+    clockDomain: clk1
+    componentName: pcdc_0_upstream
+    instanceName: u_pcdc_0_upstream
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: PCDC
+      version: r0p0
+    voltageDomain: vd0
+  u_pcdc_cfgni_clk1_downstream:
+    Parameters:
+      core(0)/all.resourcePlanesPresent: 1
+      core(0)/clockCrossingType: OneToN
+      core(0)/coreType: downstream
+      core(0)/crossing/rp(0)/all.rp.numberOfChannelCredits: 6
+      core(0)/fifoBypass: Disabled
+      core(0)/multicycleDelay: 0
+      core(0)/registeredOutputs: Disabled
+      core(0)/rp(0)/all.rp.flitSize: 1
+      core(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: aubInterfaceParameters
+      core(1)/all.resourcePlanesPresent: 1
+      core(1)/clockCrossingType: MToOne
+      core(1)/coreType: upstream
+      core(1)/crossing/rp(0)/all.rp.numberOfChannelCredits: 6
+      core(1)/fifoBypass: Disabled
+      core(1)/multicycleDelay: 0
+      core(1)/registeredInputs: Disabled
+      core(1)/rp(0)/all.rp.flitSize: 1
+      core(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: aubInterfaceParameters
+      crossesPowerDomain: Disabled
+      numberOfCores: 2
+      siblingComponent: u_pcdc_cfgni_clk1_upstream
+    clockDomain: clk1
+    componentName: pcdc_cfgni_clk1_downstream
+    instanceName: u_pcdc_cfgni_clk1_downstream
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: PCDC
+      version: r0p0
+    voltageDomain: vd0
+  u_pcdc_cfgni_clk1_upstream:
+    Parameters:
+      core(0)/all.resourcePlanesPresent: 1
+      core(0)/clockCrossingType: OneToN
+      core(0)/coreType: upstream
+      core(0)/crossing/rp(0)/all.rp.numberOfChannelCredits: 6
+      core(0)/fifoBypass: Disabled
+      core(0)/multicycleDelay: 0
+      core(0)/registeredInputs: Disabled
+      core(0)/rp(0)/all.rp.flitSize: 1
+      core(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: aubInterfaceParameters
+      core(1)/all.resourcePlanesPresent: 1
+      core(1)/clockCrossingType: MToOne
+      core(1)/coreType: downstream
+      core(1)/crossing/rp(0)/all.rp.numberOfChannelCredits: 6
+      core(1)/fifoBypass: Disabled
+      core(1)/multicycleDelay: 0
+      core(1)/registeredOutputs: Disabled
+      core(1)/rp(0)/all.rp.flitSize: 1
+      core(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: aubInterfaceParameters
+      crossesPowerDomain: Disabled
+      numberOfCores: 2
+      siblingComponent: u_pcdc_cfgni_clk1_downstream
+    clockDomain: clk0
+    componentName: pcdc_cfgni_clk1_upstream
+    instanceName: u_pcdc_cfgni_clk1_upstream
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: PCDC
+      version: r0p0
+    voltageDomain: vd0
+  u_pmu_clk0:
+    ConfigReturnRoutes:
+      u_cfgni_pd0:
+        resp: route_AubRESP_u_pmu_clk0_utilityBusResponse_u_cfgni_pd0_localSourceResponse
+    Parameters:
+      configNetworkNodeID: 2
+      globalEventRetimingMode: 4
+      numSyncStages: 2
+      utilityBusRequest/all.resourcePlanesPresent: 1
+      utilityBusRequest/rp(0)/all.rp.flitSize: 1
+      utilityBusRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusRequest/rp(0)/genericParameters: aubInterfaceParameters
+      utilityBusResponse/all.resourcePlanesPresent: 1
+      utilityBusResponse/rp(0)/all.rp.flitSize: 1
+      utilityBusResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusResponse/rp(0)/genericParameters: aubInterfaceParameters
+    clockDomain: clk0
+    componentName: pmu_clk0
+    instanceName: u_pmu_clk0
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: PMU
+      version: r0p0
+    voltageDomain: vd0
+  u_pmu_clk1:
+    ConfigReturnRoutes:
+      u_cfgni_pd0:
+        resp: route_AubRESP_u_pmu_clk1_utilityBusResponse_u_cfgni_pd0_localSourceResponse
+    Parameters:
+      configNetworkNodeID: 4
+      globalEventRetimingMode: 4
+      numSyncStages: 2
+      utilityBusRequest/all.resourcePlanesPresent: 1
+      utilityBusRequest/rp(0)/all.rp.flitSize: 1
+      utilityBusRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusRequest/rp(0)/genericParameters: aubInterfaceParameters
+      utilityBusResponse/all.resourcePlanesPresent: 1
+      utilityBusResponse/rp(0)/all.rp.flitSize: 1
+      utilityBusResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusResponse/rp(0)/genericParameters: aubInterfaceParameters
+    clockDomain: clk1
+    componentName: pmu_clk1
+    instanceName: u_pmu_clk1
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: PMU
+      version: r0p0
+    voltageDomain: vd0
+  u_power_ctrl_pd0:
+    Parameters:
+      combiner/numberOfSynchroniserStages: 3
+      numberOfSynchroniserStages: 2
+    clockDomain: clk0
+    componentName: power_ctrl_pd0
+    instanceName: u_power_ctrl_pd0
+    interface:
+    - power_ctrl_pd0_if
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd_external
+    typeID:
+      name: POWERCTRL
+      version: r0p0
+    voltageDomain: vd0
+  u_router_0:
+    Parameters:
+      core(0)/input(0)/all.resourcePlanesPresent: 1
+      core(0)/input(0)/registeredInputs: Disabled
+      core(0)/input(0)/rp(0)/all.rp.flitSize: 3
+      core(0)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(0)/all.resourcePlanesPresent: 1
+      core(0)/output(0)/registeredOutputs: Disabled
+      core(0)/output(0)/rp(0)/all.rp.flitSize: 3
+      core(0)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(1)/all.resourcePlanesPresent: 1
+      core(0)/output(1)/registeredOutputs: Disabled
+      core(0)/output(1)/rp(0)/all.rp.flitSize: 3
+      core(0)/output(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(0)/starvationAvoidancePeriod: 15
+      core(1)/input(0)/all.resourcePlanesPresent: 1
+      core(1)/input(0)/registeredInputs: Disabled
+      core(1)/input(0)/rp(0)/all.rp.flitSize: 5
+      core(1)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/output(0)/all.resourcePlanesPresent: 1
+      core(1)/output(0)/registeredOutputs: Disabled
+      core(1)/output(0)/rp(0)/all.rp.flitSize: 5
+      core(1)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/output(1)/all.resourcePlanesPresent: 1
+      core(1)/output(1)/registeredOutputs: Disabled
+      core(1)/output(1)/rp(0)/all.rp.flitSize: 5
+      core(1)/output(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(1)/starvationAvoidancePeriod: 15
+      core(2)/input(0)/all.resourcePlanesPresent: 1
+      core(2)/input(0)/registeredInputs: Disabled
+      core(2)/input(0)/rp(0)/all.rp.flitSize: 3
+      core(2)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/input(1)/all.resourcePlanesPresent: 1
+      core(2)/input(1)/registeredInputs: Disabled
+      core(2)/input(1)/rp(0)/all.rp.flitSize: 3
+      core(2)/input(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/output(0)/all.resourcePlanesPresent: 1
+      core(2)/output(0)/registeredOutputs: Disabled
+      core(2)/output(0)/rp(0)/all.rp.flitSize: 3
+      core(2)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(2)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(2)/starvationAvoidancePeriod: 15
+      core(3)/input(0)/all.resourcePlanesPresent: 1
+      core(3)/input(0)/registeredInputs: Disabled
+      core(3)/input(0)/rp(0)/all.rp.flitSize: 1
+      core(3)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/input(1)/all.resourcePlanesPresent: 1
+      core(3)/input(1)/registeredInputs: Disabled
+      core(3)/input(1)/rp(0)/all.rp.flitSize: 1
+      core(3)/input(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/output(0)/all.resourcePlanesPresent: 1
+      core(3)/output(0)/registeredOutputs: Disabled
+      core(3)/output(0)/rp(0)/all.rp.flitSize: 1
+      core(3)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(3)/rp(0)/genericParameters: ambaInterfaceParameters
+      core(3)/starvationAvoidancePeriod: 15
+      numberOfCores: 4
+    clockDomain: clk0
+    componentName: router_0
+    instanceName: u_router_0
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: ROUTER
+      version: r0p0
+    voltageDomain: vd0
+  u_router_cfg_clk0:
+    Parameters:
+      core(0)/input(0)/all.resourcePlanesPresent: 1
+      core(0)/input(0)/registeredInputs: Disabled
+      core(0)/input(0)/rp(0)/all.rp.flitSize: 1
+      core(0)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(0)/all.resourcePlanesPresent: 1
+      core(0)/output(0)/registeredOutputs: Disabled
+      core(0)/output(0)/rp(0)/all.rp.flitSize: 1
+      core(0)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(1)/all.resourcePlanesPresent: 1
+      core(0)/output(1)/registeredOutputs: Disabled
+      core(0)/output(1)/rp(0)/all.rp.flitSize: 1
+      core(0)/output(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(2)/all.resourcePlanesPresent: 1
+      core(0)/output(2)/registeredOutputs: Disabled
+      core(0)/output(2)/rp(0)/all.rp.flitSize: 1
+      core(0)/output(2)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: aubInterfaceParameters
+      core(0)/starvationAvoidancePeriod: 15
+      core(1)/input(0)/all.resourcePlanesPresent: 1
+      core(1)/input(0)/registeredInputs: Disabled
+      core(1)/input(0)/rp(0)/all.rp.flitSize: 1
+      core(1)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/input(1)/all.resourcePlanesPresent: 1
+      core(1)/input(1)/registeredInputs: Disabled
+      core(1)/input(1)/rp(0)/all.rp.flitSize: 1
+      core(1)/input(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/input(2)/all.resourcePlanesPresent: 1
+      core(1)/input(2)/registeredInputs: Disabled
+      core(1)/input(2)/rp(0)/all.rp.flitSize: 1
+      core(1)/input(2)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/output(0)/all.resourcePlanesPresent: 1
+      core(1)/output(0)/registeredOutputs: Disabled
+      core(1)/output(0)/rp(0)/all.rp.flitSize: 1
+      core(1)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: aubInterfaceParameters
+      core(1)/starvationAvoidancePeriod: 15
+      numberOfCores: 2
+    clockDomain: clk0
+    componentName: router_cfg_clk0
+    instanceName: u_router_cfg_clk0
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: ROUTER
+      version: r0p0
+    voltageDomain: vd0
+  u_router_cfg_clk1:
+    Parameters:
+      core(0)/input(0)/all.resourcePlanesPresent: 1
+      core(0)/input(0)/registeredInputs: Disabled
+      core(0)/input(0)/rp(0)/all.rp.flitSize: 1
+      core(0)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(0)/all.resourcePlanesPresent: 1
+      core(0)/output(0)/registeredOutputs: Disabled
+      core(0)/output(0)/rp(0)/all.rp.flitSize: 1
+      core(0)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/output(1)/all.resourcePlanesPresent: 1
+      core(0)/output(1)/registeredOutputs: Disabled
+      core(0)/output(1)/rp(0)/all.rp.flitSize: 1
+      core(0)/output(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(0)/rp(0)/genericParameters: aubInterfaceParameters
+      core(0)/starvationAvoidancePeriod: 15
+      core(1)/input(0)/all.resourcePlanesPresent: 1
+      core(1)/input(0)/registeredInputs: Disabled
+      core(1)/input(0)/rp(0)/all.rp.flitSize: 1
+      core(1)/input(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/input(1)/all.resourcePlanesPresent: 1
+      core(1)/input(1)/registeredInputs: Disabled
+      core(1)/input(1)/rp(0)/all.rp.flitSize: 1
+      core(1)/input(1)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/output(0)/all.resourcePlanesPresent: 1
+      core(1)/output(0)/registeredOutputs: Disabled
+      core(1)/output(0)/rp(0)/all.rp.flitSize: 1
+      core(1)/output(0)/rp(0)/all.rp.numberOfChannelCredits: 3
+      core(1)/rp(0)/genericParameters: aubInterfaceParameters
+      core(1)/starvationAvoidancePeriod: 15
+      numberOfCores: 2
+    clockDomain: clk1
+    componentName: router_cfg_clk1
+    instanceName: u_router_cfg_clk1
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: ROUTER
+      version: r0p0
+    voltageDomain: vd0
+  u_s0:
+    AccessMaps:
+      mm0_cfg:
+        default:
+          rreq:
+          - route_MemDevRREQ_u_s0_readRequest_u_cfgni_pd0_readRequest
+          wreq:
+          - route_MemDevWREQ_u_s0_writeRequest_u_cfgni_pd0_writeRequest
+      mm0_m0_if:
+        default:
+          rreq:
+          - route_MemDevRREQ_u_s0_readRequest_u_m0_readRequest
+          wreq:
+          - route_MemDevWREQ_u_s0_writeRequest_u_m0_writeRequest
+    ConfigReturnRoutes:
+      u_cfgni_pd0:
+        resp: route_AubRESP_u_s0_utilityBusResponse_u_cfgni_pd0_localSourceResponse
+    Parameters:
+      adaptor/burstSplitting: Enabled
+      adaptor/enableOverridingofIncomingQoSValue: Enabled
+      adaptor/idm: Disabled
+      adaptor/idmDeviceId: 0
+      adaptor/protocol: ACE5Lite
+      adaptor/readReorderDepth: 32
+      adaptor/readRetimingStages: 33
+      adaptor/regulatorPresent: 3
+      adaptor/starvationAvoidancePeriod: 7
+      adaptor/writeDataFIFODepth: 26
+      adaptor/writeRetimingStages: 7
+      configNetworkNodeID: 3
+      eventRetimingStages: 0
+      gateway/mergedReadWriteRequest: Disabled
+      nodeID: 0
+      readRequest/all.resourcePlanesPresent: 1
+      readRequest/rp(0)/all.rp.flitSize: 3
+      readRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      readRequest/rp(0)/genericParameters: ambaInterfaceParameters
+      readResponse/all.resourcePlanesPresent: 1
+      readResponse/rp(0)/all.rp.flitSize: 3
+      readResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      readResponse/rp(0)/genericParameters: ambaInterfaceParameters
+      utilityBusRequest/all.resourcePlanesPresent: 1
+      utilityBusRequest/rp(0)/all.rp.flitSize: 1
+      utilityBusRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusRequest/rp(0)/genericParameters: aubInterfaceParameters
+      utilityBusResponse/all.resourcePlanesPresent: 1
+      utilityBusResponse/rp(0)/all.rp.flitSize: 1
+      utilityBusResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      utilityBusResponse/rp(0)/genericParameters: aubInterfaceParameters
+      writeRequest/all.resourcePlanesPresent: 1
+      writeRequest/rp(0)/all.rp.flitSize: 5
+      writeRequest/rp(0)/all.rp.numberOfChannelCredits: 3
+      writeRequest/rp(0)/genericParameters: ambaInterfaceParameters
+      writeResponse/all.resourcePlanesPresent: 1
+      writeResponse/rp(0)/all.rp.flitSize: 1
+      writeResponse/rp(0)/all.rp.numberOfChannelCredits: 3
+      writeResponse/rp(0)/genericParameters: ambaInterfaceParameters
+    clockDomain: clk1
+    componentName: s0
+    instanceName: u_s0
+    interface:
+    - s0_if
+    physical:
+      height: 10
+      location_x: 0
+      location_y: 0
+      width: 10
+    powerDomain: pd0
+    typeID:
+      name: ASNI
+      version: r0p0
+    voltageDomain: vd0
+InterfaceParameters:
+  ambaInterfaceParameters:
+    parameters:
+      dataUnitWidth: 9
+      dataUnitsPerWord: 4
+    type: AMBA
+  aubInterfaceParameters:
+    parameters:
+      dataUnitWidth: 9
+      dataUnitsPerWord: 1
+    type: AUB
+Interfaces:
+  clock_ctrl_clk0_if:
+    direction: slave
+    interfaceID: 256
+    physical:
+      location_x: 0
+      location_y: 0
+    type: LPI-Q
+  clock_ctrl_clk1_if:
+    direction: slave
+    interfaceID: 257
+    physical:
+      location_x: 0
+      location_y: 0
+    type: LPI-Q
+  m0_if:
+    direction: master
+    interfaceID: 0
+    parameters:
+      axi/BUSER_RESP_WIDTH: 8
+      axi/RUSER_RESP_WIDTH: 8
+      axi/USER_DATA_MODE: 1
+      axi/USER_DATA_WIDTH: 8
+      axi/USER_REQ_WIDTH: 8
+      axi/addressWidth: 40
+      axi/atomicTransactionsSupport: Disabled
+      axi/dataWidth: 32
+      axi/loopback: Enabled
+      axi/maximumReadIssuing: 23
+      axi/maximumWriteIssuing: 6
+      axi/minAtomicReadIssue: 8
+      axi/mpam: MPAM_9_1
+      axi/mte: Basic
+      axi/nsaidSupport: Enabled
+      axi/prefetch: Disabled
+      axi/qosAcceptSupport: Enabled
+      axi/readDataChunking: Disabled
+      axi/readInterleaveDisabled: Disabled
+      axi/traceSupport: Disabled
+      axi/uniqueID: Disabled
+    physical:
+      location_x: 0
+      location_y: 0
+    type: AXI5
+  power_ctrl_pd0_if:
+    direction: slave
+    interfaceID: 258
+    physical:
+      location_x: 0
+      location_y: 0
+    type: LPI-P
+  s0_if:
+    direction: slave
+    interfaceID: 0
+    parameters:
+      acelite/cacheStashingSupport: Disabled
+      acelite/deallocationTransactionSupport: Enabled
+      acelite/persistCMO: Disabled
+      acelite/readCMO: Disabled
+      acelite/writeCMO: Enabled
+      acelite/writePlusCMO: Disabled
+      axi/BUSER_RESP_WIDTH: 8
+      axi/IDWidth: 5
+      axi/RUSER_RESP_WIDTH: 8
+      axi/USER_DATA_MODE: 1
+      axi/USER_DATA_WIDTH: 128
+      axi/USER_REQ_WIDTH: 8
+      axi/addressWidth: 64
+      axi/atomicTransactionsSupport: Enabled
+      axi/dataWidth: 512
+      axi/loopback: Disabled
+      axi/maximumReadAcceptance: 39
+      axi/maximumWriteAcceptance: 18
+      axi/minAtomicReadAcceptance: 16
+      axi/mpam: Disabled
+      axi/mte: Basic
+      axi/nsaidSupport: Disabled
+      axi/orderedWriteObservation: Pin
+      axi/prefetch: Disabled
+      axi/readDataChunking: Disabled
+      axi/traceSupport: Disabled
+      axi/uniqueID: Disabled
+    physical:
+      location_x: 0
+      location_y: 0
+    type: ACE5Lite
+PowerDomains:
+  pd0:
+    powerDomainType: Programmable
+    type: internal
+    voltageDomain: vd0
+  pd_external:
+    powerDomainType: AlwaysOn
+    type: external
+    voltageDomain: vd_external
+Project: brunel_1x1_ACE5Lite_AXI5
+Routes:
+  route_AubREQ_u_cfgni_pd0_localSourceRequest_u_m0_utilityBusRequest:
+    Connections:
+    - link__u_cfgni_pd0__u_router_cfg_clk0__aubRequest__0
+    - link__u_router_cfg_clk0__u_m0__aubRequest__0
+    Protocol: AubREQ
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceRequest
+    TargetNode:
+      instanceName: u_m0
+      interface: utilityBusRequest
+  route_AubREQ_u_cfgni_pd0_localSourceRequest_u_pmu_clk0_utilityBusRequest:
+    Connections:
+    - link__u_cfgni_pd0__u_router_cfg_clk0__aubRequest__0
+    - link__u_router_cfg_clk0__u_pmu_clk0__aubRequest__0
+    Protocol: AubREQ
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceRequest
+    TargetNode:
+      instanceName: u_pmu_clk0
+      interface: utilityBusRequest
+  route_AubREQ_u_cfgni_pd0_localSourceRequest_u_pmu_clk1_utilityBusRequest:
+    Connections:
+    - link__u_cfgni_pd0__u_router_cfg_clk0__aubRequest__0
+    - link__u_router_cfg_clk0__u_pcdc_cfgni_clk1_upstream__aubRequest__0
+    - link__u_pcdc_cfgni_clk1_upstream__u_pcdc_cfgni_clk1_downstream__aubRequest__0
+    - link__u_pcdc_cfgni_clk1_downstream__u_router_cfg_clk1__aubRequest__0
+    - link__u_router_cfg_clk1__u_pmu_clk1__aubRequest__0
+    Protocol: AubREQ
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceRequest
+    TargetNode:
+      instanceName: u_pmu_clk1
+      interface: utilityBusRequest
+  route_AubREQ_u_cfgni_pd0_localSourceRequest_u_s0_utilityBusRequest:
+    Connections:
+    - link__u_cfgni_pd0__u_router_cfg_clk0__aubRequest__0
+    - link__u_router_cfg_clk0__u_pcdc_cfgni_clk1_upstream__aubRequest__0
+    - link__u_pcdc_cfgni_clk1_upstream__u_pcdc_cfgni_clk1_downstream__aubRequest__0
+    - link__u_pcdc_cfgni_clk1_downstream__u_router_cfg_clk1__aubRequest__0
+    - link__u_router_cfg_clk1__u_s0__aubRequest__0
+    Protocol: AubREQ
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceRequest
+    TargetNode:
+      instanceName: u_s0
+      interface: utilityBusRequest
+  route_AubRESP_u_m0_utilityBusResponse_u_cfgni_pd0_localSourceResponse:
+    Connections:
+    - link__u_m0__u_router_cfg_clk0__aubResponse__0
+    - link__u_router_cfg_clk0__u_cfgni_pd0__aubResponse__0
+    Protocol: AubRESP
+    SourceNode:
+      instanceName: u_m0
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceResponse
+  route_AubRESP_u_pmu_clk0_utilityBusResponse_u_cfgni_pd0_localSourceResponse:
+    Connections:
+    - link__u_pmu_clk0__u_router_cfg_clk0__aubResponse__0
+    - link__u_router_cfg_clk0__u_cfgni_pd0__aubResponse__0
+    Protocol: AubRESP
+    SourceNode:
+      instanceName: u_pmu_clk0
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceResponse
+  route_AubRESP_u_pmu_clk1_utilityBusResponse_u_cfgni_pd0_localSourceResponse:
+    Connections:
+    - link__u_pmu_clk1__u_router_cfg_clk1__aubResponse__0
+    - link__u_router_cfg_clk1__u_pcdc_cfgni_clk1_downstream__aubResponse__0
+    - link__u_pcdc_cfgni_clk1_downstream__u_pcdc_cfgni_clk1_upstream__aubResponse__0
+    - link__u_pcdc_cfgni_clk1_upstream__u_router_cfg_clk0__aubResponse__0
+    - link__u_router_cfg_clk0__u_cfgni_pd0__aubResponse__0
+    Protocol: AubRESP
+    SourceNode:
+      instanceName: u_pmu_clk1
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceResponse
+  route_AubRESP_u_s0_utilityBusResponse_u_cfgni_pd0_localSourceResponse:
+    Connections:
+    - link__u_s0__u_router_cfg_clk1__aubResponse__0
+    - link__u_router_cfg_clk1__u_pcdc_cfgni_clk1_downstream__aubResponse__0
+    - link__u_pcdc_cfgni_clk1_downstream__u_pcdc_cfgni_clk1_upstream__aubResponse__0
+    - link__u_pcdc_cfgni_clk1_upstream__u_router_cfg_clk0__aubResponse__0
+    - link__u_router_cfg_clk0__u_cfgni_pd0__aubResponse__0
+    Protocol: AubRESP
+    SourceNode:
+      instanceName: u_s0
+      interface: utilityBusResponse
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: localSourceResponse
+  route_MemDevRREQ_u_s0_readRequest_u_cfgni_pd0_readRequest:
+    Connections:
+    - link__u_s0__u_pcdc_0_upstream__readRequest__0
+    - link__u_pcdc_0_upstream__u_pcdc_0_downstream__readRequest__0
+    - link__u_pcdc_0_downstream__u_router_0__readRequest__0
+    - link__u_router_0__u_cfgni_pd0__readRequest__0
+    Protocol: MemDevRREQ
+    SourceNode:
+      instanceName: u_s0
+      interface: readRequest
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: readRequest
+  route_MemDevRREQ_u_s0_readRequest_u_m0_readRequest:
+    Connections:
+    - link__u_s0__u_pcdc_0_upstream__readRequest__0
+    - link__u_pcdc_0_upstream__u_pcdc_0_downstream__readRequest__0
+    - link__u_pcdc_0_downstream__u_router_0__readRequest__0
+    - link__u_router_0__u_m0__readRequest__0
+    Protocol: MemDevRREQ
+    SourceNode:
+      instanceName: u_s0
+      interface: readRequest
+    TargetNode:
+      instanceName: u_m0
+      interface: readRequest
+  route_MemDevRRESP_u_cfgni_pd0_readResponse_u_s0_readResponse:
+    Connections:
+    - link__u_cfgni_pd0__u_router_0__readResponse__0
+    - link__u_router_0__u_pcdc_0_downstream__readResponse__0
+    - link__u_pcdc_0_downstream__u_pcdc_0_upstream__readResponse__0
+    - link__u_pcdc_0_upstream__u_s0__readResponse__0
+    Protocol: MemDevRRESP
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: readResponse
+    TargetNode:
+      instanceName: u_s0
+      interface: readResponse
+  route_MemDevRRESP_u_m0_readResponse_u_s0_readResponse:
+    Connections:
+    - link__u_m0__u_router_0__readResponse__0
+    - link__u_router_0__u_pcdc_0_downstream__readResponse__0
+    - link__u_pcdc_0_downstream__u_pcdc_0_upstream__readResponse__0
+    - link__u_pcdc_0_upstream__u_s0__readResponse__0
+    Protocol: MemDevRRESP
+    SourceNode:
+      instanceName: u_m0
+      interface: readResponse
+    TargetNode:
+      instanceName: u_s0
+      interface: readResponse
+  route_MemDevWREQ_u_s0_writeRequest_u_cfgni_pd0_writeRequest:
+    Connections:
+    - link__u_s0__u_pcdc_0_upstream__writeRequest__0
+    - link__u_pcdc_0_upstream__u_pcdc_0_downstream__writeRequest__0
+    - link__u_pcdc_0_downstream__u_router_0__writeRequest__0
+    - link__u_router_0__u_cfgni_pd0__writeRequest__0
+    Protocol: MemDevWREQ
+    SourceNode:
+      instanceName: u_s0
+      interface: writeRequest
+    TargetNode:
+      instanceName: u_cfgni_pd0
+      interface: writeRequest
+  route_MemDevWREQ_u_s0_writeRequest_u_m0_writeRequest:
+    Connections:
+    - link__u_s0__u_pcdc_0_upstream__writeRequest__0
+    - link__u_pcdc_0_upstream__u_pcdc_0_downstream__writeRequest__0
+    - link__u_pcdc_0_downstream__u_router_0__writeRequest__0
+    - link__u_router_0__u_m0__writeRequest__0
+    Protocol: MemDevWREQ
+    SourceNode:
+      instanceName: u_s0
+      interface: writeRequest
+    TargetNode:
+      instanceName: u_m0
+      interface: writeRequest
+  route_MemDevWRESP_u_cfgni_pd0_writeResponse_u_s0_writeResponse:
+    Connections:
+    - link__u_cfgni_pd0__u_router_0__writeResponse__0
+    - link__u_router_0__u_pcdc_0_downstream__writeResponse__0
+    - link__u_pcdc_0_downstream__u_pcdc_0_upstream__writeResponse__0
+    - link__u_pcdc_0_upstream__u_s0__writeResponse__0
+    Protocol: MemDevWRESP
+    SourceNode:
+      instanceName: u_cfgni_pd0
+      interface: writeResponse
+    TargetNode:
+      instanceName: u_s0
+      interface: writeResponse
+  route_MemDevWRESP_u_m0_writeResponse_u_s0_writeResponse:
+    Connections:
+    - link__u_m0__u_router_0__writeResponse__0
+    - link__u_router_0__u_pcdc_0_downstream__writeResponse__0
+    - link__u_pcdc_0_downstream__u_pcdc_0_upstream__writeResponse__0
+    - link__u_pcdc_0_upstream__u_s0__writeResponse__0
+    Protocol: MemDevWRESP
+    SourceNode:
+      instanceName: u_m0
+      interface: writeResponse
+    TargetNode:
+      instanceName: u_s0
+      interface: writeResponse
+StripeGroups: {}
+Top Component Name: ni700_brunel_1x1_ACE5Lite_AXI5
+Top Component Type:
+  library: CoreLink
+  name: Arachne_HLS-r0p0
+  vendor: arm.com
+  version: r0p0
+Top Parameters:
+  cacheLineSize: 64
+  dataAndConfigNetworksIntersect: false
+  globalRegisterHost: pd0
+  maximumNumberOfPhysicalResourcePlanes: 1
+  numberOfMasters: 1
+  numberOfSlaves: 1
+  registerOffset: 0x0
+Uniquifier: abc123
+Version: 2.0
+VoltageDomains:
+  vd0:
+    type: internal
+    voltage: 0.1
+    voltageUnit: V
+  vd_external:
+    type: external
+    voltage: 0.1
+    voltageUnit: V
diff --git a/configs_iyml/brunel_1x1_ACE5Lite_AXI5_chariot.yaml b/configs_iyml/brunel_1x1_ACE5Lite_AXI5_chariot.yaml
new file mode 100755
index 00000000000..74ae074e24e
--- /dev/null
+++ b/configs_iyml/brunel_1x1_ACE5Lite_AXI5_chariot.yaml
@@ -0,0 +1,269 @@
+---
+project: brunel_1x1_ACE5Lite_AXI5
+uniquifier: abc123
+AddressRegions:
+  mm0:
+    subscribers: s0
+    cfg:
+      startAddress: '0x0'
+      endAddress: '0xffff'
+      targets:
+        default: CONFIGURATION_SPACE
+    m0_if:
+      startAddress: '0x10000'
+      endAddress: '0x1ffff'
+      targets:
+        default: m0_if
+domains:
+  vd0:
+    pd0:
+      clk0: 1000
+      clk1: 2000
+globalParameters:
+  cacheLineSize: 64
+  PERIPHBASE: 0
+  globalRegisterHost: pd0
+  user/BRESP: 8
+  user/DATperByte: 2
+  user/REQ: 8
+  user/RRESP: 8
+  user/mode: perByte
+  ahb/AUSERWidth: 0
+  ahb/RUSERWidth: 0
+  ahb/WUSERWidth: 0
+  axistream/USERWidth: 0
+  aub/aubRequestFlitSize: 2
+  aub/aubResponseFlitSize: 2
+  aub/aubRequestNumberOfChannelCredits: 3
+  aub/aubResponseNumberOfChannelCredits: 3
+  aub/pcdcCrossingCredits: 6
+  aub/pcdcSyncStages: 2
+units:
+  asnis:
+    s0:
+      interfaces:
+        - s0_if:
+      clock: clk1
+      resourcePlane: 0
+      wireMode: high
+      parameters:
+        eventRetimingStages: 0
+        adaptor/protocol: ACE5Lite
+        adaptor/burstSplitting: Enabled
+        adaptor/regulatorPresent: 3
+        adaptor/readReorderDepth: 32
+        adaptor/writeDataFIFODepth: 26
+        adaptor/readRetimingStages: 33
+        adaptor/writeRetimingStages: 7
+        adaptor/enableOverridingofIncomingQoSValue: Enabled
+        adaptor/starvationAvoidancePeriod: 7
+        adaptor/idm: Disabled
+        adaptor/idmDeviceId: 0
+        axi/addressWidth: 64
+        axi/dataWidth: 512
+        axi/IDWidth: 5
+        axi/maximumWriteAcceptance: 18
+        axi/maximumReadAcceptance: 39
+        axi/traceSupport: Disabled
+        axi/atomicTransactionsSupport: Enabled
+        axi/loopback: Disabled
+        axi/nsaidSupport: Disabled
+        axi/orderedWriteObservation: Pin
+        axi/mpam: Disabled
+        axi/prefetch: Disabled
+        axi/mte: Basic
+        axi/minAtomicReadAcceptance: 16
+        acelite/cacheStashingSupport: Disabled
+        acelite/deallocationTransactionSupport: Enabled
+        axi/readDataChunking: Disabled
+        axi/uniqueID: Disabled
+        acelite/readCMO: Disabled
+        acelite/writeCMO: Enabled
+        acelite/writePlusCMO: Disabled
+        acelite/persistCMO: Disabled
+      routes:
+        m0: pcdc_0->router_0
+        cfgni_pd0: pcdc_0->router_0
+      channels:
+        readRequest:
+          flitSize: 3
+          numberOfChannelCredits: 3
+        writeRequest:
+          flitSize: 5
+          numberOfChannelCredits: 3
+  hsnis: {}
+  tsnis: {}
+  amnis:
+    m0:
+      interfaces:
+        - m0_if:
+      clock: clk0
+      wireMode: high
+      parameters:
+        eventRetimingStages: 0
+        adaptor/protocol: AXI5
+        adaptor/burstSplitting: Disabled
+        adaptor/readRetimingStages: 3
+        adaptor/writeRetimingStages: 6
+        adaptor/starvationAvoidancePeriod: 12
+        adaptor/idm: Disabled
+        adaptor/idmDeviceId: 0
+        axi/addressWidth: 40
+        axi/dataWidth: 32
+        axi/maximumWriteIssuing: 6
+        axi/maximumReadIssuing: 23
+        axi/traceSupport: Disabled
+        axi/atomicTransactionsSupport: Disabled
+        axi/loopback: Enabled
+        axi/nsaidSupport: Enabled
+        axi/mpam: MPAM_9_1
+        axi/prefetch: Disabled
+        axi/mte: Basic
+        axi/minAtomicReadIssue: 8
+        axi/readDataChunking: Disabled
+        axi/readInterleaveDisabled: Disabled
+        axi/uniqueID: Disabled
+        axi/qosAcceptSupport: Enabled
+      channels:
+        readResponse:
+          flitSize: 3
+          numberOfChannelCredits: 3
+        writeResponse:
+          flitSize: 1
+          numberOfChannelCredits: 3
+  hmnis: {}
+  pmnis: {}
+  tmnis: {}
+  serdes: {}
+  pcdcs:
+    pcdc_cfgni_clk1:
+      wireMode: config
+      clockCrossingType: OneToN
+      upstream:
+        clock: clk0
+      downstream:
+        clock: clk1
+    pcdc_0:
+      wireMode: high
+      clockCrossingType: MToOne
+      upstream:
+        clock: clk1
+      downstream:
+        clock: clk0
+      channels:
+        readRequest:
+          flitSize: 3
+          numberOfChannelCredits: 3
+          crossingChannelCredits: 3
+          registeredInputs: Disabled
+          registeredOutputs: Disabled
+          fifoBypass: Disabled
+        writeRequest:
+          flitSize: 5
+          numberOfChannelCredits: 3
+          crossingChannelCredits: 3
+          registeredInputs: Disabled
+          registeredOutputs: Disabled
+          fifoBypass: Disabled
+        readResponse:
+          flitSize: 3
+          numberOfChannelCredits: 3
+          crossingChannelCredits: 3
+          registeredInputs: Disabled
+          registeredOutputs: Disabled
+          fifoBypass: Disabled
+        writeResponse:
+          flitSize: 1
+          numberOfChannelCredits: 3
+          crossingChannelCredits: 3
+          registeredInputs: Disabled
+          registeredOutputs: Disabled
+          fifoBypass: Disabled
+  cfgnis:
+    cfgni_pd0:
+      clock: clk0
+      wireMode: high
+      routes:
+        s0: router_cfg_clk0->pcdc_cfgni_clk1->router_cfg_clk1
+        m0: router_cfg_clk0
+        pmu_clk0: router_cfg_clk0
+        pmu_clk1: router_cfg_clk0->pcdc_cfgni_clk1->router_cfg_clk1
+      channels:
+        readResponse:
+          flitSize: 3
+          numberOfChannelCredits: 3
+        writeResponse:
+          flitSize: 1
+          numberOfChannelCredits: 3
+  routers:
+    router_cfg_clk0:
+      clock: clk0
+      wireMode: config
+    router_cfg_clk1:
+      clock: clk1
+      wireMode: config
+    router_0:
+      clock: clk0
+      wireMode: high
+      channels:
+        readRequest:
+          flitSize: 3
+          starvationAvoidancePeriod: 15
+        writeRequest:
+          flitSize: 5
+          starvationAvoidancePeriod: 15
+        readResponse:
+          flitSize: 3
+          starvationAvoidancePeriod: 15
+        writeResponse:
+          flitSize: 1
+          starvationAvoidancePeriod: 15
+physical:
+  s0:
+    x: 0
+    y: 0
+  m0:
+    x: 0
+    y: 0
+  pcdc_cfgni_clk1:
+    x: 0
+    y: 0
+  pcdc_0:
+    x: 0
+    y: 0
+  cfgni_pd0:
+    x: 0
+    y: 0
+  router_cfg_clk0:
+    x: 0
+    y: 0
+  router_cfg_clk1:
+    x: 0
+    y: 0
+  router_0:
+    x: 0
+    y: 0
+  clock_ctrl_clk0:
+    x: 0
+    y: 0
+  clock_ctrl_clk1:
+    x: 0
+    y: 0
+  power_ctrl_pd0:
+    x: 0
+    y: 0
+  pmu_clk0:
+    x: 0
+    y: 0
+  pmu_clk1:
+    x: 0
+    y: 0
+  s0_if:
+    x: 0
+    y: 0
+  m0_if:
+    x: 0
+    y: 0
+clockRelations:
+  clk0:
+    clk1: sync
diff --git a/logical/noc_arachne/.control_files/chariot_fault_injection.ctrl b/logical/noc_arachne/.control_files/chariot_fault_injection.ctrl
index 24a835b8880..8b67a738062 100755
--- a/logical/noc_arachne/.control_files/chariot_fault_injection.ctrl
+++ b/logical/noc_arachne/.control_files/chariot_fault_injection.ctrl
@@ -1,22 +1,22 @@
 Phase Param_Engine 24h
-ae param_engine --config="brunel_1x1_ACE5Lite_AXI5"
+ae param_engine --config="brunel_1x1_ACE5Lite_AXI5_chariot"
 #ae param_engine --config=partner_0_b0_multiport_flit_optimized
 
 Phase Get_Flops 24h
-ae get_flops --config="brunel_1x1_ACE5Lite_AXI5"
+ae get_flops --config="brunel_1x1_ACE5Lite_AXI5_chariot"
 #ae get_flops --config=partner_0_b0_multiport_flit_optimized
 
 #Phase TB_Gen 24h
-#ae tb_configuration --dsbl_tbgen --config="brunel_1x1_ACE5Lite_AXI5" --junit
+#ae tb_configuration --dsbl_tbgen --config="brunel_1x1_ACE5Lite_AXI5_chariot" --junit
 #ae tb_configuration --dsbl_tbgen --config=partner_0_b0_multiport_flit_optimized --junit
 
 Phase Scenario_Generation 24h
-ae scenario_generation --config="brunel_1x1_ACE5Lite_AXI5" --test=constrained_random --set=basic --scenario=default --junit
+ae scenario_generation --config="brunel_1x1_ACE5Lite_AXI5_chariot" --test=constrained_random --set=basic --scenario=default --junit
 #ae scenario_generation --parse_only --config="partner_0_b0_multiport_flit_optimized" --test=constrained_random --set=basic --scenario=default --junit
 
 Phase Simulation 8h
-ae simulate --inject_fault --tb=top --config="brunel_1x1_ACE5Lite_AXI5" --test=constrained_random --set=basic --scenario=default_000 --run_time=120 --uvm=num_txs=1000 --junit --mem=16000 --maxlen=360 --defines CHARIOT_ASIL_B --repeat=100 --rindex=200
-#ae simulate --inject_fault --parse_only --tb=top --config="partner_0_b0_multiport_flit_optimized" --test=constrained_random --set=basic --scenario=default_000 --enable_da --repeat=1 --run_time=120 --uvm=num_txs=1000 --junit --no_wlf  --mem=16000 --maxlen=360  --formal_asserts=all --repeat=100 
+ae simulate --inject_fault --tb=top --config="brunel_1x1_ACE5Lite_AXI5_chariot" --test=constrained_random --set=basic --scenario=default_000 --run_time=120 --uvm=num_txs=1000 --junit --mem=16000 --maxlen=360 --defines CHARIOT_ASIL_B --repeat=100 --rindex=200 --fullacc
+#ae simulate --inject_fault --parse_only --tb=top --config="partner_0_b0_multiport_flit_optimized" --test=constrained_random --set=basic --scenario=default_000 --enable_da --repeat=1 --run_time=120 --uvm=num_txs=1000 --junit --no_wlf  --mem=16000 --maxlen=360  --formal_asserts=all --repeat=100
 
 #Phase Cleanup_1 2h
 #find $NOC_DIR/validation/results/ -type f | grep -vi bsub.log | grep -vi reproducer | grep -vi errors.txt | grep -vi junit.xml | xargs rm -rf
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_parity_checker.sv
new file mode 100755
index 00000000000..0d3fe7ccdec
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_parity_checker.sv
@@ -0,0 +1,27 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot parity_checker
+//------------------------------------------------------------------------------
+
+module chariot_parity_checker #(DATA_WIDTH = 32, USER_WIDTH = 8) (
+    input [DATA_WIDTH-1:0] data_i,
+    input valid_i,
+    input [USER_WIDTH-1:0] user_i,
+    output error_o
+);
+
+    assign error_o = ({{{USER_WIDTH-1{1'b0}},{~^data_i}}} == user_i) ? 1'b0 : (1'b1 & valid_i); // only set when WVALID is high
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_parity_generation.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_parity_generation.sv
new file mode 100755
index 00000000000..7134ed4cd56
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_parity_generation.sv
@@ -0,0 +1,42 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot parity_generation
+//------------------------------------------------------------------------------
+
+module chariot_parity_generation #(DATA_WIDTH = 512, USER_WIDTH = 128) (
+    input [DATA_WIDTH-1:0] data_i,     // 512 bits, 64 bytes, 16 32-bit chunks
+    input [(DATA_WIDTH/8)-1:0] strb_i, // 64 bits
+    output [USER_WIDTH-1:0] user_o     // 128 bits, 16 bytes
+);
+
+    localparam STRB_WIDTH = DATA_WIDTH / 8; // 64
+    localparam USER_BITS = USER_WIDTH / STRB_WIDTH; // 8
+
+    genvar i;
+    generate
+        // loop through data bytes 4 at a time, and put the parity into user_o
+        for (i=0; i<STRB_WIDTH; i=i+4) begin:bitnum
+            logic [31:0] packet;
+            assign packet = {
+                ((strb_i[i+3]) ? data_i[(i*8)+31:(i*8)+24] : 8'b00000000),
+                ((strb_i[i+2]) ? data_i[(i*8)+23:(i*8)+16] : 8'b00000000),
+                ((strb_i[i+1]) ? data_i[(i*8)+15:(i*8)+8]  : 8'b00000000),
+                ((strb_i[i])   ? data_i[(i*8)+7 :(i*8)+0]  : 8'b00000000)
+            };
+            assign user_o[(i*2)+7:i*2] = {{{USER_BITS-1{1'b0}},{~^packet}}}; // odd parity, even # of 1s returns 1
+        end
+    endgenerate
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
new file mode 100755
index 00000000000..4c4d2e732da
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
@@ -0,0 +1,30 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2015 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot package
+//------------------------------------------------------------------------------
+
+`ifndef CHARIOT_PKG__SV
+`define CHARIOT_PKG__SV
+
+`include "chariot_parity_generation.sv"
+`include "chariot_parity_checker.sv"
+
+package chariot_pkg;
+
+
+endpackage
+
+`endif
diff --git a/logical/noc_arachne/validation/dynamic/top/components/checkers/amba5_payload_checker_component.svh b/logical/noc_arachne/validation/dynamic/top/components/checkers/amba5_payload_checker_component.svh
index f9bdef060a7..8c2af2a77de 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/checkers/amba5_payload_checker_component.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/checkers/amba5_payload_checker_component.svh
@@ -27,7 +27,7 @@
       $sformatf("Comparison failure for %s: Expected = 0x%0h  Observed = 0x%0h \n", \
       NAME, EXPECTED, OBSERVED)}; \
     RESULT = 1'b0; \
-  end 
+  end
 
 
 `define compare_signal_multi_values(NAME, EXPECTED1, EXPECTED2, OBSERVED, RESULT, MESSAGE) \
@@ -37,7 +37,7 @@
       $sformatf("Comparison failure for %s: Expected1 = 0x%0h Expected2 = 0x%0h Observed = 0x%0h \n", \
       NAME, EXPECTED1, EXPECTED2, OBSERVED)}; \
     RESULT = 1'b0; \
-  end 
+  end
 
 //Register manager logic ends
 
@@ -123,7 +123,7 @@ class amba5_payload_checker_component extends generic_checker_component;
     vip_ahb5_transaction_item              ahb_slv_tx;
     vip_apb4_transfer                      apb_slv_tx;
     vip_ahb5_types::request_beat_struct_t  slv_req_beat;
-    int unsigned                           downsize_ratio;  
+    int unsigned                           downsize_ratio;
     data_check_variables                   vars = new();
     bit                                    split = tx_event.set.tx_array[generic_types::DEVICE__XMNI_SPLIT].size() > 1;
 
@@ -154,7 +154,7 @@ class amba5_payload_checker_component extends generic_checker_component;
       longint unsigned data_aligned_mst_addr = amba_mst_tx.axaddr - (amba_mst_tx.axaddr % vars.mst_size);
       longint unsigned dest_aligned_mst_addr = amba_mst_tx.axaddr - (amba_mst_tx.axaddr % vars.slv_size);
 
-      // Master transaction was FIXED 
+      // Master transaction was FIXED
       if (amba_mst_tx.axburst == vip_lib_types::TRANSFER_BURST_FIXED) begin
         if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AHB5, generic_types::PROTOCOL__AHB_LITE}) begin
           vars.mst_beat = slv_tx.mst_beat;
@@ -191,28 +191,28 @@ class amba5_payload_checker_component extends generic_checker_component;
         if ((slv_tx.tx_protocol inside {generic_types::PROTOCOL__AXI4, generic_types::PROTOCOL__ACE_LITE})) begin
           vars.mst_beat += (amba_slv_tx.axaddr - (amba_mst_tx.get_min_tx_address() & slv_addr_mask)) / vars.mst_size;
         end else if ((slv_tx.tx_protocol inside {generic_types::PROTOCOL__AHB5, generic_types::PROTOCOL__AHB_LITE})) begin
-          vars.mst_beat += (slv_req_beat.Address - (amba_mst_tx.get_min_tx_address() & slv_addr_mask)) / vars.mst_size; //TODO use a common address varaible and if -else on the adress 
+          vars.mst_beat += (slv_req_beat.Address - (amba_mst_tx.get_min_tx_address() & slv_addr_mask)) / vars.mst_size; //TODO use a common address varaible and if -else on the adress
         end else if ((slv_tx.tx_protocol inside {generic_types::PROTOCOL__APB4,generic_types::PROTOCOL__APB3})) begin
-          vars.mst_beat += (apb_slv_tx.addr - (amba_mst_tx.get_min_tx_address() & slv_addr_mask)) / vars.mst_size;  
+          vars.mst_beat += (apb_slv_tx.addr - (amba_mst_tx.get_min_tx_address() & slv_addr_mask)) / vars.mst_size;
 	end
       end
     end
 
     // Want the offset to this current slave address, so spoof being first beat
     if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AXI4, generic_types::PROTOCOL__ACE_LITE}) begin
-      vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(amba_slv_tx.axaddr, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0); 
+      vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(amba_slv_tx.axaddr, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0);
       vars.slv_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(amba_slv_tx.axaddr, amba_slv_tx.axsize, amba_slv_tx.axlen, amba_slv_tx.axburst, amba_slv_tx.get_data_bytes(), vars.slv_beat);
     end else if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AHB5, generic_types::PROTOCOL__AHB_LITE}) begin
       int unsigned slv_data_width = (test_config.if_params[slv_tx.src_if].data_width)/8;
       int unsigned addr = ((vars.mst_beat == 0) && (slv_req_beat.Address < amba_mst_tx.axaddr)) ? amba_mst_tx.axaddr : slv_req_beat.Address;
-      //vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(slv_req_beat.Address, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0); 
+      //vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(slv_req_beat.Address, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0);
       //vars.slv_offset = calculate_byteshift(ahb_slv_tx, vars.slv_beat, vars.slv_size, slv_data_width);
-      vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(addr, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0); 
+      vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(addr, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0);
       vars.slv_offset = calculate_byteshift(ahb_slv_tx, vars.slv_beat, vars.slv_size, slv_data_width);
       vars.slv_offset = vars.slv_offset + ( ((vars.mst_beat == 0) && (slv_req_beat.Address < amba_mst_tx.axaddr)) ? (amba_mst_tx.axaddr - ahb_slv_tx.request_beats[0].Address) : 0); // To Handle unaligned memory read addr at HMNI
     end else if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__APB4,generic_types::PROTOCOL__APB3}) begin
       int unsigned slv_data_width = (test_config.if_params[slv_tx.src_if].data_width)/8;
-      //vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(apb_slv_tx.addr, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0); 
+      //vars.mst_offset = vip_ace5_byte_lanes_handler::calculate_byte_shift(apb_slv_tx.addr, amba_mst_tx.axsize, amba_mst_tx.axlen, amba_mst_tx.axburst, amba_mst_tx.get_data_bytes(),  0);
       vars.mst_offset = apb_slv_tx.addr % mst_data_width;
       vars.slv_offset = calculate_byteshift_apb(apb_slv_tx,vars.slv_beat, vars.slv_size, slv_data_width); //review, vars.slv_beat = 1 for PMNI
     end
@@ -240,7 +240,7 @@ class amba5_payload_checker_component extends generic_checker_component;
   endfunction : check_data
 
 
-  //check_data_ahb task used to compare HSNI--AMNI 
+  //check_data_ahb task used to compare HSNI--AMNI
   virtual function data_check_variables check_data_ahb(generic_transaction_event tx_event, generic_transaction mst_tx, generic_transaction slv_tx, int unsigned slv_tx_num);
     vip_ahb5_transaction_item  ahb_mst_tx;
     vip_ace5_transaction_item  amba_slv_tx;
@@ -277,7 +277,7 @@ class amba5_payload_checker_component extends generic_checker_component;
       // INCR case and WRAP upper case
       /*end else*/ if (amba_slv_tx.axaddr >= (req_beat.Address & slv_addr_mask)) begin
         vars.mst_beat = (amba_slv_tx.axaddr - (data_aligned_mst_addr & slv_addr_mask)) / vars.mst_size;
-      end else if ((amba_slv_tx.axaddr == (dest_aligned_mst_addr & slv_addr_mask))&& (!(req_beat.Burst inside {2,4,6}))) begin 
+      end else if ((amba_slv_tx.axaddr == (dest_aligned_mst_addr & slv_addr_mask))&& (!(req_beat.Burst inside {2,4,6}))) begin
         vars.mst_beat = 0;
       // WRAP lower case
       end else begin
@@ -306,7 +306,7 @@ class amba5_payload_checker_component extends generic_checker_component;
   virtual function bit is_cmo(uvm_object amba_tx);
     vip_ace5_transaction_item axi_tx;
     bit cmo;
-   
+
     if ($cast(axi_tx, amba_tx)) begin
       cmo = (axi_tx.axsnoop == 'b1011) || // CleanUnique
             (axi_tx.axsnoop == 'b1100) || // MakeUnique
@@ -316,7 +316,7 @@ class amba5_payload_checker_component extends generic_checker_component;
             (axi_tx.axsnoop == 'b1101); // MakeInvalid
     end else begin
       cmo = 0;
-    end 
+    end
     return cmo;
   endfunction
 
@@ -341,33 +341,33 @@ class amba5_payload_checker_component extends generic_checker_component;
 
     rsp_beat = ahb_rresp_slv_tx.response_beats[real_slv_beat];
     req_beat = ahb_rresp_slv_tx.request_beats[real_slv_beat];
-     
+
     if (beat_resp[vars.mst_beat] inside {vip_ace5_types::RESP_DECODE_ERROR, vip_ace5_types::RESP_SLAVE_ERROR}) begin
       // Nothing
     end else if (incr_burst_mode && (!mst_tx.incr_burst_mode_with_split) && (real_slv_beat >= ahb_rresp_slv_tx.data.size())) begin
       beat_resp[vars.mst_beat] = vip_ace5_types::RESP_SLAVE_ERROR;
     end else if (rsp_beat.Response ==  vip_ahb5_types::RESP_ERROR) begin
       beat_resp[vars.mst_beat] = vip_ace5_types::RESP_SLAVE_ERROR;
-    end else if ((req_beat.Exclusive == 1'b1) && (rsp_beat.ExclResponse == vip_ahb5_types::EXCL_OKAY)) begin 
+    end else if ((req_beat.Exclusive == 1'b1) && (rsp_beat.ExclResponse == vip_ahb5_types::EXCL_OKAY)) begin
       beat_resp[vars.mst_beat] = vip_ace5_types::RESP_EXCL_OKAY;
-    end else /*if (beat_resp[vars.mst_beat] == vip_ace5_types::RESP_EXCL_OKAY)*/ begin 
+    end else /*if (beat_resp[vars.mst_beat] == vip_ace5_types::RESP_EXCL_OKAY)*/ begin
       beat_resp[vars.mst_beat] = vip_ace5_types::RESP_NORMAL_OKAY_EXCL_FAIL;
-    end 
+    end
     mst_tx.beats_updated++;
   endfunction
 
 
-  virtual function void update_beat_resp_apb(data_check_variables vars, vip_apb4_transfer  apb_rresp_slv_tx, int unsigned real_slv_beat); 
-     
+  virtual function void update_beat_resp_apb(data_check_variables vars, vip_apb4_transfer  apb_rresp_slv_tx, int unsigned real_slv_beat);
+
     if (beat_resp[vars.mst_beat] == vip_ace5_types::RESP_DECODE_ERROR) begin
       // Nothing
     end else if (apb_rresp_slv_tx.pslverr == 1) begin
       beat_resp[vars.mst_beat] = vip_ace5_types::RESP_SLAVE_ERROR;
     end else if (beat_resp[vars.mst_beat] == vip_ace5_types::RESP_SLAVE_ERROR) begin
       // Nothing
-    end else if (beat_resp[vars.mst_beat] == vip_ace5_types::RESP_EXCL_OKAY) begin // beat_resp is initialized to EXCL_OKAY in old code, for HMNI, it should be OKAY resp, as we have checked all error condition before this condition 
+    end else if (beat_resp[vars.mst_beat] == vip_ace5_types::RESP_EXCL_OKAY) begin // beat_resp is initialized to EXCL_OKAY in old code, for HMNI, it should be OKAY resp, as we have checked all error condition before this condition
       beat_resp[vars.mst_beat] = vip_ace5_types::RESP_NORMAL_OKAY_EXCL_FAIL;
-    end 
+    end
   endfunction
 
 
@@ -393,7 +393,7 @@ class amba5_payload_checker_component extends generic_checker_component;
     int unsigned               ored_reduced_strb;
     int unsigned               slv_offset;
     int unsigned               shift, mask;
-    
+
     if ($cast(axi_mst_tx, mst_tx.tx)) begin
       if (axi_mst_tx.read_data_chunking_enable == 0) begin
         mst_num_beats = axi_mst_tx.get_number_of_beats();
@@ -422,14 +422,14 @@ class amba5_payload_checker_component extends generic_checker_component;
     end else if ($cast(ahb_slv_tx, slv_tx.tx)) begin
       slv_num_beats = ahb_slv_tx.request_beats.size;
     end else if ($cast(apb_slv_tx, slv_tx.tx)) begin
-      slv_num_beats = 1; 
+      slv_num_beats = 1;
     end
     $cast(amba_mst_tx, mst_tx.tx);
 
 
     if (!is_write) begin
       if (mst_tx.tx_protocol inside {generic_types::PROTOCOL__AXI4, generic_types::PROTOCOL__ACE_LITE}) begin
-        $cast(amba_rresp_mst_tx, mst_tx.tx); 
+        $cast(amba_rresp_mst_tx, mst_tx.tx);
         is_asni = 1;
       end else if (mst_tx.tx_protocol inside {generic_types::PROTOCOL__AHB5, generic_types::PROTOCOL__AHB_LITE}) begin
         $cast(ahb_mst_tx, mst_tx.tx);
@@ -488,7 +488,7 @@ class amba5_payload_checker_component extends generic_checker_component;
         ++vars.crnt_slv_byte;
       // is_read
       end else begin
-        int unsigned slv_byte;	
+        int unsigned slv_byte;
         bit [31:0] apb_data;
         bit [511+64:0] act_user_full;
         bit [511+64:0] exp_user_full;
@@ -505,8 +505,8 @@ class amba5_payload_checker_component extends generic_checker_component;
                // MSB Calculation:
                // i.e. mst_data_width=512b=64B, update_idx=63/4=15, it means msb=15, lsb=15-3=12. idx=15:12
                //        There are 4 16B, and there are 4b per 16B, meaning there are 4x4b=16b tags total in 64B.
-               //        databyte 63-48 corresponding to tag 15:12, msb=15 
-               //        databyte 47-32 corresponding to tag 11:8,  msb=11 
+               //        databyte 63-48 corresponding to tag 15:12, msb=15
+               //        databyte 47-32 corresponding to tag 11:8,  msb=11
                //        databyte 31-16 corresponding to tag 7:4,   msb=7
                //        databyte 15-0  corresponding to tag 3:0; Byte(15:12, 11:8, 7:4, 3:0) corresponds to each tag bit in tag 3:0
                // Beat Calculation:
@@ -520,9 +520,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                int unsigned tag_slv_lsb = (tag_slv_msb-3);
                // memory_tag_data[beat][n][tag_bit]
-               // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+               // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-               int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+               int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                bit expected_val=0, rtl_val=0;
 
                if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AXI4, generic_types::PROTOCOL__ACE_LITE}) begin
@@ -545,7 +545,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                          expected_val =  amba_rresp_slv_tx.memory_tag_data[vars.slv_beat][n_slv][b]; //  read data originates from slave_vip to amni.
                          `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("MTE: Expect RTAG%0d[%0d:%0d]=0, n(%0d) due to bounceback", vars.slv_beat, b, b, expected_val, n_slv), UVM_FULL);
                        end
-                       rtl_val      = amba_rresp_mst_tx.memory_tag_data[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni. 
+                       rtl_val      = amba_rresp_mst_tx.memory_tag_data[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni.
                        `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("AMNI Expect: RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.slv_beat, b, b, expected_val, n_slv), UVM_FULL);
                        `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("ASNI RTL   : RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.mst_beat, b, b, rtl_val     , n_mst), UVM_FULL);
                        `compare_signal_multi_values($sformatf("ASNI RTL RTAG%0d[%0d:%0d]", vars.mst_beat, tag_mst_lsb+b, tag_mst_lsb+b),
@@ -562,10 +562,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                        act_user_full = amba_rresp_slv_tx.data_user[vars.slv_beat] >> ruser_resp_width;
                        for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++)
                          begin
-                           act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                           exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                           act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                           exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                          end
-    
+
                        `compare_signal($sformatf("RUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                                act_user_per_byte, exp_user_per_byte, vars.result, vars.msg)
                      end
@@ -584,7 +584,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                        end else begin
                          expected_val = amba_rresp_slv_tx.memory_tag_data[vars.slv_beat][n_slv][b]; //  read data originates from slave_vip to amni.
                        end
-                       rtl_val      = amba_rresp_mst_tx.memory_tag_data[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni. 
+                       rtl_val      = amba_rresp_mst_tx.memory_tag_data[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni.
                        `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("AMNI Expect: RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.slv_beat, b, b, expected_val, n_slv), UVM_FULL);
                        `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("ASNI RTL   : RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.mst_beat, b, b, rtl_val     , n_mst), UVM_FULL);
                        `compare_signal($sformatf("ASNI RTL RTAG%0d[%0d:%0d]", vars.mst_beat, tag_mst_lsb+b, tag_mst_lsb+b),
@@ -601,16 +601,16 @@ class amba5_payload_checker_component extends generic_checker_component;
                          act_user_full = ahb_rresp_slv_tx.data[vars.slv_beat].data_user ;
                          for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++)
                            begin
-                             act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                             exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                             act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                             exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                            end
-    
+
                          `compare_signal($sformatf("RUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                                  act_user_per_byte, exp_user_per_byte, vars.result, vars.msg)
                      end
                      if(mst_tx.pending_rd_rsp_seen && (mst_tx.beat_before_sreset == vars.slv_beat)) begin
                          //do not check //bookernoc 4225
-                     end 
+                     end
                      else if(slv_tx.incr_burst_mode) begin
                          if(!mst_tx.incr_burst_mode_with_split) begin
                               // we have entered soft reset and have seen an incomplete read response for incr burst
@@ -625,7 +625,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                      end
                      else begin
                          `compare_signal($sformatf("RDATA%0d[%0d:%0d]", vars.mst_beat, ((vars.crnt_mst_byte+1)*8)-1, vars.crnt_mst_byte*8),ahb_rresp_slv_tx.data[vars.slv_beat].data[vars.crnt_slv_byte], amba_rresp_mst_tx.data[vars.mst_beat][vars.crnt_mst_byte], vars.result, vars.msg)
-                     end 
+                     end
                  end
                  else begin
                    if(test_config.if_params[mst_tx.src_if].user_data_mode)
@@ -634,10 +634,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                        act_user_full = ahb_rresp_slv_tx.data[vars.slv_beat].data_user  ;
                        for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++)
                          begin
-                           act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                           exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                           act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                           exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                          end
-    
+
                        `compare_signal($sformatf("RUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                                act_user_per_byte, exp_user_per_byte, vars.result, vars.msg)
                      end
@@ -648,8 +648,8 @@ class amba5_payload_checker_component extends generic_checker_component;
 	             apb_data = apb_rresp_slv_tx.data;
                  slv_byte = (vars.crnt_mst_byte%4);
                  `compare_signal($sformatf("RDATA%0d[%0d:%0d]", vars.mst_beat, ((vars.crnt_mst_byte+1)*8)-1, vars.crnt_mst_byte*8),apb_data[slv_byte*8 +: 8], amba_rresp_mst_tx.data[vars.mst_beat][vars.crnt_mst_byte], vars.result, vars.msg) //review here apb data is 1D array
-               end 
-             end else begin 
+               end
+             end else begin
                `compare_signal($sformatf("RDATA%0d[%0d:%0d]", vars.mst_beat, ((vars.crnt_mst_byte+1)*8)-1, vars.crnt_mst_byte*8),
                               amba_rresp_slv_tx.data[vars.slv_beat][vars.crnt_slv_byte], ahb_mst_tx.data[vars.mst_beat].data[vars.crnt_mst_byte], vars.result, vars.msg)
              end
@@ -695,7 +695,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                        end
                      end
                    end
-                   
+
                    //Following logic is making sure if strb is present, and
                    //strb is 0 then increament byte as check is not happening.
                    //Here size is checked because in some cases if strb is
@@ -714,12 +714,12 @@ class amba5_payload_checker_component extends generic_checker_component;
                    //then only perform check so for instance master or slave
                    //has strb 0 then need to wait for next instance until strb
                    //is set to 1.
-                   if( (amba_rresp_mst_tx.read_data_beat_chunkstrb[vars.mst_beat][mst_crnt_beat_strb] == 1 
-                     || amba_rresp_mst_tx.read_data_beat_chunkstrb.size()==0 
+                   if( (amba_rresp_mst_tx.read_data_beat_chunkstrb[vars.mst_beat][mst_crnt_beat_strb] == 1
+                     || amba_rresp_mst_tx.read_data_beat_chunkstrb.size()==0
                      || amba_rresp_mst_tx.read_data_beat_chunkstrb[vars.mst_beat].size()==0)
-                     && (reduced_strb1[slv_crnt_beat_strb] == 1 
-                     //&& (amba_rresp_slv_tx.read_data_beat_chunkstrb[vars.slv_beat][slv_crnt_beat_strb] == 1 
-                     || amba_rresp_slv_tx.read_data_beat_chunkstrb.size()==0 
+                     && (reduced_strb1[slv_crnt_beat_strb] == 1
+                     //&& (amba_rresp_slv_tx.read_data_beat_chunkstrb[vars.slv_beat][slv_crnt_beat_strb] == 1
+                     || amba_rresp_slv_tx.read_data_beat_chunkstrb.size()==0
                      || amba_rresp_slv_tx.read_data_beat_chunkstrb[vars.slv_beat].size()==0)) begin
                      int unsigned mst_data_width = test_config.if_params[mst_tx.src_if].interface_data_width;
                      int unsigned slv_data_width = test_config.if_params[slv_tx.src_if].interface_data_width;
@@ -728,9 +728,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                      int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                      int unsigned tag_slv_lsb = (tag_slv_msb-3);
                      // memory_tag_data[beat][n][tag_bit]
-                     // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+                     // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                      int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-                     int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+                     int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                      bit expected_val=0, rtl_val=0;
 
 
@@ -751,7 +751,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                          end else begin
                            expected_val = amba_rresp_slv_tx.read_data_chunk_memory_tag[vars.slv_beat][n_slv][b]; //  read data originates from slave_vip to amni.
                          end
-                         rtl_val      = amba_rresp_mst_tx.read_data_chunk_memory_tag[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni. 
+                         rtl_val      = amba_rresp_mst_tx.read_data_chunk_memory_tag[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni.
                          `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("AMNI Expect: RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.slv_beat, b, b, expected_val, n_slv), UVM_FULL);
                          `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("ASNI RTL   : RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.mst_beat, b, b, rtl_val     , n_mst), UVM_FULL);
                          `compare_signal_multi_values($sformatf("ASNI RTL RTAG%0d[%0d:%0d]", vars.mst_beat, tag_mst_lsb+b, tag_mst_lsb+b),
@@ -775,7 +775,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                        end
                      end
                    end
-                   
+
                    //Following logic is making sure if strb is present, and
                    //strb is 0 then increament byte as check is not happening.
                    //Here size is checked because in some cases if strb is
@@ -795,13 +795,13 @@ class amba5_payload_checker_component extends generic_checker_component;
                    //then only perform check so for instance master or slave
                    //has strb 0 then need to wait for next instance until strb
                    //is set to 1.
-                   if( (amba_rresp_mst_tx.read_data_beat_chunkstrb[vars.mst_beat][mst_crnt_beat_strb] == 1 
-                     || amba_rresp_mst_tx.read_data_beat_chunkstrb.size()==0 
+                   if( (amba_rresp_mst_tx.read_data_beat_chunkstrb[vars.mst_beat][mst_crnt_beat_strb] == 1
+                     || amba_rresp_mst_tx.read_data_beat_chunkstrb.size()==0
                      || amba_rresp_mst_tx.read_data_beat_chunkstrb[vars.mst_beat].size()==0)
 
-                     //&& (amba_rresp_slv_tx.read_data_beat_chunkstrb[vars.slv_beat][slv_crnt_beat_strb] == 1 
-                     && (reduced_strb1[slv_crnt_beat_strb] == 1 
-                     || amba_rresp_slv_tx.read_data_beat_chunkstrb.size()==0 
+                     //&& (amba_rresp_slv_tx.read_data_beat_chunkstrb[vars.slv_beat][slv_crnt_beat_strb] == 1
+                     && (reduced_strb1[slv_crnt_beat_strb] == 1
+                     || amba_rresp_slv_tx.read_data_beat_chunkstrb.size()==0
                      || amba_rresp_slv_tx.read_data_beat_chunkstrb[vars.slv_beat].size()==0)) begin
                      int unsigned mst_data_width = test_config.if_params[mst_tx.src_if].interface_data_width;
                      int unsigned slv_data_width = test_config.if_params[slv_tx.src_if].interface_data_width;
@@ -810,9 +810,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                      int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                      int unsigned tag_slv_lsb = (tag_slv_msb-3);
                      // memory_tag_data[beat][n][tag_bit]
-                     // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+                     // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                      int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-                     int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+                     int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                      bit expected_val=0, rtl_val=0;
 
                      `compare_signal($sformatf("RDATA%0d[%0d:%0d]", vars.mst_beat, ((vars.crnt_mst_byte+1)*8)-1, vars.crnt_mst_byte*8),amba_rresp_slv_tx.read_data_chunk[vars.slv_beat][vars.crnt_slv_byte], amba_rresp_mst_tx.read_data_chunk[vars.mst_beat][vars.crnt_mst_byte], vars.result, vars.msg)
@@ -831,7 +831,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                          end else begin
                            expected_val = amba_rresp_slv_tx.read_data_chunk_memory_tag[vars.slv_beat][n_slv][b]; //  read data originates from slave_vip to amni.
                          end
-                         rtl_val      = amba_rresp_mst_tx.read_data_chunk_memory_tag[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni. 
+                         rtl_val      = amba_rresp_mst_tx.read_data_chunk_memory_tag[vars.mst_beat][n_mst][b];   // checking read_data when it reach asni.
                          `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("AMNI Expect: RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.slv_beat, b, b, expected_val, n_slv), UVM_FULL);
                          `uvm_info("AMBA5 PAYLOAD CHECKER", $sformatf("ASNI RTL   : RTAG%0d[%0d:%0d]=0x%0x, n(%0d)", vars.mst_beat, b, b, rtl_val     , n_mst), UVM_FULL);
                          `compare_signal($sformatf("ASNI RTL RTAG%0d[%0d:%0d]", vars.mst_beat, tag_mst_lsb+b, tag_mst_lsb+b),
@@ -855,7 +855,11 @@ class amba5_payload_checker_component extends generic_checker_component;
           if(!test_config.if_params[slv_tx.src_if].user_data_mode) begin // Upsizing or downsizing cases are checked along with data for new user_mode
             bit check_data_1;
             check_data_1 = (test_config.if_params[slv_tx.src_if].user_data_width > 0) ? 1 : 0;
-            cast_then_check_wr_data_user(mst_tx, slv_tx, vars, 1'b0, check_data_1);
+            `ifdef CHARIOT_ASIL_B
+              cast_then_check_wr_data_user(mst_tx, slv_tx, vars, 1'b0, 1'b0);
+            `else
+              cast_then_check_wr_data_user(mst_tx, slv_tx, vars, 1'b0, check_data_1);
+            `endif
           end
         end else begin
           if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AXI4, generic_types::PROTOCOL__ACE_LITE}) begin
@@ -911,12 +915,12 @@ class amba5_payload_checker_component extends generic_checker_component;
                  `compare_signal($sformatf("RRESP%0d", vars.mst_beat), amba_rresp_slv_tx.read_data_chunk_resp[real_slv_beat], amba_rresp_mst_tx.read_data_chunk_resp[vars.mst_beat], vars.result, vars.msg)
                end
              end else if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AHB5, generic_types::PROTOCOL__AHB_LITE}) begin
-                 //need to know expected RUSER when in sreset to update here 
+                 //need to know expected RUSER when in sreset to update here
                  if ($test$plusargs("IDM_TEST_EN")) begin // Blocking all IDM code with plusarg
                      if(!mst_tx.incr_burst_mode_with_split) begin
-                         //it's very difficult to predict resp when we enter soft reset while getting rd response  
+                         //it's very difficult to predict resp when we enter soft reset while getting rd response
                          //when it's incr burst with one master txn splitting into multiple slave txns.
-                         //TODO : Pragya get back to this if bandwidth left  
+                         //TODO : Pragya get back to this if bandwidth left
                          if((slv_tx.incr_burst_mode) && (real_slv_beat >= ahb_rresp_slv_tx.data.size())) begin
 	                         Expected_Ruser = 0;
                          end
@@ -928,7 +932,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                             if(!test_config.if_params[mst_tx.src_if].user_data_mode)
                               `compare_signal($sformatf("RUSER%0d", vars.mst_beat),Expected_Ruser, Actual_Ruser, vars.result, vars.msg)
 	                     end
-                         `compare_signal($sformatf("RRESP%0d", vars.mst_beat), beat_resp[vars.mst_beat], amba_rresp_mst_tx.read_resp[vars.mst_beat], vars.result, vars.msg)   
+                         `compare_signal($sformatf("RRESP%0d", vars.mst_beat), beat_resp[vars.mst_beat], amba_rresp_mst_tx.read_resp[vars.mst_beat], vars.result, vars.msg)
                      end
                  end
                  else begin
@@ -938,7 +942,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                         if(!test_config.if_params[mst_tx.src_if].user_data_mode)
                           `compare_signal($sformatf("RUSER%0d", vars.mst_beat),Expected_Ruser, Actual_Ruser, vars.result, vars.msg)
 	                 end
-                     `compare_signal($sformatf("RRESP%0d", vars.mst_beat), beat_resp[vars.mst_beat], amba_rresp_mst_tx.read_resp[vars.mst_beat], vars.result, vars.msg)   
+                     `compare_signal($sformatf("RRESP%0d", vars.mst_beat), beat_resp[vars.mst_beat], amba_rresp_mst_tx.read_resp[vars.mst_beat], vars.result, vars.msg)
                  end
              end else if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__APB4,generic_types::PROTOCOL__APB3}) begin
                if(!test_config.if_params[mst_tx.src_if].user_data_mode)
@@ -995,10 +999,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                     act_user_full = amba_slv_tx.data_user[vars.slv_beat];
                     for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++)
                       begin
-                        act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                        exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                        act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                        exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                       end
-                     
+
                     if (check_user) begin
                       `compare_signal($sformatf("WUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte), exp_user_per_byte, act_user_per_byte, vars.result, vars.msg)
                     end
@@ -1022,9 +1026,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                 int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                 int unsigned tag_slv_lsb = (tag_slv_msb-3);
                 // memory_tag_data[beat][n][tag_bit]
-                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                 int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                 bit expected_val=0, rtl_val=0;
                 int unsigned tag_update_mst_idx = vars.crnt_mst_byte/16; // i.e. mst_data_width=512b=64B, update_tag_idx=63/16=3
                 int unsigned tag_update_slv_idx = vars.crnt_slv_byte/16; // i.e. slv_data_width=256b=32B, update_tag_idx=31/16=1
@@ -1068,19 +1072,20 @@ class amba5_payload_checker_component extends generic_checker_component;
               if (amba_mst_tx.byte_enable[vars.mst_beat][vars.crnt_mst_byte] == 1'b1) begin
                 `compare_signal($sformatf("WDATA%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*8)-1, vars.crnt_slv_byte*8),
                         amba_mst_tx.data[vars.mst_beat][vars.crnt_mst_byte], amba_slv_tx.data[vars.slv_beat][vars.crnt_slv_byte], vars.result, vars.msg)
-                if(test_config.if_params[mst_tx.src_if].user_data_mode)
-                  begin
+                if (check_user) begin
+                  if(test_config.if_params[mst_tx.src_if].user_data_mode) begin
                     exp_user_full = amba_mst_tx.data_user[vars.mst_beat];
                     act_user_full = amba_slv_tx.data_user[vars.slv_beat];
                     for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++)
                       begin
-                        act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                        exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                        act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                        exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                       end
-    
+
                     `compare_signal($sformatf("WUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                             exp_user_per_byte, act_user_per_byte, vars.result, vars.msg)
                   end
+                end
               end
               if (amba_mst_tx.byte_enable[vars.mst_beat][vars.crnt_mst_byte] == 1'b0) begin
                 //0th beat... if strobe is 0... always expect 0
@@ -1091,7 +1096,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                 //next beat... if strobe is 0... expect 0 or previous beat's data
                   `compare_signal_multi_values($sformatf("WDATA%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*8)-1, vars.crnt_slv_byte*8),
                              0, amba_slv_tx.data[vars.slv_beat-1][vars.crnt_slv_byte], amba_slv_tx.data[vars.slv_beat][vars.crnt_slv_byte], vars.result, vars.msg)
-                end         
+                end
                   //`compare_signal($sformatf("WUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                   //      0, amba_slv_tx.data[vars.slv_beat][vars.crnt_slv_byte], vars.result, vars.msg)
               end
@@ -1106,9 +1111,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                 int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                 int unsigned tag_slv_lsb = (tag_slv_msb-3);
                 // memory_tag_data[beat][n][tag_bit]
-                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                 int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                 bit expected_val=0, rtl_val=0;
                 int unsigned tag_update_mst_idx = vars.crnt_mst_byte/16; // i.e. mst_data_width=512b=64B, update_tag_idx=63/16=3
                 int unsigned tag_update_slv_idx = vars.crnt_slv_byte/16; // i.e. slv_data_width=256b=32B, update_tag_idx=31/16=1
@@ -1165,10 +1170,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                     act_user_full = amba_slv_tx.data_user[vars.slv_beat];
                     for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++)
                       begin
-                        act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                        exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                        act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                        exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                       end
-    
+
                     `compare_signal($sformatf("WUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                             exp_user_per_byte, act_user_per_byte, vars.result, vars.msg)
                   end
@@ -1191,9 +1196,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                 int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                 int unsigned tag_slv_lsb = (tag_slv_msb-3);
                 // memory_tag_data[beat][n][tag_bit]
-                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                 int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                 bit expected_val=0, rtl_val=0;
                 int unsigned tag_update_mst_idx = vars.crnt_mst_byte/16; // i.e. mst_data_width=512b=64B, update_tag_idx=63/16=3
                 int unsigned tag_update_slv_idx = vars.crnt_slv_byte/16; // i.e. slv_data_width=256b=32B, update_tag_idx=31/16=1
@@ -1247,7 +1252,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                 //next beat... if strobe is 0... expect 0 or previous beat's data
                   `compare_signal_multi_values($sformatf("WDATA%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*8)-1, vars.crnt_slv_byte*8),
                              0, amba_slv_tx.data[vars.slv_beat-1][vars.crnt_slv_byte], amba_slv_tx.data[vars.slv_beat][vars.crnt_slv_byte], vars.result, vars.msg)
-                end         
+                end
               end
 
               `compare_signal($sformatf("WSTRB%0d[%0d]", vars.slv_beat, vars.crnt_slv_byte),
@@ -1268,9 +1273,9 @@ class amba5_payload_checker_component extends generic_checker_component;
                 int unsigned tag_slv_msb = vars.crnt_slv_byte>15 ? vars.crnt_slv_byte/4 : 3; // i.e. slv_data_width=256b=32B, update_idx=31/4=7, it means msb=7, lsb=7-3=4. idx=7:4
                 int unsigned tag_slv_lsb = (tag_slv_msb-3);
                 // memory_tag_data[beat][n][tag_bit]
-                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0] 
+                // n_mst/n_slv is for accessing vip's memory_tag_data structure.  n = nth tag within a beat (0..3).  i.e.  beat[n=3, n=2, n=1, n=0]
                 int unsigned n_mst = tag_mst_msb/(4); // i.e. for 128b datawidth, tag_msb=3, div by 4 because 4b/beat. n = 3/4 = 0th tag w/in a beat;
-                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat. 
+                int unsigned n_slv = tag_slv_msb/(4); // i.e. for 512b datawidth == max beat width, tag_msb=15,11,7,3, n=0,1,2,3; for msb=15, n = 15/4 = 3th within a beat.
                 bit expected_val=0, rtl_val=0;
                 int unsigned tag_update_mst_idx = vars.crnt_mst_byte/16; // i.e. mst_data_width=512b=64B, update_tag_idx=63/16=3
                 int unsigned tag_update_slv_idx = vars.crnt_slv_byte/16; // i.e. slv_data_width=256b=32B, update_tag_idx=31/16=1
@@ -1329,10 +1334,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                   exp_user_full = amba_mst_tx.data[vars.mst_beat].data_user;
                   act_user_full = amba_slv_tx.data_user[vars.slv_beat];
                   for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++) begin
-                    act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                    exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                    act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                    exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                   end
-    
+
                   `compare_signal($sformatf("WUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                   exp_user_per_byte, act_user_per_byte, vars.result, vars.msg)
                 end
@@ -1361,7 +1366,7 @@ class amba5_payload_checker_component extends generic_checker_component;
             if (check_data) begin
 	            //if (vars.mst_beat < amba_mst_tx.data.data.size()) begin //VIP migration code change, AHB AUg vip
 	            if (vars.mst_beat < amba_mst_tx.data.size()) begin
-	      
+
                 `compare_signal($sformatf("WDATA%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*8)-1, vars.crnt_slv_byte*8),
                 amba_mst_tx.data[vars.mst_beat].data[vars.crnt_mst_byte], amba_slv_tx.data[vars.slv_beat][vars.crnt_slv_byte], vars.result, vars.msg)
                 `compare_signal($sformatf("WSTRB%0d[%0d]", vars.slv_beat, vars.crnt_slv_byte),
@@ -1370,10 +1375,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                   exp_user_full = amba_mst_tx.data[vars.mst_beat].data_user;
                   act_user_full = amba_slv_tx.data_user[vars.slv_beat];
                   for(int a_width = vars.crnt_slv_byte*user_per_byte,e_width = vars.crnt_mst_byte*user_per_byte; a_width < ((vars.crnt_slv_byte+1)*user_per_byte); a_width++,e_width++) begin
-                    act_user_per_byte = {act_user_per_byte,act_user_full[a_width]}; 
-                    exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]}; 
+                    act_user_per_byte = {act_user_per_byte,act_user_full[a_width]};
+                    exp_user_per_byte = {exp_user_per_byte,exp_user_full[e_width]};
                   end
-    
+
                   `compare_signal($sformatf("WUSER%0d[%0d:%0d]", vars.slv_beat, ((vars.crnt_slv_byte+1)*user_per_byte)-1, vars.crnt_slv_byte*user_per_byte),
                   exp_user_per_byte, act_user_per_byte, vars.result, vars.msg)
                 end
@@ -1438,7 +1443,7 @@ class amba5_payload_checker_component extends generic_checker_component;
 
 
       if (s_req || s_req_data) begin
-        mst_tx = tx_event.set.tx_array[generic_types::DEVICE__MASTER][0];  
+        mst_tx = tx_event.set.tx_array[generic_types::DEVICE__MASTER][0];
         slv_tx = tx_event.tx;
 
         //$cast(amba_mst_tx, mst_tx.tx);
@@ -1510,7 +1515,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                 snoop = 4'b1000;
               // Convert write_plus_cmo_full to write_plus_cmo_partial if address not aligned to the data bus
               end else if ((amni_split_tx.snoop == 4'b1011) && ((amba_slv_tx.axaddr % amba_slv_tx.get_data_bytes) != 0)) begin
-                snoop = test_config.if_params[mst_tx.dst_if].write_plus_cmo ? 
+                snoop = test_config.if_params[mst_tx.dst_if].write_plus_cmo ?
                         4'b1010 : test_config.if_params[mst_tx.dst_if].write_plus_cmo;
               end
               else if ((amni_split_tx.snoop == 4'b1010) || (amni_split_tx.snoop == 4'b1011)) begin
@@ -1568,16 +1573,16 @@ class amba5_payload_checker_component extends generic_checker_component;
         `compare_signal("AxUSER"  , amni_split_tx.user  , amba_slv_tx.addr_user  , result, msg)
 
         if (test_config.if_params[slv_tx.src_if].nsaid_support) begin
-          if ($cast(amba_mst_tx, mst_tx.tx)) begin // Workaround : VIP monitor sometimes doesnt give correct NSAID value during REQ_V event 
+          if ($cast(amba_mst_tx, mst_tx.tx)) begin // Workaround : VIP monitor sometimes doesnt give correct NSAID value during REQ_V event
             `compare_signal("AxNSAID"  , amba_mst_tx.nsaid, amba_slv_tx.nsaid, result, msg)
           end else begin
             `compare_signal("AxNSAID"  , amni_split_tx.nsaid, amba_slv_tx.nsaid, result, msg)
           end
         end
-             
+
 
         if (test_config.if_params[slv_tx.src_if].mte_support != 0) begin
-          if ($cast(amba_mst_tx, mst_tx.tx)) begin  
+          if ($cast(amba_mst_tx, mst_tx.tx)) begin
             `compare_signal("AxTAGOP"  , amba_mst_tx.memory_tag_operation, amba_slv_tx.memory_tag_operation, result, msg)
           end else begin
             `compare_signal("AxTAGOP"  , amni_split_tx.memory_tag_operation, amba_slv_tx.memory_tag_operation, result, msg)
@@ -1585,7 +1590,7 @@ class amba5_payload_checker_component extends generic_checker_component;
         end
 
         if (test_config.if_params[slv_tx.src_if].loop_signals) begin
-          if ($cast(amba_mst_tx, mst_tx.tx)) begin  
+          if ($cast(amba_mst_tx, mst_tx.tx)) begin
             `compare_signal("AxLOOP"  , amba_mst_tx.addr_loop, amba_slv_tx.addr_loop, result, msg)
           end else begin
             `compare_signal("AxLOOP"  , amni_split_tx.addr_loop, amba_slv_tx.addr_loop, result, msg)
@@ -1597,7 +1602,7 @@ class amba5_payload_checker_component extends generic_checker_component;
           `compare_signal("AWUNIQUE", ax_unique, amba_slv_tx.awunique, result, msg)
           `compare_signal("AWATOP"  , amni_split_tx.atomic_op_type, amba_slv_tx.atomic_op_type, result, msg)
           if (!converted_wu_wlu_stash) begin
-            if ($cast(amba_mst_tx, mst_tx.tx)) begin // Workaround : VIP monitor sometimes doesnt give correct stah_node_id value during REQ_V event 
+            if ($cast(amba_mst_tx, mst_tx.tx)) begin // Workaround : VIP monitor sometimes doesnt give correct stah_node_id value during REQ_V event
               `compare_signal("AWSTASHNID"   , amba_mst_tx.stash_node_id     , amba_slv_tx.stash_node_id   , result, msg)
             end else begin
               `compare_signal("AWSTASHNID"   , amni_split_tx.stash_node_id   , amba_slv_tx.stash_node_id   , result, msg)
@@ -1615,7 +1620,7 @@ class amba5_payload_checker_component extends generic_checker_component;
         data_check_variables vars;
         int unsigned slave_index = 0;
 
-        
+
         if (amni_split_tx.mst_burst_type == 0) begin
           // Find which number slave transaction this is
           int unsigned num_slave_tx = tx_event.set.tx_array[generic_types::DEVICE__SLAVE].size();
@@ -1676,7 +1681,7 @@ class amba5_payload_checker_component extends generic_checker_component;
         if(mte_support==2 && (amba_mst_wr_rsp.get_memory_tag_operation == vip_ace5_types::MEM_TAG_OP_WRITE_MATCH_READ_FETCH)) begin
           // Note: default btagmatch=fail=2 for dst=non-amba endpoints.  if its amba endpoints or txn bounceback by ansi, code below will override tagmatch.
           bcomp     = 1;
-          btagmatch = 2; 
+          btagmatch = 2;
           `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: axaddr(0x%0x), memory_tag_op(%0s), default btagmatch=(%0b) due to mte_support=2.", amba_mst_wr_rsp.axaddr, amba_mst_wr_rsp.get_memory_tag_operation, btagmatch), UVM_FULL);
         end
 
@@ -1730,7 +1735,7 @@ class amba5_payload_checker_component extends generic_checker_component;
               resp = vip_ace5_types::RESP_SLAVE_ERROR;
               break;
             end
-          end 
+          end
 
           // Grab the last slave transaction to work out the user in the non
           // FIXED case
@@ -1744,7 +1749,7 @@ class amba5_payload_checker_component extends generic_checker_component;
           for (int unsigned x = 0; x < num_slave_tx; ++x) begin
             slv_tx = tx_event.set.tx_array[generic_types::DEVICE__SLAVE][x];
 
-            if (slv_tx != null )  
+            if (slv_tx != null )
             begin
               slv_addr_width = test_config.if_params[slv_tx.src_if].addr_width;
               slv_addr_mask = (1 << slv_addr_width) - 1;
@@ -1757,15 +1762,15 @@ class amba5_payload_checker_component extends generic_checker_component;
                 end
                 if ($cast(ahb_slv_wr_rsp, slv_tx.tx)) begin
                   //TODO slv_user = ahb_slv_wr_rsp.request_beats[0].AUser;
-                  slv_ahb_resp_beat = ahb_slv_wr_rsp.response_beats.size(); 
-                  slv_addr = ahb_slv_wr_rsp.request_beats[0].Address; 
+                  slv_ahb_resp_beat = ahb_slv_wr_rsp.response_beats.size();
+                  slv_addr = ahb_slv_wr_rsp.request_beats[0].Address;
                   dst_hmni = 1;
                 end
                 if ($cast(apb_slv_wr_rsp, slv_tx.tx)) begin
-                  slv_user = 'b0; //review 
-                  slv_addr = apb_slv_wr_rsp.addr; 
+                  slv_user = 'b0; //review
+                  slv_addr = apb_slv_wr_rsp.addr;
                 end
- 
+
                 num_amni_splits = tx_event.set.tx_array[generic_types::DEVICE__XMNI_SPLIT].size();
                 for (int unsigned x = 0; x < num_amni_splits; ++x) begin
                   amni_split_gen_tx = tx_event.set.tx_array[generic_types::DEVICE__XMNI_SPLIT][x];
@@ -1787,7 +1792,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                 if (slv_tx.tx_protocol inside {generic_types::PROTOCOL__AXI4, generic_types::PROTOCOL__ACE_LITE}) begin
                   if ($test$plusargs("IDM_TEST_EN")) begin // Blocking all IDM code with plusarg
                       if(mst_tx.split_write_unfinished_bef_sreset == 0) begin
-                          if (resp == vip_ace5_types::RESP_DECODE_ERROR) begin 
+                          if (resp == vip_ace5_types::RESP_DECODE_ERROR) begin
                             continue;
                           end else if (amba_slv_wr_rsp.write_resp == vip_ace5_types::RESP_DECODE_ERROR) begin
                             resp = vip_ace5_types::RESP_DECODE_ERROR;
@@ -1795,11 +1800,11 @@ class amba5_payload_checker_component extends generic_checker_component;
                             continue;
                           end else if (amba_slv_wr_rsp.write_resp != vip_ace5_types::RESP_EXCL_OKAY) begin
                             resp = amba_slv_wr_rsp.write_resp;
-                          end //if -else if 
-                      end  
+                          end //if -else if
+                      end
                   end
                   else begin
-                      if (resp == vip_ace5_types::RESP_DECODE_ERROR) begin 
+                      if (resp == vip_ace5_types::RESP_DECODE_ERROR) begin
                         continue;
                       end else if (amba_slv_wr_rsp.write_resp == vip_ace5_types::RESP_DECODE_ERROR) begin
                         resp = vip_ace5_types::RESP_DECODE_ERROR;
@@ -1807,8 +1812,8 @@ class amba5_payload_checker_component extends generic_checker_component;
                         continue;
                       end else if (amba_slv_wr_rsp.write_resp != vip_ace5_types::RESP_EXCL_OKAY) begin
                         resp = amba_slv_wr_rsp.write_resp;
-                      end //if -else if 
-                  end  
+                      end //if -else if
+                  end
 
 
                   //################
@@ -1829,7 +1834,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                       btagmatch = 0; // btagmatch=not a match txn
                     `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: axaddr(0x%0x), mte_support(%0d), bcomp(%0b), btagmatch=0", amba_mst_wr_rsp.axaddr, mte_support, bcomp), UVM_FULL);
                     end else begin // MTE_SUPPORT_STANDARD
-                      xmni_mte_support = test_config.if_params[slv_tx.src_if].mte_support; 
+                      xmni_mte_support = test_config.if_params[slv_tx.src_if].mte_support;
                       if(!(amba_mst_wr_rsp.get_memory_tag_operation inside {vip_ace5_types::MEM_TAG_OP_WRITE_MATCH_READ_FETCH})) begin
                         bcomp     = 1; // if not tag match op, for any resp, BCOMP=1
                         btagmatch = 0; // btagmatch=0=not a match txn for either pcmo case or not.
@@ -1879,10 +1884,10 @@ class amba5_payload_checker_component extends generic_checker_component;
                   $cast(xsni_split, gen_xsni_split.tx);
                   //`uvm_info("AMBA5_PAYLOAD_CHKR", "before looping through beats", UVM_NONE)
 
-                  for (int i = 0 ; i < slv_ahb_resp_beat ; i++) begin 
+                  for (int i = 0 ; i < slv_ahb_resp_beat ; i++) begin
                     rsp_beat = ahb_slv_wr_rsp.response_beats[i];
                     request_beat = ahb_slv_wr_rsp.request_beats[i];
- 
+
                     if (resp inside {vip_ace5_types::RESP_DECODE_ERROR, vip_ace5_types::RESP_SLAVE_ERROR}) begin
                       continue;
                     end else begin
@@ -1898,7 +1903,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                     end
                   end //for
                 end else if  (slv_tx.tx_protocol inside {generic_types::PROTOCOL__APB4,generic_types::PROTOCOL__APB3}) begin
-                  if (resp == vip_ace5_types::RESP_DECODE_ERROR) begin 
+                  if (resp == vip_ace5_types::RESP_DECODE_ERROR) begin
                     continue;
                   end else if (apb_slv_wr_rsp.pslverr == 'b1) begin
                     resp = vip_ace5_types::RESP_SLAVE_ERROR;
@@ -1914,7 +1919,7 @@ class amba5_payload_checker_component extends generic_checker_component;
             end
           end
         end //for loop end
-  
+
 
 
         //REVISIT_BOOKER_NOC_LAC: Enable the below checks for CMOs. Known TB issue
@@ -1931,7 +1936,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                   if(mst_tx.split_write_unfinished_bef_sreset) begin
                       user = 0;
                   end
-                  else begin  
+                  else begin
                       user      = user & ((1 << test_config.if_params[mst_tx.src_if].buser_width) - 1);
                   end
                   resp_user = amba_mst_wr_rsp.resp_user & (( 1 << test_config.if_params[mst_tx.src_if].buser_width) - 1);
@@ -1981,7 +1986,7 @@ class amba5_payload_checker_component extends generic_checker_component;
         end
         if((check_mte_btagmatch|check_mte_bcomp)==1) begin : mte_bcomp_btagmatch_check
           bit asni_rsp_nml = (mst_tx.dst_status == generic_transaction::STAT__NML);
-          `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: axaddr(0x%0x), mte_support=(%0d), persist_cmo(%0b), int_rsp(%0b), asni_rsp_nml(%0b)", 
+          `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: axaddr(0x%0x), mte_support=(%0d), persist_cmo(%0b), int_rsp(%0b), asni_rsp_nml(%0b)",
                      amba_mst_wr_rsp.axaddr, (mte_support), (test_config.if_params[mst_tx.src_if].persist_cmo), int_rsp, asni_rsp_nml), UVM_FULL);
           // BCOMP/BTAGMATCH override due to bouncebacks
           if(mte_support==2 && int_rsp==1) begin  // only applicable for mte_support_standard
@@ -1999,29 +2004,29 @@ class amba5_payload_checker_component extends generic_checker_component;
 
           // MTE Support incompatible case:
           // AMNI Spec
-          // In case Memory tagging is disabled for master interface (MTE_SUPPORT) but AMNI receives tag request (GT_MTE=1) then BCOMP and BTAGMATCH values in GT response will take following values: 
-          // 
+          // In case Memory tagging is disabled for master interface (MTE_SUPPORT) but AMNI receives tag request (GT_MTE=1) then BCOMP and BTAGMATCH values in GT response will take following values:
+          //
           // BCOMP:
           //   If AXI has BCOMP pin configured then AMNI will pack the value to GT.BCOMP.
-          //   If AXI doesn\xbft have BCOMP pin then AMNI will tie-off \xbf1\xbf always indicating completion response. 
-          // 
+          //   If AXI doesn\xbft have BCOMP pin then AMNI will tie-off \xbf1\xbf always indicating completion response.
+          //
           // BTAGMATH:
           //   If Request opcode was Match then AMNI will drive GT.BTAGMATCH = 2'b10 (that is Fail response)
           //   If Request opcode was Invalid, Transfer or Update then AMNI will drive GT.BTAGMATCH = 2'b00 (that is "Match not performed").
-          // 
-          if(mte_support==2 && xmni_mte_support inside {0}) begin  
+          //
+          if(mte_support==2 && xmni_mte_support inside {0}) begin
             if(amba_mst_wr_rsp.get_memory_tag_operation == vip_ace5_types::MEM_TAG_OP_WRITE_MATCH_READ_FETCH) begin // tagop=3=match
               // Note: This is only for bouceback case where asni responds with bcomp=1 & btagmatch=2. If the master uses the Match operation, the response will not be protocol compliant.
               // Per Naveen: This is not disabled in DRC.  All combinations of MTE are supported, except: ASNI=Standard and AMNI=Basic
               // In this case where (ASNI=Standard and AMNI=Disabled), it is allowed and AMNI is supposed to bounce it back.
               bcomp     = 1;
               btagmatch = 2; // btagmatch=fail
-              `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: MATCH txn with incompatible mte case. asni_mte_support(%0d), xmni_mte_support(%0d), memory_tag_op(%0s), bcomp=%0b, btagmatch(%0b), write_resp(%0s).  txn should be bouceback in this case.", 
+              `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: MATCH txn with incompatible mte case. asni_mte_support(%0d), xmni_mte_support(%0d), memory_tag_op(%0s), bcomp=%0b, btagmatch(%0b), write_resp(%0s).  txn should be bouceback in this case.",
                        mte_support, xmni_mte_support, amba_mst_wr_rsp.get_memory_tag_operation, bcomp, btagmatch,amba_mst_wr_rsp.write_resp), UVM_FULL);
             end  else begin
               bcomp     = 1;
-              btagmatch = 0; 
-              `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: Non-MATCH txn with incompatible mte case. asni_mte_support(%0d), xmni_mte_support(%0d), memory_tag_op(%0s), bcomp=%0b, btagmatch(%0b), write_resp(%0s).  txn should be bouceback in this case.", 
+              btagmatch = 0;
+              `uvm_info("AMBA5_PAYLOAD_CHKR", $sformatf("MTE: Non-MATCH txn with incompatible mte case. asni_mte_support(%0d), xmni_mte_support(%0d), memory_tag_op(%0s), bcomp=%0b, btagmatch(%0b), write_resp(%0s).  txn should be bouceback in this case.",
                        mte_support, xmni_mte_support, amba_mst_wr_rsp.get_memory_tag_operation, bcomp, btagmatch,amba_mst_wr_rsp.write_resp), UVM_FULL);
             end
           end
@@ -2059,11 +2064,11 @@ class amba5_payload_checker_component extends generic_checker_component;
           int unsigned num_beats = amba_mst_tx.get_number_of_beats();
           $cast(amba_rresp_mst_tx, mst_tx.tx);
           mst_size_int = 1 << amba_mst_tx.axsize;
-          slv_size_int = test_config.if_params[mst_tx.dst_if].interface_data_width/8; 
+          slv_size_int = test_config.if_params[mst_tx.dst_if].interface_data_width/8;
           downsize_int = mst_size_int/slv_size_int;
- 
+
           if(downsize_int > 1)  mst_tx.rd_rsp_done_bef_sreset = mst_tx.rd_rsp_done_bef_sreset/downsize_int;
-          
+
 
           case (mst_tx.dst_status)
             generic_transaction::STAT__NON : resp = vip_ace5_types::RESP_DECODE_ERROR;
@@ -2095,7 +2100,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                    `compare_signal($sformatf("RUSER%0d", x), 0, amba_rresp_mst_tx.data_user[x], result, msg)
                `compare_signal($sformatf("RRESP%0d", x), resp, amba_rresp_mst_tx.read_resp[x], result, msg)
              end
-          end  
+          end
 
           //REVISIT_BOOKER_NOC_LAC : jira BOOKERNOC-2420 ..Remove this gating
           if(amba_mst_tx.read_data_chunking_enable == 0) begin
@@ -2107,7 +2112,7 @@ class amba5_payload_checker_component extends generic_checker_component;
               end
             end
           end
-        end 
+        end
         else begin
           int unsigned num_slave_tx = tx_event.set.tx_array[generic_types::DEVICE__SLAVE].size();
           int unsigned num_xsni_split = tx_event.set.tx_array[generic_types::DEVICE__XSNI_SPLIT].size();
@@ -2117,7 +2122,7 @@ class amba5_payload_checker_component extends generic_checker_component;
           int unsigned num_idm_slverr;
           int unsigned slv_to_master_txn_ratio;
           int unsigned mst_txn_done_on_slv;
- 
+
           // Clear current array
           beat_resp.delete(); // ENHANCEMENT - refactor for performance
           if(num_xmni_split > (amba_mst_tx.axlen+1)) begin
@@ -2159,7 +2164,7 @@ class amba5_payload_checker_component extends generic_checker_component;
                   else begin
                       beat_resp[completed_beats + i] =  vip_ace5_types::RESP_SLAVE_ERROR;
                   end
-                  
+
               end
               num_idm_slverr++;
             end
@@ -2172,7 +2177,7 @@ class amba5_payload_checker_component extends generic_checker_component;
             if(test_config.if_params[mst_tx.dst_if].protocol_type == generic_types::PROTOCOL__AXI4) bounceback_cmo = 1;
             if((test_config.if_params[mst_tx.dst_if].protocol_type == generic_types::PROTOCOL__ACE_LITE) && (test_config.if_params[mst_tx.dst_if].read_cmo == 0) && (test_config.if_params[mst_tx.dst_if].write_cmo == 0)) bounceback_cmo = 1;
             if((test_config.if_params[mst_tx.dst_if].protocol_type == generic_types::PROTOCOL__ACE_LITE) && (test_config.if_params[mst_tx.dst_if].read_cmo == 0) && (test_config.if_params[mst_tx.dst_if].write_cmo == 1)) bounceback_cmo = 1;
-          end 
+          end
           if((amba_mst_tx.txn_type == vip_ace5_types::WRITE_TRANSACTION) && (amba_mst_tx.axsnoop == vip_ace5_types::AWSNOOP_CMO))
           begin
             if(test_config.if_params[mst_tx.dst_if].protocol_type == generic_types::PROTOCOL__AXI4) bounceback_cmo = 1;
@@ -2190,7 +2195,7 @@ class amba5_payload_checker_component extends generic_checker_component;
           if ((num_slave_tx == 0) && (bounceback_cmo == 0) && ((num_idm_slverr > 0) ? (num_idm_slverr != num_xsni_split) : 1)) begin
             `uvm_error("PAYLOAD CHECKER", $sformatf("No Slave Transaction Found : src_if = %0d, addr = %0h", mst_tx.src_if, mst_tx.addr))
           end
- 
+
           for (int unsigned x = 0; x < num_slave_tx; ++x) begin
             slv_tx = tx_event.set.tx_array[generic_types::DEVICE__SLAVE][x];
             if ($test$plusargs("IDM_TEST_EN_DBG")) begin
@@ -2273,7 +2278,7 @@ class amba5_payload_checker_component extends generic_checker_component;
   virtual function int get_min_addr(uvm_object txn);
     vip_ahb5_transaction_item ahb_tx;
     int unsigned min_addr;
-    
+
     if ($cast(ahb_tx, txn)) begin
       vip_ahb5_types::request_beat_struct_t  req_beat;
       req_beat = ahb_tx.request_beats[0];
@@ -2285,7 +2290,7 @@ class amba5_payload_checker_component extends generic_checker_component;
         txn_size = (2**req_beat.Size) * calculate_ahb_burst_len(ahb_tx);
         min_addr = min_addr - (min_addr % txn_size);
       end
-    end 
+    end
 
     return(min_addr);
   endfunction
@@ -2293,7 +2298,7 @@ class amba5_payload_checker_component extends generic_checker_component;
   virtual function int get_max_addr(uvm_object txn);
     vip_ahb5_transaction_item ahb_tx;
     int unsigned max_addr;
-    
+
     if ($cast(ahb_tx, txn)) begin
       vip_ahb5_types::request_beat_struct_t  req_beat;
       int txn_size;
@@ -2306,7 +2311,7 @@ class amba5_payload_checker_component extends generic_checker_component;
       end else begin
         max_addr = req_beat.Address + txn_size;
       end
-    end 
+    end
 
     return(max_addr-1);
   endfunction
@@ -2323,7 +2328,7 @@ class amba5_payload_checker_component extends generic_checker_component;
       4,5 : burst_length = 8;
       6,7 : burst_length = 16;
     endcase
-    
+
     return burst_length;
   endfunction
 
diff --git a/logical/noc_arachne/validation/dynamic/top/testbench.sv b/logical/noc_arachne/validation/dynamic/top/testbench.sv
index 9fcbd169ff0..adf1e480c74 100755
--- a/logical/noc_arachne/validation/dynamic/top/testbench.sv
+++ b/logical/noc_arachne/validation/dynamic/top/testbench.sv
@@ -40,6 +40,9 @@
 `include "sva/arachne_xmni_srcid_scov_sva.sv"
 `include "sva/arachne_crb_converter_scov_sva.sv"
 `include "components/scov/arachne_qch_dbgmsg.sv"
+`ifdef CHARIOT_ASIL_B
+  `include "components/chariot/chariot_pkg.svh"
+`endif // CHARIOT_ASIL_B
 
 
 module testbench;
@@ -50,6 +53,9 @@ module testbench;
   `ifdef POWER_AWARE
     import UPF::*;
   `endif
+  `ifdef CHARIOT_ASIL_B
+    import chariot_pkg::*;
+  `endif // CHARIOT_ASIL_B
 
   `include "configuration_local_params.svh"
 
@@ -86,11 +92,11 @@ module testbench;
   wire [NUM_CD+NUM_COMB-1:0] clk_enable;
   wire [NUM_CD+NUM_COMB-1:0] RSTn_CFG;
 
-  test_configuration_functions tst_cfg; 
+  test_configuration_functions tst_cfg;
   `ifdef POWER_AWARE
     //power aware
     string power_domain_str;
-    string rao_domain_str; //Relatively always on power domain 
+    string rao_domain_str; //Relatively always on power domain
   // Include UPF isolation nets for power aware simulation
     `include "iso_nets.svh"
   `endif
@@ -130,7 +136,7 @@ module testbench;
             .SAR_CFG     (           )
         );
     end : g_q_domain
- 
+
 
     // Create each power domain
     for (genvar a = 0; a < NUM_PD; a++)
@@ -449,8 +455,8 @@ module testbench;
              .CACHE_STASH_TRANSACTIONS  (IF_CACHE_STASH[a]            ),
              .PERSIST_CMO               (IF_PERSIST_CMO[a]            ),
              .WRITE_PLUS_CMO            (IF_WRITE_PLUS_CMO[a]         ),
-             .CMO_ON_WRITE              (IF_WRITE_CMO[a]              ), 
-             .CMO_ON_READ               (IF_READ_CMO[a]               ), 
+             .CMO_ON_WRITE              (IF_WRITE_CMO[a]              ),
+             .CMO_ON_READ               (IF_READ_CMO[a]               ),
              .MTE_SUPPORT               (IF_MTE_SUPPORT[a]            ),
              .PREFETCH_TRANSACTION      (IF_PREFETCH_TRANSACTION[a]   ),
              .DEALLOCATION_TRANSACTIONS (IF_DEALLOCATION[a]           ),
@@ -490,7 +496,7 @@ module testbench;
            (
              .ACLK                      (CLK_TB[CLOCK_MAP[a]]         ),
              .ACLKEN                    (1'b1                         ),
-          `ifdef PERF_TB 
+          `ifdef PERF_TB
             `ifdef IDM_PRESENT
               .ARESETn                 (ARESETn [CLOCK_MAP[a]] ),
               .SRESETn                 (g_idm_interface.idm_if_i.SRESETN[a]),
@@ -511,7 +517,7 @@ module testbench;
             .AHB_RESETn               (ARESETn[CLOCK_MAP[a]]        )
           `endif
            );
-        
+
         initial
         begin
            `ifndef PERF_TB
@@ -550,8 +556,8 @@ module testbench;
            .CACHE_STASH_TRANSACTIONS  (IF_CACHE_STASH[a]           ),
            .PERSIST_CMO               (IF_PERSIST_CMO[a]           ),
            .WRITE_PLUS_CMO            (IF_WRITE_PLUS_CMO[a]        ),
-           .CMO_ON_WRITE              (IF_WRITE_CMO[a]             ), 
-           .CMO_ON_READ               (IF_READ_CMO[a]              ), 
+           .CMO_ON_WRITE              (IF_WRITE_CMO[a]             ),
+           .CMO_ON_READ               (IF_READ_CMO[a]              ),
            .MTE_SUPPORT               (IF_MTE_SUPPORT[a]            ),
            .PREFETCH_TRANSACTION      (IF_PREFETCH_TRANSACTION[a]   ),
            .DEALLOCATION_TRANSACTIONS (IF_DEALLOCATION[a]          ),
@@ -585,7 +591,7 @@ module testbench;
          (
            .ACLK                      (CLK_TB[CLOCK_MAP[a]]        ),
            .ACLKEN                    (1'b1                        ),
-          `ifdef PERF_TB 
+          `ifdef PERF_TB
             `ifdef IDM_PRESENT
               .ARESETn                (IF_IDM_SUPPORT[a] ? (g_idm_interface.idm_if_i.SRESETN[a] & ARESETn[CLOCK_MAP[a]]) : ARESETn[CLOCK_MAP[a]]     ),
               .SRESETn                (g_idm_interface.idm_if_i.SRESETN[a]),
@@ -621,13 +627,13 @@ module testbench;
             begin
               vifs_ready.trigger();
             end
-           `endif       
+           `endif
         end
 
         `ifdef IDM_PRESENT
           assign g_idm_interface.idm_if_i.SRESETN[a] = g_idm_interface.idm_if_i.XMNI_SRESETN[IF_NODE_ID[a]];
-        `endif       
- 
+        `endif
+
       end : slave
     endcase
   end : g_interface
@@ -671,7 +677,7 @@ module testbench;
 
   interrupt_block #(NUM_PD) g_interrupt_interface ();
 
-  `ifdef PERF_TB 
+  `ifdef PERF_TB
     perf_debug_if #(NUM_ASNI,NUM_AMNI,NUM_HSNI,NUM_HMNI,NUM_PMNI) perf_debug_if_();
     top_debug_if top_debug_if_();
   `endif
@@ -679,16 +685,33 @@ module testbench;
 
   // Each reset for the DUT is a combination of a system reset and a power
   // domain reset
-  `ifndef PERF_TB 
+  `ifndef PERF_TB
     assign ARESETn = CD_RESETn & SYS_RESETn;
   `endif
 
+  `ifdef CHARIOT_ASIL_B
+    logic [IF_W_USER_WIDTH[0]-1:0] err_detection_code;
+    logic parity_error;
+    chariot_parity_generation #(IF_DATA_WIDTH[0], IF_W_USER_WIDTH[0]) add_parity_instance (
+      .data_i (g_interface[0].master.u_if.g_ace4_lite.u_if.WDATA),
+      .strb_i (g_interface[0].master.u_if.g_ace4_lite.u_if.WSTRB),
+      .user_o (err_detection_code)
+    );
+
+    chariot_parity_checker #(IF_DATA_WIDTH[1], IF_W_USER_WIDTH[1]) check_parity_instance (
+      .data_i (g_interface[1].slave.u_if.g_axi4.u_if.WDATA),
+      .valid_i (g_interface[1].slave.u_if.g_axi4.u_if.WVALID),
+      .user_i (g_interface[1].slave.u_if.g_axi4.u_if.WUSER),
+      .error_o (parity_error)
+    );
+  `endif // CHARIOT_ASIL_B
+
   // Connect the interfaces to the DUT
   `include "wrapper_connect.svh"
 
   initial
   begin
-  `ifdef PERF_TB 
+  `ifdef PERF_TB
       uvm_config_db#(virtual perf_debug_if#(NUM_ASNI,NUM_AMNI,NUM_HSNI,NUM_HMNI,NUM_PMNI))::set(uvm_root::get(), "*","perf_debug_vif",perf_debug_if_);
 
       uvm_config_db#(virtual top_debug_if)  ::set(uvm_root::get(), "*","top_debug_if" ,top_debug_if_ );
@@ -696,18 +719,18 @@ module testbench;
 
     `ifdef POWER_AWARE
       tst_cfg = test_configuration_functions::get_instance();
-      foreach (tst_cfg.power_domains_name[i]) begin //i is power domain number 
+      foreach (tst_cfg.power_domains_name[i]) begin //i is power domain number
         power_domain_str = tst_cfg.power_domains_name[i];
         void'(supply_on($sformatf("VDD_%0s",power_domain_str.toupper()), 1.0));
         void'(supply_on($sformatf("VSS_%0s",power_domain_str.toupper()), 0.0));
       end
-      
+
       rao_domain_str = tst_cfg.rao_domain;
       void'(supply_on($sformatf("VDD_%0s",rao_domain_str.toupper()), 1.0));
       void'(supply_on($sformatf("VSS_%0s",rao_domain_str.toupper()), 0.0));
 
     `endif
-    `ifdef PERF_TB 
+    `ifdef PERF_TB
       vifs_ready.wait_ptrigger();
     `else
       u_sys_clock.vif_ready.wait_trigger();
@@ -723,7 +746,7 @@ module testbench;
 
   assign top_fusa_interrupt_if.clk = TB_SYS_CLK;
   assign top_fusa_interrupt_if.fault_is_being_injected = fault_is_being_injected;
-  assign top_fusa_interrupt_if.safety_interrupt = 0; // Michael, we should connect this to our safety mechanism outputs
+  assign top_fusa_interrupt_if.safety_interrupt = parity_error; // Michael, we should connect this to our safety mechanism outputs
   initial begin
     uvm_config_db#(virtual fusa_interrupt_if)::set(uvm_root::get(), "*","fusa_interrupt_if" ,top_fusa_interrupt_if);
   end
@@ -753,7 +776,7 @@ endmodule
     u_asni_idm_greybox(.*);
   `endif
 
-  bind arachne_asni_axi4_adaptor 
+  bind arachne_asni_axi4_adaptor
     cdas_tb_assertions
     #(
       .NODE_ID                (NODE_ID                     ),
diff --git a/logical/shared/scripts/arm_engine/services/param_engine/param_engine.sm b/logical/shared/scripts/arm_engine/services/param_engine/param_engine.sm
index 3d322751a50..621e711dad6 100644
--- a/logical/shared/scripts/arm_engine/services/param_engine/param_engine.sm
+++ b/logical/shared/scripts/arm_engine/services/param_engine/param_engine.sm
@@ -106,6 +106,8 @@ class param_engine (sm_base):
 
      group_sm.add_option("--hlk_check"      ,  dest="hlk_check"      , action="store_true",  default=False, help='Executes a simple check that the HLK is inline with stored version')
      group_sm.add_option("--remove_render"  ,  dest="remove_render"  , action="store_true",  default=False, help='Removes the rendered RTL associated with the build process')
+     group_sm.add_option("--chariot_b"      ,  dest="chariot_b"  , action="store_true",  default=False, help='Configures design to add Chariot ASIL B safety mechanisms')
+
 
 
      self.parser.add_option_group(group_sm)
@@ -227,7 +229,7 @@ class param_engine (sm_base):
      report_output    = directory
      bundle_target    = '' + environ.get("NOC_DIR") + "/../../"
      config_name      = "%s_%s" % (self.options.product_name,config)
-     
+
      vc_output        = '' + environ.get("NOC_DIR") + "/../../%s/%s/logical/%s/%s.vc" % (config_type, config, config_name, config_name)
 
      # HLK information
@@ -250,7 +252,7 @@ class param_engine (sm_base):
      validation_opts = " --internal_schema " if self.options.validation  else ""
      colour_opts     = " --report_colour "   if self.options.colour      else ""
      clean_opts      = " --clean_build "     if self.options.clean_build else ""
-
+     chariot_b_str   = " --chariot_b "       if self.options.chariot_b   else ""
 
      # --- Generate directory and param engine execution script
 
@@ -260,10 +262,10 @@ class param_engine (sm_base):
      # Build param engine source script
      param_engine_script = ['\n\n# Execute Parameter Engine Build']
      param_engine_script.extend(['\n\nsetenv BOOKER_NCI $NOC_DIR/../../configs/%s/logical/%s_%s' % (config, self.options.product_name, config)])
-     
+
      # Launch appropriate command
      if self.options.external : param_engine_script.extend(["python -B $NOC_SCRIPTING_DIR/noc_param_engine/noc_external_build.py --target=" + str(synth_yaml) + " --output=" + str(rtl_output) + " --report --report_output=" + str(report_output) + " --bundle=" + str(bundle_target) + " --cfg_name=" + str(config_name) + " " + str(validation_opts) + " " + str(colour_opts) + " " + str(clean_opts) + "\n"])
-     else                     : param_engine_script.extend(["python -B $NOC_SCRIPTING_DIR/noc_param_engine/noc_internal_build.py --target=" + str(synth_yaml) + " --output=" + str(rtl_output) + " --report --report_output=" + str(report_output) + " --bundle=" + str(bundle_target) + " --cfg_name=" + str(config_name) + " " + str(validation_opts) + " " + str(colour_opts) + " " + str(clean_opts) + "\n"])
+     else                     : param_engine_script.extend(["python -B $NOC_SCRIPTING_DIR/noc_param_engine/noc_internal_build.py --target=" + str(synth_yaml) + " --output=" + str(rtl_output) + " --report --report_output=" + str(report_output) + " --bundle=" + str(bundle_target) + " --cfg_name=" + str(config_name) + " " + str(validation_opts) + " " + str(colour_opts) + " " + chariot_b_str + " " + str(clean_opts) + "\n"])
 
      # Execute simple HLK check
      if self.options.hlk_check :
diff --git a/logical/shared/scripts/noc_param_engine/noc_core_build.py b/logical/shared/scripts/noc_param_engine/noc_core_build.py
index 9251c8588d3..5a7c9b5e9d6 100755
--- a/logical/shared/scripts/noc_param_engine/noc_core_build.py
+++ b/logical/shared/scripts/noc_param_engine/noc_core_build.py
@@ -74,6 +74,9 @@ class noc_core_build(object) :
     self.hlk_set  = kvarg_default("hlk_set", kwargs, False)
     self.base_hlk = sys.path[0] + "/base_hlk.json"
 
+    # chariot_b boolean
+    self.chariot_b = kvarg_default("chariot_b", kwargs, False)
+
 
     # --- Capture internal file pointers
 
diff --git a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
index 47518a27ca5..6344082e33d 100644
--- a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
+++ b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
@@ -101,7 +101,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
           _fh.write("always @(negedge testbench.u_dut."+instance_name+".u_asni_idm_greybox.gb_sreset_ack) begin\n")
           _fh.write("  $asserton(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI4_ERRS_RDATA_NUM_CHUNKING_ENABLE_RLAST_assert.assert_AXI4_ERRS_RDATA_NUM_CHUNKING_ENABLE_RLAST);\n")
           _fh.write("end\n")
-          
+
 
       # Specific to AXI
       if paramObj["ACE_LITE"] == 0:
@@ -112,14 +112,14 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
           _fh.write("always @(negedge testbench.u_dut."+instance_name+".u_asni_idm_greybox.gb_sreset_ack) begin\n")
           _fh.write("  $asserton(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI5_ERRS_LOOPBACK_BLOOP_assert.assert_AXI5_ERRS_LOOPBACK_BLOOP);\n")
           _fh.write("end\n")
-          
+
           _fh.write("always @(posedge testbench.u_dut."+instance_name+".u_asni_idm_greybox.gb_sreset_req) begin\n")
           _fh.write("  $assertoff(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI5_ERRS_LOOPBACK_RLOOP_assert.assert_AXI5_ERRS_LOOPBACK_RLOOP);\n")
           _fh.write("end\n")
           _fh.write("always @(negedge testbench.u_dut."+instance_name+".u_asni_idm_greybox.gb_sreset_ack) begin\n")
           _fh.write("  $asserton(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI5_ERRS_LOOPBACK_RLOOP_assert.assert_AXI5_ERRS_LOOPBACK_RLOOP);\n")
           _fh.write("end\n")
-        
+
         if paramObj["READ_DATA_CHUNKING"] :
           _fh.write("always @(posedge testbench.u_dut."+instance_name+".u_asni_idm_greybox.gb_sreset_req) begin\n")
           _fh.write("  $assertoff(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI4_ERRS_RDATA_NUM_CHUNKING_ENABLE_RLAST_assert.assert_AXI4_ERRS_RDATA_NUM_CHUNKING_ENABLE_RLAST);\n")
@@ -128,7 +128,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
           _fh.write("  $asserton(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI4_ERRS_RDATA_NUM_CHUNKING_ENABLE_RLAST_assert.assert_AXI4_ERRS_RDATA_NUM_CHUNKING_ENABLE_RLAST);\n")
           _fh.write("end\n")
 
-              
+
         _fh.write("always @(posedge testbench.u_dut."+instance_name+".u_asni_idm_greybox.gb_sreset_req) begin\n")
         _fh.write("  $assertoff(1, testbench.g_interface["+str(interface_index)+"].master.u_if."+pc_path+".g_AXI4_ERRS_BVALID_RESET_assert.assert_AXI4_ERRS_BVALID_RESET);\n")
         _fh.write("end\n")
@@ -215,7 +215,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
   # Close file upon completion
   _fh.close()
 
-def generate_binding(_dataset_file, _cfgname, _output) :
+def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
 
   # Generate configuration file output path
   config_file = _output + "/wrapper_connect.svh"
@@ -350,7 +350,7 @@ def generate_binding(_dataset_file, _cfgname, _output) :
 
       # Handle ordered write observation
       if buildparamObj["axi/orderedWriteObservation"][0] == "Pin" : wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ORDERED_WRITE_OBSERVATION " , "Testbench" : "g_sideband[" + str(clock_index) + "].u_sideband.sb_if_i.ORDERED_WRITE_OBSERVATION_SAR[" + str(domain_index) + "]"})
-    
+
 
 
       wrapper_data["Interface"].append({"Port" :                                  str(export_id) + "_CONFIG_ACCESS             " , "Testbench" : "g_sideband[" + str(clock_index) + "].u_sideband.sb_if_i.CONFIG_SI_ACCESS_SAR[" + str(domain_index) + "]"})
@@ -456,12 +456,16 @@ def generate_binding(_dataset_file, _cfgname, _output) :
 
       # USER WIDTH signals
       if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_AWUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.AWUSER       "})
-      if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_WUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.WUSER        "})
+      if paramObj["USER_DATA_WIDTH"] > 0:
+        if _chariot_b:
+          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_WUSER                    " , "Testbench" : "err_detection_code   "})
+        else:
+          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_WUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.WUSER        "})
       ruser_extra_bits = paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] - paramObj["BUSER_RESP_WIDTH"] # VIP-11616
       if (ruser_extra_bits <=0): # buser_width > ruser_width
         if paramObj["BUSER_RESP_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER        "})
       else:
-        if paramObj["BUSER_RESP_WIDTH"] > 0: 
+        if paramObj["BUSER_RESP_WIDTH"] > 0:
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["BUSER_RESP_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_BUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER = {" + str(ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_BUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_BUSER"})
@@ -469,7 +473,7 @@ def generate_binding(_dataset_file, _cfgname, _output) :
       if (ruser_extra_bits >= 0): # ruser width > buser_width
         if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER        "})
       else:
-        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: 
+        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_RUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER = {" + str(0-ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_RUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_RUSER"})
@@ -862,7 +866,7 @@ def generate_binding(_dataset_file, _cfgname, _output) :
 
   # Iterate over the interfaces
 
-  interface_count = 0 
+  interface_count = 0
 
   for interface in wrapper_data["Interface"] :
 
@@ -921,7 +925,7 @@ def generate_oob_binding(_dataset_file, _cfgname, _output) :
   dataset = load_data_check[2]
 
   # Load JSON interface ordering
-  interface_data = load_json_file(_output + "/interface_mapping.json")[2] 
+  interface_data = load_json_file(_output + "/interface_mapping.json")[2]
 
   # Generate the required configuration data
   configuration_functions.execute_base_function(dataset)
@@ -1129,7 +1133,7 @@ def generate_oob_binding(_dataset_file, _cfgname, _output) :
       if (ruser_extra_bits <=0): # buser_width > ruser_width
         if paramObj["BUSER_RESP_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER        "})
       else:
-        if paramObj["BUSER_RESP_WIDTH"] > 0: 
+        if paramObj["BUSER_RESP_WIDTH"] > 0:
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["BUSER_RESP_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_BUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER = {" + str(ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_BUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_BUSER"})
@@ -1137,7 +1141,7 @@ def generate_oob_binding(_dataset_file, _cfgname, _output) :
       if (ruser_extra_bits >= 0): # ruser width > buser_width
         if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER        "})
       else:
-        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: 
+        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_RUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER = {" + str(0-ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_RUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_RUSER"})
diff --git a/logical/shared/scripts/noc_param_engine/noc_internal_build.py b/logical/shared/scripts/noc_param_engine/noc_internal_build.py
index 589dfe01906..9669432bafb 100755
--- a/logical/shared/scripts/noc_param_engine/noc_internal_build.py
+++ b/logical/shared/scripts/noc_param_engine/noc_internal_build.py
@@ -91,7 +91,7 @@ class noc_internal_build(noc_external_build.noc_external_build) :
     noc_external_bindings.noc_test_configuration.generate_binding(self.connected_rtl_file, self.build_output)
 
     # --- Wrapper generation
-    noc_external_bindings.noc_testbench_wrapper.generate_binding(self.connected_rtl_file, self.build_name, self.build_output)
+    noc_external_bindings.noc_testbench_wrapper.generate_binding(self.connected_rtl_file, self.build_name, self.build_output, self.chariot_b)
     noc_external_bindings.noc_testbench_wrapper.generate_idm_binding(self.connected_rtl_file, self.build_name, self.build_output)
 
     # -- CDC waiver generation
@@ -133,6 +133,7 @@ if __name__ == '__main__':
   parser.add_option("--report"        , dest="report"        , default=False , action="store_true" , help="Enables report generation")
   parser.add_option("--report_output" , dest="report_output" , default=""    , action="store"      , help="Configures the report target directory - if unspecified output is used")
   parser.add_option("--report_colour" , dest="report_colour" , default=False , action="store_true" , help="Enables report colouring on the terminal output - useful visual feedback")
+  parser.add_option("--chariot_b"     , dest="chariot_b"     , default=False , action="store_true" , help="Configures design to add Chariot ASIL B safety mechanisms")
 
   # Parse the arguments
   (options, args) = parser.parse_args()
@@ -143,6 +144,9 @@ if __name__ == '__main__':
   # Append data cleaning action
   kwargs["clean"] = options.clean_build
 
+  # Add chariot_b option
+  kwargs["chariot_b"] = options.chariot_b
+
   # Append reporting functionality
   if options.report :
 
diff --git a/logical/shared/scripts/tooling_scripts/generate_top_summary.pl b/logical/shared/scripts/tooling_scripts/generate_top_summary.pl
index a82dc542748..c14a414af45 100755
--- a/logical/shared/scripts/tooling_scripts/generate_top_summary.pl
+++ b/logical/shared/scripts/tooling_scripts/generate_top_summary.pl
@@ -96,7 +96,9 @@ push(@sim_waivers, ".*Delimiter or last must be observed in response to a disabl
 push(@sim_waivers, ".*read transactions outstanding when OT limit is .*"); # BOOKERNOC-4127
 push(@sim_waivers, ".*Unabled to match master response to order tracker entry.*"); # BOOKERNOC-XXXX CS to file a JIRA
 push(@sim_waivers, "UVM_ERROR :");
+push(@sim_waivers, "UVM_ERROR reports");
 push(@sim_waivers, "UVM_FATAL :");
+push(@sim_waivers, "UVM_FATAL reports");
 
 my @scenario_waivers;
 push(@scenario_waivers, " could not be satisfied"); #waiving the case where we apply a constraint (eg, config must have >1 hsni), and config doesn't
```

## 8452bb85684afd82d80cdc2e90a7d3296dacaf4c

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 8452bb85684afd82d80cdc2e90a7d3296dacaf4c
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Mon Jan 25 18:21:50 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Mon Jan 25 18:21:50 2021 +0000

    Add parity protection for read requests and responses
    Increase number of protected address bits for write and read requests
    
    Change-Id: I756587d03284d565f2e6a5bc1d7c7d866fb79a50

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
index b72b0c85582..bcf18752b04 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
@@ -28,9 +28,8 @@ module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     logic [USER_WIDTH-1:0] err_array;
     logic [USER_WIDTH-1:0] user_expected;
 
-    logic [ADDR_WIDTH-20:0] protectable_value;
-    
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
+    logic [ADDR_WIDTH-10+1:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
     assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
     assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
index 14b5a261929..2055fc82eb8 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
@@ -24,8 +24,8 @@ module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     output [USER_WIDTH-1:0] user_o
 );
 
-    logic [ADDR_WIDTH-20:0] protectable_value; 
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
+    logic [ADDR_WIDTH-10+1:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
     assign user_o = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
 
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 2f83975d237..14cf393f92c 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -108,8 +108,8 @@ module interface_block
               PC_SLAVE_XCHECK_PROPTYPE  = 0,
 
               HSEL_WIDTH                = 1, // REVISIT MB: Need an actual value for this (param)  - Sean Steel's response - we only support one bit at the moment, this is fine
-              EXTENDED_MEMORY_TYPES     = 0, 
-              AHB_MIRROR                = 0, 
+              EXTENDED_MEMORY_TYPES     = 0,
+              AHB_MIRROR                = 0,
 
               IDM_SUPPORT               = 0
   )
@@ -146,7 +146,7 @@ module interface_block
   //delying sreset going to xsni by 1 cycle
   assign ARESETn_final =  ((IDM_SUPPORT) && (DEVICE == generic_types::DEVICE__MASTER))?(ARESETn & sreset_delayed):ARESETn;
   assign AHB_RESETn_final =  ((IDM_SUPPORT) && (DEVICE == generic_types::DEVICE__MASTER))?(AHB_RESETn & SRESETn):AHB_RESETn;
-  
+
 
   logic [COV_AWUSER_WIDTH-1:0] cov_awuser;
   logic                        cov_awvalid;
@@ -700,10 +700,13 @@ module interface_block
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
+                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
+                      logic [ARUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
                         logic parity_err_wrsp;
-                        assign parity_error = parity_err_wrsp;
+                        logic parity_err_rrsp;
+                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -715,15 +718,27 @@ module interface_block
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
                         );
+                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i (u_if.ARUSER),
+                          .nonsec_i (u_if.ARPROT[1]),
+                          .user_o (rreq_err_code)
+                        );
                         chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
                           .valid_i (u_if.BVALID),
                           .user_i  (u_if.BUSER),
                           .error_o (parity_err_wrsp)
                         );
+                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
+                          .valid_i (u_if.RVALID),
+                          .user_i  (u_if.RUSER),
+                          .error_o (parity_err_rrsp)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
+                        logic parity_err_rreq;
                         logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat;
+                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -738,9 +753,19 @@ module interface_block
                           .valid_i (u_if.AWVALID),
                           .error_o (parity_err_wreq)
                         );
+                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i  (u_if.ARUSER),
+                          .nonsec_i  (u_if.ARPROT[1]),
+                          .valid_i (u_if.ARVALID),
+                          .error_o (parity_err_rreq)
+                        );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
                           .user_o (wrsp_err_code)
                         );
+                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
+                          .user_o (rrsp_err_code)
+                        );
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_ace4_lite
@@ -1177,10 +1202,13 @@ module interface_block
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
+                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
+                      logic [ARUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
                         logic parity_err_wrsp;
-                        assign parity_error = parity_err_wrsp;
+                        logic parity_err_rrsp;
+                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -1192,15 +1220,27 @@ module interface_block
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
                         );
+                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i (u_if.ARUSER),
+                          .nonsec_i (u_if.ARPROT[1]),
+                          .user_o (rreq_err_code)
+                        );
                         chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
                           .valid_i (u_if.BVALID),
                           .user_i  (u_if.BUSER),
                           .error_o (parity_err_wrsp)
                         );
+                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
+                          .valid_i (u_if.RVALID),
+                          .user_i  (u_if.RUSER),
+                          .error_o (parity_err_rrsp)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
+                        logic parity_err_rreq;
                         logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat;
+                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -1215,9 +1255,19 @@ module interface_block
                           .valid_i (u_if.AWVALID),
                           .error_o (parity_err_wreq)
                         );
+                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i  (u_if.ARUSER),
+                          .nonsec_i  (u_if.ARPROT[1]),
+                          .valid_i (u_if.ARVALID),
+                          .error_o (parity_err_rreq)
+                        );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
                           .user_o (wrsp_err_code)
                         );
+                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
+                          .user_o (rrsp_err_code)
+                        );
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_axi4
@@ -1326,13 +1376,13 @@ module interface_block
          end
 	else begin
          ahb_mirror : assert property(@(posedge ACLK)
-           (u_if.HREADY == u_if.HREADYOUT)) 
+           (u_if.HREADY == u_if.HREADYOUT))
          else  `uvm_error(
                                 "AHB_MIRROR",
                                 "Hready is not eqaul to Hreadyout"
                               );
          end
-         
+
       end
 
       // Create the applicable virtual interface wrapper and add it to the
@@ -1341,10 +1391,10 @@ module interface_block
       begin
         //vip_ahb5_if_wrapper       vif_wrapper;
         //typedef virtual vip_ahb5_uvm_interface vip_ahb5_uvm_vif;
-	//8.2 of AHB-C spec: AHB Issue B recommends that: slaves do not insert more than 16 wait states, to prevent any single access locking the bus for a large number of clock cycles.In the case of multi-layer interconnects and when bridging to other protocols, this recommendation can easily be exceeded without system impact. It is proposed that this recommendation is removed from the specification, and replaced with a note that excessive numbers of wait states might impact system performance 
+	//8.2 of AHB-C spec: AHB Issue B recommends that: slaves do not insert more than 16 wait states, to prevent any single access locking the bus for a large number of clock cycles.In the case of multi-layer interconnects and when bridging to other protocols, this recommendation can easily be exceeded without system impact. It is proposed that this recommendation is removed from the specification, and replaced with a note that excessive numbers of wait states might impact system performance
        //Below assertion won't exist unless (PROTOCOL_VERSION == 0) so AHB3-Lite is enabled on PC
 
-        //REVISIT Enable below assertion for AHB3-LITE when we test it 
+        //REVISIT Enable below assertion for AHB3-LITE when we test it
 	// $assertoff(1, u_pc.AHB_RECS_HREADYOUT_MAX.assert_AHB_RECS_HREADYOUT_MAX);
         // Add the virtual interface to the uvm_config_db
         uvm_config_db#(vip_ahb5_uvm_vif)::set(
@@ -1400,7 +1450,6 @@ module interface_block
       `ifdef CHARIOT_ASIL_B
         logic [WUSER_WIDTH-1:0]  wdat_err_code;
         logic [AWUSER_WIDTH-1:0] wreq_err_code;
-        logic [AWUSER_WIDTH-1:0] wrsp_err_code;
         logic [DATA_WIDTH/8-1:0] strobe; //strobe not part of the ahb protocol, so we generate it here
 
         chariot_ahb_strobe_generation #(.DATA_WIDTH(DATA_WIDTH), .ADDR_WIDTH(ADDR_WIDTH)) strobe_gen (
@@ -1433,8 +1482,8 @@ module interface_block
           assign parity_error = parity_err_wreq | parity_err_wdat;
           chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
             .data_i  (u_if.HWDATA),
-            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent 
-            .strb_i  (strobe), // 
+            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
+            .strb_i  (strobe), //
             .user_i  (u_if.HWUSER),
             .error_o (parity_err_wdat)
           );
@@ -1442,7 +1491,7 @@ module interface_block
             .addr_i   (u_if.HADDR),
             .user_i   (u_if.HAUSER),
             .nonsec_i (u_if.HNONSEC),
-            .valid_i  (u_if.HREADY && u_if.HTRANS[1] && u_if.HWRITE),
+            .valid_i  (u_if.HREADY && u_if.HTRANS[1]),
             .error_o  (parity_err_wreq)
           );
         end
@@ -1492,7 +1541,7 @@ module interface_block
        .PADDR                       (u_if.PADDR        ),
        //.PPROT                       (if (SECURE_TRANSFERS == 1) ? u_if.PPROT : (if (SECURE_TRANSFERS == 3) ?  1 : 0)),
        //.PPROT                       ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? ((SECURE_TRANSFERS == 1) & u_if.PPROT)  : 0), //PPROT not present in APB3
-       .PPROT                       ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? u_if.PPROT  : 0), //PPROT not present in APB3 , removing above SECURE_TRANSFER condition as PPROT will be always present in  BOOKER NCI 2522 jira. 
+       .PPROT                       ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? u_if.PPROT  : 0), //PPROT not present in APB3 , removing above SECURE_TRANSFER condition as PPROT will be always present in  BOOKER NCI 2522 jira.
        .PSELx                       (u_if.PSEL         ),
        .PENABLE                     (u_if.PENABLE      ),
        .PWRITE                      (u_if.PWRITE       ),
diff --git a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
index 52c6ad86c33..e7524cc5ae1 100644
--- a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
+++ b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
@@ -64,7 +64,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
     instance_name = instanceObj["componentInfo"]["instanceName"]
     instanceLinks = instanceObj["componentMisc"]["instance_links"]
     buildDataObj  = instanceObj["componentMisc"]["build_data"]
-    
+
     #if instance_type == "noc_hmni_core" and paramObj["IDM_SUPPORT"]:
     #  instance_name = ".".join(instance.split("/"))
     #  _fh.write("always @(posedge testbench.u_dut."+instance_name+".u_hmni_adaptor.u_hmni_idm_greybox.gb_sreset_req) begin\n")
@@ -81,7 +81,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
     #  _fh.write("end\n")
     if instance_type == "arachne_hsni_core" and paramObj["IDM_SUPPORT"]:
       _fh.write("assign sreset_control["+str(interface_index)+"] = 0;\n")
-               
+
 
     if instance_type == "arachne_asni_axi_core" and paramObj["IDM_SUPPORT"]:
       instance_name = ".".join(instance.split("/"))
@@ -514,14 +514,18 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_WUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.WUSER        "})
       ruser_extra_bits = paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] - paramObj["BUSER_RESP_WIDTH"] # VIP-11616
       if (ruser_extra_bits <=0): # buser_width > ruser_width
-        if paramObj["BUSER_RESP_WIDTH"] > 0: 
+        if paramObj["BUSER_RESP_WIDTH"] > 0:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER        "})
       else:
         if paramObj["BUSER_RESP_WIDTH"] > 0:
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["BUSER_RESP_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_BUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER = {" + str(ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_BUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_BUSER"})
-      if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
+      if paramObj["USER_REQ_WIDTH"] > 0:
+        if _chariot_b:
+          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".rreq_err_code     "})
+        else:
+          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
       if (ruser_extra_bits >= 0): # ruser width > buser_width
         if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER        "})
       else:
@@ -634,13 +638,13 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HAUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wreq_err_code   "})
         else:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HAUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HAUSER     "})
-          
-      if paramObj["USER_DATA_WIDTH"] > 0: 
+
+      if paramObj["USER_DATA_WIDTH"] > 0:
         if _chariot_b:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HWUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wdat_err_code  "})
         else:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HWUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HWUSER     "})
-        
+
       if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HRUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HRUSER     "})
 
 
@@ -770,13 +774,17 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_BUSER        " , "Testbench" : " amni_" + str(interface_index) + "_BUSER    "})
       if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_ARUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.ARUSER       "})
       # if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
-      if (ruser_extra_bits >= 0): # ruser width > buser_width
-        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
+      if _chariot_b:
+        if (ruser_extra_bits >= 0): # ruser width > buser_width
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rrsp_err_code     "})
       else:
-        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
-          wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0] amni_" + str(interface_index) + "_RUSER;\n")
-          wrapper_data["AHB_User_Bits"].append("assign amni_" + str(interface_index) + "_RUSER = g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER[" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0];\n")
-          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "amni_" + str(interface_index) + "_RUSER"})
+        if (ruser_extra_bits >= 0): # ruser width > buser_width
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
+        else:
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
+            wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0] amni_" + str(interface_index) + "_RUSER;\n")
+            wrapper_data["AHB_User_Bits"].append("assign amni_" + str(interface_index) + "_RUSER = g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER[" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0];\n")
+            wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "amni_" + str(interface_index) + "_RUSER"})
 
       # IDM soft reset signals
       if paramObj["IDM_SUPPORT"] :
```

## 41d2221e7973c21437e040d51dbe75cbf73ed3c0

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 41d2221e7973c21437e040d51dbe75cbf73ed3c0
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Thu Jan 28 17:05:15 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Fri Jan 29 17:15:00 2021 +0000

    Revert "Revert "Add parity protection for read requests and responses""
    
    This reverts commit 99937b8c02a02511fba7c67e602dce610aca453e.
    
    Change-Id: Ifae733006c4d5572fc72bee8cec1b379ac6473b3

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
index b72b0c85582..bcf18752b04 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
@@ -28,9 +28,8 @@ module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     logic [USER_WIDTH-1:0] err_array;
     logic [USER_WIDTH-1:0] user_expected;
 
-    logic [ADDR_WIDTH-20:0] protectable_value;
-    
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
+    logic [ADDR_WIDTH-10+1:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
     assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
     assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
index 14b5a261929..2055fc82eb8 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
@@ -24,8 +24,8 @@ module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     output [USER_WIDTH-1:0] user_o
 );
 
-    logic [ADDR_WIDTH-20:0] protectable_value; 
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
+    logic [ADDR_WIDTH-10+1:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
     assign user_o = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
 
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 2f83975d237..14cf393f92c 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -108,8 +108,8 @@ module interface_block
               PC_SLAVE_XCHECK_PROPTYPE  = 0,
 
               HSEL_WIDTH                = 1, // REVISIT MB: Need an actual value for this (param)  - Sean Steel's response - we only support one bit at the moment, this is fine
-              EXTENDED_MEMORY_TYPES     = 0, 
-              AHB_MIRROR                = 0, 
+              EXTENDED_MEMORY_TYPES     = 0,
+              AHB_MIRROR                = 0,
 
               IDM_SUPPORT               = 0
   )
@@ -146,7 +146,7 @@ module interface_block
   //delying sreset going to xsni by 1 cycle
   assign ARESETn_final =  ((IDM_SUPPORT) && (DEVICE == generic_types::DEVICE__MASTER))?(ARESETn & sreset_delayed):ARESETn;
   assign AHB_RESETn_final =  ((IDM_SUPPORT) && (DEVICE == generic_types::DEVICE__MASTER))?(AHB_RESETn & SRESETn):AHB_RESETn;
-  
+
 
   logic [COV_AWUSER_WIDTH-1:0] cov_awuser;
   logic                        cov_awvalid;
@@ -700,10 +700,13 @@ module interface_block
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
+                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
+                      logic [ARUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
                         logic parity_err_wrsp;
-                        assign parity_error = parity_err_wrsp;
+                        logic parity_err_rrsp;
+                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -715,15 +718,27 @@ module interface_block
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
                         );
+                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i (u_if.ARUSER),
+                          .nonsec_i (u_if.ARPROT[1]),
+                          .user_o (rreq_err_code)
+                        );
                         chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
                           .valid_i (u_if.BVALID),
                           .user_i  (u_if.BUSER),
                           .error_o (parity_err_wrsp)
                         );
+                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
+                          .valid_i (u_if.RVALID),
+                          .user_i  (u_if.RUSER),
+                          .error_o (parity_err_rrsp)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
+                        logic parity_err_rreq;
                         logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat;
+                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -738,9 +753,19 @@ module interface_block
                           .valid_i (u_if.AWVALID),
                           .error_o (parity_err_wreq)
                         );
+                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i  (u_if.ARUSER),
+                          .nonsec_i  (u_if.ARPROT[1]),
+                          .valid_i (u_if.ARVALID),
+                          .error_o (parity_err_rreq)
+                        );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
                           .user_o (wrsp_err_code)
                         );
+                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
+                          .user_o (rrsp_err_code)
+                        );
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_ace4_lite
@@ -1177,10 +1202,13 @@ module interface_block
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
+                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
+                      logic [ARUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
                         logic parity_err_wrsp;
-                        assign parity_error = parity_err_wrsp;
+                        logic parity_err_rrsp;
+                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -1192,15 +1220,27 @@ module interface_block
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
                         );
+                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i (u_if.ARUSER),
+                          .nonsec_i (u_if.ARPROT[1]),
+                          .user_o (rreq_err_code)
+                        );
                         chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
                           .valid_i (u_if.BVALID),
                           .user_i  (u_if.BUSER),
                           .error_o (parity_err_wrsp)
                         );
+                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
+                          .valid_i (u_if.RVALID),
+                          .user_i  (u_if.RUSER),
+                          .error_o (parity_err_rrsp)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
+                        logic parity_err_rreq;
                         logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat;
+                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -1215,9 +1255,19 @@ module interface_block
                           .valid_i (u_if.AWVALID),
                           .error_o (parity_err_wreq)
                         );
+                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
+                          .addr_i  (u_if.ARADDR),
+                          .user_i  (u_if.ARUSER),
+                          .nonsec_i  (u_if.ARPROT[1]),
+                          .valid_i (u_if.ARVALID),
+                          .error_o (parity_err_rreq)
+                        );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
                           .user_o (wrsp_err_code)
                         );
+                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
+                          .user_o (rrsp_err_code)
+                        );
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_axi4
@@ -1326,13 +1376,13 @@ module interface_block
          end
 	else begin
          ahb_mirror : assert property(@(posedge ACLK)
-           (u_if.HREADY == u_if.HREADYOUT)) 
+           (u_if.HREADY == u_if.HREADYOUT))
          else  `uvm_error(
                                 "AHB_MIRROR",
                                 "Hready is not eqaul to Hreadyout"
                               );
          end
-         
+
       end
 
       // Create the applicable virtual interface wrapper and add it to the
@@ -1341,10 +1391,10 @@ module interface_block
       begin
         //vip_ahb5_if_wrapper       vif_wrapper;
         //typedef virtual vip_ahb5_uvm_interface vip_ahb5_uvm_vif;
-	//8.2 of AHB-C spec: AHB Issue B recommends that: slaves do not insert more than 16 wait states, to prevent any single access locking the bus for a large number of clock cycles.In the case of multi-layer interconnects and when bridging to other protocols, this recommendation can easily be exceeded without system impact. It is proposed that this recommendation is removed from the specification, and replaced with a note that excessive numbers of wait states might impact system performance 
+	//8.2 of AHB-C spec: AHB Issue B recommends that: slaves do not insert more than 16 wait states, to prevent any single access locking the bus for a large number of clock cycles.In the case of multi-layer interconnects and when bridging to other protocols, this recommendation can easily be exceeded without system impact. It is proposed that this recommendation is removed from the specification, and replaced with a note that excessive numbers of wait states might impact system performance
        //Below assertion won't exist unless (PROTOCOL_VERSION == 0) so AHB3-Lite is enabled on PC
 
-        //REVISIT Enable below assertion for AHB3-LITE when we test it 
+        //REVISIT Enable below assertion for AHB3-LITE when we test it
 	// $assertoff(1, u_pc.AHB_RECS_HREADYOUT_MAX.assert_AHB_RECS_HREADYOUT_MAX);
         // Add the virtual interface to the uvm_config_db
         uvm_config_db#(vip_ahb5_uvm_vif)::set(
@@ -1400,7 +1450,6 @@ module interface_block
       `ifdef CHARIOT_ASIL_B
         logic [WUSER_WIDTH-1:0]  wdat_err_code;
         logic [AWUSER_WIDTH-1:0] wreq_err_code;
-        logic [AWUSER_WIDTH-1:0] wrsp_err_code;
         logic [DATA_WIDTH/8-1:0] strobe; //strobe not part of the ahb protocol, so we generate it here
 
         chariot_ahb_strobe_generation #(.DATA_WIDTH(DATA_WIDTH), .ADDR_WIDTH(ADDR_WIDTH)) strobe_gen (
@@ -1433,8 +1482,8 @@ module interface_block
           assign parity_error = parity_err_wreq | parity_err_wdat;
           chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
             .data_i  (u_if.HWDATA),
-            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent 
-            .strb_i  (strobe), // 
+            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
+            .strb_i  (strobe), //
             .user_i  (u_if.HWUSER),
             .error_o (parity_err_wdat)
           );
@@ -1442,7 +1491,7 @@ module interface_block
             .addr_i   (u_if.HADDR),
             .user_i   (u_if.HAUSER),
             .nonsec_i (u_if.HNONSEC),
-            .valid_i  (u_if.HREADY && u_if.HTRANS[1] && u_if.HWRITE),
+            .valid_i  (u_if.HREADY && u_if.HTRANS[1]),
             .error_o  (parity_err_wreq)
           );
         end
@@ -1492,7 +1541,7 @@ module interface_block
        .PADDR                       (u_if.PADDR        ),
        //.PPROT                       (if (SECURE_TRANSFERS == 1) ? u_if.PPROT : (if (SECURE_TRANSFERS == 3) ?  1 : 0)),
        //.PPROT                       ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? ((SECURE_TRANSFERS == 1) & u_if.PPROT)  : 0), //PPROT not present in APB3
-       .PPROT                       ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? u_if.PPROT  : 0), //PPROT not present in APB3 , removing above SECURE_TRANSFER condition as PPROT will be always present in  BOOKER NCI 2522 jira. 
+       .PPROT                       ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? u_if.PPROT  : 0), //PPROT not present in APB3 , removing above SECURE_TRANSFER condition as PPROT will be always present in  BOOKER NCI 2522 jira.
        .PSELx                       (u_if.PSEL         ),
        .PENABLE                     (u_if.PENABLE      ),
        .PWRITE                      (u_if.PWRITE       ),
diff --git a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
index 52c6ad86c33..e7524cc5ae1 100644
--- a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
+++ b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
@@ -64,7 +64,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
     instance_name = instanceObj["componentInfo"]["instanceName"]
     instanceLinks = instanceObj["componentMisc"]["instance_links"]
     buildDataObj  = instanceObj["componentMisc"]["build_data"]
-    
+
     #if instance_type == "noc_hmni_core" and paramObj["IDM_SUPPORT"]:
     #  instance_name = ".".join(instance.split("/"))
     #  _fh.write("always @(posedge testbench.u_dut."+instance_name+".u_hmni_adaptor.u_hmni_idm_greybox.gb_sreset_req) begin\n")
@@ -81,7 +81,7 @@ def generate_idm_binding(_dataset_file, _cfgname, _output) :
     #  _fh.write("end\n")
     if instance_type == "arachne_hsni_core" and paramObj["IDM_SUPPORT"]:
       _fh.write("assign sreset_control["+str(interface_index)+"] = 0;\n")
-               
+
 
     if instance_type == "arachne_asni_axi_core" and paramObj["IDM_SUPPORT"]:
       instance_name = ".".join(instance.split("/"))
@@ -514,14 +514,18 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_WUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.WUSER        "})
       ruser_extra_bits = paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] - paramObj["BUSER_RESP_WIDTH"] # VIP-11616
       if (ruser_extra_bits <=0): # buser_width > ruser_width
-        if paramObj["BUSER_RESP_WIDTH"] > 0: 
+        if paramObj["BUSER_RESP_WIDTH"] > 0:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER        "})
       else:
         if paramObj["BUSER_RESP_WIDTH"] > 0:
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["BUSER_RESP_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_BUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER = {" + str(ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_BUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_BUSER"})
-      if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
+      if paramObj["USER_REQ_WIDTH"] > 0:
+        if _chariot_b:
+          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".rreq_err_code     "})
+        else:
+          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
       if (ruser_extra_bits >= 0): # ruser width > buser_width
         if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER        "})
       else:
@@ -634,13 +638,13 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HAUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wreq_err_code   "})
         else:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HAUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HAUSER     "})
-          
-      if paramObj["USER_DATA_WIDTH"] > 0: 
+
+      if paramObj["USER_DATA_WIDTH"] > 0:
         if _chariot_b:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HWUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wdat_err_code  "})
         else:
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HWUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HWUSER     "})
-        
+
       if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HRUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HRUSER     "})
 
 
@@ -770,13 +774,17 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_BUSER        " , "Testbench" : " amni_" + str(interface_index) + "_BUSER    "})
       if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_ARUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.ARUSER       "})
       # if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
-      if (ruser_extra_bits >= 0): # ruser width > buser_width
-        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
+      if _chariot_b:
+        if (ruser_extra_bits >= 0): # ruser width > buser_width
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rrsp_err_code     "})
       else:
-        if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
-          wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0] amni_" + str(interface_index) + "_RUSER;\n")
-          wrapper_data["AHB_User_Bits"].append("assign amni_" + str(interface_index) + "_RUSER = g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER[" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0];\n")
-          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "amni_" + str(interface_index) + "_RUSER"})
+        if (ruser_extra_bits >= 0): # ruser width > buser_width
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
+        else:
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
+            wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0] amni_" + str(interface_index) + "_RUSER;\n")
+            wrapper_data["AHB_User_Bits"].append("assign amni_" + str(interface_index) + "_RUSER = g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER[" + str(paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"]-1) + ":0];\n")
+            wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "amni_" + str(interface_index) + "_RUSER"})
 
       # IDM soft reset signals
       if paramObj["IDM_SUPPORT"] :
```

## 0061d5b19fa53c919287bfa6ccc9150edba032df

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 0061d5b19fa53c919287bfa6ccc9150edba032df
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Fri Jan 29 16:34:51 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Fri Jan 29 17:15:01 2021 +0000

    Reduce number of protected address bits to 21
    
    Change-Id: I0f88005b6cc1ad8833a99ef9ce9a7ad387b124b1

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
index bcf18752b04..89f2cac2c35 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
@@ -28,8 +28,8 @@ module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     logic [USER_WIDTH-1:0] err_array;
     logic [USER_WIDTH-1:0] user_expected;
 
-    logic [ADDR_WIDTH-10+1:0] protectable_value;
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
+    logic [ADDR_WIDTH-12:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:10]};
     assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
     assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
index 2055fc82eb8..b026dc298d4 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
@@ -24,8 +24,8 @@ module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     output [USER_WIDTH-1:0] user_o
 );
 
-    logic [ADDR_WIDTH-10+1:0] protectable_value;
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
+    logic [ADDR_WIDTH-12:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:10]};
     assign user_o = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
 
 endmodule
```

## ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Fri Jan 29 20:24:33 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Sat Feb 6 01:05:14 2021 +0000

    Add rdat parity generation and checker. 2 bits of user (1 valid bit, 1 parity bit) per 8 bits of data for both
    AXI and AHB.
    Set the 'invalid_byte_lanes_mode' on the transaction
    item in the testbench to 'INVALID_BYTE_LANES_RANDOM' to send random 0s and 1s instead of Xs for invalid read
    data.
    
    Change-Id: I74d4eb9a8e8772d5e1d70f014a01c78acf099565

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
index 244a1c91f53..7bccc2255d6 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
@@ -26,10 +26,11 @@
 `include "chariot_wrsp_parity_generator.sv"
 `include "chariot_wrsp_parity_checker.sv"
 `include "chariot_ahb_strobe_generation.sv"
+`include "chariot_rdat_parity_generator.sv"
+`include "chariot_rdat_parity_checker.sv"
 
 package chariot_pkg;
 
-
 endpackage
 
 `endif
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_checker.sv
new file mode 100644
index 00000000000..a25278f0a33
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_checker.sv
@@ -0,0 +1,39 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot read data channel parity checker
+//           This channel also carries the read response which is not yet protected
+//------------------------------------------------------------------------------
+module chariot_rdat_parity_checker #(DATA_WIDTH = -1, USER_WIDTH = -1, RESP_WIDTH = -1, NUM_SAFETY_BITS = -1) (
+  input [DATA_WIDTH-1:0] data_i,
+  input valid_i,
+  input [USER_WIDTH+RESP_WIDTH-1:0] user_i,
+  output error_o
+);
+
+  localparam BITS_TO_PARITY = 4 * NUM_SAFETY_BITS;
+  localparam DATA_SIZE = DATA_WIDTH / BITS_TO_PARITY;
+  logic [DATA_SIZE-1:0] parity_check;
+
+  genvar i;
+  generate
+    for (i=0; i<DATA_SIZE; i=i+1) begin
+      assign parity_check[i] = (user_i[(i*NUM_SAFETY_BITS)+(NUM_SAFETY_BITS-1)+RESP_WIDTH] == 0) ? 0 :
+        ((~^data_i[(i*BITS_TO_PARITY)+(BITS_TO_PARITY-1):i*BITS_TO_PARITY]) == (user_i[i*NUM_SAFETY_BITS+RESP_WIDTH])) ? 0 : 1;
+    end
+  endgenerate
+
+  assign error_o = (|parity_check) & valid_i;
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_generator.sv
new file mode 100644
index 00000000000..b652a1c1f94
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_generator.sv
@@ -0,0 +1,35 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot read data channel parity generation
+//           This channel also carries the read response which is not yet protected
+//------------------------------------------------------------------------------
+module chariot_rdat_parity_generator #(DATA_WIDTH = -1, USER_WIDTH = -1, RESP_WIDTH = -1, NUM_SAFETY_BITS = -1) (
+  input [DATA_WIDTH-1:0] data_i,
+  input valid_i,
+  output [USER_WIDTH-1:0] user_o
+);
+
+  localparam BITS_TO_PARITY = 4 * NUM_SAFETY_BITS;
+  localparam DATA_SIZE = DATA_WIDTH / BITS_TO_PARITY;
+
+  genvar i;
+  generate
+    for (i=0; i<DATA_SIZE; i=i+1) begin
+      assign user_o[(i*NUM_SAFETY_BITS)+(NUM_SAFETY_BITS-1):(i*NUM_SAFETY_BITS)] = {{1'b1},{(NUM_SAFETY_BITS-2){1'b0}},{~^data_i[(i*BITS_TO_PARITY)+(BITS_TO_PARITY-1):i*BITS_TO_PARITY]}};
+    end
+  endgenerate
+
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/slaves/amba5_slave_controller_component.svh b/logical/noc_arachne/validation/dynamic/top/components/slaves/amba5_slave_controller_component.svh
index 78aa4dec9ee..47f87e6ed8e 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/slaves/amba5_slave_controller_component.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/slaves/amba5_slave_controller_component.svh
@@ -205,7 +205,7 @@ class amba5_slave_controller_component extends generic_controller_component;
   vip_ace5_transaction_item                      rd_reqs[$];
 
   event                                          rd_driven;
-  event                                          wr_driven; 
+  event                                          wr_driven;
   vip_ace5_transaction_item                      pending_responses[vip_ace5_types::txn_type_t][int unsigned][$];
   b_response_type                                required_b_resp[int unsigned][$];
 
@@ -367,7 +367,7 @@ class amba5_slave_controller_component extends generic_controller_component;
     cfg = _cfg;
     vif = _vif;
 
-    
+
 
     vif_util = ace5_interface_utilities::type_id::create("vif_util", this);
     vif_util.configure(vif, 1'b0);
@@ -440,7 +440,7 @@ class amba5_slave_controller_component extends generic_controller_component;
     // dependency components
     slave_dependencies = amba5_slave_dependency_component::type_id::create("dependencies", this);
     slave_dependencies.configure(cfg.dependencies);
-    dependencies.push_back(slave_dependencies);    
+    dependencies.push_back(slave_dependencies);
 
     // Set VARQOSACCEPT and VAWQOSACCEPT control knobs to values from
     // configuration class
@@ -583,15 +583,15 @@ class amba5_slave_controller_component extends generic_controller_component;
 
               // Model whether the slave is powered up
               manage_power();
-              
-              //trigger event for processing wr reqs 
+
+              //trigger event for processing wr reqs
               req_event_triggering(WR_REQ_REG_ID);
-              
-              //trigger event for processing wr reqs 
+
+              //trigger event for processing wr reqs
               req_event_triggering(RD_REQ_REG_ID);
 
               // Drive the values of VARQOSACCEPT and VAWQOSACCEPT
-              manage_vaxqosaccept(VARQOSACCEPT_ID); 
+              manage_vaxqosaccept(VARQOSACCEPT_ID);
               manage_vaxqosaccept(VAWQOSACCEPT_ID);
 
             join
@@ -640,7 +640,7 @@ class amba5_slave_controller_component extends generic_controller_component;
         end join
       end
     join_none
-  
+
     /*if (1) begin
       forever
       begin
@@ -738,7 +738,7 @@ class amba5_slave_controller_component extends generic_controller_component;
             "AMBA5 SLAVE CONTROLLER COMPONENT",
             "Failed to randomize ar_rdy_long_delay."
           )
-        end 
+        end
 
         if(arready_idm_stall) begin
             delay = 10000;
@@ -795,7 +795,7 @@ class amba5_slave_controller_component extends generic_controller_component;
               wl_ot++;
               wr_ot++;
               wr_start.trigger();
-            end 
+            end
             else
             begin
               if (aw_ot++ == wr_ot)
@@ -811,7 +811,7 @@ class amba5_slave_controller_component extends generic_controller_component;
           end
           W_RDY_DLY_ID:
           begin
-            if (vif.WIntf.channel_xlast) 
+            if (vif.WIntf.channel_xlast)
               wl_ot++;
             if (vif.WIntf.channel_xlast ? (wl_ot >  wr_ot)
                                         : (wl_ot == wr_ot) )
@@ -825,7 +825,7 @@ class amba5_slave_controller_component extends generic_controller_component;
               rd_ot++;
           end
         endcase
-        
+
         if(!mid_sim_reset_seen) begin
             // Inform the top dependencies a transaction has started
             for (int unsigned i = 0; i < dependencies.size(); ++i) begin
@@ -969,7 +969,7 @@ class amba5_slave_controller_component extends generic_controller_component;
         if (wnr) begin
           wr_reqs.delete(req_sel);
           `uvm_info("AMBA5 SLAVE CONTROLLER COMPONENT", $sformatf("stage3a: deleted wr req from wr_reqs queue for request::uid=0x%h  axaddr=0x%h axid=0x%h ",req.get_transaction_uid(), req.axaddr, req.axid) , UVM_DEBUG)
-        end  
+        end
         else
           rd_reqs.delete(req_sel);
         // If not randomly ordering responses, wait until the response has been
@@ -1004,7 +1004,7 @@ class amba5_slave_controller_component extends generic_controller_component;
           create_timing_control_knobs.set_timing_response_delay_min(10000);
           create_timing_control_knobs.set_timing_response_delay_max(10000);
           `uvm_info("AMBA5 SLAVE CONTROLLER COMPONENT", $sformatf("In generate_response setting bchannel time out conditions for for request::uid=0x%h  axaddr=0x%h axid=0x%h ",rsp.get_transaction_uid(), rsp.axaddr, rsp.axid) , UVM_DEBUG)
-        end 
+        end
         else if (wr_rsp_long_delay)
         begin
           create_timing_control_knobs.set_timing_response_delay_min(cfg.get_wr_rsp_long_delay_min());
@@ -1019,12 +1019,12 @@ class amba5_slave_controller_component extends generic_controller_component;
                                           cfg.get_wr_rsp_delay_max() ,
                                           cfg.get_wr_rsp_delay_mean(),
                                           cfg.get_wr_rsp_delay_sd()
-                                        ) 
+                                        )
           );
           create_timing_control_knobs.set_timing_response_delay_max(create_timing_control_knobs.get_timing_response_delay_min());
           if (rsp.is_atomic_transaction_with_read()) begin
 
-            // delay between aw finishing and first beat of atomic read should be same as normal reads 
+            // delay between aw finishing and first beat of atomic read should be same as normal reads
             if (!randomize(rd_rsp_long_delay))
               `uvm_error("AMBA5 SLAVE CONTROLLER COMPONENT", "Failed to randomize rd_rsp_long_delay.")
             if(rvalid_idm_stall) begin
@@ -1050,7 +1050,7 @@ class amba5_slave_controller_component extends generic_controller_component;
               );
               create_timing_control_knobs.set_timing_first_secondary_data_delay_max(create_timing_control_knobs.get_timing_first_secondary_data_delay_min());
             end
-            
+
             // atomic rd inter data delay
             create_timing_control_knobs.set_timing_inter_secondary_data_delay_min(
               generic_utils::dist_in_range( cfg.get_rd_rsp_delay_dist(),
@@ -1059,7 +1059,7 @@ class amba5_slave_controller_component extends generic_controller_component;
                                             cfg.get_rd_rsp_delay_max() ,
                                             cfg.get_rd_rsp_delay_mean(),
                                             cfg.get_rd_rsp_delay_sd()
-                                          ) 
+                                          )
             );
             create_timing_control_knobs.set_timing_inter_secondary_data_delay_max(create_timing_control_knobs.get_timing_inter_secondary_data_delay_min());
           end
@@ -1134,6 +1134,8 @@ class amba5_slave_controller_component extends generic_controller_component;
     vip_ace5_timing_control_knobs             timing_control_knobs;
     bit skip_queue_update;
 
+    rsp.set_invalid_byte_lanes_mode(vip_ace5_types::INVALID_BYTE_LANES_RANDOM);
+
     `uvm_info("AMBA5 SLAVE CONTROLLER COMPONENT", $sformatf("stage4: In task generate_response  for request::uid=0x%h  axaddr=0x%h axid=0x%h ",rsp.get_transaction_uid(), rsp.axaddr, rsp.axid) , UVM_DEBUG)
     // Get permission to access shared resource
     super.get_order(p_id, p);
@@ -1246,7 +1248,7 @@ class amba5_slave_controller_component extends generic_controller_component;
               end
             end
           endcase
-        end 
+        end
         else if (req.is_atomic_transaction()) begin
           randcase
             cfg.get_rd_atom_rresp_all_same_chance_ptt() :
@@ -1274,7 +1276,7 @@ class amba5_slave_controller_component extends generic_controller_component;
               end
             end
           endcase
-        end 
+        end
         else begin
           randcase
             cfg.get_rd_rresp_all_same_chance_ptt() :
@@ -1457,12 +1459,12 @@ class amba5_slave_controller_component extends generic_controller_component;
       if (req.get_txn_type() == vip_ace5_types::WRITE_TRANSACTION) begin
         b_response_type tmp = new();
 
-        if ( (rsp.get_axsnoop() inside {vip_ace5_types::AWSNOOP_CMO, vip_ace5_types::AWSNOOP_WRITE_PARTIAL_CMO, vip_ace5_types::AWSNOOP_WRITE_FULL_CMO}) && 
-             (rsp.get_write_cmo_operation() inside {vip_ace5_types::AWCMO_CLEAN_SHARED_PERSIST, vip_ace5_types::AWCMO_CLEAN_SHARED_DEEP_PERSIST})) 
+        if ( (rsp.get_axsnoop() inside {vip_ace5_types::AWSNOOP_CMO, vip_ace5_types::AWSNOOP_WRITE_PARTIAL_CMO, vip_ace5_types::AWSNOOP_WRITE_FULL_CMO}) &&
+             (rsp.get_write_cmo_operation() inside {vip_ace5_types::AWCMO_CLEAN_SHARED_PERSIST, vip_ace5_types::AWCMO_CLEAN_SHARED_DEEP_PERSIST}))
         begin
           tmp.comp = 1;
           tmp.persist = 1;
-        end 
+        end
         if (rsp.get_memory_tag_operation() == vip_ace5_types::MEM_TAG_OP_WRITE_MATCH_READ_FETCH)
         begin
           tmp.comp = 1;
@@ -1490,7 +1492,7 @@ class amba5_slave_controller_component extends generic_controller_component;
     // prevent the task being killed until this completes in order to prevent
     // errors from the sequencer
     can_reset_lock.get();
-    
+
     `uvm_info("AMBA5 SLAVE CONTROLLER COMPONENT", $sformatf("stage4c: In task generate_response about to call reactive seq send_response checking for request/response::uid=0x%h  axaddr=0x%h axid=0x%h ",rsp.get_transaction_uid(), rsp.axaddr, rsp.axid) , UVM_DEBUG)
     if (cfg.get_protocol() == generic_types::PROTOCOL__AXI4) begin
       axi_seq.send_response(p_id, p, rsp);
@@ -1642,7 +1644,7 @@ class amba5_slave_controller_component extends generic_controller_component;
   // Trigger the driven and completed events when a write response is handshaked
   // on the interface
   virtual task manage_wr_events();
-    
+
     vip_ace5_transaction_item rsp;
 
     forever
@@ -1667,25 +1669,25 @@ class amba5_slave_controller_component extends generic_controller_component;
       // the outstanding transactions counts for writes and trigger the
       // write and transaction complete events
       super.get_order(WR_RSP_CMP_ID, process::self());
-      
+
       // Find the correct transaction
       if (bpersist === 1'b1) begin
         for (int unsigned x = 0; x < required_b_resp[id].size(); ++x) begin
           if (required_b_resp[id][x].persist == 1'b1) begin
             rsp_index = x;
-            break;           
+            break;
           end
-        end 
+        end
       end
 
       if ((btagmatch === 'b10) || (btagmatch === 'b11)) begin
         for (int unsigned x = 0; x < required_b_resp[id].size(); ++x) begin
           if (required_b_resp[id][x].tagmatch == 1'b1) begin
-            rsp_index = x;  
-            break;                
+            rsp_index = x;
+            break;
           end
-        end 
-      end 
+        end
+      end
 
       if (bcomp === 1'b1) required_b_resp[id][rsp_index].comp = 0;
       if (bpersist === 1'b1) required_b_resp[id][rsp_index].persist = 0;
@@ -1848,7 +1850,7 @@ class amba5_slave_controller_component extends generic_controller_component;
         // Use the sequence ID to determine whether this task call is ordering
         // read or write responses
         WR_REQ_REG_ID: if(wr_reqs.size() > 0) ->wr_req;
-        RD_REQ_REG_ID: if(rd_reqs.size() > 0) ->rd_req; 
+        RD_REQ_REG_ID: if(rd_reqs.size() > 0) ->rd_req;
         // Give a fatal message if the task is started with an unexpected sequence
         // ID
         default:
@@ -2107,7 +2109,7 @@ class amba5_slave_controller_component extends generic_controller_component;
     if ((p_id < NUM_RSVD_IDS) && !checking_dependencies[p_id]) begin
         if ($test$plusargs("IDM_TEST_EN")) begin // REVISIT: Blocking all IDM code with plusarg
             //there are mid sim reset clean up issues in slave ctrl which is tricky to debug and fix
-            //changing fatal to err to avoid ending the test 
+            //changing fatal to err to avoid ending the test
               `uvm_error(
                 "AMBA5 SLAVE CONTROLLER COMPONENT",
                 $sformatf({"Function called with reserved ID.  Use IDs starting at an",
@@ -2158,7 +2160,7 @@ class amba5_slave_controller_component extends generic_controller_component;
           order_done(WR_REQ_REG_ID);
       end
   endtask : handle_write_requests
-              
+
   // Function : register_request
   // Store transaction requests at the back of the relevant queues and trigger
   // the applicable event to indicate there are pending requests in the queue.
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index ec5aaaa5df9..fd22b6bf293 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -20,6 +20,9 @@
 `ifndef INTERFACE_BLOCK__SV
 `define INTERFACE_BLOCK__SV
 
+`define AXI_NUM_SAFETY_BITS 2
+`define AHB_NUM_SAFETY_BITS 2
+
 `include "uvm_macros.svh"
 `include "generic_common_pkg.sv"
 `include "local_params_pkg.sv"
@@ -139,8 +142,8 @@ module interface_block
   logic ARESETn_final;
   logic AHB_RESETn_final;
   always @(posedge ACLK or negedge ARESETn) begin
-  	if (!ARESETn) sreset_delayed <= 0;
-  	else sreset_delayed <= SRESETn;
+    if (!ARESETn) sreset_delayed <= 0;
+    else sreset_delayed <= SRESETn;
   end
   //If xsni accepts a txn from master in cycle x, vip sends the event to scb in cycle x+1. If in cycle x+1 xsni is going into sreset, vip does not send an indication to dv causing fails.
   //delying sreset going to xsni by 1 cycle
@@ -699,15 +702,17 @@ module interface_block
                     end : g_idm
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
+                      logic [WUSER_WIDTH-1:0]  rdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
                       logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
-                      logic  [RUSER_WIDTH-1:0] rrsp_err_code;
-    
+                      logic [RUSER_WIDTH-WUSER_WIDTH-1:0] rrsp_err_code;
+
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
+                        logic parity_err_rdat;
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
-                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
+                        assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -735,6 +740,12 @@ module interface_block
                           .user_i  (u_if.RUSER),
                           .error_o (parity_err_rrsp)
                         );
+                        chariot_rdat_parity_checker #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_check (
+                          .data_i (u_if.RDATA),
+                          .valid_i (u_if.RVALID),
+                          .user_i (u_if.RUSER),
+                          .error_o (parity_err_rdat)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
                         logic parity_err_rreq;
@@ -765,9 +776,13 @@ module interface_block
                           .user_o (wrsp_err_code)
                         );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
-                          .user_o (rrsp_err_code[RUSER_WIDTH-WUSER_WIDTH-1:0])
+                          .user_o (rrsp_err_code)
+                        );
+                        chariot_rdat_parity_generator #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_gen (
+                          .data_i (u_if.RDATA),
+                          .valid_i (u_if.RVALID),
+                          .user_o (rdat_err_code)
                         );
-                        assign rrsp_err_code[RUSER_WIDTH-1:RUSER_WIDTH-WUSER_WIDTH] = 0;
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_ace4_lite
@@ -1203,14 +1218,16 @@ module interface_block
                     end : g_idm
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
+                      logic [WUSER_WIDTH-1:0]  rdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
                       logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
-                      logic  [RUSER_WIDTH-1:0] rrsp_err_code;
+                      logic [RUSER_WIDTH-WUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
+                        logic parity_err_rdat;
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
-                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
+                        assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -1238,6 +1255,12 @@ module interface_block
                           .user_i  (u_if.RUSER),
                           .error_o (parity_err_rrsp)
                         );
+                        chariot_rdat_parity_checker #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_check (
+                          .data_i (u_if.RDATA),
+                          .valid_i (u_if.RVALID),
+                          .user_i (u_if.RUSER),
+                          .error_o (parity_err_rdat)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
                         logic parity_err_rreq;
@@ -1268,9 +1291,13 @@ module interface_block
                           .user_o (wrsp_err_code)
                         );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
-                          .user_o (rrsp_err_code[RUSER_WIDTH-WUSER_WIDTH-1:0])
+                          .user_o (rrsp_err_code)
+                        );
+                        chariot_rdat_parity_generator #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_gen (
+                          .data_i (u_if.RDATA),
+                          .valid_i (u_if.RVALID),
+                          .user_o (rdat_err_code)
                         );
-                        assign rrsp_err_code[RUSER_WIDTH-1:RUSER_WIDTH-WUSER_WIDTH] = 0;
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_axi4
@@ -1377,7 +1404,7 @@ module interface_block
            assign u_if.HREADY = u_if.HREADYOUT ;  // REVISIT MB: TB loops back signal - see RHODESNOC-170
            assign u_if.HSELX  = 1'b1           ;
          end
-	else begin
+  else begin
          ahb_mirror : assert property(@(posedge ACLK)
            (u_if.HREADY == u_if.HREADYOUT))
          else  `uvm_error(
@@ -1394,11 +1421,11 @@ module interface_block
       begin
         //vip_ahb5_if_wrapper       vif_wrapper;
         //typedef virtual vip_ahb5_uvm_interface vip_ahb5_uvm_vif;
-	//8.2 of AHB-C spec: AHB Issue B recommends that: slaves do not insert more than 16 wait states, to prevent any single access locking the bus for a large number of clock cycles.In the case of multi-layer interconnects and when bridging to other protocols, this recommendation can easily be exceeded without system impact. It is proposed that this recommendation is removed from the specification, and replaced with a note that excessive numbers of wait states might impact system performance
+  //8.2 of AHB-C spec: AHB Issue B recommends that: slaves do not insert more than 16 wait states, to prevent any single access locking the bus for a large number of clock cycles.In the case of multi-layer interconnects and when bridging to other protocols, this recommendation can easily be exceeded without system impact. It is proposed that this recommendation is removed from the specification, and replaced with a note that excessive numbers of wait states might impact system performance
        //Below assertion won't exist unless (PROTOCOL_VERSION == 0) so AHB3-Lite is enabled on PC
 
         //REVISIT Enable below assertion for AHB3-LITE when we test it
-	// $assertoff(1, u_pc.AHB_RECS_HREADYOUT_MAX.assert_AHB_RECS_HREADYOUT_MAX);
+  // $assertoff(1, u_pc.AHB_RECS_HREADYOUT_MAX.assert_AHB_RECS_HREADYOUT_MAX);
         // Add the virtual interface to the uvm_config_db
         uvm_config_db#(vip_ahb5_uvm_vif)::set(
           uvm_root::get()                         ,
@@ -1454,6 +1481,7 @@ module interface_block
         logic [WUSER_WIDTH-1:0]  wdat_err_code;
         logic [AWUSER_WIDTH-1:0] wreq_err_code;
         logic [DATA_WIDTH/8-1:0] strobe; //strobe not part of the ahb protocol, so we generate it here
+        logic [RUSER_WIDTH-1:0]  rdat_err_code;
 
         chariot_ahb_strobe_generation #(.DATA_WIDTH(DATA_WIDTH), .ADDR_WIDTH(ADDR_WIDTH)) strobe_gen (
           .HCLK     (ACLK),
@@ -1467,7 +1495,8 @@ module interface_block
         );
 
         if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
-          assign parity_error = 0; // no buser on this interface
+          logic parity_err_rdat;
+          assign parity_error = parity_err_rdat; // no buser on this interface
           chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
             .data_i (u_if.HWDATA),
             .strb_i (strobe),
@@ -1479,14 +1508,20 @@ module interface_block
             .nonsec_i (u_if.HNONSEC),
             .user_o (wreq_err_code)
           );
+          chariot_rdat_parity_checker #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AHB_NUM_SAFETY_BITS)) rdat_parity_check (
+            .data_i (u_if.HRDATA),
+            .valid_i (u_if.HREADY && u_if.HTRANS[1] && !u_if.HWRITE),
+            .user_i (u_if.HRUSER),
+            .error_o (parity_err_rdat)
+          );
         end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
           logic parity_err_wreq;
           logic parity_err_wdat;
           assign parity_error = parity_err_wreq | parity_err_wdat;
           chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
             .data_i  (u_if.HWDATA),
-            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
-            .strb_i  (strobe), //
+            .valid_i (|strobe && u_if.HWRITE), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
+            .strb_i  (strobe),
             .user_i  (u_if.HWUSER),
             .error_o (parity_err_wdat)
           );
@@ -1497,6 +1532,11 @@ module interface_block
             .valid_i  (u_if.HREADY && u_if.HTRANS[1]),
             .error_o  (parity_err_wreq)
           );
+          chariot_rdat_parity_generator #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AHB_NUM_SAFETY_BITS)) rdat_parity_gen (
+            .data_i (u_if.HRDATA),
+            .valid_i (u_if.HREADY && u_if.HTRANS[1] && !u_if.HWRITE),
+            .user_o (rdat_err_code)
+          );
         end
       `endif // CHARIOT_ASIL_B
     end : g_ahb
@@ -1533,8 +1573,8 @@ module interface_block
        //  . 2: ignore
        .MASTER_REQUIREMENT_PROPTYPE (2'b00              ),
        .SLAVE_REQUIREMENT_PROPTYPE  (2'b01              ),
-       .PPROT_FUNCTIONAL  	    ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? 1 : 0),
-       .PSTRB_FUNCTIONAL   	    ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? 1 : 0)
+       .PPROT_FUNCTIONAL        ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? 1 : 0),
+       .PSTRB_FUNCTIONAL        ((generic_types::protocol_t'(PROTOCOL) == generic_types::PROTOCOL__APB4) ? 1 : 0)
 
      )
      u_pc
diff --git a/logical/noc_arachne/validation/dynamic/top/testbench.sv b/logical/noc_arachne/validation/dynamic/top/testbench.sv
index 6a179d8b276..ad30c648df3 100755
--- a/logical/noc_arachne/validation/dynamic/top/testbench.sv
+++ b/logical/noc_arachne/validation/dynamic/top/testbench.sv
@@ -440,12 +440,12 @@ module testbench;
 
   // all things chariot_b
   `ifdef CHARIOT_ASIL_B
-    logic                 parity_error;
-    logic [NUM_IF-1:0] if_parity_error;
+    logic          parity_error;
+    logic [1:0] if_parity_error [0:NUM_IF-1];
     fusa_interrupt_if top_fusa_interrupt_if();
     bit fault_is_being_injected; //pin for chariot random fault injection only, and set by a tcl script force statement
 
-    assign parity_error = |if_parity_error;
+    assign parity_error = |(if_parity_error.or());
     assign top_fusa_interrupt_if.clk = TB_SYS_CLK;
     assign top_fusa_interrupt_if.fault_is_being_injected = fault_is_being_injected;
     assign top_fusa_interrupt_if.safety_interrupt = parity_error; // Michael, we should connect this to our safety mechanism outputs
diff --git a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
index e7524cc5ae1..20847a6c31a 100644
--- a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
+++ b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
@@ -776,7 +776,7 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
       # if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
       if _chariot_b:
         if (ruser_extra_bits >= 0): # ruser width > buser_width
-          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rrsp_err_code     "})
+          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "{g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rdat_err_code,g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rrsp_err_code}"})
       else:
         if (ruser_extra_bits >= 0): # ruser width > buser_width
           if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
@@ -883,7 +883,10 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
       # USER WIDTH signals
       if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HAUSER     "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HAUSER     "})
       if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HWUSER     "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HWUSER     "})
-      if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HRUSER     "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HRUSER     "})
+      if _chariot_b:
+        if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HRUSER     "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rdat_err_code   "})
+      else:
+        if paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HRUSER     "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HRUSER     "})
 
 
 
```

## d8e7d9edefe1c18d2cb15669cc682d7375d6c900

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit d8e7d9edefe1c18d2cb15669cc682d7375d6c900
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Tue Feb 2 04:21:30 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Tue Feb 2 04:21:30 2021 +0000

    Num unprotected bits = 15
    
    Change-Id: I20cad7b417cfafba9b76f4f512bdc2420dc00b71

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
index 89f2cac2c35..73068054d7d 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
@@ -28,8 +28,8 @@ module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     logic [USER_WIDTH-1:0] err_array;
     logic [USER_WIDTH-1:0] user_expected;
 
-    logic [ADDR_WIDTH-12:0] protectable_value;
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:10]};
+    logic [ADDR_WIDTH-16:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:15]};
     assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
     assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
index b026dc298d4..fc182cbea61 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
@@ -24,8 +24,8 @@ module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     output [USER_WIDTH-1:0] user_o
 );
 
-    logic [ADDR_WIDTH-12:0] protectable_value;
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:10]};
+    logic [ADDR_WIDTH-16:0] protectable_value;
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:15]};
     assign user_o = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
 
 endmodule
```

## 3ba56bea53a1b7e239c7f609ef88bf8b60e83829

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 3ba56bea53a1b7e239c7f609ef88bf8b60e83829
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Fri Feb 19 07:01:29 2021 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Thu Feb 25 22:59:33 2021 +0000

    Add chariot_ahb_hang_detector.sv (hang_error fires if HREADY is low for
    >=1000 cycles)
    Change delay_count to 5000 in chariot_fault_injection_scoreboard.svh
    
    Change-Id: I1bd0f69b49b99249029950e4411f1fdc96ef53ce

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_ahb_hang_detector.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_ahb_hang_detector.sv
new file mode 100644
index 00000000000..ada605507c6
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_ahb_hang_detector.sv
@@ -0,0 +1,55 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot AHB hang detector
+//------------------------------------------------------------------------------
+module chariot_ahb_hang_detector #(NUM_CLK_CYCLES_HANG = -1) (
+  input clk_i,
+  input reset_i,
+  input ready_i,
+  output logic error_o
+);
+
+  logic [31:0] cycle_count;
+  logic [31:0] cycle_count_reg;
+
+  always @(*) begin
+    if (reset_i) begin
+      cycle_count = cycle_count_reg;
+      error_o = 0;
+      if (~ready_i) begin
+        cycle_count = cycle_count + 1;
+        if (cycle_count >= NUM_CLK_CYCLES_HANG) begin
+          error_o = 1;
+        end
+      end
+      else begin
+        cycle_count = 0;
+      end
+    end else begin
+      cycle_count = 0;
+      error_o = 0;
+    end
+  end
+
+  always @(posedge clk_i) begin
+    if (reset_i) begin
+      cycle_count_reg <= cycle_count;
+    end
+    else begin
+      cycle_count_reg <= 0;
+    end
+  end
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
index 7bccc2255d6..0ddf6d771cc 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
@@ -28,6 +28,7 @@
 `include "chariot_ahb_strobe_generation.sv"
 `include "chariot_rdat_parity_generator.sv"
 `include "chariot_rdat_parity_checker.sv"
+`include "chariot_ahb_hang_detector.sv"
 
 package chariot_pkg;
 
diff --git a/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh b/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh
index 9a7bb49fc91..1267856d200 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh
@@ -43,7 +43,7 @@ class chariot_fault_injection_scoreboard extends uvm_scoreboard;
   function void build_phase(uvm_phase phase);
     super.build_phase(phase);
     uvm_config_db#(virtual fusa_interrupt_if)::get(uvm_root::get(), "*","fusa_interrupt_if" ,top_fusa_interrupt_if);
-    if($test$plusargs("inject_fault")) begin 
+    if($test$plusargs("inject_fault")) begin
       demoter = new;
       demoter.top_fusa_interrupt_if = top_fusa_interrupt_if;
       demoter.parent = this;
@@ -51,7 +51,7 @@ class chariot_fault_injection_scoreboard extends uvm_scoreboard;
   endfunction
 
   task run_phase(uvm_phase phase);
-    if($test$plusargs("inject_fault")) begin 
+    if($test$plusargs("inject_fault")) begin
       demote_errors(); // demote errors if injecting fault
     end
 
@@ -62,7 +62,7 @@ class chariot_fault_injection_scoreboard extends uvm_scoreboard;
     end
     caught_safety_interrupt = 1;
 
-    if($test$plusargs("inject_fault")) begin 
+    if($test$plusargs("inject_fault")) begin
       `uvm_info(get_type_name(), "Caught expected interrupt - force ending test", UVM_NONE)
       uvm_domain::jump_all(uvm_extract_phase::get());
     end else begin
@@ -99,7 +99,7 @@ class chariot_fault_injection_scoreboard extends uvm_scoreboard;
     bit delay_all; // this variable delays the fatals/errors for N cycles to give time for the fusa interrupt
     bit allow_uvm_info;
     uvm_report_object permitted_reporter;
-    int delay_count = 1000;
+    int delay_count = 5000;
     virtual fusa_interrupt_if top_fusa_interrupt_if;
     string first_fail_message;
     string message_queue[$];
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 7ab1f58401e..bfd8f871065 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -22,6 +22,7 @@
 
 `define AXI_NUM_SAFETY_BITS 2
 `define AHB_NUM_SAFETY_BITS 2
+`define NUM_CLK_CYCLES_HANG 100000
 
 `include "uvm_macros.svh"
 `include "generic_common_pkg.sv"
@@ -175,6 +176,7 @@ module interface_block
 
   `ifdef CHARIOT_ASIL_B
     logic parity_error;
+    logic hang_error;
   `endif // CHARIOT_ASIL_B
 
   // Event for signalling that the virtual interface has been added to the
@@ -715,6 +717,7 @@ module interface_block
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
+                        assign hang_error = 0;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -753,6 +756,7 @@ module interface_block
                         logic parity_err_rreq;
                         logic parity_err_wdat;
                         assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
+                        assign hang_error = 0;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -1230,6 +1234,7 @@ module interface_block
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
+                        assign hang_error = 0;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -1268,6 +1273,7 @@ module interface_block
                         logic parity_err_rreq;
                         logic parity_err_wdat;
                         assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
+                        assign hang_error = 0;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -1913,7 +1919,9 @@ module interface_block
 
         if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
           logic parity_err_rdat;
+          logic hang_err_ahb;
           assign parity_error = parity_err_rdat; // no buser on this interface
+          assign hang_error = hang_err_ahb;
           chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
             .data_i (u_if.HWDATA),
             .strb_i (strobe),
@@ -1931,10 +1939,17 @@ module interface_block
             .user_i (u_if.HRUSER),
             .error_o (parity_err_rdat)
           );
+          chariot_ahb_hang_detector #(.NUM_CLK_CYCLES_HANG(`NUM_CLK_CYCLES_HANG)) ahb_hang_detector (
+            .clk_i (u_if.HCLK),
+            .reset_i (u_if.HRESET_N),
+            .ready_i (u_if.HREADY),
+            .error_o(hang_err_ahb)
+          );
         end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
           logic parity_err_wreq;
           logic parity_err_wdat;
           assign parity_error = parity_err_wreq | parity_err_wdat;
+          assign hang_error = 0;
           chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
             .data_i  (u_if.HWDATA),
             .valid_i (|strobe && u_if.HWRITE), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
@@ -2088,6 +2103,7 @@ module interface_block
 
     `ifdef CHARIOT_ASIL_B
       assign parity_error = 0; // no parity on APB yet - todo once apb gets user bits
+      assign hang_error = 0;
     `endif // CHARIOT_ASIL_B
 
     end : g_apb
diff --git a/logical/noc_arachne/validation/dynamic/top/testbench.sv b/logical/noc_arachne/validation/dynamic/top/testbench.sv
index 8f120b64e8c..0ccddbe343e 100755
--- a/logical/noc_arachne/validation/dynamic/top/testbench.sv
+++ b/logical/noc_arachne/validation/dynamic/top/testbench.sv
@@ -442,14 +442,17 @@ module testbench;
   // all things chariot_b
   `ifdef CHARIOT_ASIL_B
     logic          parity_error;
+    logic          hang_error;
     logic [1:0] if_parity_error [0:NUM_IF-1];
+    logic [1:0] if_hang_error [0:NUM_IF-1];
     fusa_interrupt_if top_fusa_interrupt_if();
     bit fault_is_being_injected; //pin for chariot random fault injection only, and set by a tcl script force statement
 
     assign parity_error = |(if_parity_error.or());
+    assign hang_error = |(if_hang_error.or());
     assign top_fusa_interrupt_if.clk = TB_SYS_CLK;
     assign top_fusa_interrupt_if.fault_is_being_injected = fault_is_being_injected;
-    assign top_fusa_interrupt_if.safety_interrupt = parity_error; // Michael, we should connect this to our safety mechanism outputs
+    assign top_fusa_interrupt_if.safety_interrupt = parity_error | hang_error;
     initial begin
       uvm_config_db#(virtual fusa_interrupt_if)::set(uvm_root::get(), "*","fusa_interrupt_if" ,top_fusa_interrupt_if);
     end
@@ -560,6 +563,7 @@ module testbench;
 
         `ifdef CHARIOT_ASIL_B
           assign if_parity_error[a] = u_if.parity_error;
+          assign if_hang_error[a] = u_if.hang_error;
         `endif // CHARIOT_ASIL_B
 
      end : master
@@ -659,6 +663,7 @@ module testbench;
 
         `ifdef CHARIOT_ASIL_B
           assign if_parity_error[a] = u_if.parity_error;
+          assign if_hang_error[a] = u_if.hang_error;
         `endif // CHARIOT_ASIL_B
 
       end : slave
```

## 2cb79d4081f5d79cd0aba93217e2c121b4e6348f

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 2cb79d4081f5d79cd0aba93217e2c121b4e6348f
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Wed Feb 24 21:34:22 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Thu Mar 4 21:20:03 2021 +0000

    Replace chariot_wdat_parity_generator/chariot_wdat_parity_checker with chariot_wdat_ecc_generator/chariot_wdat_ecc_checker
    
    Change-Id: I7a75132fadb0d014e785915899ccc91e8309e058

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
index 0ddf6d771cc..7b79f91771c 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
@@ -29,6 +29,8 @@
 `include "chariot_rdat_parity_generator.sv"
 `include "chariot_rdat_parity_checker.sv"
 `include "chariot_ahb_hang_detector.sv"
+`include "chariot_wdat_ecc_generator.sv"
+`include "chariot_wdat_ecc_checker.sv"
 
 package chariot_pkg;
 
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
new file mode 100644
index 00000000000..1668c626477
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
@@ -0,0 +1,84 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot write data ECC checker
+//------------------------------------------------------------------------------
+
+module chariot_wdat_ecc_checker #(DATA_WIDTH = -1, USER_WIDTH = -1) (
+  input [DATA_WIDTH-1:0] data_i,
+  input [USER_WIDTH-1:0] user_i,
+  input valid_i,
+  input [DATA_WIDTH/8-1:0] strb_i,
+  output logic [(DATA_WIDTH/32)-1:0] error_o,
+  output logic [(32*(DATA_WIDTH/32))-1:0] errors_1_bit_o,
+  output logic [(DATA_WIDTH/32)-1:0] errors_2_bits_o
+);
+
+  genvar i;
+  generate
+    for (i=0; i<DATA_WIDTH/32; i=i+1) begin
+      logic [63:0] msg;
+      logic [5:0] index_xor;
+      integer j;
+      always @(*) begin
+        error_o[i] = 0;
+        errors_1_bit_o[(i*32)+31:(i*32)] = 32'd0;
+        errors_2_bits_o[i] = 0;
+        msg = 0;
+        index_xor = 0;
+        j = 0;
+        if (valid_i && user_i[i*8+7] && (strb_i[i*(DATA_WIDTH/8)+((DATA_WIDTH/8)-1):i*(DATA_WIDTH/8)] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
+          msg = {
+            25'b0,                             //msg[63:39]
+            data_i[(i*32)+31:(i*32)+26],       //msg[38:33]//33
+            user_i[(i*8)+6],                   //msg[32]
+            data_i[(i*32)+25:(i*32)+11],       //msg[31:17]
+            user_i[(i*8)+5],                   //msg[16]
+            data_i[(i*32)+10:(i*32)+4],        //msg[15:9]
+            user_i[(i*8)+4],                   //msg[8]
+            data_i[(i*32)+3:(i*32)+1],         //msg[7:5]
+            user_i[(i*8)+3],                   //msg[4]
+            data_i[(i*32)+0],                  //msg[3]
+            user_i[(i*8)+2],                   //msg[2]
+            user_i[(i*8)+1],                   //msg[1]
+            user_i[(i*8)+0]                    //msg[0]
+          };
+          for (j=0; j<64; j=j+1) begin
+            if (msg[j]) begin
+              index_xor = index_xor ^ j;
+            end
+          end
+          if (user_i[i*8] != ~^msg[63:1]) begin // 1 bit flip
+            error_o[i] = 1;
+            index_xor = ~index_xor;
+            errors_1_bit_o[(i*32)+31:(i*32)] = (index_xor == 6'd3) ? 0 :
+                          (index_xor >= 6'd5  && index_xor <= 6'd7)  ? (index_xor-4)+(i*32) :
+                          (index_xor >= 6'd9  && index_xor <= 6'd15) ? (index_xor-5)+(i*32) :
+                          (index_xor >= 6'd17 && index_xor <= 6'd31) ? (index_xor-6)+(i*32) :
+                          (index_xor >= 6'd33 && index_xor <= 6'd38) ? (index_xor-7)+(i*32) :
+                          ~32'b0; // error was not a data bit
+
+          end else begin // no errors or 2 bit flips
+            if (index_xor != 6'b111111) begin
+              error_o[i] = 1;
+              errors_2_bits_o[i] = 1;
+            end
+          end
+        end
+      end
+    end
+  endgenerate
+
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv
new file mode 100644
index 00000000000..d1a0ed51eda
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv
@@ -0,0 +1,81 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot write data ECC generation
+//------------------------------------------------------------------------------
+
+module chariot_wdat_ecc_generator #(DATA_WIDTH = -1, USER_WIDTH = -1) (
+  input [DATA_WIDTH-1:0] data_i,
+  input [(DATA_WIDTH/8)-1:0] strb_i,
+  output logic [USER_WIDTH-1:0] user_o
+);
+
+  parameter DATA_SIZE = DATA_WIDTH / 32;
+
+  // calculate ECC for data_i
+  genvar i;
+  generate
+    for (i=0; i<DATA_SIZE; i=i+1) begin
+      logic [DATA_WIDTH-1:0] strobed_data;
+      logic [6:0] parity_bits;
+      logic [63:0] msg;
+      logic [5:0] index_xor;
+      integer j;
+      integer k;
+      always @(*) begin
+        strobed_data = {
+          ((strb_i[(i*4)+3]) ? data_i[(i*32)+31:(i*32)+24] : 8'b0),
+          ((strb_i[(i*4)+2]) ? data_i[(i*32)+23:(i*32)+16] : 8'b0),
+          ((strb_i[(i*4)+1]) ? data_i[(i*32)+15:(i*32)+8]  : 8'b0),
+          ((strb_i[(i*4)])   ? data_i[(i*32)+7 :(i*32)+0]  : 8'b0)
+        };
+
+        parity_bits = 0;
+        msg = {
+          25'b0,
+          strobed_data[31:26],
+          parity_bits[6],
+          strobed_data[25:11],
+          parity_bits[5],
+          strobed_data[10:4],
+          parity_bits[4],
+          strobed_data[3:1],
+          parity_bits[3],
+          strobed_data[0],
+          parity_bits[2],
+          parity_bits[1],
+          parity_bits[0]
+        };
+
+        index_xor = 0;
+        for (j=0; j<64; j=j+1) begin
+          if (msg[j]) begin
+            index_xor = index_xor ^ j;
+          end
+        end
+
+        // For odd parity, if a bit in index_xor == 0, toggle the corresponding parity_bit
+        for (k=0; k<6; k=k+1) begin // parity_bits[6:1] (user_o[6:1]) should be inverse of index_xor
+          if (~index_xor[k]) begin
+            parity_bits[k+1] ^= 1;
+          end
+        end
+        parity_bits[0] = ~^{strobed_data[31:0],parity_bits[6:1]}; // odd parity of entire message
+        user_o[(i*8)+7:(i*8)] = {1'b1,parity_bits[6:0]};
+      end
+    end
+  endgenerate
+
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 6008f4e640b..89451cda034 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -177,6 +177,7 @@ module interface_block
   `ifdef CHARIOT_ASIL_B
     logic parity_error;
     logic hang_error;
+    logic ecc_error;
   `endif // CHARIOT_ASIL_B
 
   // Event for signalling that the virtual interface has been added to the
@@ -718,7 +719,8 @@ module interface_block
                         logic parity_err_rrsp;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
                         assign hang_error = 0;
-                        chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
+                        assign ecc_error = 0;
+                        chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
                           .user_o (wdat_err_code)
@@ -754,15 +756,18 @@ module interface_block
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
                         logic parity_err_rreq;
-                        logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
+                        logic [(DATA_WIDTH/32)-1:0] ecc_err_wdat;
+                        assign parity_error = parity_err_wreq | parity_err_rreq;
                         assign hang_error = 0;
-                        chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
+                        assign ecc_error = |ecc_err_wdat;
+                        chariot_wdat_ecc_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_check (
                           .data_i  (u_if.WDATA),
+                          .user_i  (u_if.WUSER),
                           .valid_i (u_if.WVALID),
                           .strb_i  (u_if.WSTRB),
-                          .user_i  (u_if.WUSER),
-                          .error_o (parity_err_wdat)
+                          .error_o (ecc_err_wdat),
+                          .errors_1_bit_o(),
+                          .errors_2_bits_o()
                         );
                         chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_check (
                           .addr_i  (u_if.AWADDR),
@@ -1235,13 +1240,14 @@ module interface_block
                         logic parity_err_rrsp;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
                         assign hang_error = 0;
-                        chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
+                        assign ecc_error = 0;
+                        chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
                           .user_o (wdat_err_code)
                         );
                         chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_gen (
-                          .addr_i  (u_if.AWADDR),
+                          .addr_i (u_if.AWADDR),
                           .user_i (u_if.AWUSER),
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
@@ -1271,15 +1277,18 @@ module interface_block
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
                         logic parity_err_rreq;
-                        logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
+                        logic [(DATA_WIDTH/32)-1:0] ecc_err_wdat;
+                        assign parity_error = parity_err_wreq | parity_err_rreq;
                         assign hang_error = 0;
-                        chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
+                        assign ecc_error = |ecc_err_wdat;
+                        chariot_wdat_ecc_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_check (
                           .data_i  (u_if.WDATA),
+                          .user_i  (u_if.WUSER),
                           .valid_i (u_if.WVALID),
                           .strb_i  (u_if.WSTRB),
-                          .user_i  (u_if.WUSER),
-                          .error_o (parity_err_wdat)
+                          .error_o (ecc_err_wdat),
+                          .errors_1_bit_o(),
+                          .errors_2_bits_o()
                         );
                         chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_check (
                           .addr_i  (u_if.AWADDR),
@@ -1926,7 +1935,8 @@ module interface_block
           logic hang_err_ahb;
           assign parity_error = parity_err_rdat; // no buser on this interface
           assign hang_error = hang_err_ahb;
-          chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
+          assign ecc_error = 0;
+          chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
             .data_i (u_if.HWDATA),
             .strb_i (strobe),
             .user_o (wdat_err_code)
@@ -1951,15 +1961,18 @@ module interface_block
           );
         end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
           logic parity_err_wreq;
-          logic parity_err_wdat;
-          assign parity_error = parity_err_wreq | parity_err_wdat;
+          logic [(DATA_WIDTH/32)-1:0] ecc_err_wdat;
+          assign parity_error = parity_err_wreq;
           assign hang_error = 0;
-          chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
+          assign ecc_error = |ecc_err_wdat;
+          chariot_wdat_ecc_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_check (
             .data_i  (u_if.HWDATA),
-            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
-            .strb_i  (strobe),
             .user_i  (u_if.HWUSER),
-            .error_o (parity_err_wdat)
+            .valid_i (|strobe && u_if.HWRITE), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
+            .strb_i  (strobe),
+            .error_o (ecc_err_wdat),
+            .errors_1_bit_o(),
+            .errors_2_bits_o()
           );
           chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_check (
             .addr_i   (u_if.HADDR),
@@ -2108,6 +2121,7 @@ module interface_block
     `ifdef CHARIOT_ASIL_B
       assign parity_error = 0; // no parity on APB yet - todo once apb gets user bits
       assign hang_error = 0;
+      assign ecc_error = 0;
     `endif // CHARIOT_ASIL_B
 
     end : g_apb
diff --git a/logical/noc_arachne/validation/dynamic/top/testbench.sv b/logical/noc_arachne/validation/dynamic/top/testbench.sv
index 0ccddbe343e..dd03f12d2e1 100755
--- a/logical/noc_arachne/validation/dynamic/top/testbench.sv
+++ b/logical/noc_arachne/validation/dynamic/top/testbench.sv
@@ -443,16 +443,19 @@ module testbench;
   `ifdef CHARIOT_ASIL_B
     logic          parity_error;
     logic          hang_error;
+    logic          ecc_error;
     logic [1:0] if_parity_error [0:NUM_IF-1];
     logic [1:0] if_hang_error [0:NUM_IF-1];
+    logic [1:0] if_ecc_error [0:NUM_IF-1];
     fusa_interrupt_if top_fusa_interrupt_if();
     bit fault_is_being_injected; //pin for chariot random fault injection only, and set by a tcl script force statement
 
     assign parity_error = |(if_parity_error.or());
     assign hang_error = |(if_hang_error.or());
+    assign ecc_error = |(if_ecc_error.or());
     assign top_fusa_interrupt_if.clk = TB_SYS_CLK;
     assign top_fusa_interrupt_if.fault_is_being_injected = fault_is_being_injected;
-    assign top_fusa_interrupt_if.safety_interrupt = parity_error | hang_error;
+    assign top_fusa_interrupt_if.safety_interrupt = parity_error | hang_error | ecc_error;
     initial begin
       uvm_config_db#(virtual fusa_interrupt_if)::set(uvm_root::get(), "*","fusa_interrupt_if" ,top_fusa_interrupt_if);
     end
@@ -528,7 +531,7 @@ module testbench;
           `else
             `ifdef IDM_PRESENT
               .ARESETn                (SYS_RESETn[CLOCK_MAP[a]]     ),
-              .SRESETn                (g_idm_interface.idm_if_i.SRESETN[a] && (~sreset_control[a])), 
+              .SRESETn                (g_idm_interface.idm_if_i.SRESETN[a] && (~sreset_control[a])),
             `else
               .ARESETn                (SYS_RESETn[CLOCK_MAP[a]]     ),
             `endif
@@ -564,6 +567,7 @@ module testbench;
         `ifdef CHARIOT_ASIL_B
           assign if_parity_error[a] = u_if.parity_error;
           assign if_hang_error[a] = u_if.hang_error;
+          assign if_ecc_error[a] = u_if.ecc_error;
         `endif // CHARIOT_ASIL_B
 
      end : master
@@ -664,6 +668,7 @@ module testbench;
         `ifdef CHARIOT_ASIL_B
           assign if_parity_error[a] = u_if.parity_error;
           assign if_hang_error[a] = u_if.hang_error;
+          assign if_ecc_error[a] = u_if.ecc_error;
         `endif // CHARIOT_ASIL_B
 
       end : slave
```

## 5d88abb380368baa73f3e9e2b8b6f4d2033aa398

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 5d88abb380368baa73f3e9e2b8b6f4d2033aa398
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Fri Mar 26 22:00:06 2021 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Thu Apr 1 19:36:47 2021 +0100

    Adding AXI read hang detector
    
    Change-Id: Ida157424d8d9ee818fc15ad60bedbf3c4cc206a5

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_read_hang_detector.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_read_hang_detector.sv
new file mode 100644
index 00000000000..f25b8f9fa73
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_read_hang_detector.sv
@@ -0,0 +1,183 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot AXI hang detector
+//------------------------------------------------------------------------------
+module chariot_axi_read_hang_detector #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
+  input clk_i,
+  input reset_i,
+  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] arid_i,
+  input arvalid_i,
+  input arready_i,
+  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] rid_i,
+  input rvalid_i,
+  input rlast_i,
+  input rready_i,
+  output logic error_o
+);
+
+  logic [COUNTER_WIDTH-1:0] counter;
+  logic [COUNTER_WIDTH-1:0] counter_reg;
+  logic [TRACKER_LENGTH-1:0] tracker_valid_mask_inverted;
+  logic [TRACKER_LENGTH-1:0] insert_index_encoded;
+  logic [TRACKER_LENGTH-1:0] insert_index;
+  logic insert_complete;
+  logic insert_complete_reg;
+  // a full tracker entry consists of the tracker_valid, tracker_id, and the tracker_timestamp
+  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids;
+  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids_reg;
+  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids_reg [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps_reg [0:TRACKER_LENGTH-1];
+  integer i;
+  integer j;
+  integer k;
+  integer a;
+
+  // if arvalid_i && arready_i, insert into a non-valid tracker entry and mark valid
+  // if rvalid_i && rlast_i && rready_i, find the valid entries in the tracker with matching IDs, and remove the oldest one
+
+  // inserting into the tracker
+  always @(*) begin
+    if (reset_i) begin
+      counter = counter_reg + 1;
+      insert_index_encoded = 0;
+      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      insert_complete = 0;
+      tracker_valid_mask_inverted = ~tracker_valids_reg;
+      // get lowest index that is not valid
+      insert_index_encoded = tracker_valid_mask_inverted & ~(tracker_valid_mask_inverted-1);
+      for (i=0; i<TRACKER_LENGTH; i=i+1) begin
+        if (insert_index_encoded[i]) begin
+          insert_index = i;
+        end
+      end
+      if (arvalid_i && arready_i) begin
+        insert_complete = insert_complete_reg;
+        if (!insert_complete_reg) begin
+          tracker_valids[insert_index] = 1;
+          tracker_ids[insert_index] = arid_i;
+          tracker_timestamps[insert_index] = counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2];
+          insert_complete = 1;
+        end
+      end
+    end else begin
+      counter = 0;
+      tracker_valid_mask_inverted = 0;
+      insert_index_encoded = 0;
+      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      insert_complete = 0;
+      tracker_valids = 0;
+    end
+  end
+
+  logic remove_complete;
+  logic [TRACKER_LENGTH-1:0] remove_index;
+  logic [TRACKER_LENGTH-1:0] remove_mask;
+
+  // removing from tracker
+  // if multiple entries in the tracker are valid, have the same ID, and have the same timestamp, the entry with the largest index will be removed
+  always @(*) begin
+    if (reset_i) begin
+      remove_complete = 0;
+      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      remove_mask = 0;
+      // check to see which tracker entries are valid and have a matching rid
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_valids_reg[j] && tracker_ids_reg[j] == rid_i) begin
+          remove_mask[j] = 1;
+        end
+      end
+      // check to see which valid tracker entries with matching rids are the oldest
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+1)%4 && remove_mask[j]) begin
+          remove_complete = 1;
+          remove_index = j;
+        end
+      end
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+2)%4 && remove_mask[j] && !remove_complete) begin
+          remove_complete = 1;
+          remove_index = j;
+        end
+      end
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+3)%4 && remove_mask[j] && !remove_complete) begin
+          remove_complete = 1;
+          remove_index = j;
+        end
+      end
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+4)%4 && remove_mask[j] && !remove_complete) begin
+          remove_index = j;
+        end
+      end
+      if (rvalid_i && rlast_i && rready_i && (remove_index >= 0 && remove_index < TRACKER_LENGTH)) begin
+        tracker_valids[remove_index] = 0;
+      end
+    end else begin
+      remove_complete = 0;
+      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      remove_mask = 0;
+    end
+  end
+
+  // hang detection
+  `define IDLE 0
+  `define CHECK_FOR_HANG 1
+  logic hang_detection_state;
+  logic hang_detection_state_reg;
+
+  always @(*) begin
+    error_o = 0;
+    if (reset_i) begin
+      if (hang_detection_state_reg == `IDLE) begin
+        if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
+          hang_detection_state = `CHECK_FOR_HANG;
+        end
+      end else if (hang_detection_state_reg == `CHECK_FOR_HANG) begin
+        hang_detection_state = `IDLE;
+        for (k=0; k<TRACKER_LENGTH; k=k+1) begin
+          // if any tracker entry is valid and has a timestamp that matches the most significant 2 bits of the counter, throw hang error
+          if (tracker_valids_reg[k] && tracker_timestamps_reg[k]==counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
+            error_o = 1;
+          end
+        end
+      end
+    end else begin
+      hang_detection_state = `IDLE;
+    end
+  end
+
+  always @(posedge clk_i or negedge reset_i) begin
+    if (reset_i) begin
+      counter_reg <= counter;
+      insert_complete_reg <= insert_complete;
+      hang_detection_state_reg <= hang_detection_state;
+      tracker_valids_reg <= tracker_valids;
+      for (a=0; a<TRACKER_LENGTH; a=a+1) begin
+        tracker_ids_reg[a] <= tracker_ids[a];
+        tracker_timestamps_reg[a] <= tracker_timestamps[a];
+      end
+    end else begin
+      counter_reg <= 0;
+      insert_complete_reg <= 0;
+      hang_detection_state_reg <= `IDLE;
+      tracker_valids_reg <= 0;
+    end
+  end
+
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
index de05116b8be..b95dda8806e 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
@@ -31,6 +31,7 @@
 `include "chariot_ahb_hang_detector.sv"
 `include "chariot_wdat_ecc_generator.sv"
 `include "chariot_wdat_ecc_checker.sv"
+`include "chariot_axi_read_hang_detector.sv"
 
 `include "uvm_macros.svh"
 
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 211ee4473f6..46ddfde2d73 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -22,7 +22,8 @@
 
 `define AXI_NUM_SAFETY_BITS 2
 `define AHB_NUM_SAFETY_BITS 2
-`define NUM_CLK_CYCLES_HANG 100000
+`define NUM_CLK_CYCLES_HANG 400000
+`define AXI_HANG_COUNTER_WIDTH 19
 
 `include "uvm_macros.svh"
 `include "generic_common_pkg.sv"
@@ -717,8 +718,9 @@ module interface_block
                         logic parity_err_rdat;
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
+                        logic hang_err_axi;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
-                        assign hang_error = 0;
+                        assign hang_error = hang_err_axi;
                         assign ecc_error = 0;
                         chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
                           .data_i (u_if.WDATA),
@@ -753,6 +755,18 @@ module interface_block
                           .user_i (u_if.RUSER),
                           .error_o (parity_err_rdat)
                         );
+                        chariot_axi_read_hang_detector #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
+                          .clk_i(ACLK),
+                          .reset_i(u_if.ARESETn),
+                          .arid_i(u_if.ARID),
+                          .arvalid_i(u_if.ARVALID),
+                          .arready_i(u_if.ARREADY),
+                          .rid_i(u_if.RID),
+                          .rvalid_i(u_if.RVALID),
+                          .rlast_i(u_if.RLAST),
+                          .rready_i(u_if.RREADY),
+                          .error_o(hang_err_axi)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
                         logic parity_err_rreq;
@@ -1238,8 +1252,9 @@ module interface_block
                         logic parity_err_rdat;
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
+                        logic hang_err_axi;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
-                        assign hang_error = 0;
+                        assign hang_error = hang_err_axi;
                         assign ecc_error = 0;
                         chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
                           .data_i (u_if.WDATA),
@@ -1274,6 +1289,18 @@ module interface_block
                           .user_i (u_if.RUSER),
                           .error_o (parity_err_rdat)
                         );
+                        chariot_axi_read_hang_detector #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
+                          .clk_i(ACLK),
+                          .reset_i(u_if.ARESETn),
+                          .arid_i(u_if.ARID),
+                          .arvalid_i(u_if.ARVALID),
+                          .arready_i(u_if.ARREADY),
+                          .rid_i(u_if.RID),
+                          .rvalid_i(u_if.RVALID),
+                          .rlast_i(u_if.RLAST),
+                          .rready_i(u_if.RREADY),
+                          .error_o(hang_err_axi)
+                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
                         logic parity_err_rreq;
```

## c22154dd2c2f91d60d1f15c6b83053be63a708eb

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit c22154dd2c2f91d60d1f15c6b83053be63a708eb
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Wed Apr 7 22:05:34 2021 +0100
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Wed Apr 7 22:05:34 2021 +0100

    Generalize the AXI hang detector to work for both reads and writes
    
    Change-Id: I93912d17d18ba76dc5dab23b55413706b11ca63a

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
new file mode 100644
index 00000000000..c58da6bbcb9
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
@@ -0,0 +1,170 @@
+//------------------------------------------------------------------------------
+// The confidential and proprietary information contained in this file may only
+// be used by a person authorised under and to the extent permitted by a
+// subsisting licensing agreement from ARM Limited.
+//
+//        (C) COPYRIGHT 2020 ARM Limited.
+//            ALL RIGHTS RESERVED
+//
+// This entire notice must  be reproduced on all copies of this file and copies
+// of this file may only be made by a person if such person is permitted to do
+// so under the terms of a subsisting license agreement from ARM Limited.
+//
+// Release Information : $State$
+//
+//------------------------------------------------------------------------------
+// Purpose : Chariot AXI hang detector
+//------------------------------------------------------------------------------
+module chariot_axi_hang_detector #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
+  input clk_i,
+  input reset_i,
+  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] aid_i,
+  input avalid_i,
+  input aready_i,
+  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] id_i,
+  input valid_i,
+  input last_i,
+  input ready_i,
+  output logic error_o
+);
+
+  logic [COUNTER_WIDTH-1:0] counter;
+  logic [COUNTER_WIDTH-1:0] counter_reg;
+  logic [TRACKER_LENGTH-1:0] tracker_valid_mask_inverted;
+  logic [TRACKER_LENGTH-1:0] insert_index_encoded;
+  logic [TRACKER_LENGTH-1:0] insert_index;
+  logic remove_complete;
+  logic [TRACKER_LENGTH-1:0] remove_index;
+  logic [TRACKER_LENGTH-1:0] remove_mask;
+  // a full tracker entry consists of the tracker_valid, tracker_id, and the tracker_timestamp
+  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids;
+  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids_reg;
+  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids_reg [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps_reg [0:TRACKER_LENGTH-1];
+  integer i;
+  integer j;
+  integer k;
+  integer a;
+
+  // if avalid_i && aready_i, insert into a non-valid tracker entry and mark valid
+  // if valid_i && last_i && ready_i, find the valid entries in the tracker with matching IDs, and remove the oldest one
+
+  always @(*) begin
+    if (reset_i) begin
+      counter = counter_reg + 1;
+      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      tracker_valid_mask_inverted = ~tracker_valids_reg;
+      remove_complete = 0;
+      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      remove_mask = 0;
+      tracker_valids = tracker_valids_reg;
+      for (i=0; i<TRACKER_LENGTH; i=i+1) begin
+        tracker_ids[i] = tracker_ids_reg[i];
+        tracker_timestamps[i] = tracker_timestamps_reg[i];
+      end
+      // inserting into the tracker
+      // get lowest index that is not valid
+      insert_index_encoded = tracker_valid_mask_inverted & ~(tracker_valid_mask_inverted-1);
+      for (i=0; i<TRACKER_LENGTH; i=i+1) begin
+        if (insert_index_encoded[i]) begin
+          insert_index = i;
+        end
+      end
+      if (avalid_i && aready_i) begin
+        tracker_valids[insert_index] = 1;
+        tracker_ids[insert_index] = aid_i;
+        tracker_timestamps[insert_index] = counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2];
+      end
+      // removing from tracker
+      // if multiple entries in the tracker are valid, have the same ID, and have the same timestamp, the entry with the largest index will be removed
+      // check to see which tracker entries are valid and have a matching rid
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_valids_reg[j] && tracker_ids_reg[j] == id_i) begin
+          remove_mask[j] = 1;
+        end
+      end
+      // check to see which valid tracker entries with matching rids are the oldest
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+1)%4 && remove_mask[j]) begin
+          remove_complete = 1;
+          remove_index = j;
+        end
+      end
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+2)%4 && remove_mask[j] && !remove_complete) begin
+          remove_complete = 1;
+          remove_index = j;
+        end
+      end
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+3)%4 && remove_mask[j] && !remove_complete) begin
+          remove_complete = 1;
+          remove_index = j;
+        end
+      end
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+4)%4 && remove_mask[j] && !remove_complete) begin
+          remove_index = j;
+        end
+      end
+      if (valid_i && last_i && ready_i && (remove_index >= 0 && remove_index < TRACKER_LENGTH)) begin
+        tracker_valids[remove_index] = 0;
+      end
+    end else begin
+      counter = 0;
+      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      tracker_valid_mask_inverted = 0;
+      remove_complete = 0;
+      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      remove_mask = 0;
+      tracker_valids = 0;
+      insert_index_encoded = 0;
+    end
+  end
+
+  // hang detection
+  `define IDLE 0
+  `define CHECK_FOR_HANG 1
+  logic hang_detection_state;
+  logic hang_detection_state_reg;
+
+  always @(*) begin
+    error_o = 0;
+    if (reset_i) begin
+      if (hang_detection_state_reg == `IDLE) begin
+        if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
+          hang_detection_state = `CHECK_FOR_HANG;
+        end
+      end else if (hang_detection_state_reg == `CHECK_FOR_HANG) begin
+        hang_detection_state = `IDLE;
+        for (k=0; k<TRACKER_LENGTH; k=k+1) begin
+          // if any tracker entry is valid and has a timestamp that matches the most significant 2 bits of the counter, throw hang error
+          if (tracker_valids_reg[k] && tracker_timestamps_reg[k]==counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
+            error_o = 1;
+          end
+        end
+      end
+    end else begin
+      hang_detection_state = `IDLE;
+    end
+  end
+
+  always @(posedge clk_i or negedge reset_i) begin
+    if (reset_i) begin
+      counter_reg <= counter;
+      hang_detection_state_reg <= hang_detection_state;
+      tracker_valids_reg <= tracker_valids;
+      for (a=0; a<TRACKER_LENGTH; a=a+1) begin
+        tracker_ids_reg[a] <= tracker_ids[a];
+        tracker_timestamps_reg[a] <= tracker_timestamps[a];
+      end
+    end else begin
+      counter_reg <= 0;
+      hang_detection_state_reg <= `IDLE;
+      tracker_valids_reg <= 0;
+    end
+  end
+
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_read_hang_detector.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_read_hang_detector.sv
deleted file mode 100644
index f25b8f9fa73..00000000000
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_read_hang_detector.sv
+++ /dev/null
@@ -1,183 +0,0 @@
-//------------------------------------------------------------------------------
-// The confidential and proprietary information contained in this file may only
-// be used by a person authorised under and to the extent permitted by a
-// subsisting licensing agreement from ARM Limited.
-//
-//        (C) COPYRIGHT 2020 ARM Limited.
-//            ALL RIGHTS RESERVED
-//
-// This entire notice must  be reproduced on all copies of this file and copies
-// of this file may only be made by a person if such person is permitted to do
-// so under the terms of a subsisting license agreement from ARM Limited.
-//
-// Release Information : $State$
-//
-//------------------------------------------------------------------------------
-// Purpose : Chariot AXI hang detector
-//------------------------------------------------------------------------------
-module chariot_axi_read_hang_detector #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
-  input clk_i,
-  input reset_i,
-  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] arid_i,
-  input arvalid_i,
-  input arready_i,
-  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] rid_i,
-  input rvalid_i,
-  input rlast_i,
-  input rready_i,
-  output logic error_o
-);
-
-  logic [COUNTER_WIDTH-1:0] counter;
-  logic [COUNTER_WIDTH-1:0] counter_reg;
-  logic [TRACKER_LENGTH-1:0] tracker_valid_mask_inverted;
-  logic [TRACKER_LENGTH-1:0] insert_index_encoded;
-  logic [TRACKER_LENGTH-1:0] insert_index;
-  logic insert_complete;
-  logic insert_complete_reg;
-  // a full tracker entry consists of the tracker_valid, tracker_id, and the tracker_timestamp
-  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids;
-  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids_reg;
-  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids [0:TRACKER_LENGTH-1];
-  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids_reg [0:TRACKER_LENGTH-1];
-  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps [0:TRACKER_LENGTH-1];
-  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps_reg [0:TRACKER_LENGTH-1];
-  integer i;
-  integer j;
-  integer k;
-  integer a;
-
-  // if arvalid_i && arready_i, insert into a non-valid tracker entry and mark valid
-  // if rvalid_i && rlast_i && rready_i, find the valid entries in the tracker with matching IDs, and remove the oldest one
-
-  // inserting into the tracker
-  always @(*) begin
-    if (reset_i) begin
-      counter = counter_reg + 1;
-      insert_index_encoded = 0;
-      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
-      insert_complete = 0;
-      tracker_valid_mask_inverted = ~tracker_valids_reg;
-      // get lowest index that is not valid
-      insert_index_encoded = tracker_valid_mask_inverted & ~(tracker_valid_mask_inverted-1);
-      for (i=0; i<TRACKER_LENGTH; i=i+1) begin
-        if (insert_index_encoded[i]) begin
-          insert_index = i;
-        end
-      end
-      if (arvalid_i && arready_i) begin
-        insert_complete = insert_complete_reg;
-        if (!insert_complete_reg) begin
-          tracker_valids[insert_index] = 1;
-          tracker_ids[insert_index] = arid_i;
-          tracker_timestamps[insert_index] = counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2];
-          insert_complete = 1;
-        end
-      end
-    end else begin
-      counter = 0;
-      tracker_valid_mask_inverted = 0;
-      insert_index_encoded = 0;
-      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
-      insert_complete = 0;
-      tracker_valids = 0;
-    end
-  end
-
-  logic remove_complete;
-  logic [TRACKER_LENGTH-1:0] remove_index;
-  logic [TRACKER_LENGTH-1:0] remove_mask;
-
-  // removing from tracker
-  // if multiple entries in the tracker are valid, have the same ID, and have the same timestamp, the entry with the largest index will be removed
-  always @(*) begin
-    if (reset_i) begin
-      remove_complete = 0;
-      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
-      remove_mask = 0;
-      // check to see which tracker entries are valid and have a matching rid
-      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
-        if (tracker_valids_reg[j] && tracker_ids_reg[j] == rid_i) begin
-          remove_mask[j] = 1;
-        end
-      end
-      // check to see which valid tracker entries with matching rids are the oldest
-      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
-        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+1)%4 && remove_mask[j]) begin
-          remove_complete = 1;
-          remove_index = j;
-        end
-      end
-      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
-        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+2)%4 && remove_mask[j] && !remove_complete) begin
-          remove_complete = 1;
-          remove_index = j;
-        end
-      end
-      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
-        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+3)%4 && remove_mask[j] && !remove_complete) begin
-          remove_complete = 1;
-          remove_index = j;
-        end
-      end
-      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
-        if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+4)%4 && remove_mask[j] && !remove_complete) begin
-          remove_index = j;
-        end
-      end
-      if (rvalid_i && rlast_i && rready_i && (remove_index >= 0 && remove_index < TRACKER_LENGTH)) begin
-        tracker_valids[remove_index] = 0;
-      end
-    end else begin
-      remove_complete = 0;
-      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
-      remove_mask = 0;
-    end
-  end
-
-  // hang detection
-  `define IDLE 0
-  `define CHECK_FOR_HANG 1
-  logic hang_detection_state;
-  logic hang_detection_state_reg;
-
-  always @(*) begin
-    error_o = 0;
-    if (reset_i) begin
-      if (hang_detection_state_reg == `IDLE) begin
-        if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
-          hang_detection_state = `CHECK_FOR_HANG;
-        end
-      end else if (hang_detection_state_reg == `CHECK_FOR_HANG) begin
-        hang_detection_state = `IDLE;
-        for (k=0; k<TRACKER_LENGTH; k=k+1) begin
-          // if any tracker entry is valid and has a timestamp that matches the most significant 2 bits of the counter, throw hang error
-          if (tracker_valids_reg[k] && tracker_timestamps_reg[k]==counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
-            error_o = 1;
-          end
-        end
-      end
-    end else begin
-      hang_detection_state = `IDLE;
-    end
-  end
-
-  always @(posedge clk_i or negedge reset_i) begin
-    if (reset_i) begin
-      counter_reg <= counter;
-      insert_complete_reg <= insert_complete;
-      hang_detection_state_reg <= hang_detection_state;
-      tracker_valids_reg <= tracker_valids;
-      for (a=0; a<TRACKER_LENGTH; a=a+1) begin
-        tracker_ids_reg[a] <= tracker_ids[a];
-        tracker_timestamps_reg[a] <= tracker_timestamps[a];
-      end
-    end else begin
-      counter_reg <= 0;
-      insert_complete_reg <= 0;
-      hang_detection_state_reg <= `IDLE;
-      tracker_valids_reg <= 0;
-    end
-  end
-
-endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
index b95dda8806e..3d516172539 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh
@@ -31,7 +31,7 @@
 `include "chariot_ahb_hang_detector.sv"
 `include "chariot_wdat_ecc_generator.sv"
 `include "chariot_wdat_ecc_checker.sv"
-`include "chariot_axi_read_hang_detector.sv"
+`include "chariot_axi_hang_detector.sv"
 
 `include "uvm_macros.svh"
 
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 7cea969fa89..f8fa7d824a9 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -405,7 +405,7 @@ module interface_block
                         .RLAST                 (u_if.RLAST            ),
                         .RDATA                 (u_if.RDATA            ),
                         .RRESP                 ({1'b0,u_if.RRESP[1:0]}), //REVISIT_SANTHOSH: Remove after VIP-9636 is fixed
-                        .RUSER                 (RUSER_WIDTH > 0 ? u_if.RUSER[LOCAL_RUSER_WIDTH-1:0] : 1'b0      ), // 
+                        .RUSER                 (RUSER_WIDTH > 0 ? u_if.RUSER[LOCAL_RUSER_WIDTH-1:0] : 1'b0      ), //
                         .RTRACE                (u_if.RTRACE           ),
                         .RVALID                (IDM_SUPPORT ? shim_if.RVALID : u_if.RVALID           ),
                         .RREADY                (IDM_SUPPORT ? shim_if.RREADY : u_if.RREADY           ),
@@ -721,9 +721,10 @@ module interface_block
                         logic parity_err_rdat;
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
-                        logic hang_err_axi;
+                        logic hang_err_axi_write;
+                        logic hang_err_axi_read;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
-                        assign hang_error = hang_err_axi;
+                        assign hang_error = hang_err_axi_write | hang_err_axi_read;
                         assign ecc_error = 0;
                         chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
                           .data_i (u_if.WDATA),
@@ -758,17 +759,29 @@ module interface_block
                           .user_i (u_if.RUSER),
                           .error_o (parity_err_rdat)
                         );
-                        chariot_axi_read_hang_detector #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
+                        chariot_axi_hang_detector #(.ID_WIDTH(WID_WIDTH), .TRACKER_LENGTH(MAX_WRITES_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_write_hang_detector (
                           .clk_i(ACLK),
                           .reset_i(u_if.ARESETn),
-                          .arid_i(u_if.ARID),
-                          .arvalid_i(u_if.ARVALID),
-                          .arready_i(u_if.ARREADY),
-                          .rid_i(u_if.RID),
-                          .rvalid_i(u_if.RVALID),
-                          .rlast_i(u_if.RLAST),
-                          .rready_i(u_if.RREADY),
-                          .error_o(hang_err_axi)
+                          .aid_i(u_if.AWID),
+                          .avalid_i(u_if.AWVALID),
+                          .aready_i(u_if.AWREADY),
+                          .id_i(u_if.BID),
+                          .valid_i(u_if.BVALID),
+                          .last_i(1),
+                          .ready_i(u_if.BREADY),
+                          .error_o(hang_err_axi_write)
+                        );
+                        chariot_axi_hang_detector #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
+                          .clk_i(ACLK),
+                          .reset_i(u_if.ARESETn),
+                          .aid_i(u_if.ARID),
+                          .avalid_i(u_if.ARVALID),
+                          .aready_i(u_if.ARREADY),
+                          .id_i(u_if.RID),
+                          .valid_i(u_if.RVALID),
+                          .last_i(u_if.RLAST),
+                          .ready_i(u_if.RREADY),
+                          .error_o(hang_err_axi_read)
                         );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
@@ -1255,9 +1268,10 @@ module interface_block
                         logic parity_err_rdat;
                         logic parity_err_wrsp;
                         logic parity_err_rrsp;
-                        logic hang_err_axi;
+                        logic hang_err_axi_write;
+                        logic hang_err_axi_read;
                         assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
-                        assign hang_error = hang_err_axi;
+                        assign hang_error = hang_err_axi_write | hang_err_axi_read;
                         assign ecc_error = 0;
                         chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
                           .data_i (u_if.WDATA),
@@ -1292,17 +1306,29 @@ module interface_block
                           .user_i (u_if.RUSER),
                           .error_o (parity_err_rdat)
                         );
-                        chariot_axi_read_hang_detector #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
+                        chariot_axi_hang_detector #(.ID_WIDTH(WID_WIDTH), .TRACKER_LENGTH(MAX_WRITES_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_write_hang_detector (
+                          .clk_i(ACLK),
+                          .reset_i(u_if.ARESETn),
+                          .aid_i(u_if.AWID),
+                          .avalid_i(u_if.AWVALID),
+                          .aready_i(u_if.AWREADY),
+                          .id_i(u_if.BID),
+                          .valid_i(u_if.BVALID),
+                          .last_i(1),
+                          .ready_i(u_if.BREADY),
+                          .error_o(hang_err_axi_write)
+                        );
+                        chariot_axi_hang_detector #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
                           .clk_i(ACLK),
                           .reset_i(u_if.ARESETn),
-                          .arid_i(u_if.ARID),
-                          .arvalid_i(u_if.ARVALID),
-                          .arready_i(u_if.ARREADY),
-                          .rid_i(u_if.RID),
-                          .rvalid_i(u_if.RVALID),
-                          .rlast_i(u_if.RLAST),
-                          .rready_i(u_if.RREADY),
-                          .error_o(hang_err_axi)
+                          .aid_i(u_if.ARID),
+                          .avalid_i(u_if.ARVALID),
+                          .aready_i(u_if.ARREADY),
+                          .id_i(u_if.RID),
+                          .valid_i(u_if.RVALID),
+                          .last_i(u_if.RLAST),
+                          .ready_i(u_if.RREADY),
+                          .error_o(hang_err_axi_read)
                         );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
```

## 996cb7d4e7b7ab29b5478dd39bffaf0fe802495a

Classification: ordinary-commit; selected HEAD ancestry: True.

```diff
commit 996cb7d4e7b7ab29b5478dd39bffaf0fe802495a
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Thu Apr 8 00:41:40 2021 +0100
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Thu Apr 8 00:41:40 2021 +0100

    Fix latch in the AXI hang detector
    
    Change-Id: Ifb8e938f0786a15925ff87f3ebd2740f95bbf411

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
index c58da6bbcb9..fbc506180d8 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
@@ -134,6 +134,7 @@ module chariot_axi_hang_detector #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_W
     error_o = 0;
     if (reset_i) begin
       if (hang_detection_state_reg == `IDLE) begin
+        hang_detection_state = `IDLE;
         if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
           hang_detection_state = `CHECK_FOR_HANG;
         end
```

## 81dabe34f1c49adf6fd00e1ad5456c801f8f50b9

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit 81dabe34f1c49adf6fd00e1ad5456c801f8f50b9
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Mon Dec 9 19:54:03 2024 -0600
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Mon Dec 9 19:54:03 2024 -0600

    Testing Brunel 2024.rtl.0

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index 9b253077904..6e6f7684686 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "2024.11.19rh7test"
+setenv BRUNEL_VERSION "arm/brunel/2024.rtl.0"
 
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 
```

## ce7563ed91e6b163872d4b642b9d5a85298456cf

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit ce7563ed91e6b163872d4b642b9d5a85298456cf
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Mon Dec 9 19:56:32 2024 -0600
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Mon Dec 9 19:56:32 2024 -0600

    Testing Brunel 2024.rtl.0 fix typo

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index 6e6f7684686..58893e227e7 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "arm/brunel/2024.rtl.0"
+setenv BRUNEL_VERSION "2024.rtl.0"
 
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 
```

## 5047992d67b81c6d7098cac6e32ab96373847985

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit 5047992d67b81c6d7098cac6e32ab96373847985
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Mon Dec 9 20:12:09 2024 -0600
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Mon Dec 9 20:12:09 2024 -0600

    Testing Brunel 2024.rtl.0
    
    Change-Id: Ib5f4d1c44325a340999ce8407e7d515e9cdc781d

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index d8fe37b7b20..e6b8f2ec384 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "2024.11.19rh7test"
+setenv BRUNEL_VERSION "2024.rtl.0"
 
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 
```

## 4ecbc240850052ce6105a7bcde2745438539c0d1

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit 4ecbc240850052ce6105a7bcde2745438539c0d1
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Mon Dec 9 20:19:30 2024 -0600
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Mon Dec 9 20:19:30 2024 -0600

    Testing Brunel 2024.rtl.0
    
    Change-Id: Iebd2fca1c685edb73ad1558b3de5545212530ddf

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index 9b253077904..58893e227e7 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "2024.11.19rh7test"
+setenv BRUNEL_VERSION "2024.rtl.0"
 
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 
```

## 2971e359debd42c9831b7bc1b9aff08b650a36ee

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit 2971e359debd42c9831b7bc1b9aff08b650a36ee
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Tue Dec 10 10:39:34 2024 -0600
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Tue Dec 10 10:39:34 2024 -0600

    Testing Brunel 2024.rtl.0
    
    Change-Id: I937caccdb57a83e2e486e94c17469bf29e744052

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index ea15aaa7324..71e34d9ce7f 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "2024.12.00test"
+setenv BRUNEL_VERSION "2024.rtl.0"
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 module load eda arm/brunel/${BRUNEL_VERSION}
 
```

## c4454008e9b44b2045a71003484cc9d61d18c51a

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit c4454008e9b44b2045a71003484cc9d61d18c51a
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Mon Dec 16 17:34:47 2024 +0000
Commit:     Naveen Anumalla <naveen.anumalla@arm.com>
CommitDate: Tue Dec 17 11:59:39 2024 -0600

    Testing Brunel 2024.rtl.0
    
    Change-Id: Ic75c9a71ceb23bad95a056c627c959c872805f0b

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index a90cf8c3e75..71e34d9ce7f 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "2024.11.19rh7test"
+setenv BRUNEL_VERSION "2024.rtl.0"
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 module load eda arm/brunel/${BRUNEL_VERSION}
 
```

## 25e56dce89fd5bc49da9dc16a2ebad22b3c56246

Classification: ordinary-commit; selected HEAD ancestry: False.

```diff
commit 25e56dce89fd5bc49da9dc16a2ebad22b3c56246
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Tue Dec 17 16:36:58 2024 +0000
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Tue Dec 17 16:36:58 2024 +0000

    Testing Brunel 2024.rtl.0
    
    Change-Id: I771644d2785aa4de410321a5c0d9da2686e77050

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
index a90cf8c3e75..71e34d9ce7f 100644
--- a/logical/shared/scripts/end_to_end/load_brunel.sh
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -1,6 +1,6 @@
 #!/bin/tcsh
 
-setenv BRUNEL_VERSION "2024.11.19rh7test"
+setenv BRUNEL_VERSION "2024.rtl.0"
 setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
 module load eda arm/brunel/${BRUNEL_VERSION}
 
```

## 2ffec6bd4c8180b5089cc542fe4a195bcabbbb87

Classification: stash-working-tree; selected HEAD ancestry: False.

```diff
commit 2ffec6bd4c8180b5089cc542fe4a195bcabbbb87
Merge: 9e3dd54486e d9cbdcbc175
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Thu Aug 13 22:59:56 2026 -0500
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Thu Aug 13 22:59:56 2026 -0500

    On dev: codex-nitwain-vertical-arachne-workarounds-2026-08-13

diff --git a/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/asni_decoder.py b/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/asni_decoder.py
index 55c4dc2bef0..051be812d45 100644
--- a/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/asni_decoder.py
+++ b/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/asni_decoder.py
@@ -413,24 +413,26 @@ def build_request(_dataset, _cdata, _data, _instance, _region, _remap, _type) :
         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
           ublkRoute = route
           break
-      ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
-      _data[_instance]["unblock"][if_targets[x]] = {}
-      _data[_instance]["unblock"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
-      _data[_instance]["unblock"][if_targets[x]]["decode"] = ublkVector
-      if _debug:
-        print("\t      ublk - tgtID={:s} decode={:s}".format(str(_data[_instance]["unblock"][if_targets[x]]["target_id"]), str(_data[_instance]["unblock"][if_targets[x]]["decode"])))
+      if ublkRoute is not None:
+        ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
+        _data[_instance]["unblock"][if_targets[x]] = {}
+        _data[_instance]["unblock"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
+        _data[_instance]["unblock"][if_targets[x]]["decode"] = ublkVector
+        if _debug:
+          print("\t      ublk - tgtID={:s} decode={:s}".format(str(_data[_instance]["unblock"][if_targets[x]]["target_id"]), str(_data[_instance]["unblock"][if_targets[x]]["decode"])))
     if owo_stream and _region in areq_maps and _remap in areq_maps[_region]:
       areqRoute = None
       for route in areq_maps[_region][_remap]['areq']:
         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
           areqRoute = route
           break
-      areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
-      _data[_instance]["areq"][if_targets[x]] = {}
-      _data[_instance]["areq"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
-      _data[_instance]["areq"][if_targets[x]]["decode"] = areqVector
-      if _debug:
-        print("\t      areq - tgtID={:s} decode={:s}".format(str(_data[_instance]["areq"][if_targets[x]]["target_id"]), str(_data[_instance]["areq"][if_targets[x]]["decode"])))
+      if areqRoute is not None:
+        areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
+        _data[_instance]["areq"][if_targets[x]] = {}
+        _data[_instance]["areq"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
+        _data[_instance]["areq"][if_targets[x]]["decode"] = areqVector
+        if _debug:
+          print("\t      areq - tgtID={:s} decode={:s}".format(str(_data[_instance]["areq"][if_targets[x]]["target_id"]), str(_data[_instance]["areq"][if_targets[x]]["decode"])))
 
     if inst_target not in noc_configuration.configuration_functions.gt_targets[_instance]:
       noc_configuration.configuration_functions.gt_targets[_instance][inst_target] = {}
@@ -501,4 +503,3 @@ def build_bypass(_dataset, _cdata, _instance, _type, uniquify, nposted, _target_
 
   return empty_data
 
-
diff --git a/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/dsni_decoder.py b/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/dsni_decoder.py
index 7bc34336a0a..3fc350aaefa 100644
--- a/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/dsni_decoder.py
+++ b/logical/shared/scripts/noc_param_engine/noc_configuration/decoders/dsni_decoder.py
@@ -411,24 +411,26 @@ def build_request(_dataset, _cdata, _data, _instance, _region, _remap, _type) :
         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
           ublkRoute = route
           break
-      ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
-      _data[_instance]["unblock"][if_targets[x]] = {}
-      _data[_instance]["unblock"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
-      _data[_instance]["unblock"][if_targets[x]]["decode"] = ublkVector
-      if _debug:
-        print("\tublk - tgt_id={:s} decode={:s}".format(str(_data[_instance]["unblock"][if_targets[x]]["target_id"]), str(_data[_instance]["unblock"][if_targets[x]]["decode"])))
+      if ublkRoute is not None:
+        ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
+        _data[_instance]["unblock"][if_targets[x]] = {}
+        _data[_instance]["unblock"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
+        _data[_instance]["unblock"][if_targets[x]]["decode"] = ublkVector
+        if _debug:
+          print("\tublk - tgt_id={:s} decode={:s}".format(str(_data[_instance]["unblock"][if_targets[x]]["target_id"]), str(_data[_instance]["unblock"][if_targets[x]]["decode"])))
     if owo_stream and _region in areq_maps and _remap in areq_maps[_region]:
       areqRoute = None
       for route in areq_maps[_region][_remap]['areq']:
         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
           areqRoute = route
           break
-      areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
-      _data[_instance]["areq"][if_targets[x]] = {}
-      _data[_instance]["areq"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
-      _data[_instance]["areq"][if_targets[x]]["decode"] = areqVector
-      if _debug:
-        print("\tareq - tgt_id={:s} decode={:s}".format(str(_data[_instance]["areq"][if_targets[x]]["target_id"]), str(_data[_instance]["areq"][if_targets[x]]["decode"])))
+      if areqRoute is not None:
+        areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
+        _data[_instance]["areq"][if_targets[x]] = {}
+        _data[_instance]["areq"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
+        _data[_instance]["areq"][if_targets[x]]["decode"] = areqVector
+        if _debug:
+          print("\tareq - tgt_id={:s} decode={:s}".format(str(_data[_instance]["areq"][if_targets[x]]["target_id"]), str(_data[_instance]["areq"][if_targets[x]]["decode"])))
   # Perform stripe aliasing
 
   # When single target assign first element to all stripes
@@ -478,4 +480,3 @@ def build_bypass(_dataset, _cdata, _instance, _type, nposted) :
   return empty_data
 
 
-
diff --git a/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/arachne_asni_axi_core.py b/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/arachne_asni_axi_core.py
index 9bf110a279c..56a9c57df97 100644
--- a/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/arachne_asni_axi_core.py
+++ b/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/arachne_asni_axi_core.py
@@ -195,23 +195,38 @@ def dtm_route_derivation(_dataset):
   result = configuration_functions.connections_dataset[route]["route_vector"]
   return True, result
 
+def _owo_streaming_interfaces(_dataset):
+  component_misc = _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]
+  access_maps = component_misc.get("UblkAccessMaps", {})
+  credits = component_misc.get("UblkCredits", {})
+  if not access_maps or not credits:
+    return []
+
+  interfaces = noc_configuration.configuration_functions.get_access_maps_strip_ifs(
+    _dataset["config"], access_maps
+  )
+  return [intf for intf in interfaces if intf in credits]
+
+
 def owo_streaming_map_derivation(_dataset):
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
+  interfaces = _owo_streaming_interfaces(_dataset)
+  if not interfaces:
     return True, [0]
 
   tgtid_arr = []
-  for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
+  for intf in interfaces:
     inst_target = noc_configuration.configuration_functions.convert_interface(intf)
     tgtid = noc_configuration.interfaces.interface_common.get_comp_interface_id(_dataset["config"], intf, inst_target)
     tgtid_arr.append(tgtid)
   return True, tgtid_arr
 
 def owo_streaming_tgt_type_derivation(_dataset):
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
+  interfaces = _owo_streaming_interfaces(_dataset)
+  if not interfaces:
     return True, 0
 
   aux_vec = 0
-  for intf in reversed(noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"])):
+  for intf in reversed(interfaces):
     aux_vec <<= 1
     inst_target = noc_configuration.configuration_functions.convert_interface(intf)
     if _dataset["config"]["Instances"][inst_target]["componentInfo"]["componentType"] == "arachne_amni_axi_core":
@@ -222,18 +237,18 @@ def owo_streaming_tgt_type_derivation(_dataset):
   return True, aux_vec
 
 def owo_streaming_max_credit_acc_derivation(_dataset):
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
+  interfaces = _owo_streaming_interfaces(_dataset)
+  if not interfaces:
     return True, [0]
 
+  credits = _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkCredits"]
   cred_arr = []
-  for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
-    cred_arr.append(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkCredits"][intf])
+  for intf in interfaces:
+    cred_arr.append(credits[intf])
   return True, cred_arr
 
 def num_owo_streaming_tgt_derivation(_dataset)             :
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
-    return True, 0
-  result = len(noc_configuration.configuration_functions.get_access_maps_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]))
+  result = len(_owo_streaming_interfaces(_dataset))
 
   # Return computed value
   return True, result
diff --git a/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/noc_dsni_core.py b/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/noc_dsni_core.py
index 5353fe3137b..0d1436ab5f7 100755
--- a/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/noc_dsni_core.py
+++ b/logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/noc_dsni_core.py
@@ -237,12 +237,26 @@ def dtm_route_derivation(_dataset):
   result = configuration_functions.connections_dataset[route]["route_vector"]
   return True, result
 
+def _owo_streaming_interfaces(_dataset):
+  component_misc = _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]
+  access_maps = component_misc.get("UblkAccessMaps", {})
+  credits = component_misc.get("UblkCredits", {})
+  if not access_maps or not credits:
+    return []
+
+  interfaces = noc_configuration.configuration_functions.get_access_maps_strip_ifs(
+    _dataset["config"], access_maps
+  )
+  return [intf for intf in interfaces if intf in credits]
+
+
 def owo_streaming_tgt_type_derivation(_dataset):
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
+  interfaces = _owo_streaming_interfaces(_dataset)
+  if not interfaces:
     return True, 0
 
   aux_vec = 0
-  for intf in reversed(noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"])):
+  for intf in reversed(interfaces):
     aux_vec <<= 1
     inst_target = noc_configuration.configuration_functions.convert_interface(intf)
     if _dataset["config"]["Instances"][inst_target]["componentInfo"]["componentType"] == "arachne_amni_axi_core":
@@ -264,29 +278,30 @@ def streaming_credit_support_derivation(_dataset)             :
   return True, result
 
 def owo_streaming_map_derivation(_dataset):
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
+  interfaces = _owo_streaming_interfaces(_dataset)
+  if not interfaces:
     return True, [0]
 
   tgtid_arr = []
-  for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
+  for intf in interfaces:
     inst_target = noc_configuration.configuration_functions.convert_interface(intf)
     tgtid = noc_configuration.interfaces.interface_common.get_comp_interface_id(_dataset["config"], intf, inst_target)
     tgtid_arr.append(tgtid)
   return True, tgtid_arr
 
 def owo_streaming_max_credit_acc_derivation(_dataset):
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
+  interfaces = _owo_streaming_interfaces(_dataset)
+  if not interfaces:
     return True, [0]
 
+  credits = _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkCredits"]
   cred_arr = []
-  for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
-    cred_arr.append(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkCredits"][intf])
+  for intf in interfaces:
+    cred_arr.append(credits[intf])
   return True, cred_arr
 
 def num_owo_streaming_tgt_derivation(_dataset)             :
-  if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
-    return True, 0
-  result = len(noc_configuration.configuration_functions.get_access_maps_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]))
+  result = len(_owo_streaming_interfaces(_dataset))
 
   # Return computed value
   return True, result
diff --git a/logical/shared/scripts/sticho/sticho/StichoRender.py b/logical/shared/scripts/sticho/sticho/StichoRender.py
index fabea949940..d09586599af 100644
--- a/logical/shared/scripts/sticho/sticho/StichoRender.py
+++ b/logical/shared/scripts/sticho/sticho/StichoRender.py
@@ -2724,9 +2724,11 @@ class StichoRenderSDC( StichoRender ) :
                         self.sdc_global_iter += 1
 
 
-                    if (sdcObj["src_freq"] > sdcObj["dst_freq"]):
+                    src_freq_value = float(sdcObj["src_freq"])
+                    dst_freq_value = float(sdcObj["dst_freq"])
+                    if (src_freq_value > dst_freq_value):
                         start_end_flag = "-start"
-                    elif (sdcObj["dst_freq"] > sdcObj["src_freq"]):
+                    elif (dst_freq_value > src_freq_value):
                         start_end_flag = "-end"
                     else:
                         # Default flag if same frequency
```

## d9cbdcbc1751740ece9dd329bd5487f5423d4e75

Classification: stash-index; selected HEAD ancestry: False.

```diff
commit d9cbdcbc1751740ece9dd329bd5487f5423d4e75
Author:     Michael Coulter <michael.coulter@arm.com>
AuthorDate: Thu Aug 13 22:59:56 2026 -0500
Commit:     Michael Coulter <michael.coulter@arm.com>
CommitDate: Thu Aug 13 22:59:56 2026 -0500

    index on dev: 9e3dd54486e Merge R1 baseline into dev with replayed dev edits
```

