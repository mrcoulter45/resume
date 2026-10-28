# Locally captured Interconnect Architect Git and implementation evidence

Captured for Michael Coulter career research on 2026-10-27. PRIVATE: source paths, internal product terms and code excerpts are research evidence, not application copy.

Checkout HEAD: `e24d80378096cb8d7a0ad87c20929cb520fa49d7`. All reads use local Git objects; no fetch, builds, tests, generated docs or product mutations. Git author identity is attribution evidence, not sole ownership or employer verification.

Diffs below are explicit excerpts. Full selected diffs were captured in local scratch; key implementation hunks were reviewed; captured current excerpts retain original source line numbers. Current blame describes surviving lines, not total lifetime contribution. Blank-context acceptance definitions are not execution results.

## integration

### Commit bde8578f4858ffe38b25dfc814bd3cb777e4819d
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-01-24T18:02:59-06:00; reachable from selected HEAD: True.
Subject: Adding files for Socrates integration:
Change-Ids: I516c3cdd58609375a567fce9683bd085d7236953.
Diff excerpt, `scripts/socrates_integration/BrunelLauncher.py`:
```diff
@@ -0,0 +1,211 @@
+import logging
+import os
+import subprocess
+import sys
+import shutil
+
+from string import Template
+from pathlib import Path
+
+from lxml import etree
+
+from arm.ipcatalog.full.Process import IPCatalogOperation
+
+logger = logging.getLogger(__name__)
+
+class BrunelLauncher(IPCatalogOperation):
+    def __init__(self, project, catalog, properties):
+        super().__init__(project, catalog, properties)
+        self._operation_logger = None
+        self._operation_name = None
+        self._working_dir = None
+
+    def get_operation_logger(self):
+        return self._operation_logger
+
+    def run(self, configured, **kwargs):
+        command = []
+        env = dict()
+        self._project_yaml = None
+
+        env["DISPLAY"] = os.getenv("DISPLAY")
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `scripts/socrates_integration/CcxmlToIyml.py`:
```diff
@@ -0,0 +1,224 @@
+import logging
+import os
+import subprocess
+import sys
+import shutil
+
+from string import Template
+from pathlib import Path
+from lxml import etree
+from inspect import currentframe, getframeinfo
+
+# filename and line number info
+frameinfo = getframeinfo(currentframe())
+# get location and name of this script
+script_path = os.path.dirname(os.path.abspath(__file__))
+script_file_name = frameinfo.filename.split("/")[-1]
+# get location of ideas CE module
+ideas_ce_module_path = script_path + "/integration_build/CE"
+sys.path.append(ideas_ce_module_path)
+from arm.ipcatalog.full.Process import IPCatalogOperation
+from ideas.api.nci import Nci
+nci = Nci()
+
+logger = logging.getLogger(__name__)
+
+
+class CcxmlToIyml(IPCatalogOperation):
+    def __init__(self, project, catalog, properties):
+        super().__init__(project, catalog, properties)
+        self._operation_logger = None
+        self._operation_name = None
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `scripts/socrates_integration/JsonToCcxml.py`:
```diff
@@ -0,0 +1,248 @@
+import logging
+import os
+import subprocess
+import sys
+import shutil
+import json
+import hashlib
+
+from string import Template
+from pathlib import Path
+from lxml import etree
+from inspect import currentframe, getframeinfo
+
+# filename and line number info
+frameinfo = getframeinfo(currentframe())
+# get location and name of this script
+script_path = os.path.dirname(os.path.abspath(__file__))
+script_file_name = frameinfo.filename.split("/")[-1]
+
+from arm.ipcatalog.full.Process import IPCatalogOperation
+
+logger = logging.getLogger(__name__)
+
+class JsonToCcxml(IPCatalogOperation):
+    def __init__(self, project, catalog, properties):
+        super().__init__(project, catalog, properties)
+        self._operation_logger = None
+        self._operation_name = None
+        self._working_dir = None
+
+    def get_operation_logger(self):
[hunk excerpt ends; remaining lines omitted]
```
### Commit 9a9a6e9964ce5f3abebeee2463d4c290cdf615f0
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-02-04T13:32:10-06:00; reachable from selected HEAD: True.
Subject: Update CcxmlToIyml.py to allow for an IYML to be specified as part of IPCatalog creation wizard in Socrates
Change-Ids: I2160bd59d1b606df1fdffc71d3bd6eaf9facd166.
Diff excerpt, `scripts/socrates_integration/BrunelLauncher.py`:
```diff
@@ -34,46 +32,47 @@ class BrunelLauncher(IPCatalogOperation):
         env["XAUTHORITY"] = os.path.join(user_home, ".Xauthority")
 
         for key, value in kwargs.items():
-            if ( key == "PATH" or key == "LD_LIBRARY_PATH" or key == "PYTHONPATH" or key == "SYNTH_ENGINE" or key == "PERL5LIB" or key == "BE_PYTHONPATH"):
+            if (key == "PATH" or key == "LD_LIBRARY_PATH" or key == "PYTHONPATH" or key == "SYNTH_ENGINE" or key == "PERL5LIB" or key == "BE_PYTHONPATH"):
                 env[key] = value
-            elif ( key == "executable"):
+            elif (key == "executable"):
                 command.insert(0, value)
-            elif ( key == "build_dir"):
+            elif (key == "build_dir"):
                 print("The build directory is:" + value)
                 command.insert(1, value)
-            elif ( key == "config_file_path"):
+            elif (key == "config_file_path"):
                 self._project_yaml = value
                 yaml_arg = key + "=" + value
                 command.insert(2, yaml_arg)
                 print("This is the path to the yaml:" + yaml_arg)
-            elif ( key == "option"):
+            elif (key == "option"):
                 command.insert(3, value)
-            elif ( key == "debug"):
+            elif (key == "debug"):
                 command.insert(4, value)
-            elif ( key == "OperationName"):
+            elif (key == "OperationName"):
                 self._operation_name = value
-            elif ( key == "WorkingDir"):
+            elif (key == "WorkingDir"):
                 self._working_dir = value
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `scripts/socrates_integration/BrunelLauncher.py`:
```diff
@@ -81,41 +80,39 @@ class BrunelLauncher(IPCatalogOperation):
             else:
                 parameter = configured.get_parameter("PresetTemplate")
                 if (parameter is not None):
-                    project_init_command.insert(1, scriptDir + "/integration_build/brunel-linux-x64/resources/app/assets/scripts/project_init.py")
+                    project_init_command.insert(
+                        1, scriptDir + "/integration_build/brunel-linux-x64/resources/app/assets/scripts/project_init.py")
                     project_init_command.insert(2, "-e")
                     project_init_command.insert(3, parameter.get_value())
                     project_init_command.insert(4, self._project_yaml)
                     project_init_command.insert(5, name)
-                else:
-                    #IP has neither ExternalPath or Template parameter. The IP was not created through the IPCatalog creation wizard
-                    #but rather through the Interconnect Assistant
-                    print("TODO: need to call script to generate yaml from xml when IP is created from InterconnectAssistant flow")
 
-
-            #Run command to initialise project (create IYML in project/component folder)
-            self._operation_logger = OperationLogger(configured, self._operation_name)
+            # Run command to initialise project (create IYML in project/component folder)
+            self._operation_logger = OperationLogger(
+                configured, self._operation_name)
             if self._working_dir is not None:
                 print(project_init_command)
                 self.execute(project_init_command, env, self._working_dir)
             else:
                 self.execute(project_init_command, env, None)
 
-
-        #Get bundle location
-        association = configured.properties.get_association(configured.configurable)
+        # Get bundle location
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `scripts/socrates_integration/BrunelLauncher.py`:
```diff
@@ -135,10 +132,10 @@ class BrunelLauncher(IPCatalogOperation):
             # devnull = open(os.devnull, 'w')
             if working_dir is not None:
                 process = subprocess.Popen(command, env=environment, stdout=subprocess.PIPE,
-                                            stderr=subprocess.STDOUT, bufsize=-1, cwd=working_dir)
+                                           stderr=subprocess.STDOUT, bufsize=-1, cwd=working_dir)
             else:
                 process = subprocess.Popen(command, env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
-                                            bufsize=-1)
+                                           bufsize=-1)
 
             with process.stdout:
                 for line in iter(process.stdout.readline, b''):
```
### Commit 81689f1799fc07e1ce845cb7b8c8a211790b7187
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-05-22T14:01:04-05:00; reachable from selected HEAD: True.
Subject: IPTOOLING-14229: Display import error messages from Brunel (project_init.py) in Socrates
Change-Ids: Ia4adf6c8dfe2e7614b2554110df87ffacfedfcc0.
Diff excerpt, `resources/scripts/project_init.py`:
```diff
@@ -169,11 +169,11 @@ config_name = os.path.splitext(os.path.basename(args.outfile))[0]
 # =========================================
 # Print a summary before we start
 # =========================================
-print("\n\nRunning project_init.py\n\n")
-print("Template path : " + str(src_config_file))
-print("Output yaml   : " + str(args.outfile))
-print("Ip Version    : " + str(args.ipver))
-print("Config name   : " + str(config_name))
+print("\n\nRunning project_init.py\n\n", flush=True)
+print("Template path : " + str(src_config_file), flush=True)
+print("Output yaml   : " + str(args.outfile), flush=True)
+print("Ip Version    : " + str(args.ipver), flush=True)
+print("Config name   : " + str(config_name), flush=True)
 
 
 # =========================================
```
### Commit a08ab38bc571d160441c0593f5d68a7c4ca5a411
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-05-22T15:07:04-05:00; reachable from selected HEAD: True.
Subject: deprecate scripts/socrates_integration/BrunelLauncher.py
Change-Ids: I1d7751044bd72460bc1b7423fb997ac3bee3d275.
Diff excerpt, `scripts/socrates_integration/BrunelLauncher.py`:
```diff
@@ -1,233 +0,0 @@
-# ----------------------------------------------------------------------------
-# The confidential and proprietary information contained in this file may
-# only be used by a person authorised under and to the extent permitted
-# by a subsisting licensing agreement from Arm Limited or its affiliates.
-#
-# (C) COPYRIGHT 2020-2024 Arm Limited or its affiliates.
-# ALL RIGHTS RESERVED
-#
-# This entire notice must be reproduced on all copies of this file
-# and copies of this file may only be made by a person if such person is
-# permitted to do so under the terms of a subsisting license agreement
-# from Arm Limited or its affiliates.
-#
-# Release Information : $State$
-#
-# ----------------------------------------------------------------------------
-
-import logging
-import os
-import subprocess
-import sys
-import shutil
-
-from string import Template
-from pathlib import Path
-from lxml import etree
-from arm.ipcatalog.full.Process import IPCatalogOperation
-
-logger = logging.getLogger(__name__)
-
-class BrunelLauncher(IPCatalogOperation):
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `scripts/socrates_integration/BrunelLauncherDeprecated.py`:
```diff
@@ -0,0 +1,280 @@
+#----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2024 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#----------------------------------------------------------------------------
+
+# This copy of BrunelLauncher.py is now deprecated, the version that is used for Socrates integration is located here:
+# https://eu-gerrit-1.euhpc.arm.com/admin/repos/sipt/applications,general
+# applications/catalog/applications/brunel/r3p0/BrunelLauncher.py
+
+import logging
+import os
+import subprocess
+import sys
+import shutil
+
+from string import Template
+from pathlib import Path
+from lxml import etree
+
+from inspect import currentframe, getframeinfo
+
+# filename and line number info
[hunk excerpt ends; remaining lines omitted]
```
### Current source `scripts/socrates_integration/CcxmlToIyml.py`
Snapshot: HEAD; SHA-256 `356864db21b79d298bef74c2ac4bfe62945e6f64eb6525a6fda37c2a806c3d74`.
Surviving-line author counts (attribution context only): {'Christopher Alvarez': 16, 'lingao01': 1, 'Michael Coulter': 243, 'Kelly Alvarez': 3}.
Introduction/rename-follow candidates: bde8578f4858ffe38b25dfc814bd3cb777e4819d 2022-01-24T18:02:59-06:00 Michael Coulter <michael.coulter@arm.com> Adding files for Socrates integration: 	- application.xml 	- BrunelLauncher.py 	- CcxmlToIyml.py 	- JsonToCcxml.py.
```text
17: 
18: import logging
19: import os
20: import subprocess
21: import sys
22: import shutil
23: 
24: from string import Template
25: from pathlib import Path
26: from lxml import etree
27: from inspect import currentframe, getframeinfo
28: 
```
```text
87:         voltage_domains = configured.get_voltage_domains()
88:         power_domains = configured.get_power_domains()
89:         clock_domains = configured.get_clock_domains()
90:         domains_hierarchy_voltage = None
91:         domains_hierarchy_power = None
92:         domains_hierarchy_clock = None
93:         domains_hierarchy_clock_frequency = None
94:         if (len(voltage_domains) >= 1):
95:             for vd in voltage_domains:
96:                 domains_hierarchy_voltage = vd.get_name()
97:                 if (len(power_domains) >= 1):
98:                     for pd in power_domains:
99:                         if (pd.get_voltage_domain_ref() == vd.get_UID()):
100:                             domains_hierarchy_power = pd.get_name()
101:                             if (len(clock_domains) >= 1):
```
### Current source `scripts/socrates_integration/JsonToCcxml.py`
Snapshot: HEAD; SHA-256 `300f828852f7ffb0b0ae08a2caa4c7fc29dc1993b75d7623baad1c74a1dee1b9`.
Surviving-line author counts (attribution context only): {'Christopher Alvarez': 16, 'lingao01': 1, 'Michael Coulter': 245, 'Dustin Divis': 1}.
Introduction/rename-follow candidates: bde8578f4858ffe38b25dfc814bd3cb777e4819d 2022-01-24T18:02:59-06:00 Michael Coulter <michael.coulter@arm.com> Adding files for Socrates integration: 	- application.xml 	- BrunelLauncher.py 	- CcxmlToIyml.py 	- JsonToCcxml.py.
```text
17: 
18: import logging
19: import os
20: import subprocess
21: import sys
22: import shutil
23: import json
24: import hashlib
25: 
26: from string import Template
27: from pathlib import Path
28: from lxml import etree
```
```text
64:                 file.write(data)
65: 
66:         # sha256 hash function
67:         def hash_json_file(json_file_path):
68:             json_to_ccxml_log(f"{script_file_name}, {getframeinfo(currentframe()).lineno}: running hash_json_file\n")
69:             BUF_SIZE = 65536  # read file in 64kb chunks
70:             sha256 = hashlib.sha256()
71: 
72:             with open(json_file_path, 'rb') as f:
73:                 while True:
74:                     data = f.read(BUF_SIZE)
75:                     if not data:
76:                         break
```
```text
115:         config_rtl_connected_json_prev_hash = open(json_hashes_path).readlines()[0].strip()
116:         config_synth_instance_json_prev_hash = open(json_hashes_path).readlines()[1].strip()
117:         # get current json hashes
118:         config_rtl_connected_json_current_hash = hash_json_file(config_rtl_connected_json_path)
119:         config_synth_instance_json_current_hash = hash_json_file(config_synth_instance_json_path)
120:         # check if json hashes have changed, return if they have not. You can force the rest of this script to re-run by deleting "json_hashes.txt", will then pass the following if statement
121:         if ( (config_rtl_connected_json_prev_hash == config_rtl_connected_json_current_hash) and (config_synth_instance_json_prev_hash == config_synth_instance_json_current_hash) ):
122:             json_to_ccxml_log(f"{script_file_name}, {getframeinfo(currentframe()).lineno}: no changes in build output json files, exiting JsonToCcxml.py\n")
123:             return
124:         # overwrite old hashes
125:         json_hashes_file = open(json_hashes_path, 'w')
126:         json_hashes_file.write(config_rtl_connected_json_current_hash + "\n")
127:         json_hashes_file.write(config_synth_instance_json_current_hash + "\n")
```
### Current source `scripts/socrates_integration/BrunelLauncherDeprecated.py`
Snapshot: HEAD; SHA-256 `a4a3b1d36b628fc20cc9a576a427cbc10ade2fe16aca5448f26a68cce7c1decf`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 269, 'Christopher Alvarez': 11}.
Introduction/rename-follow candidates: bde8578f4858ffe38b25dfc814bd3cb777e4819d 2022-01-24T18:02:59-06:00 Michael Coulter <michael.coulter@arm.com> Adding files for Socrates integration: 	- application.xml 	- BrunelLauncher.py 	- CcxmlToIyml.py 	- JsonToCcxml.py.
```text
18: 
19: import logging
20: import os
21: import subprocess
22: import sys
23: import shutil
24: 
25: from string import Template
26: from pathlib import Path
27: from lxml import etree
28: 
29: from inspect import currentframe, getframeinfo
```
```text
105:             brunel_launcher_log_file.write(f"{script_file_name}, {getframeinfo(currentframe()).lineno}: IYML file does not exist generate IYML in project folder\n")
106: 
107:             templateYaml = None
108:             project_init_command = []
109:             project_init_command.insert(0, "python3")
110: 
111:             # get location of this script
112:             scriptDir = os.path.dirname(os.path.abspath(__file__))
113: 
114:             # Get name_shortVersion string
115:             configurable = configured.get_configurable()
116:             name = configurable.get_name() # use the brunelIPTable to return the brunel ipname
117:             if name is not None:
```
```text
126:                 brunel_launcher_log_file.write(f"{script_file_name}, {getframeinfo(currentframe()).lineno}: An IYML was specified as part of IPCatalog creation wizard {parameter.get_value()}\n")
127: 
128:                 # ExternalPath parameter takes precedence over PresetTemplate parameter
129:                 project_init_command.insert(
130:                     1, scriptDir + "/integration_build/resources/scripts/project_init.py")
131:                 project_init_command.insert(2, "-p")
132:                 project_init_command.insert(3, parameter.get_value())
133:                 project_init_command.insert(4, "-q")
134:                 project_init_command.insert(5, quality)
135:                 project_init_command.insert(6, self._project_yaml)
136:                 project_init_command.insert(7, name)
137: 
138:                 brunel_launcher_log_file.write(f"{script_file_name}, {getframeinfo(currentframe()).lineno}: Using ExternalPath parameter value, Command to execute create project yaml {' '.join(map(str, project_init_command))}\n")
```

## bitfields

### Commit 5cebeb111cf2f7fa49bba4c08b354e1c5a882a10
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-03-29T14:31:25-05:00; reachable from selected HEAD: True.
Subject: Add/integrate bitfield-input component for parameters that have a "bits" constraint
Change-Ids: I4ea6ee403e1dd4e55eec785962ebc6e7d3624a8d.
Diff excerpt, `GUI/src/app/shared/components/bitfield-input/bitfield-input.component.ts`:
```diff
@@ -0,0 +1,105 @@
+import { Component, OnInit, Input } from '@angular/core';
+import { FormControl, NG_VALUE_ACCESSOR, ControlValueAccessor } from '@angular/forms';
+
+@Component({
+  selector: 'app-bitfield-input',
+  templateUrl: './bitfield-input.component.html',
+  styleUrls: ['./bitfield-input.component.css'],
+  providers: [
+    {
+      provide: NG_VALUE_ACCESSOR,
+      multi: true,
+      useExisting: BitfieldInputComponent
+    }
+  ]
+})
+export class BitfieldInputComponent implements OnInit, ControlValueAccessor {
+  @Input() parameter: any;
+
+  vector_input : any[] = [];
+  output_value: number = 0;
+  disabled = false;
+
+  onChange = (value: number) => {};
+  onTouched = () => {};
+
+  constructor() {}
+
+  ngOnInit(): void {
+    this.output_value = this.parameter.value;
+    let parameter_bits : any[] = Object.values(this.parameter.bits);
+    let inserted = false;
[hunk excerpt ends; remaining lines omitted]
```
### Commit 759c72f0ec74fc97432265d66019ed3662d74fb3
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-10-11T10:48:16-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2536: Update GUI bitfield inputs to handle new retiming param format
Change-Ids: I629fe6f76f00f47940fe95b55c975bfa7f412fd0.
Diff excerpt, `GUI/src/app/canvas/canvas-sidebar/property-editor/canvas-instance-properties/canvas-instance-properties.component.ts`:
```diff
@@ -266,9 +266,11 @@ export class CanvasInstancePropertiesComponent implements OnInit, OnDestroy {
     }
     this.instanceResourcePlaneForm = new FormGroup(rpControls);
     /* Wiremode form */
+    this.currInstance['wiremode'] = 'none';
     const wiremodeControls: { [key: string]: AbstractControl } = {};
     if (this.validInstanceAttrs.includes('wireMode')) {
       wiremodeControls.wiremode = new FormControl(this.instanceInfo.info.wiremode.value, Validators.required);
+      this.currInstance['wiremode'] = this.instanceInfo.info.wiremode.value;
       if (['low', 'high'].includes(this.instanceInfo.info.wiremode.value)) {
         this.instanceInfo.info.wiremode.legalValues = ['low', 'high'];
       } else {
```
Diff excerpt, `GUI/src/app/shared/components/bitfield-input/bitfield-input.component.ts`:
```diff
@@ -16,6 +16,7 @@
 ***************************************************************************/
 import { Component, OnInit, Input } from '@angular/core';
 import { FormControl, NG_VALUE_ACCESSOR, ControlValueAccessor } from '@angular/forms';
+import cloneDeep from 'lodash/cloneDeep';
 
 @Component({
   selector: 'app-bitfield-input',
```
Diff excerpt, `GUI/src/app/shared/components/bitfield-input/bitfield-input.component.ts`:
```diff
@@ -31,6 +32,7 @@ import { FormControl, NG_VALUE_ACCESSOR, ControlValueAccessor } from '@angular/f
 })
 export class BitfieldInputComponent implements OnInit, ControlValueAccessor {
   @Input() parameter: any;
+  @Input() wiremode: any = null;
 
   vector_input: any[] = [];
   output_value: number = 0;
```
### Commit e2e685fb7e666d29b22982d370751c5cd7d9e8ae
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-12-06T16:47:04-06:00; reachable from selected HEAD: False.
Subject: update/fix IP-specific bits constraint in default-params and CE
Change-Ids: I83de6440aa3785a4303d250e4837bf83d786f9d1.
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -12736,184 +12739,188 @@
               },
             },
             bits: {
-              0: {
-                display: "Request Path/Ingress register",
-                mask: 0x1,
-                latency: {
-                  high: {
-                    readRequestPath: {
-                      asserted: 1,
-                      deasserted: 0,
+              "all": {
+                0: {
+                  display: "Request Path/Ingress register",
+                  mask: 0x1,
+                  latency: {
+                    high: {
+                      readRequestPath: {
+                        asserted: 1,
+                        deasserted: 0,
+                      },
                     },
-                  },
-                  low: {
-                    readRequestPath: {
-                      asserted: 1,
-                      deasserted: 0,
+                    low: {
+                      readRequestPath: {
+                        asserted: 1,
+                        deasserted: 0,
[hunk excerpt ends; remaining lines omitted]
```
### Current source `GUI/src/app/shared/components/bitfield-input/bitfield-input.component.ts`
Snapshot: HEAD; SHA-256 `24823557c5311b0c7e327ffc0d221cdb224038b1b17591bd508bdb005161af2b`.
Surviving-line author counts (attribution context only): {'Kelly Alvarez': 26, 'Michael Coulter': 84, 'Pawan Kakarla': 25, 'Dustin divis': 21}.
Introduction/rename-follow candidates: 5cebeb111cf2f7fa49bba4c08b354e1c5a882a10 2022-03-29T14:31:25-05:00 Michael Coulter <michael.coulter@arm.com> Add/integrate bitfield-input component for parameters that have a "bits" constraint Fixes for faulty validators.
```text
15: *
16: ***************************************************************************/
17: import { Component, OnInit, Input } from '@angular/core';
18: import { NG_VALUE_ACCESSOR, ControlValueAccessor } from '@angular/forms';
19: import { expandBitfieldDisplayEntries } from 'src/app/shared/utils/parameter-display.utils';
20: import { parameterLockReason } from 'src/app/shared/ce-policy/ce-policy';
21: 
22: @Component({
23:     selector: 'app-bitfield-input',
24:     templateUrl: './bitfield-input.component.html',
25:     styleUrls: ['./bitfield-input.component.css'],
26:     providers: [
```
```text
32:     ],
33:     standalone: false
34: })
35: export class BitfieldInputComponent implements OnInit, ControlValueAccessor {
36:   @Input() parameter: any;
37:   @Input() wiremode: any = null;
38: 
39:   vector_input: any[] = [];
40:   output_value = 0;
41:   disabled = false;
42:   private hasWrittenValue = false;
43:   readonly parameterLockReason = parameterLockReason;
44:   idFormatRegex = new RegExp("[/ ()]", "g");
45: 
```
```text
57:       const bit = {
58:         id: null,
59:         value: 0,
60:         mask: 0,
61:         desc: "",
62:         display: "",
63:         index: i,
64:       };
65:       bit.value = (this.output_value & (2 ** i)) >>> i;
66:       bit.mask = parameter_bits[i].mask;
67:       if (typeof bit.mask !== 'number') {
68:         bit.mask = bit.mask[this.wiremode]; // wiremode dependent mask, wiremode input must not be null here
69:       }
70:       bit.desc = parameter_bits[i].desc;
71:       if (parameter_bits[i].groupName) { // vector_input will contain multiple elements, one for each bit group
72:         bit_group_name = parameter_bits[i].groupName;
73:         bit.display = parameter_bits[i].visibleDisplay;
74:         for (const bitGroup of this.vector_input) { // check if bit group already exists
```
### Current source `GUI/src/app/shared/components/bitfield-input/bitfield-input.component.spec.ts`
Snapshot: HEAD; SHA-256 `e8b576bc23ceba51f7bc3ac9f3d1c4e10bcdc8bb082d4ad04ecc8476f9adb25a`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 85, 'Dustin divis': 42}.
Introduction/rename-follow candidates: 3287440c76c2ab24aceaee5b73ebcc42cda052dc 2026-07-29T13:20:27-05:00 Michael Coulter <michael.coulter@arm.com> Implement the NoC-Lite guided GUI flow; 5cebeb111cf2f7fa49bba4c08b354e1c5a882a10 2022-03-29T14:31:25-05:00 Michael Coulter <michael.coulter@arm.com> Add/integrate bitfield-input component for parameters that have a "bits" constraint Fixes for faulty validators.
```text
29:     bits: {
30:       0: {
31:         display: 'Ingress',
32:         mask: 1,
33:         desc: 'Ingress register'
34:       },
35:       1: {
36:         display: 'Internal',
37:         mask: 1,
38:         desc: 'Internal register'
39:       },
40:       2: {
41:         display: 'Reserved',
42:         mask: 0,
43:         desc: 'Reserved'
44:       }
45:     }
46:   };
47: 
48:   beforeEach(waitForAsync(() => {
49:     TestBed.configureTestingModule({
50:       declarations: [BitfieldInputComponent]
```
```text
70:     expect(checkboxes.every(checkbox => checkbox.disabled)).toBeTrue();
71:   });
72: 
73:   it('keeps masked bits disabled when the control is enabled', () => {
74:     component.setDisabledState(false);
75:     fixture.detectChanges();
76: 
77:     const checkboxes = Array.from<HTMLInputElement>(
78:       fixture.nativeElement.querySelectorAll('input[type="checkbox"]')
79:     );
80: 
81:     expect(checkboxes[0].disabled).toBeFalse();
```

## cmn-editor

### Commit 7996d5bb3a4bd9a7ed5836c8acb4013acc722c2c
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-06-14T13:36:11-05:00; reachable from selected HEAD: True.
Subject: Add node-configuration component
Change-Ids: I9b5ee888a7c51a872e155a6d95fc79c123f7d968.
Diff excerpt, `GUI/src/app/node-configuration/device-table/device-table.component.ts`:
```diff
@@ -0,0 +1,76 @@
+import { Component, NgModule, OnDestroy, OnInit, OnChanges, SimpleChanges, ViewChild, ChangeDetectorRef, AfterViewInit, Input, Output, EventEmitter, Directive, ViewContainerRef, ComponentFactoryResolver, ComponentRef } from "@angular/core";
+import { MatTable } from "@angular/material/table";
+import { PlaceholderDirective } from 'src/app/shared/directives/placeholder.directive';
+import { NodeConfigurationModalService } from '../node-configuration.modal.service';
+import {NodeConfigurationAddModalComponent} from '../node-configuration-add-modal/node-configuration-add-modal.component';
+
+@Component({
+  selector: "app-device-table",
+  templateUrl: "./device-table.component.html",
+  styleUrls: ["./device-table.component.css"]
+})
+export class DeviceTableComponent implements OnInit, OnChanges {
+  @Input() view: "data" | "config" | "error";
+  @Input() deviceTableSchema: any;
+  @Input() deviceTableHeading: string;
+  @Input() deviceParameters: any;
+  @Output() deviceGroupUpdateEmitter = new EventEmitter<any>();
+  @Output() deleteGroupEmitter = new EventEmitter<any>();
+
+  currentView: string = "";
+  showAddModal: boolean = false;
+  showParametersModal: boolean = false;
+  selectedAddDevice: string;
+  addFormInput: any;
+  existingDevice: any;
+
+  constructor(
+    private nodeConfigurationModalService: NodeConfigurationModalService,
+    private cdr: ChangeDetectorRef,
+  ) { }
+
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/node-configuration/node-configuration.component.ts`:
```diff
@@ -0,0 +1,3974 @@
+import { ChangeDetectorRef, Component, OnDestroy, OnInit } from '@angular/core';
+import { Subscription } from 'rxjs';
+import { NodeConfigurationService } from './node-configuration.service';
+import structuredClone from '@ungap/structured-clone';
+
+@Component({
+  selector: 'app-node-configuration',
+  templateUrl: './node-configuration.component.html',
+  styleUrls: ['./node-configuration.component.css']
+})
+export class NodeConfigurationComponent implements OnInit {
+  result: any = 0;
+  nodeObserv: any;
+  sidebarTabIndex: any;
+  networkType: string = "data";
+  networks: any = ["data", "chi", "error"];
+  deviceTableHeading: string = "Add Devices";
+  deviceTableSchema: any = [
+    {
+      button: "Add Requestor Nodes",
+      id: "requestorNodes",
+      addModalFields: [
+        {
+          label: "Group Name",
+          formControlName: "group",
+          desc: "Device group name",
+        }, {
+          label: "Device Type",
+          formControlName: "deviceType",
+          options: ["ccgs", "hnds", "hnfs", "hnis", "hnps", "hnss", "hnts", "hnvs", "master", "rnds", "rnis", "sbsxs", "slave"],
+          desc: "Group device type",
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/node-configuration/node-configuration.modal.service.ts`:
```diff
@@ -0,0 +1,194 @@
+/***************************************************************************
+* The confidential and proprietary information contained in this file may
+* only be used by a person authorised under and to the extent permitted
+* by a subsisting licensing agreement from Arm Limited or its affiliates.
+*
+* (C) COPYRIGHT 2021 Arm Limited or its affiliates.
+* ALL RIGHTS RESERVED
+*
+* This entire notice must be reproduced on all copies of this file
+* and copies of this file may only be made by a person if such person is
+* permitted to do so under the terms of a subsisting license agreement
+* from Arm Limited or its affiliates.
+*
+* Release Information : $State$
+*
+***************************************************************************/
+import { Injectable, ComponentFactoryResolver } from '@angular/core';
+
+import { Subscription, Observable } from 'rxjs';
+
+import { PlaceholderDirective } from '../shared/directives/placeholder.directive';
+
+import { NodeConfigurationAddModalComponent } from './node-configuration-add-modal/node-configuration-add-modal.component';
+
+@Injectable({
+  providedIn: 'root'
+})
+export class NodeConfigurationModalService {
+  // private closeModalSubscription: Subscription;
+
+  constructor() { }
[hunk excerpt ends; remaining lines omitted]
```
### Commit 1ff7b26ffd816acc1fbfabe4bb2b7e06d213f7fb
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-12-08T18:26:01-06:00; reachable from selected HEAD: True.
Subject: Rendering all devices/cal devices on logical canvas from API data
Change-Ids: I2d0084629bf89e58bec9d238ebc0ec678069063c.
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -1028,6 +1028,27 @@
         ],
       },
     },
+    cmn800_r3p0: {
+      tabs: {
+        uniqueLink: ["project", "global-mesh", "node-configuration", "canvas", "test-and-report", "build"],
+        order: ["Global Mesh Configuration", "Node Configuration", "Canvas", "Test & Report", "Build"]
+      },
+      canvas: {
+        floorplan: "logical",
+        designFlow: ["canvas-mesh-configuration", "canvas-toolbar", "canvas-palette-cmn"],
+        sideBar: ["canvas-visualizations", "instance-viewer", "property-editor", "route-editor"],
+        canvasTools: [
+          {
+            name: "pointer",
+            display: "Pointer",
+          },
+          {
+            name: "pan",
+            display: "Pan",
+          },
+        ],
+      },
+    },
     default: {
       tabs: {
         uniqueLink: ["project", "domains", "globals", "interfaces", "paths", "basic-traffic", "traffic", "memory-maps", "canvas", "test-and-report", "build"],
```
Diff excerpt, `GUI/src/app/canvas/canvas-design-flow/canvas-mesh-configuration/canvas-mesh-configuration.component.ts`:
```diff
@@ -10,23 +10,28 @@ import { CanvasLogicalService } from 'src/app/canvas/canvas-logical.service';
   styleUrls: ['./canvas-mesh-configuration.component.css']
 })
 export class CanvasMeshConfigurationComponent implements OnInit {
-  meshDimensions: any = {};
-  meshDimensionsForm: FormGroup;
+  meshDimensions: any;
+  meshDimensionsForm: FormGroup = new FormGroup({});
   meshDimensionOptions: any = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];
 
   constructor(
     private canvasLogicalService: CanvasLogicalService,
+    private cdr: ChangeDetectorRef,
   ) { }
 
   ngOnInit(): void {
-    this.meshDimensions = this.canvasLogicalService.getMeshDimensions();
-    this.createForm();
+    this.canvasLogicalService.meshDimensionsSubject.subscribe(resp => {
+      this.meshDimensions = resp;
+      console.log(this.meshDimensions);
+      this.createForm();
+      this.cdr.detectChanges();
+    });
   }
 
   private createForm() {
     const meshDimensionsFormControls = {};
-    meshDimensionsFormControls['x'] = new FormControl({value: this.meshDimensions.x, disabled: false}, [Validators.pattern('^[1-9]*$'), Validators.required]);
-    meshDimensionsFormControls['y'] = new FormControl({value: this.meshDimensions.y, disabled: false}, [Validators.pattern('^[1-9]*$'), Validators.required]);
+    meshDimensionsFormControls['x'] = new FormControl({value: this.meshDimensions.x, disabled: false}, [Validators.pattern('^[0-9]*$'), Validators.required]);
+    meshDimensionsFormControls['y'] = new FormControl({value: this.meshDimensions.y, disabled: false}, [Validators.pattern('^[0-9]*$'), Validators.required]);
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -17,22 +17,14 @@
 
 import { Component, OnDestroy, OnInit, AfterViewInit, ChangeDetectorRef } from '@angular/core';
 
-import { fromEvent, Subject } from 'rxjs';
+import { fromEvent, Subject, combineLatest } from 'rxjs';
 import { filter, map, pairwise, switchMap, takeUntil, tap } from 'rxjs/operators';
 
 import { CanvasStaticDataService } from 'src/app/canvas/shared/services/canvas-static-data.service';
-import { CanvasPhysicalService } from '../canvas-physical.service';
 import { CanvasLogicalService } from 'src/app/canvas/canvas-logical.service';
 import { CanvasConfigDataService } from '../shared/services/canvas-config-data.service';
 import { CanvasGuiDataService } from '../shared/services/canvas-gui-data.service';
-import { CanvasInstancesService } from '../shared/services/canvas-instances.service';
-import { CanvasSelectorsService } from '../shared/services/canvas-selectors.service';
-import { CanvasBlockagesService } from '../shared/services/canvas-blockages.service';
-import { CanvasInterfacesService } from '../shared/services/canvas-interfaces.service';
-import { CanvasConnectionsRoutesService } from '../shared/services/canvas-connections-routes.service';
 import { UiComponent } from 'src/app/shared/models/ui-info.model';
-import { Blockages } from 'src/app/shared/models/blockages.model';
-import { Coordinates } from 'src/app/shared/models/coordinates.model';
 import { CanvasConnection, Connections, NetworkType } from 'src/app/shared/models/connections.model';
 import { CanvasTool } from 'src/app/shared/models/canvas-tool.enum';
 import cloneDeep from 'lodash/cloneDeep';
```
### Commit 122a9594cf683d1f0cec7a856e5fe6dbbf0bc796
Author: Michael Coulter <michael.coulter@arm.com>; author date 2023-05-22T15:03:24-05:00; reachable from selected HEAD: True.
Subject: CMN: bulk GUI set-functionality updates
Change-Ids: Iac972241b9c672d04bec96f9bab5093ac2463820.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -146,6 +146,8 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
         this.canvasGuiDataService.viewBoxInfo = this.viewBox;
       });
     });
+    this.canvasLogicalService.getMeshDimensions();
+    this.canvasLogicalService.getInstances();
     const canvasInfoSub = combineLatest(
       this.canvasLogicalService.meshDimensionsSubject,
       this.canvasLogicalService.instancesSubject,
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -278,6 +280,8 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
             y1: this.meshOrigin + (((this.meshDimensions.y - 1) - y) * this.linkLength) + (crosspoint["height"] / 2),
             x2: (x * this.linkLength) + this.meshOrigin + (crosspoint["width"] / 2),
             y2: this.meshOrigin + (((this.meshDimensions.y - 1) - y) * this.linkLength) - this.linkLength + (crosspoint["height"] / 2),
+            // id: ,
+
           };
           newLinks.push(link);
         }
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -1130,7 +1134,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
   }
 
   configMcs(mcs) {
-    if (mcs.mcs_list.length === 0) {
+    if (mcs["slices"].length === 0) {
       return;
     }
     let mxpDownstreamX = Number(`0x${mcs.mxp_downstream[0]}`);
```
### Commit d951e149f26fc6349582361130bfa0906669ad77
Author: Michael Coulter <michael.coulter@arm.com>; author date 2023-11-14T17:18:06-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-1283: Logical canvas group editing features
Change-Ids: I3ec383abfb349ff36747f0b3c099aa0e68a1f79b.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -26,10 +26,13 @@ import { CanvasConfigDataService } from 'src/app/canvas/shared/services/canvas-c
 import { CanvasGuiDataService } from 'src/app/canvas/shared/services/canvas-gui-data.service';
 import { CanvasInstancesService } from 'src/app/canvas/shared/services/canvas-instances.service';
 import { CanvasSelectorsService } from 'src/app/canvas/shared/services/canvas-selectors.service';
+import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
+import { UserDefinedGroupService } from 'src/app/shared/services/user-defined-group.service';
 import { UiComponent } from 'src/app/shared/models/ui-info.model';
 import { CanvasConnection, Connections, NetworkType } from 'src/app/shared/models/connections.model';
 import { CanvasTool } from 'src/app/shared/models/canvas-tool.enum';
 import cloneDeep from 'lodash/cloneDeep';
+import { UserDefinedGroups } from 'src/app/shared/models/user-defined-group';
 
 @Component({
   selector: 'app-canvas-floorplan-logical',
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -46,6 +49,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
   private unsubscribe$: Subject<void> = new Subject<void>();
   private connectionsUnsubscribe$: Subject<void> = new Subject<void>();
   private draggablesUnsubscribe$: Subject<void> = new Subject<void>();
+  private unsubscribeAll: Subject<void> = new Subject<void>();
 
   viewBox = {x: 0, y: 0, width: 100, height: 100};
   canvasScale = 0;
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -127,6 +131,11 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
   zoomMin: number = 0.2;
   zoomMax: number = 0.9;
   zoomHideTextTimeout: any;
+  // user defined group variables
+  userDefinedGroups: UserDefinedGroups;
+  groupMemberOutlines: any = {};
+  currentGroupOutlined: string = null;
+
   private unlistener0: () => void;
   private unlistener1: () => void;
   private unlistener2: () => void;
```
### Current source `GUI/src/app/node-configuration/node-configuration.component.ts`
Snapshot: HEAD; SHA-256 `be02e46ba05b6bb9112bb02ecc38e2873b65c18c629a55ef86e8e04ba348d1c2`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 233, 'Pawan Kakarla': 7, 'Dustin Divis': 2, 'Kelly Alvarez': 24}.
Introduction/rename-follow candidates: 7996d5bb3a4bd9a7ed5836c8acb4013acc722c2c 2022-06-14T13:36:11-05:00 Michael Coulter <michael.coulter@arm.com> Add node-configuration component.
```text
3: import { takeUntil } from 'rxjs/operators';
4: import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
5: import { UserDefinedGroupService } from 'src/app/shared/services/user-defined-group.service';
6: import { CanvasLogicalDataService } from 'src/app/canvas/core/services/canvas-logical-data.service';
7: 
8: @Component({
9:     selector: 'app-node-configuration',
10:     templateUrl: './node-configuration.component.html',
11:     styleUrls: ['./node-configuration.component.css'],
12:     standalone: false
13: })
14: export class NodeConfigurationComponent implements OnInit, OnDestroy {
15:   expandableTableInput: any;
16:   showAddGroupModal = false;
17:   showGroupAttributesModal = false;
18:   showGroupParametersModal = false;
19:   showGroupMemberPortModal = false;
20:   showConfirmationModal: boolean;
21:   modalize = true;
22: 
23:   private unsubscribeAll: Subject<void> = new Subject<void>();
24: 
25:   constructor(
26:     private userDefinedGroupServiceAPI: UserDefinedGroupServiceAPI,
27:     private userDefinedGroupService: UserDefinedGroupService,
28:     private canvasLogicalDataService: CanvasLogicalDataService,
29:     private cdr: ChangeDetectorRef,
30:     private ngZone: NgZone,
31:   ) { }
32: 
33:   inputScrollPosition: number = this.userDefinedGroupService.nodeConfigurationTableScrollPosition;
34: 
35:   ngOnInit(): void {
36:     this.initExpandableTableInput(); // <- gets called twice, fix at some point
37:     this.init();
38:     this.setupSubscriptions();
39:   }
40: 
41:   ngOnDestroy(): void {
42:     this.unsubscribeAll.next(undefined);
43:     this.unsubscribeAll.complete();
44:   }
```
```text
47:     const nodeConfigInfoSub = combineLatest([
48:       this.userDefinedGroupServiceAPI.getUserDefinedGroupsSubject,
49:       this.userDefinedGroupServiceAPI.getInstanceDisplayNamesSubject
50:     ]).subscribe(([userDefinedGroups]) => { // instanceDisplayNamesMap is set in userDefinedGroupServiceAPI, needs to be called here
51:       nodeConfigInfoSub.unsubscribe();
52:       this.ngZone.run(() => {
53:         this.userDefinedGroupService.userDefinedGroups = userDefinedGroups;
54:         this.inputScrollPosition = this.userDefinedGroupService.nodeConfigurationTableScrollPosition;
55:         this.initExpandableTableInput(); // <- gets called twice, fix at some point
56:         this.createExpandableTableInput();
57:         this.userDefinedGroupService.addGroupButtonDisabled = false;
58:       });
```
### Current source `GUI/src/app/shared/components/group-attributes-modal/group-attributes-modal.component.ts`
Snapshot: HEAD; SHA-256 `43002e04031e963119cd60eb033f7ecc37094a8ec2430f4f29083a4b92514eb9`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 950, 'Pawan Kakarla': 8, 'Kelly Alvarez': 37, 'Dustin divis': 16}.
Introduction/rename-follow candidates: 4e82f9b9908b55699fb8fe6326c4a4dbe7db997d 2023-05-10T20:02:58-05:00 Michael Coulter <michael.coulter@arm.com> CMN: node config Add Group modal.
```text
32:   validInterfaceInstanceGroupings: any;
33:   meshInternalInterfaceConstraints: any;
34:   globalParametersInfo: any;
35:   meshInfo: any[] = [];
36:   emptyPorts: any;
37:   superDeviceConfig: any = { enabled: false, devices: {}, reserved_attributes: [] };
38:   instanceTypes: any;
39:   instanceDisplayNames: any;
40:   memberMax = 32;
41:   nonUniquePorts = false;
42:   submitButtonText: string;
43:   submitButtonDisabled = true;
```
```text
84:       this.userDefinedGroupServiceAPI.getValidInterfaceInstanceGroupingsSubject,
85:       this.userDefinedGroupServiceAPI.getMeshInternalInterfaceConstraintsSubject,
86:       this.userDefinedGroupServiceAPI.getGlobalParametersInfoSubject,
87:       this.userDefinedGroupServiceAPI.getMeshInfoSubject,
88:       this.userDefinedGroupServiceAPI.getAllEmptyPortsSubject,
89:       this.userDefinedGroupServiceAPI.getSuperDeviceConfigSubject,
90:       this.userDefinedGroupServiceAPI.getUserDefinedGroupInternalInterfaceConstraintsSubject
91:     ]).subscribe(([
92:       validInterfaceInstanceGroupings,
93:       meshInternalInterfaceConstraints,
94:       globalParametersInfo,
95:       meshInfo,
96:       emptyPorts,
97:       superDeviceConfig,
98:       groupInternalInterfaceConstraints
99:     ]) => {
100:       getInterfaceInfoSub.unsubscribe();
101:       this.ngZone.run(() => {
102:         this.validInterfaceInstanceGroupings = validInterfaceInstanceGroupings;
103:         this.globalParametersInfo = globalParametersInfo || {};
104:         this.meshInfo = Array.isArray(meshInfo) ? meshInfo : [];
105:         this.meshInternalInterfaceConstraints = this.mergeGroupInternalInterfaceConstraints(
106:           this.mergeSafeGlobalInternalInterfaceConstraints(meshInternalInterfaceConstraints),
107:           groupInternalInterfaceConstraints
108:         );
109:         this.emptyPorts = emptyPorts;
110:         this.superDeviceConfig = superDeviceConfig || { enabled: false, devices: {}, reserved_attributes: [] };
111:         this.initGroupInfo();
112:         this.createForm();
```
```text
117:     this.userDefinedGroupServiceAPI.getValidInterfaceInstanceGroupings();
118:     this.userDefinedGroupServiceAPI.getMeshInternalInterfaceConstraints();
119:     this.userDefinedGroupServiceAPI.getGlobalParametersInfo();
120:     this.userDefinedGroupServiceAPI.getMeshInfo();
121:     const cal = (this.userDefinedGroupService.infoForAttributesModal.cal === "None") ? null : this.userDefinedGroupService.infoForAttributesModal.cal.toLowerCase();
122:     this.userDefinedGroupServiceAPI.getAllEmptyPorts(cal);
123:     this.userDefinedGroupServiceAPI.getSuperDeviceConfig();
124:     if (this.userDefinedGroupService.infoForAttributesModal.mode === "edit") {
125:       this.userDefinedGroupServiceAPI.getUserDefinedGroupInternalInterfaceConstraints(
126:         this.userDefinedGroupService.infoForAttributesModal.groupName
127:       );
128:     } else {
```
### Current source `GUI/src/app/canvas/renderers/svg/logical-mesh/svg-logical-mesh-renderer.base.ts`
Snapshot: HEAD; SHA-256 `d64ab18b1e8a7005d381a8f4128d1d02d5cc3ac5141892857979cb0f448a3c11`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 2899, 'Pawan Kakarla': 8, 'Michael Coulter': 2494, 'Dustin divis': 27}.
Introduction/rename-follow candidates: b286908dff4f44fb05eba07e22dbe31807634144 2020-11-16T12:45:30-06:00 Dustin Divis <dustin.divis@arm.com> [GUI] Canvas: Adding intermediate canvas components.
```text
40: import { CanvasStaticMetadataService } from 'src/app/canvas/core/services/canvas-static-metadata.service';
41: import { CanvasToolCursorService } from 'src/app/canvas/core/services/canvas-tool-cursor.service';
42: import {
43:   CanvasLogicalDataService,
44:   DeadlockDirtyState,
45:   isNativeMcsImplementationUnitType,
46:   normalizeCalPortValue,
47: } from 'src/app/canvas/core/services/canvas-logical-data.service';
48: import { fitLabelFontSize } from 'src/app/canvas/core/utils/canvas-label.util';
49: import { CanvasViewStateService } from 'src/app/canvas/core/services/canvas-view-state.service';
50: import { CanvasSelectorsService } from 'src/app/canvas/core/services/canvas-selectors.service';
51: import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
52: import { UserDefinedGroupService } from 'src/app/shared/services/user-defined-group.service';
53: import { NavigationService } from 'src/app/shared/services/navigation.service';
54: import { TileService } from 'src/app/shared/services/tile.service';
55: import { InfoPopupService } from 'src/app/shared/services/info-popup.service';
```
```text
65: 
66: import { CanvasInteractionController } from 'src/app/canvas/core/interaction/canvas-interaction.controller';
67: import { fixNullAndInfinity } from 'src/app/canvas/core/utils/canvas-transform.util';
68: import { shouldRenderLogicalMeshGenericInstance } from 'src/app/canvas/core/utils/canvas-logical-mesh-render-visibility.util';
69: import {
70:   clearSvgLogicalMeshGroupMemberOutlines,
71:   drawSvgLogicalMeshGroupMemberOutlines,
72: } from './svg-logical-mesh-renderer.outlines';
73: import {
74:   MeshDeadlockChannelPayload,
75:   MeshDeadlockDeadlockedPair,
76:   MeshDeadlockPayload,
77:   MeshDeadlockTurnDetail,
78:   MeshDeadlockTurnRoute,
```

## cmn-tiles

### Commit dbcfdb561663d19eb96c6225ecde625f47da57b6
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-05-22T14:20:17-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2904 BRUNEL-3247: Tile Definition for CMN
Change-Ids: I70221696f59eba5b394925f22e82c9e55620ed3c.
Diff excerpt, `CE/ideas/ui-framesets.yaml`:
```diff
@@ -625,29 +629,32 @@
                     tooltip: "MCS Selection\nAllows the user to click and drag a selection box around multiple MCS to set their values simultaneously\nHotkey: S",
                     icon: {
                         type: "svg",
+                        offsetX: "-2.6px",
+                        offsetY: "4.5px",
                         rect: [
                             {
-                                x: "0.5",
-                                y: "0.5",
-                                width: "32.5",
-                                height: "22.75",
-                                style: "stroke: rgb(27,30,38); fill: transparent; stroke-dasharray: 4; stroke-width: 1.5px;",
+                                x: "0.494505",
+                                y: "0.494505",
+                                width: "27.5824",
+                                height: "19.011",
+                                style: "stroke: rgb(27,30,38); fill: transparent; stroke-dasharray: 3.3 3.3; stroke-width: 0.989011;",
                             },
                             {
                                 x: "0",
-                                y: "18.5",
-                                width: "10.4",
-                                height: "5.2",
+                                y: "14.5055",
+                                width: "15.3846",
+                                height: "5.49451",
                                 style: "fill: rgb(40,46,55);",
                             },
                         ],
-                        text: [
+                        path: [
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/ui-framesets.yaml`:
```diff
@@ -697,6 +712,51 @@
                         ]
                     }
                 },
+                flipHorizontal: {
+                    hotKey: "Y",
+                    tooltip: "Flip Horizontal\nWill flip selected item over the Y axis\nHotkey: Shift+Y",
+                    icon: {
+                        type: svg,
+                        offsetX: "1px",
+                        offsetY: "2.5px",
+                        path: [
+                            {
+                                d: "M7 22.7273H2.33333C1.69167 22.7273 1.14236 22.5047 0.685417 22.0597C0.228472 21.6146 0 21.0795 0 20.4545L0 4.54545C0 3.92045 0.228472 3.38542 0.685417 2.94034C1.14236 2.49527 1.69167 2.27273 2.33333 2.27273L7 2.27273V4.54545L2.33333 4.54545L2.33333 20.4545H7V22.7273ZM9.33333 25L9.33333 0L11.6667 0L11.6667 25H9.33333ZM14 22.7273L14 20.4545H16.3333V22.7273H14ZM14 4.54545L14 2.27273L16.3333 2.27273V4.54545L14 4.54545ZM18.6667 22.7273V20.4545H21C21 21.0795 20.7715 21.6146 20.3146 22.0597C19.8576 22.5047 19.3083 22.7273 18.6667 22.7273ZM18.6667 18.1818V15.9091H21V18.1818H18.6667ZM18.6667 13.6364V11.3636H21V13.6364H18.6667ZM18.6667 9.09091L18.6667 6.81818L21 6.81818L21 9.09091H18.6667ZM18.6667 4.54545V2.27273C19.3083 2.27273 19.8576 2.49527 20.3146 2.94034C20.7715 3.38542 21 3.92045 21 4.54545L18.6667 4.54545Z",
+                                style: "fill: rgb(40,46,55);"
+                            },
+                        ]
+                    }
+                },
+                flipVertical: {
+                    hotKey: "X",
+                    tooltip: "Flip Vertical\nWill flip selected item over the X axis\nHotkey: Shift+X",
+                    icon: {
+                        type: svg,
+                        offsetX: "-0.51px",
+                        offsetY: "4.4px",
+                        path: [
+                            {
+                                d: "M2.27273 7V2.33333C2.27273 1.69167 2.49526 1.14236 2.94034 0.685417C3.38542 0.228472 3.92045 0 4.54545 0L20.4545 0C21.0795 0 21.6146 0.228472 22.0597 0.685417C22.5047 1.14236 22.7273 1.69167 22.7273 2.33333V7L20.4545 7V2.33333L4.54545 2.33333V7L2.27273 7ZM-7.45058e-07 9.33333L25 9.33333L25 11.6667L-7.45058e-07 11.6667L-7.45058e-07 9.33333ZM2.27273 14H4.54545V16.3333H2.27273V14ZM20.4545 14H22.7273V16.3333H20.4545V14ZM2.27273 18.6667H4.54545V21C3.92045 21 3.38542 20.7715 2.94034 20.3146C2.49526 19.8576 2.27273 19.3083 2.27273 18.6667ZM6.81818 18.6667H9.09091V21H6.81818V18.6667ZM11.3636 18.6667H13.6364V21H11.3636V18.6667ZM15.9091 18.6667H18.1818V21H15.9091V18.6667ZM20.4545 18.6667H22.7273C22.7273 19.3083 22.5047 19.8576 22.0597 20.3146C21.6146 20.7715 21.0795 21 20.4545 21V18.6667Z",
+                                style: "fill: rgb(40,46,55);"
+                            },
+                        ]
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -2878,10 +2878,16 @@
         },
       },
     },
-    cmns3_r2p3: {
+    cmns3_r2p3: { # TODO: revert cmns3_r2p3 changes once we get the new CMN IP version
       tabs: {
-        uniqueLink: ["project", "mesh", "globals", "node-configuration", "canvas", "test-and-report", "build"],
-        order: ["Mesh", "Global Configuration", "Node Configuration", "Canvas", "Test & Report", "Build"]
+        noTiling: {
+          uniqueLink: ["project", "mesh", "globals", "node-configuration", "canvas", "test-and-report", "build"],
+          order: ["Mesh", "Global Configuration", "Node Configuration", "Canvas", "Test & Report", "Build"]
+        },
+        tiling: {
+          uniqueLink: ["project", "globals", "tile-definition", "tile-integration", "test-and-report", "build"],
+          order: ["Global Configuration", "Tile Definition", "Tile Integration", "Test & Report", "Build"]
+        }
       },
       canvas: {
         floorplan: ["logicalMesh"],
```
### Commit ffad4a69dc271816dfeedc2b927d71990cbafee1
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-05-30T15:30:59-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2905: Combined mesh view
Change-Ids: I081bb1fcd29ab4e4219cbb046fdf69429fcc48e1.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -119,7 +123,7 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
   private measurementContext: CanvasRenderingContext2D = this.measurementCanvas.getContext('2d')!;
 
   // tiling
-  currentTile: TileGroup | null;
+  currentTile: TileGroup | null = null;
 
   constructor(
     private ngZone: NgZone,
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -131,12 +135,18 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
     private canvasSelectorsService: CanvasSelectorsService,
     private userDefinedGroupServiceAPI: UserDefinedGroupServiceAPI,
     private userDefinedGroupService: UserDefinedGroupService,
+    private navigationService: NavigationService,
     private cdr: ChangeDetectorRef,
     private renderer2: Renderer2,
   ) { }
 
   ngOnInit(): void {
-    this.currentTile = this.canvasLogicalService.currentTile;
+    if (this.canvasGuiDataService.tiling) {
+      this.canvasGuiDataService.logicalMeshTileView = (this.navigationService.currentUrl === '/tile-definition') ? true : false;
+      if (this.canvasGuiDataService.logicalMeshTileView) {
+        this.currentTile = this.canvasLogicalService.currentTile;
+      }
+    }
     // console.log(`currentTile`);
     // console.log(this.currentTile);
     this.canvasInteraction.viewBox = this.canvasGuiDataService.viewBoxInfo;
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-tile-definition/canvas-floorplan-tile-definition.component.ts`:
```diff
@@ -63,6 +63,7 @@ export class CanvasFloorplanTileDefinitionComponent implements OnInit, AfterView
   TILE_UNIT_SIZE = 20;
   TEXT_RESOLUTION = 15;
   zIndexes = ['tile', 'triangle', 'tileNameText', 'overlapStripes', 'boundaryButton', 'hoverHighlight', 'selectionBox'];
+  initialLoad: boolean = true;
 
   // Spinner
   spinnerIsActive = false;
```
### Current source `GUI/src/app/tiling-configuration/tiling-configuration.component.ts`
Snapshot: HEAD; SHA-256 `61e83febc91366e8c051cbd9e2b5352dcf702458f8711a645fd5dba70760ca70`.
Surviving-line author counts (attribution context only): {'Dustin divis': 47, 'Dustin Divis': 42, 'Kelly Alvarez': 185, 'Pawan Kakarla': 4}.
Introduction/rename-follow candidates: cf7d962746e4ffd5134075393e487b1b11772efe 2023-08-31T10:09:12-05:00 Kelly Alvarez <kelly.alvarez@arm.com> Adding missing files.
```text
51:   init() {
52:     this.initExpandableTableInput();
53:     this.tilingConfigurationService.load().pipe(takeUntil(this.destroyed)).subscribe({
54:       error: error => console.error('Unable to read saved tile groups', error),
55:     });
56:   }
57: 
58:   private showSaved() {
59:     this.ngZone.run(() => {
60:       this.userDefinedGroups = this.tilingConfigurationService.groups;
61:       this.addGroupButtonValid = false;
62:       this.initExpandableTableInput();
```
### Current source `GUI/src/app/canvas/renderers/svg/tile-definition/svg-tile-definition-renderer.base.ts`
Snapshot: HEAD; SHA-256 `0d745513dc50e995efc18a3e2c4704549d4ec0b2566188b31d69b3b3f2128a17`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 894}.
Introduction/rename-follow candidates: dbcfdb561663d19eb96c6225ecde625f47da57b6 2025-05-22T14:20:17-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-2904 BRUNEL-3247: Tile Definition for CMN.
```text
1: // canvas-floorplan-tile-definition.component.ts
2: import { ChangeDetectorRef, Directive, ElementRef, NgZone, ViewChild } from '@angular/core';
3: import { Subject } from 'rxjs';
4: import { takeUntil } from 'rxjs/operators';
5: import { Application, Container, Graphics, Text } from 'pixi.js';
6: import { CanvasViewStateService } from 'src/app/canvas/core/services/canvas-view-state.service';
7: import { CanvasSelectorsService } from 'src/app/canvas/core/services/canvas-selectors.service';
8: import { CanvasLogicalDataService } from 'src/app/canvas/core/services/canvas-logical-data.service';
9: import { TileService } from 'src/app/shared/services/tile.service';
10: import { TileGroup, TileGroups, TileServiceAPI } from 'src/app/shared/services/tile.service.api';
11: import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
12: import { NavigationService } from 'src/app/shared/services/navigation.service';
13: import { CanvasTool } from 'src/app/shared/models/canvas-tool.enum';
14: import { SpinnerDisplay } from 'src/app/shared/models/spinner-display.model';
15: import { ProgressSpinnerMode } from '@angular/material/progress-spinner';
16: import cloneDeep from 'lodash/cloneDeep';
17: import { drawSvgTileDefinitionDiagonalStripes } from './svg-tile-definition-renderer.draw';
18: 
19: interface RectLike {
20:   x: number;
21:   y: number;
22:   width: number;
23:   height: number;
24: }
25: 
26: @Directive()
27: export class SvgTileDefinitionRendererBase {
28:   @ViewChild('pixiCanvas', { static: true }) protected canvasRef!: ElementRef<HTMLCanvasElement>;
29: 
30:   private app!: Application;
31:   private container!: Container;
32:   private resizeObserver!: ResizeObserver;
33:   private hoverHighlight!: Graphics;
34:   private lastHoveredTile: Container | null = null;
35:   private dragging = false;
```
### Current source `GUI/src/app/mesh/mesh.component.ts`
Snapshot: HEAD; SHA-256 `57886ebd97963bc7ff07ba2745acc1a525f6626fa867eaccf44200dd0a4d7f31`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 64, 'Dustin Divis': 2, 'Pawan Kakarla': 9, 'Kelly Alvarez': 1, 'Dustin divis': 1}.
Introduction/rename-follow candidates: 0dc0ea0701bdbcff412112d478bba354073817aa 2023-04-24T10:20:43-05:00 Michael Coulter <michael.coulter@arm.com> CMN: begin creation of set components.

## cmn-multiport

### Commit 5236c96147b0e3211477d33c461a4a1420e11d5a
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-01T22:49:20-05:00; reachable from selected HEAD: True.
Subject: Support super-device ports in group editing
Change-Ids: I0085dce55ede2a0e1bb70a0565f3be023e4404a2.
Diff excerpt, `GUI/src/app/canvas/ui/sidebar/group-editor/group-editor.component.spec.ts`:
```diff
@@ -1,16 +1,67 @@
+import { NO_ERRORS_SCHEMA } from '@angular/core';
 import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
+import { Subject } from 'rxjs';
 
+import { CanvasLogicalDataService } from 'src/app/canvas/core/services/canvas-logical-data.service';
+import { CanvasSelectorsService } from 'src/app/canvas/core/services/canvas-selectors.service';
+import { ModalService } from 'src/app/shared/services/modal.service';
+import { UserDefinedGroupService } from 'src/app/shared/services/user-defined-group.service';
+import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
 import { GroupEditorComponent } from './group-editor.component';
 
 describe('GroupEditorComponent', () => {
   let component: GroupEditorComponent;
   let fixture: ComponentFixture<GroupEditorComponent>;
+  let userDefinedGroupService: any;
 
   beforeEach(waitForAsync(() => {
+    userDefinedGroupService = {
+      userDefinedGroups: {},
+      addGroupButtonDisabled: false,
+      refreshSubject: new Subject<void>(),
+      setShowAddGroupModalSubject: new Subject<boolean>(),
+      setShowGroupAttributesModalSubject: new Subject<boolean>(),
+      setShowGroupParametersModalSubject: new Subject<boolean>(),
+      setShowGroupMemberPortModalSubject: new Subject<boolean>(),
+      setShowConfirmationModalSubject: new Subject<boolean>(),
+      createAttributesModalInput: jasmine.createSpy('createAttributesModalInput').and.returnValue({}),
+      nextToAttributes: jasmine.createSpy('nextToAttributes'),
+      nextToParameters: jasmine.createSpy('nextToParameters'),
+      refreshGroupViewer: jasmine.createSpy('refreshGroupViewer'),
+      addGroupMember: jasmine.createSpy('addGroupMember'),
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/ui/sidebar/group-editor/group-editor.component.spec.ts`:
```diff
@@ -22,4 +73,17 @@ describe('GroupEditorComponent', () => {
   it('should create', () => {
     expect(component).toBeTruthy();
   });
+
+  it('uses the Ports tab label only for selected super-device groups', () => {
+    userDefinedGroupService.userDefinedGroups = {
+      standard_group: { super_device: false },
+      dual_group: { super_device: true },
+    };
+
+    component.currentGroup = 'standard_group';
+    expect(component.currentGroupIsSuperDevice()).toBeFalse();
+
+    component.currentGroup = 'dual_group';
+    expect(component.currentGroupIsSuperDevice()).toBeTrue();
+  });
 });
```
Diff excerpt, `GUI/src/app/canvas/ui/sidebar/group-editor/group-editor.component.ts`:
```diff
@@ -248,6 +248,13 @@ export class GroupEditorComponent implements OnInit, OnDestroy {
     this.userDefinedGroupService.addGroupMember(info);
   }
 
+  currentGroupIsSuperDevice(): boolean {
+    if (!this.currentGroup) {
+      return false;
+    }
+    return this.userDefinedGroupService.userDefinedGroups?.[this.currentGroup]?.super_device === true;
+  }
+
   getConfirmationModalMsg() {
     return this.userDefinedGroupService.confirmationModalMsg;
   }
```
### Commit d98d6c2f9058186885304249cbcffcd51d46de3a
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-08T17:30:02-05:00; reachable from selected HEAD: True.
Subject: Delphi R1 updates: add Multi-CHI Port and advanced settings UI
Change-Ids: I460cc59a7712221aa76481715fa0d6e68f65e19a.
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -5850,6 +5850,11 @@
           logicalMesh: ["pointer", "pan", "selectionMcs", "zoomToInstance", "zoomToSelection", "refreshCanvas", "zoomToFit", "fullScreen"],
         },
       },
+      menuBar: {
+        advancedSettings: {
+          customAttributes: true
+        }
+      },
       console: {
         tabOrder: ["CONFIG", "BUILD", "DRC", "TERMINAL"]
       },
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -5868,6 +5873,11 @@
           logicalMesh: ["pointer", "pan", "selectionMcs", "zoomToInstance", "zoomToSelection", "refreshCanvas", "zoomToFit", "fullScreen"],
         },
       },
+      menuBar: {
+        advancedSettings: {
+          customAttributes: true
+        }
+      },
       console: {
         tabOrder: ["CONFIG", "BUILD", "DRC", "TERMINAL"]
       },
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -5886,6 +5896,11 @@
           logicalMesh: ["pointer", "pan", "selectionMcs", "zoomToInstance", "zoomToSelection", "refreshCanvas", "zoomToFit", "fullScreen"],
         },
       },
+      menuBar: {
+        advancedSettings: {
+          customAttributes: true
+        }
+      },
       console: {
         tabOrder: ["CONFIG", "BUILD", "DRC", "TERMINAL"]
       },
```
### Commit 55885d15452b3f8af975d724a94ad52095dc1784
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-07T14:01:54-05:00; reachable from selected HEAD: True.
Subject: Drive UDG Playwright coverage from live CE metadata
Change-Ids: I214d34ce5bc6444194c57e1a6304fb95cdf551d1.
Diff excerpt, `GUI/tests/fixtures/index.ts`:
```diff
@@ -4,7 +4,6 @@ import { test as electronTest } from './electron-fixtures-utils';
 import { InterconnectArchitect } from '../modules/ui/interconnect-architect';
 import { resolveIaOptions } from '../config/runtime-options';
 import { normalizeIpKey, capabilitiesForIp, NavigationCapabilities } from '../config/ip-capabilities';
-import fs from 'fs';
 import { startInactivityWatchdog, InactivityWatchdog } from '../modules/utils/inactivity-watchdog';
 
 interface IaConfig {
```
Diff excerpt, `GUI/tests/fixtures/index.ts`:
```diff
@@ -109,22 +107,6 @@ export const test = electronTest.extend<TestFixtures, WorkerFixtures>({
     await use(resolveConfigFromOptions(iaIp, iaTemplate));
   },
 
-  // eslint-disable-next-line no-empty-pattern
-  udgMeta: async ({}, use) => {
-    const metaPath = process.env.UDG_META_PATH;
-    if (metaPath && fs.existsSync(metaPath)) {
-      try {
-        const raw = fs.readFileSync(metaPath, 'utf-8');
-        const parsed = JSON.parse(raw);
-        await use(parsed);
-        return;
-      } catch (err) {
-        console.warn('[udgMeta] failed to read/parse', metaPath, err);
-      }
-    }
-    await use(undefined);
-  },
-
   capabilities: async ({ iaConfig }, use) => {
     await use(capabilitiesForIp(iaConfig.ip));
   },
```
Diff excerpt, `GUI/tests/modules/ui/canvas/canvas-assertions.ts`:
```diff
@@ -5,6 +5,30 @@ import { createClassLogger, ScopedLogger } from '../../utils/logger';
 
 const WAIT_OPTS = { timeout: Number(process.env.PW_EXPECT_TIMEOUT ?? 30_000) };
 type CanvasView = 'logical' | 'physical';
+interface UserDefinedGroupCanvasState {
+  memberCount: number;
+  rendered: {
+    id: string;
+    visible: boolean;
+    featureIds: string[];
+    visibleFeatureIds: string[];
+  }[];
+}
+export interface UserDefinedGroupCanvasDetailsState {
+  internalInterfaces: { id: string; text: string; visible: boolean; hasTypeText: boolean; hasValueText: boolean }[];
+  externalInterfaces: { id: string; visible: boolean }[];
+  dcs: { id: string; visible: boolean }[];
+  ccs: { id: string; text: string; visible: boolean; hasValueText: boolean }[];
+  calLabels: {
+    id: string;
+    text: string;
+    labelText: string;
+    expectedText: string;
+    visible: boolean;
+    hasLabelText: boolean;
+  }[];
+  missing: string[];
+}
 
 export class CanvasAssertions {
   private readonly page: Page;
```
### Commit ac9d282c943590a48a40a9c791531935f2eb6a44
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-28T16:56:59-05:00; reachable from selected HEAD: True.
Subject: Prevent duplicate user-defined group names
Change-Ids: I7508ac337a2a1fe6d1a6b41922f79bd8bd0ab73e.
Diff excerpt, `GUI/src/app/shared/components/add-group-modal/add-group-modal.component.spec.ts`:
```diff
@@ -10,6 +10,7 @@ import { ValidatorService } from 'src/app/shared/services/validator.service';
 describe('AddGroupModalComponent', () => {
   let component: AddGroupModalComponent;
   let fixture: ComponentFixture<AddGroupModalComponent>;
+  let userDefinedGroupServiceSpy: jasmine.SpyObj<UserDefinedGroupService>;
 
   beforeEach(waitForAsync(() => {
     const instanceCalCombinationsSubject = new Subject<any>();
```
Diff excerpt, `GUI/src/app/shared/components/add-group-modal/add-group-modal.component.spec.ts`:
```diff
@@ -39,9 +40,21 @@ describe('AddGroupModalComponent', () => {
       getSuperDeviceConfigSubject.next({ enabled: false, devices: {}, reserved_attributes: ['cid'] });
     });
 
-    const userDefinedGroupServiceSpy = jasmine.createSpyObj<UserDefinedGroupService>(
+    userDefinedGroupServiceSpy = jasmine.createSpyObj<UserDefinedGroupService>(
       'UserDefinedGroupService',
-      ['nextToAttributes', 'setShowAddGroupModal']
+      ['nextToAttributes', 'setShowAddGroupModal'],
+      {
+        userDefinedGroups: {
+          existing_group: {
+            attributes: {},
+            members: [],
+            parameters: {},
+            cal_type: null,
+            count: 0,
+            instance_type: [],
+          },
+        },
+      },
     );
 
     TestBed.configureTestingModule({
```
Diff excerpt, `GUI/src/app/shared/components/add-group-modal/add-group-modal.component.spec.ts`:
```diff
@@ -66,6 +79,18 @@ describe('AddGroupModalComponent', () => {
     expect(component).toBeTruthy();
   });
 
+  it('blocks adding a user-defined group whose name already exists', () => {
+    component.onFormChange('existing_group', 'groupName');
+    fixture.detectChanges();
+
+    const groupNameControl = component.addGroupForm.get('groupName');
+    expect(groupNameControl.errors?.userDefinedGroupAlreadyExists.msg)
+      .toBe('User defined group existing_group already exists.');
+    expect(fixture.nativeElement.querySelector('#group-name-exists-error').textContent.trim())
+      .toBe('User defined group existing_group already exists.');
+    expect(fixture.nativeElement.querySelector('#next-button').disabled).toBeTrue();
+  });
+
   it('does not add a Multi-CHI Port tooltip section when CE reports no valid devices', () => {
     component.superDeviceConfig = { enabled: false, devices: {}, reserved_attributes: ['cid'] };
     component.constructHeadingTooltip();
```
### Current source `GUI/src/app/shared/components/group-member-port-modal/group-member-port-modal.component.ts`
Snapshot: HEAD; SHA-256 `5b0d0f1bdfad2e63efca1d6375e2d60858ef7f5cb95fb326514ba0412f5d2268`.
Surviving-line author counts (attribution context only): {'Dustin divis': 19, 'Pawan Kakarla': 10, 'Michael Coulter': 149, 'Kelly Alvarez': 12}.
Introduction/rename-follow candidates: 122a9594cf683d1f0cec7a856e5fe6dbbf0bc796 2023-05-22T15:03:24-05:00 Michael Coulter <michael.coulter@arm.com> CMN: bulk GUI set-functionality updates.
```text
1: import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
2: import { Subject, takeUntil } from 'rxjs';
3: import { UntypedFormGroup, Validators, UntypedFormArray, UntypedFormBuilder, AbstractControl, ValidatorFn } from '@angular/forms';
4: 
5: import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
6: import { UserDefinedGroupService } from 'src/app/shared/services/user-defined-group.service';
7: 
8: @Component({
9:     selector: 'app-group-member-port-modal',
10:     templateUrl: './group-member-port-modal.component.html',
11:     styleUrls: ['./group-member-port-modal.component.css'],
12:     standalone: false
13: })
14: export class GroupMemberPortModalComponent implements OnInit, OnDestroy {
```
### Current source `GUI/src/app/shared/components/add-group-modal/add-group-modal.component.ts`
Snapshot: HEAD; SHA-256 `c7fb398ea62af805e4ba833347af13d99526cce337d7b4fc9beb6252fb064680`.
Surviving-line author counts (attribution context only): {'Pawan Kakarla': 10, 'Michael Coulter': 385, 'Kelly Alvarez': 21}.
Introduction/rename-follow candidates: 4e82f9b9908b55699fb8fe6326c4a4dbe7db997d 2023-05-10T20:02:58-05:00 Michael Coulter <michael.coulter@arm.com> CMN: node config Add Group modal.
```text
1: import { Component, OnInit, Output, EventEmitter, ChangeDetectorRef, NgZone } from '@angular/core';
2: import { combineLatest } from 'rxjs';
3: import { UntypedFormControl, UntypedFormGroup, Validators } from '@angular/forms';
4: 
5: import { UserDefinedGroupServiceAPI } from 'src/app/shared/services/user-defined-group.service.api';
6: import { UserDefinedGroupService } from 'src/app/shared/services/user-defined-group.service';
7: import { ValidatorService } from 'src/app/shared/services/validator.service';
8: 
9: @Component({
10:     selector: 'app-add-group-modal',
11:     templateUrl: './add-group-modal.component.html',
12:     styleUrls: ['./add-group-modal.component.css'],
13:     standalone: false
14: })
```
### Current source `GUI/tests/ui/user-defined-groups/user-defined-groups.spec.ts`
Snapshot: HEAD; SHA-256 `6e518f7c381e2d3230bda3ebe6387caf4c2bd533bfc3e73c5891793ad4b59564`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 320, 'Liza Dayoub': 19}.
Introduction/rename-follow candidates: 5f0efa4b9fd94b94c5f24c67994779ab1f3a44e4 2026-02-09T11:50:08-06:00 Liza Dayoub <liza.dayoub@arm.com> BRUNEL-3884 increase code coverage.
```text
16:  * each two-character CE type-prefix pattern.
17:  *
18:  * Every scenario follows the same GUI lifecycle:
19:  * 1. Create the group with one member and verify one logical-canvas member.
20:  * 2. Rename it by appending "0" and set applicable attributes: CAL credit
21:  *    slices to 2, CAL bypass enabled, the last nonzero A4S/AXU option, the
22:  *    first compatible external interface, and DCS to 4.
23:  * 3. For every distinct device and selected external interface, change up to
24:  *    five visible configurable parameters, or all available parameters when
25:  *    fewer than five exist, and verify them through get_user_defined_groups.
26:  * 4. Add a second member, move it to a third port, and verify the canvas member
27:  *    count remains correct.
28:  * 5. Reset attributes, delete the original member, delete the group, and
29:  *    verify the canvas transitions from two members to one to absent.
30:  * 6. Create a new normal (non-super-device) group with three members selected
31:  *    in the creation flow. Set every visible attribute to its maximum value,
32:  *    independently randomize up to five configurable parameters for every
33:  *    distinct device and selected external interface, verify the values
34:  *    through CE, and verify all three members and supported attribute details
35:  *    on the logical canvas.
36:  *    Device types with no configurable parameters still run the complete
37:  *    three-member maximum-attribute flow.
38:  *
39:  * Current ports selected from the loaded 4x4 example are:
40:  * - no CAL, CAL2, HCAL2: create at (0,0,p1), add at (0,0,p2), move to
41:  *   (0,0,p3).
42:  * - CAL4, HCAL3: create at (0,0,p1), add at (1,0,p1), move to (2,3,p1).
43:  *
```

## nci-canvas

### Commit e0a9fdd0159f724fcbf6988cfead60a55a282fed
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-01-14T08:59:34-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-1816, BRUNEL-2779: Logical canvas for NCI
Change-Ids: I2add2d8e8d496ce0eecb8c67a8f7e5359dde51f9.
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -238,6 +286,7 @@
             display: 'MCN',
             desc: 'MCN',
             tooltip: 'Memory controller node',
+            category: 'node',
             ui: {
               fill: 'grey',
               stroke: 'grey',
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -647,11 +767,17 @@
               {
                 d: "M 25.5 13 A 12.5 12.5 0 0 1 13 25.5 A 12.5 12.5 0 0 1 0.5 13 A 12.5 12.5 0 0 1 13 0.5 A 12.5 12.5 0 0 1 25.5 13 Z",
                 style: "fill: url(#routerGradient);",
+                fill: "url(#routerGradient)",
+                stroke: "none",
+                strokeWidth: 0,
                 transform: "",
               },
               {
                 d: "M 26 13 C 26 16.554 24.517 19.867 22.192 22.192 C 19.867 24.517 16.554 26 13 26 C 9.446 26 6.133 24.517 3.808 22.192 C 1.483 19.867 0 16.554 0 13 C 0 9.446 1.483 6.133 3.808 3.808 C 6.133 1.483 9.446 0 13 0 C 16.554 0 19.867 1.483 22.192 3.808 C 24.517 6.133 26 9.446 26 13 Z M 21.485 4.515 C 19.286 2.316 16.35 1 13 1 C 9.65 1 6.714 2.316 4.515 4.515 C 2.316 6.714 1 9.65 1 13 C 1 16.35 2.316 19.286 4.515 21.485 C 6.714 23.684 9.65 25 13 25 C 16.35 25 19.286 23.684 21.485 21.485 C 23.684 19.286 25 16.35 25 13 C 25 9.65 23.684 6.714 21.485 4.515 Z",
                 style: "fill: rgb(240, 101, 251);",
+                fill: "rgb(240, 101, 251)",
+                stroke: "none",
+                strokeWidth: 0,
                 transform: "",
               },
             ],
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -2294,51 +2494,13 @@
         basicTrafficTabs: ['data']
       },
       canvas: {
-        floorplan: "physical",
+        floorplan: ["physical", "logical"],
         designFlow: ["canvas-analysis-tools", "canvas-die-properties", "canvas-palette-hls", "canvas-palette-u-arch", "canvas-synth-constraints", "canvas-design-constraints", "canvas-toolbar"],
         sideBar: ["canvas-visualizations", "instance-viewer", "property-editor", "route-editor"],
-        canvasTools: [
-          {
-            name: "pointer",
-            display: "Pointer",
-          },
-          {
-            name: "pointerHLS",
-            display: "Pointer HLS",
-          },
-          {
-            name: "pointerInstance",
-            display: "Pointer Instance",
-          },
-          {
-            name: "pointerConnection",
-            display: "Pointer Connection",
-          },
-          {
-            name: "move",
-            display: "Move",
-          },
-          {
-            name: "moveHLS",
-            display: "Move HLS",
[hunk excerpt ends; remaining lines omitted]
```
### Commit 82ff7cdeea292d5f48f6b335a937e449a8bc1eeb
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-05-18T14:42:56-05:00; reachable from selected HEAD: True.
Subject: Rebuild logical canvas render model
Change-Ids: I37a769ee514ed9486c07a63b9507ba1fd9bda1b8.
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -245,6 +245,7 @@
             tooltip: 'Requester Interface',
             type: 'requesterInterface',
             category: 'interface',
+            logicalLayout: { bucket: 'managerInterface' },
             ui: {
               fill: '#ff0808',
               stroke: 'rgb(139, 0, 0)',
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -268,6 +269,7 @@
             tooltip: 'Completer Interface',
             type: 'completerInterface',
             category: 'interface',
+            logicalLayout: { bucket: 'subordinateInterface' },
             ui: {
               fill: '#3b7f22',
               stroke: 'rgb(0, 117, 0)',
```
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -291,6 +293,7 @@
             tooltip: 'Bidirectional Interface',
             type: 'bidirectionalInterface',
             category: 'interface',
+            logicalLayout: { bucket: 'managerInterface' },
             ui: {
               fill: 'rgb(246, 201, 68)',
               stroke: 'rgb(246, 201, 68)',
```
### Commit 155fd4ed9db7abd727c72c91db65472bc2180d73
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-05-18T14:43:33-05:00; reachable from selected HEAD: True.
Subject: Fix Route Editor candidate routing state
Change-Ids: Ibf3d0c10a0d99da67d90e142b9f04606a00363cc.
Diff excerpt, `GUI/src/app/canvas/core/services/canvas-connections.service.spec.ts`:
```diff
@@ -390,6 +390,27 @@ describe('CanvasConnectionsService', () => {
     expect(canvasInstancesService.updateInstancesClockCalls).toEqual([]);
     expect(canvasInstancesService.updateInstanceUpstreamDownstreamClocksCalls).toEqual([]);
   });
+  it('preserves CAL object-hop shape when fetching route candidates', () => {
+    const results: any[] = [];
+
+    service.fetchRouteCandidates('s_chi_dsu_0_if', 'm_mem_if_1').subscribe(candidates => results.push(candidates));
+
+    expect(dataService.brunelCEApiCalls[0].apiName).toBe('get_route_candidates');
+    expect(dataService.brunelCEApiCalls[0].args).toEqual([
+      true,
+      true,
+      's_chi_dsu_0_if',
+      'm_mem_if_1'
+    ]);
+
+    const ceCandidates = [[{ cal_0: 0 }, 'cdb_0', 'dcs_up_0', { cal_1: 1 }, 'mcn_1']];
+    dataService.brunelCEResponse.next({
+      id: dataService.brunelCEApiCalls[0].id,
+      res: ceCandidates
+    });
+
+    expect(results).toEqual([ceCandidates]);
+  });
 });
 
 describe('filterRouterOutputConnectionHighThroughputParams', () => {
```
Diff excerpt, `GUI/src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts`:
```diff
@@ -0,0 +1,43 @@
+import {
+  buildCanonicalCanvasRouteKey,
+  normalizeCanvasRouteHop
+} from './canvas-route-hop-normalization.util';
+
+describe('canvas route-hop normalization', () => {
+  it('uses the same canonical key for CAL string endpoints and object port hops', () => {
+    expect(buildCanonicalCanvasRouteKey(['cal_0(0)', 'cdb_0', 'cal_1(1)'])).toEqual(
+      buildCanonicalCanvasRouteKey([{ cal_0: 0 }, 'cdb_0', { cal_1: 1 }])
+    );
+  });
+
+  it('preserves CAL ports as display metadata', () => {
+    expect(normalizeCanvasRouteHop('cal_1(2)')).toEqual({
+      rawHop: 'cal_1(2)',
+      nodeName: 'cal_1',
+      endpoint: 'cal_1(2)',
+      canonicalKey: 'cal:cal_1:2',
+      routePort: '2',
+      channels: []
+    });
+
+    expect(normalizeCanvasRouteHop({ cal_1: 2 })).toEqual({
+      rawHop: { cal_1: 2 },
+      nodeName: 'cal_1',
+      endpoint: 'cal_1(2)',
+      canonicalKey: 'cal:cal_1:2',
+      routePort: 2,
+      channels: []
+    });
+  });
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/core/utils/canvas-route-hop-normalization.util.ts`:
```diff
@@ -0,0 +1,115 @@
+/***************************************************************************
+* The confidential and proprietary information contained in this file may
+* only be used by a person authorised under and to the extent permitted
+* by a subsisting licensing agreement from Arm Limited or its affiliates.
+*
+* (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+* ALL RIGHTS RESERVED
+*
+* This entire notice must be reproduced on all copies of this file
+* and copies of this file may only be made by a person if such person is
+* permitted to do so under the terms of a subsisting license agreement
+* from Arm Limited or its affiliates.
+*
+* Release Information : $State$
+*
+***************************************************************************/
+
+import { CanvasRouteHop, CanvasRouteHopList } from 'src/app/shared/models/canvas-path-info.model';
+import { extractCalName, extractCalPortInfo, isCalPort } from './canvas-cal.util';
+
+export interface NormalizedCanvasRouteHop {
+  rawHop: CanvasRouteHop;
+  nodeName: string;
+  endpoint: string;
+  canonicalKey: string;
+  routePort: string | number | null;
+  channels: string[];
+}
+
+export function normalizeCanvasRouteHop(hop: CanvasRouteHop): NormalizedCanvasRouteHop {
+  if (typeof hop === 'string') {
[hunk excerpt ends; remaining lines omitted]
```
### Current source `GUI/src/app/canvas/core/services/canvas-logical-layout.service.ts`
Snapshot: HEAD; SHA-256 `b169d1d583588497aa8760faa9167fb6cc013967be8e084b2fee61358e298f8a`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 421, 'Pawan Kakarla': 664, 'Michael Coulter': 1377, 'Dustin divis': 51}.
Introduction/rename-follow candidates: 3f5a7b2dec4f48426258dfd1a88080de29f3104e 2026-02-21T12:18:11-06:00 Dustin Divis <dustin.divis@arm.com> Phase A: reword commit later.
```text
14: import { LogicalRenderModel, LogicalSectionBand, LogicalSectionLabel } from 'src/app/canvas/core/models/logical-render.model';
15: import { CanvasRenderBounds } from 'src/app/canvas/core/models/canvas-render.model';
16: import { CanvasAutoPlacementAllocator } from 'src/app/canvas/core/utils/canvas-auto-placement.util';
17: import { getEdgePoint, getNodeCenter } from 'src/app/canvas/core/utils/canvas-connection-geometry.util';
18: import { extractCalName, extractCalPortInfo, isCalPort } from 'src/app/canvas/core/utils/canvas-cal.util';
19: import {
20:   buildLogicalRouteBucketHints,
21:   classifyLogicalNode,
22:   getLogicalLayoutBucketOrder,
23:   getLogicalLayoutSectionLabel,
24:   getLogicalLayoutSections,
25:   LogicalLayoutBucket,
26:   LogicalLayoutSectionDefinition,
27:   resolveLogicalNodeNetworks
28: } from 'src/app/canvas/core/utils/canvas-logical-layout-classifier.util';
29: import { buildCcgGroups, buildCcgRenderGroups, getCcgCandidateNodes, getCcgRenderedNodes, getLogicalCcgRole, isCxsOnlyCcgView, LogicalCcgRenderGroup, refreshCcgRenderGroupConnections, resolveLogicalCcgPrefix } from 'src/app/canvas/core/utils/canvas-logical-ccg.util';
30: import {
31:   isRenderableLogicalConnection,
```
### Current source `GUI/src/app/canvas/core/utils/canvas-logical-layout-classifier.util.ts`
Snapshot: HEAD; SHA-256 `e38a648d8b4c34bd4e2a9b8d1b476cc2d9a088f8a84beaa610cac7a93cbedc76`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 302}.
Introduction/rename-follow candidates: 82ff7cdeea292d5f48f6b335a937e449a8bc1eeb 2026-05-18T14:42:56-05:00 Michael Coulter <michael.coulter@arm.com> Rebuild logical canvas render model.
```text
1: import { NetworkType } from 'src/app/shared/models/connections.model';
2: import {
3:   getLogicalCcgRole,
4:   resolveLogicalCcgPrefix
5: } from 'src/app/canvas/core/utils/canvas-logical-ccg.util';
6: import { extractCalName, isCalPort } from 'src/app/canvas/core/utils/canvas-cal.util';
7: import { shouldRenderUiInfoComponent } from 'src/app/canvas/core/utils/canvas-render-visibility.util';
8: 
9: export type LogicalLayoutBucket =
10:   'subordinateInterface' |
11:   'subordinateDomainBridge' |
12:   'subordinateBridge' |
13:   'routing' |
14:   'managerBridge' |
15:   'managerDomainBridge' |
16:   'managerInterface' |
17:   'sidecar' |
18:   'hidden' |
19:   'groupedRouting';
20: 
21: export interface LogicalLayoutSectionDefinition {
22:   bucket: LogicalLayoutBucket;
23:   label: string;
24:   order?: number;
25: }
26: 
27: export interface LogicalNodeClassification {
28:   bucket: LogicalLayoutBucket;
29:   sectionLabel: string;
```

## renderers

### Commit 35d9937af5473b8cdc558edb68611e304ddbbe8d
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-06-22T23:35:22-05:00; reachable from selected HEAD: True.
Subject: Centralize canvas renderer metadata and behavior
Change-Ids: Ie085bcada8cc175b9f4142f9b0fd9c1b303322e7.
Diff excerpt, `CE/ideas/ui-framesets.yaml`:
```diff
@@ -425,95 +425,28 @@
                 pointer: {
                     hotKey: "p",
                     tooltip: "Pointer\nAllows the user to select any component on the canvas.\nUse Ctrl or Cmd for multi-selecting same type of instance or interface.\nHotkey: P",
+                    cursor: {
+                        value: "pointer"
+                    },
                     icon: {
                         type: "mat-icon",
-                        offsetX: "0px",
-                        offsetY: "0.5px",
+                        offsetX: "-1px",
+                        offsetY: "-1.5px",
+                        size: "23px",
                         matIcon: "touch_app"
                     }
                 },
-                # pointerHLS: {
-                #     hotKey: "h",
-                #     tooltip: "HLS Pointer\nAllows the user to select any HLS component on the canvas\nHotkey: H",
-                #     icon: {
-                #         type: "svg",
-                #         path: [
-                #             {
-                #                 x: "0",
-                #                 y: "0",
-                #                 d: "M9,11.24V7.5C9,6.12,10.12,5,11.5,5S14,6.12,14,7.5v3.74c1.21-0.81,2-2.18,2-3.74C16,5.01,13.99,3,11.5,3S7,5.01,7,7.5 C7,9.06,7.79,10.43,9,11.24z M18.84,15.87l-4.54-2.26c-0.17-0.07-0.35-0.11-0.54-0.11H13v-6C13,6.67,12.33,6,11.5,6 S10,6.67,10,7.5v10.74c-3.6-0.76-3.54-0.75-3.67-0.75c-0.31,0-0.59,0.13-0.79,0.33l-0.79,0.8l4.94,4.94 C9.96,23.83,10.34,24,10.75,24h6.79c0.75,0,1.33-0.55,1.44-1.28l0.75-5.27c0.01-0.07,0.02-0.14,0.02-0.2 C19.75,16.63,19.37,16.09,18.84,15.87z",
-                #                 style: "fill: rgb(40,46,55);",
-                #                 gTransform: "matrix(1.0476189851760864, 0, 0, 1.0476189851760864, -4.97619104385376, -3.1428580284118635)",
-                #                 pathTransform: "",
-                #             },
-                #         ],
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/ui-framesets.yaml`:
```diff
@@ -536,103 +469,70 @@
                         ],
                     }
                 },
-                # moveHLS: {
-                #     hotKey: "l",
-                #     tooltip: "HLS Move\nAllows the user to move any HLS component on the canvas via drag and drop\nHotkey: L",
-                #     icon: {
-                #         type: "svg",
-                #         path: [
-                #             {
-                #                 x: "0",
-                #                 y: "0",
-                #                 d: "M 17 24 L 11.9 18.9 L 13.61 17.19 L 15.8 19.38 L 15.8 14.4 L 18.2 14.4 L 18.2 19.35 L 20.36 17.16 L 22.1 18.9 L 17 24 Z M 10.1 17.1 L 5 12 L 10.07 6.93 L 11.78 8.64 L 9.62 10.8 L 14.6 10.8 L 14.6 13.2 L 9.65 13.2 L 11.84 15.36 L 10.1 17.1 Z M 23.9 17.1 L 22.19 15.39 L 24.38 13.2 L 19.4 13.2 L 19.4 10.8 L 24.35 10.8 L 22.16 8.64 L 23.9 6.9 L 29 12 L 23.9 17.1 Z M 15.8 9.6 L 15.8 4.62 L 13.61 6.81 L 11.9 5.1 L 17 0 L 22.1 5.1 L 20.39 6.81 L 18.2 4.62 L 18.2 9.6 L 15.8 9.6 Z",
-                #                 style: "fill: rgb(40,46,55);",
-                #                 gTransform: "",
-                #                 pathTransform: "",
-                #             },
-                #         ],
-                #         text: [
-                #             {
-                #                 x: "15.9",
-                #                 y: "30.439",
-                #                 style: "font-family: Arial, sans-serif; font-size: 8px; stroke-width: 0px; white-space: pre; fill: rgb(40,46,55);",
-                #                 transform: "",
-                #                 content: "HLS",
-                #             },
-                #         ],
-                #     }
-                # },
-                # moveInstance: {
-                #     hotKey: "e",
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/ui-framesets.yaml`:
```diff
@@ -656,6 +556,9 @@
                 },
                 global: {
                     tooltip: "Using a mouse: Scroll wheel to Zoom In/Out. Press wheel to pan.",
+                    cursor: {
+                        value: "help"
+                    },
                     icon: {
                         type: "mat-icon",
                         matIcon: "touch_app"
```
### Commit b1361c9f775374129b1b98fa709f148bf10a9d83
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-18T17:26:05-05:00; reachable from selected HEAD: True.
Subject: Fix CAL connector and route editor behavior
Change-Ids: I2be9fb98e7a69b398d41c2b6464c169cc0b579a1.
Diff excerpt, `GUI/package.json`:
```diff
@@ -42,7 +42,7 @@
     "test": "ng test",
     "test:spec:electron-karma": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts --karma-only",
     "test:runtime:electron": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts",
-    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/canvas.component.spec.ts --include=src/app/canvas/core/interaction/canvas-interaction.controller.spec.ts --include=src/app/canvas/core/renderers/logical/logical-renderer.driver.spec.ts --include=src/app/canvas/core/renderers/physical/physical-renderer.driver.spec.ts --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-expansion.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-input-interpreter.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/canvas-physical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-scene-model.service.spec.ts --include=src/app/canvas/core/services/canvas-spinner.service.spec.ts --include=src/app/canvas/core/services/canvas-static-metadata.service.spec.ts --include=src/app/canvas/core/services/canvas-tool-cursor.service.spec.ts --include=src/app/canvas/core/services/canvas-view-state.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/core/utils/canvas-transform.util.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts --include=src/app/canvas/renderers/svg/physical/svg-physical-renderer.base.spec.ts --include=src/app/canvas/ui/components/canvas-network-dropdown/canvas-network-dropdown.component.spec.ts --include=src/app/canvas/ui/components/component-node/instance-svg/instance-svg.component.spec.ts --include=src/app/canvas/ui/design-flow/canvas-toolbar/canvas-toolbar.component.spec.ts --include=src/app/canvas/ui/diff/canvas-diff.component.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-visualizations/canvas-visualizations.component.spec.ts --include=src/app/shared/components/svg-renderer/svg-renderer.component.spec.ts",
+    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/canvas.component.spec.ts --include=src/app/canvas/core/interaction/canvas-connector.tool.spec.ts --include=src/app/canvas/core/interaction/canvas-interaction.controller.spec.ts --include=src/app/canvas/core/renderers/logical/logical-renderer.driver.spec.ts --include=src/app/canvas/core/renderers/physical/physical-renderer.driver.spec.ts --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-route-highlight.service.spec.ts --include=src/app/canvas/core/services/canvas-route-state.service.spec.ts --include=src/app/canvas/core/services/canvas-selectors.service.spec.ts --include=src/app/canvas/core/services/canvas-expansion.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-input-interpreter.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/canvas-physical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-scene-model.service.spec.ts --include=src/app/canvas/core/services/canvas-renderer-context.service.spec.ts --include=src/app/canvas/core/services/canvas-spinner.service.spec.ts --include=src/app/canvas/core/services/canvas-static-metadata.service.spec.ts --include=src/app/canvas/core/services/canvas-tool-cursor.service.spec.ts --include=src/app/canvas/core/services/canvas-view-state.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/services/physical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-cal-endpoint.util.spec.ts --include=src/app/canvas/core/utils/canvas-connection-identity.util.spec.ts --include=src/app/canvas/core/utils/canvas-connection-style.util.spec.ts --include=src/app/canvas/core/utils/canvas-connector-policy.util.spec.ts --include=src/app/canvas/core/utils/canvas-nci-cal-route-usage.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/core/utils/canvas-transform.util.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.connector.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.connector.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts --include=src/app/canvas/renderers/svg/physical/svg-physical-renderer.base.spec.ts --include=src/app/canvas/ui/components/canvas-network-dropdown/canvas-network-dropdown.component.spec.ts --include=src/app/canvas/ui/components/component-node/instance-svg/instance-svg.component.spec.ts --include=src/app/canvas/ui/design-flow/canvas-toolbar/canvas-toolbar.component.spec.ts --include=src/app/canvas/ui/diff/canvas-diff.component.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-visualizations/canvas-visualizations.component.spec.ts --include=src/app/paths/path.service.api.spec.ts --include=src/app/shared/components/svg-renderer/svg-renderer.component.spec.ts",
     "test:spec:shell-synthesis": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.shell-synthesis.json --include=src/app/app.component.spec.ts --include=src/app/status-bar/export-dialog/export-dialog.component.spec.ts --include=src/app/status-bar/status-bar.component.spec.ts --include=src/app/shared/directives/native-panel-resize.directive.spec.ts --include=src/app/project --include=src/app/menu-bar/menu-bar.component.spec.ts --include=src/app/shared/services/nav-bar.utils.spec.ts --include=src/app/synthesis-constraints",
     "lint": "eslint --fix",
     "e2e": "ng e2e",
```
Diff excerpt, `GUI/src/app/canvas/core/interaction/canvas-connector.tool.spec.ts`:
```diff
@@ -73,4 +75,157 @@ describe('CanvasConnectorTool CAL geometry', () => {
 
     expect((tool as any).getConnectorEndpointId('s_nci_if_0')).toBe('mcn_0');
   });
+
+  it('dispatches eligible SVG scene endpoints through the shared connector policy', () => {
+    document.body.innerHTML = `
+      <svg id="test-canvas">
+        <path id="cal_0(1)" name="calPort"></path>
+        <path id="cal_1" name="calPort"></path>
+      </svg>
+    `;
+    const addConnectionWrapper = jasmine.createSpy('addConnectionWrapper');
+    const componentRef = {
+      editNetwork: NetworkType.chi,
+      currentFloorplanType: 'physical',
+      canvasElement: document.getElementById('test-canvas'),
+      cdr: { detectChanges: jasmine.createSpy('detectChanges') },
+      canvasService: { addConnectionWrapper },
+      canvasConnectionsService: { connections: { chi: { in_use: {}, not_in_use: {} } } },
+      instancesInfo: { cals: { cal_0: {}, cal_1: {} } },
+      getInstanceType: () => 'cals',
+      uiInfo: {},
+    };
+    const context = {
+      componentRef,
+      instanceAttrs: {
+        InstanceType: ['cals'],
+        ImplicitType: [],
+        InstanceNetworkType: { cals: ['chi'] },
+        ImplicitNetworkType: {},
+        PortCount: {},
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/core/interaction/canvas-connector.tool.ts`:
```diff
@@ -10,16 +11,30 @@ import {
   resolveLogicalMcnDisplayEndpointName,
   resolveLogicalMcnOwningEndpointName
 } from '../utils/canvas-logical-mcn.util';
+import {
+  buildCanvasConnectorConnection,
+  canvasConnectorConnectionExists,
+  CanvasConnectorConnectionBuckets,
+  CanvasConnectorEndpointSelection,
+  isCanvasConnectorEndpointEnabledForNetwork,
+  resolveCanvasConnectorEndpoint,
+  resolveCanvasConnectorCapacity,
+  validateCanvasConnectorCapacity,
+  validateCanvasConnectorEndpoints,
+  validateCanvasConnectorStartEndpoint,
+} from '../utils/canvas-connector-policy.util';
 
 export class CanvasConnectorTool {
   private connectionsUnsubscribe$ = new Subject<void>();
   private mouseConnectionUnsubscribe$ = new Subject<void>();
   private clickSubscriptions = new Map<HTMLElement, Subscription>();
+  private suppressedElementClicks = new Set<HTMLElement>();
+  private connectionStartEndpoint: CanvasConnectorEndpointSelection | null = null;
 
   constructor(private context: CanvasInteractionController) {}
 
   setupConnectionSubs(): void {
-    this.disableConnectionSubs();
+    this.clearConnectionClickSubscriptions();
 
     const instanceElements = document.getElementsByName('instance');
     let instType: string | null = null;
```
### Commit b2bdbf984870ee6846f4231644e4ab3e24c81cf4
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-10-03T21:49:48-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-4855: Fix CAL/MCN connectivity and route rendering across SVG and Pixi
Change-Ids: I2f876eaa7846a82a9026fa89d61d9eca62c8a09b.
Diff excerpt, `GUI/package.json`:
```diff
@@ -44,7 +44,7 @@
     "test": "ng test",
     "test:spec:electron-karma": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts --karma-only",
     "test:runtime:electron": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts",
-    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/canvas.component.spec.ts --include=src/app/canvas/core/interaction/canvas-connector.tool.spec.ts --include=src/app/canvas/core/interaction/canvas-interaction.controller.spec.ts --include=src/app/canvas/core/interaction/canvas-polygon.tool.spec.ts --include=src/app/canvas/core/renderers/logical/logical-renderer.driver.spec.ts --include=src/app/canvas/core/renderers/physical/physical-renderer.driver.spec.ts --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-route-highlight.service.spec.ts --include=src/app/canvas/core/services/canvas-route-state.service.spec.ts --include=src/app/canvas/core/services/canvas-selectors.service.spec.ts --include=src/app/canvas/core/services/canvas-expansion.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-input-interpreter.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/canvas-physical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-scene-model.service.spec.ts --include=src/app/canvas/core/services/canvas-renderer-context.service.spec.ts --include=src/app/canvas/core/services/canvas-spinner.service.spec.ts --include=src/app/canvas/core/services/canvas-static-metadata.service.spec.ts --include=src/app/canvas/core/services/canvas-tool-cursor.service.spec.ts --include=src/app/canvas/core/services/canvas-view-state.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/services/subsection-connectivity-scene.service.spec.ts --include=src/app/canvas/core/services/physical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-cal-endpoint.util.spec.ts --include=src/app/canvas/core/utils/canvas-connection-identity.util.spec.ts --include=src/app/canvas/core/utils/canvas-connection-style.util.spec.ts --include=src/app/canvas/core/utils/canvas-connector-policy.util.spec.ts --include=src/app/canvas/core/utils/canvas-nci-cal-route-usage.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/core/utils/canvas-transform.util.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.connector.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.connector.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts --include=src/app/canvas/renderers/svg/physical/svg-physical-renderer.base.spec.ts --include=src/app/canvas/ui/components/canvas-network-dropdown/canvas-network-dropdown.component.spec.ts --include=src/app/canvas/ui/components/subsection-boundary-name-modal/subsection-boundary-name-modal.component.spec.ts --include=src/app/canvas/ui/components/component-node/instance-svg/instance-svg.component.spec.ts --include=src/app/canvas/ui/design-flow/canvas-toolbar/canvas-toolbar.component.spec.ts --include=src/app/canvas/ui/diff/canvas-diff.component.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-visualizations/canvas-visualizations.component.spec.ts --include=src/app/paths/path.service.api.spec.ts --include=src/app/shared/components/svg-renderer/svg-renderer.component.spec.ts",
+    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/canvas.component.spec.ts --include=src/app/canvas/core/interaction/canvas-connector.tool.spec.ts --include=src/app/canvas/core/interaction/canvas-interaction.controller.spec.ts --include=src/app/canvas/core/interaction/canvas-polygon.tool.spec.ts --include=src/app/canvas/core/renderers/logical/logical-renderer.driver.spec.ts --include=src/app/canvas/core/renderers/physical/physical-renderer.driver.spec.ts --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-route-highlight.service.spec.ts --include=src/app/canvas/core/services/canvas-route-state.service.spec.ts --include=src/app/canvas/core/services/canvas-selectors.service.spec.ts --include=src/app/canvas/core/services/canvas-expansion.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-input-interpreter.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/canvas-physical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-scene-model.service.spec.ts --include=src/app/canvas/core/services/canvas-renderer-context.service.spec.ts --include=src/app/canvas/core/services/canvas-spinner.service.spec.ts --include=src/app/canvas/core/services/canvas-static-metadata.service.spec.ts --include=src/app/canvas/core/services/canvas-tool-cursor.service.spec.ts --include=src/app/canvas/core/services/canvas-view-state.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/services/subsection-connectivity-scene.service.spec.ts --include=src/app/canvas/core/services/physical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-cal-endpoint.util.spec.ts --include=src/app/canvas/core/utils/canvas-connection-identity.util.spec.ts --include=src/app/canvas/core/utils/canvas-connection-style.util.spec.ts --include=src/app/canvas/core/utils/canvas-connector-policy.util.spec.ts --include=src/app/canvas/core/utils/canvas-nci-cal-route-usage.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-mcn-connectivity.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/core/utils/canvas-transform.util.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.connector.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.connector.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts --include=src/app/canvas/renderers/svg/physical/svg-physical-renderer.base.spec.ts --include=src/app/canvas/ui/components/canvas-network-dropdown/canvas-network-dropdown.component.spec.ts --include=src/app/canvas/ui/components/subsection-boundary-name-modal/subsection-boundary-name-modal.component.spec.ts --include=src/app/canvas/ui/components/component-node/instance-svg/instance-svg.component.spec.ts --include=src/app/canvas/ui/design-flow/canvas-toolbar/canvas-toolbar.component.spec.ts --include=src/app/canvas/ui/diff/canvas-diff.component.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-visualizations/canvas-visualizations.component.spec.ts --include=src/app/paths/path.service.api.spec.ts --include=src/app/shared/components/svg-renderer/svg-renderer.component.spec.ts",
     "test:spec:cmn-routing": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.cmn-routing.json --include=src/app/mesh/base-routing/base-routing.component.spec.ts --include=src/app/shared/components/routing-scheme-modal/routing-scheme-modal.component.spec.ts --include=src/app/canvas/ui/sidebar/mesh-route-editor/mesh-route-editor.component.spec.ts --include=src/app/canvas/ui/sidebar/mesh-deadlock/mesh-deadlock.component.spec.ts --include=src/app/canvas/core/services/canvas-logical-data.service.spec.ts --include=src/app/canvas/renderers/svg/logical-mesh/svg-logical-mesh-renderer.base.spec.ts --include=src/app/canvas/canvas.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-visualizations/canvas-visualizations.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-sidebar.component.spec.ts",
     "test:spec:shell-synthesis": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.shell-synthesis.json --include=src/app/app.component.spec.ts --include=src/app/status-bar/export-dialog/export-dialog.component.spec.ts --include=src/app/status-bar/status-bar.component.spec.ts --include=src/app/shared/directives/native-panel-resize.directive.spec.ts --include=src/app/project --include=src/app/menu-bar/menu-bar.component.spec.ts --include=src/app/shared/services/nav-bar.utils.spec.ts --include=src/app/synthesis-constraints",
     "lint": "eslint --fix",
```
Diff excerpt, `GUI/src/app/canvas/core/interaction/canvas-connector.tool.spec.ts`:
```diff
@@ -78,10 +78,58 @@ describe('CanvasConnectorTool CAL geometry', () => {
   it('uses ui-info dynamic CAL port metadata for generated connector paths', () => {
     const tool = createTool();
 
-    expect(tool.genConnectionSvgPath('cal_0(2)', 'router_0')).toBe('M31,38 110,32.5');
+    expect(tool.genConnectionSvgPath('cal_0(2)', 'router_0')).toBe('M31,27 110,32.5');
     expect(tool.genConnectionSvgPath('router_0', 'cal_0')).toBe('M110,32.5 14,32.5');
   });
 
+  it('refreshes physical scene paths instead of looking up legacy raw CAL IDs', () => {
+    const tool = createTool();
+    const component = (tool as any).context.componentRef;
+    component.currentFloorplanType = 'physical';
+    component.refreshPhysicalSceneModel = jasmine.createSpy('refreshPhysicalSceneModel');
+    const error = spyOn(console, 'error');
+    tool.updateConnectionSvgPath('cal_0(1)', 'mcn_0');
+    expect(component.refreshPhysicalSceneModel).toHaveBeenCalled();
+    expect(error).not.toHaveBeenCalled();
+  });
+
+  it('preserves the resolved CDI attachment while updating a logical SVG path', () => {
+    const tool = createTool();
+    const component = (tool as any).context.componentRef;
+    component.currentFloorplanType = 'logical';
+    component.interfaces = { cdi: { protocol: 'CHI5CDI' }, ncdi: { protocol: 'CHI5NCDI' } };
+    component.interfacesInfo = undefined;
+    component.canvasConnectionsService = { resolveMcnIncomingInterface: () => 'cdi' };
+    component.mcnGroup = { interfaceConnectionPoints: {
+      cdi: { mcnName: 'mcn_0', type: 'top' }, ncdi: { mcnName: 'mcn_0', type: 'top' },
+    } };
+    const geometry = spyOn<any>(tool, 'resolveNodeGeometry').and.returnValue({
+      svgX: 10, svgY: 20, width: 25, height: 25, shape: 'rect',
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/core/interaction/canvas-connector.tool.ts`:
```diff
@@ -7,6 +7,7 @@ import { CanvasSceneEntity } from 'src/app/canvas/core/models/canvas-scene.model
 import { CanvasInteractionController } from './canvas-interaction.controller';
 import { CanvasGeometry, getEdgePoint, getNodeCenter } from '../utils/canvas-connection-geometry.util';
 import { resolveCanvasCalPortPoint } from '../utils/canvas-cal-dynamic-paths.util';
+import { resolvePhysicalMcnDisplayEndpointName } from '../utils/canvas-mcn-connectivity.util';
 import {
   resolveLogicalMcnDisplayEndpointName,
   resolveLogicalMcnOwningEndpointName
```
### Current source `GUI/src/app/canvas/core/services/canvas-input-interpreter.service.ts`
Snapshot: HEAD; SHA-256 `988ff113b48d53bca6bdd1a1c62590bd3aab31b02d808b6dab80809b2b8c7bb9`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 291, 'Michael Coulter': 168, 'Dustin divis': 9, 'Pawan Kakarla': 32}.
Introduction/rename-follow candidates: 2d40b3c5c155b16ac250ff34e06cdc578ebc6213 2026-02-12T21:34:47-06:00 Dustin Divis <dustin.divis@arm.com> refactor(canvas): add renderer-agnostic scene + input interpreter.
```text
85:     };
86:     const ngZone = canvasInteraction?.componentRef?.ngZone;
87: 
88:     if (ngZone?.runOutsideAngular) {
89:       ngZone.runOutsideAngular(addListeners);
90:     } else {
91:       addListeners();
92:     }
93: 
94:     return {
95:       cleanup: () => {
96:         document.removeEventListener('mousedown', onMouseDown);
97:         document.removeEventListener('mouseup', onMouseUp);
```
```text
205:     const onPointerMove = (event: PointerEvent) => {
206:       pendingPointerMoveEvent = event;
207:       if (pointerMoveFrame === null) {
208:         pointerMoveFrame = requestAnimationFrame(processPointerMove);
209:       }
210:     };
211: 
212:     const onPointerUp = (event: PointerEvent) => {
213:       flushPendingPointerMove();
214:       const context = resolveContext(event);
215:       if (!context) {
216:         return;
```
```text
403:     const onPointerMove = (event: PointerEvent) => {
404:       pendingPointerMoveEvent = event;
405:       if (pointerMoveFrame === null) {
406:         pointerMoveFrame = requestAnimationFrame(processPointerMove);
407:       }
408:     };
409: 
410:     const onPointerUp = (event: PointerEvent) => {
411:       const context = resolveContext(event);
412:       if (!context) {
413:         return;
414:       }
```
### Current source `GUI/src/app/canvas/core/utils/canvas-logical-layout-classifier.util.ts`
Snapshot: HEAD; SHA-256 `e38a648d8b4c34bd4e2a9b8d1b476cc2d9a088f8a84beaa610cac7a93cbedc76`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 302}.
Introduction/rename-follow candidates: 82ff7cdeea292d5f48f6b335a937e449a8bc1eeb 2026-05-18T14:42:56-05:00 Michael Coulter <michael.coulter@arm.com> Rebuild logical canvas render model.
```text
15:   'managerDomainBridge' |
16:   'managerInterface' |
17:   'sidecar' |
18:   'hidden' |
19:   'groupedRouting';
20: 
21: export interface LogicalLayoutSectionDefinition {
22:   bucket: LogicalLayoutBucket;
23:   label: string;
24:   order?: number;
25: }
26: 
27: export interface LogicalNodeClassification {
28:   bucket: LogicalLayoutBucket;
29:   sectionLabel: string;
30:   networks: string[];
31:   visible: boolean;
32: }
33: 
34: export interface LogicalNodeClassificationInput {
35:   name: string;
36:   nodeType: string | null;
37:   wireMode?: string | null;
38:   node?: Record<string, any> | null;
39:   uiInfo?: Record<string, any>;
40:   instanceAttributes?: Record<string, any>;
41:   routingWireModeNetworks?: Record<string, string[]>;
42:   viewNetworks?: NetworkType[];
```
```text
61: export const LOGICAL_LAYOUT_BUCKET_ORDER: Record<LogicalLayoutBucket, number> =
62:   getLogicalLayoutBucketOrder(buildDefaultLogicalLayoutSections());
63: 
64: export function classifyLogicalNode(input: LogicalNodeClassificationInput): LogicalNodeClassification {
65:   const bucket = resolveLogicalLayoutBucket(input);
66:   const networks = resolveLogicalNodeNetworks(input);
67:   const selectedNetworks = new Set((input.viewNetworks ?? []).map((network) => NetworkType[network]));
68:   const visible = bucket !== 'hidden' && (
69:     input.isInterface ||
70:     selectedNetworks.size === 0 ||
71:     networks.length === 0 ||
72:     networks.some((network) => selectedNetworks.has(network))
73:   );
74: 
75:   return {
76:     bucket,
```

## performance

### Commit e93183095a43d3607cbe8bf6e2337edb7fc4c68e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-08-28T17:42:33-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2503, BRUNEL-2020
Change-Ids: Ife0cf1ef13d7fc890efa8e222d71d29d69f96426.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -205,12 +206,13 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
         this.viewBox.width = this.fixNullAndInfinityValues(this.viewBox.width);
         this.viewBox.height = this.fixNullAndInfinityValues(this.viewBox.height);
         this.canvasGuiDataService.viewBoxInfo = this.viewBox;
-        // For cursor coordinates display
-        const fpRect = this.floorplanElement.getBoundingClientRect();
-        this.floorplanElement.style.setProperty('--fp-left', fpRect.left + 'px');
-        this.floorplanElement.style.setProperty('--fp-top', fpRect.top + 'px');
-        this.floorplanElement.style.setProperty('--fp-width', fpRect.width + 'px');
-        this.floorplanElement.style.setProperty('--fp-height', fpRect.height + 'px');
+        // getBoundingClientRect() returns size and position of element relative to viewport (DOM object with x,y,width,height,top,right,bottom,left)
+        this.floorplanElementBoundingClientRect = this.floorplanElement.getBoundingClientRect();
+        this.canvasElementBoundingClientRect = this.canvasElement.getBoundingClientRect();
+        this.floorplanElement.style.setProperty('--fp-left', this.floorplanElementBoundingClientRect.left + 'px');
+        this.floorplanElement.style.setProperty('--fp-top', this.floorplanElementBoundingClientRect.top + 'px');
+        this.floorplanElement.style.setProperty('--fp-width', this.floorplanElementBoundingClientRect.width + 'px');
+        this.floorplanElement.style.setProperty('--fp-height', this.floorplanElementBoundingClientRect.height + 'px');
       });
     });
     this.canvasLogicalService.expandAllCalInstancesSubject.pipe(takeUntil(this.unsubscribeAll)).pipe(takeUntil(this.unsubscribeAll)).subscribe(res => {
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -249,20 +251,27 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
     this.canvasLogicalService.removeGroupMemberOutlinesSubject.pipe(takeUntil(this.unsubscribeAll)).subscribe(() => {
       this.removeGroupMemberOutlines();
     });
-    this.unlistener0 = this.renderer2.listen("document", "mousedown", (e) => this.mouseDownHandler(e));
-    this.unlistener1 = this.renderer2.listen("document", "mousemove", (e) => this.mouseMoveHandler(e));
-    this.unlistener2 = this.renderer2.listen("document", "mouseup", (e) => this.mouseUpHandler(e));
     this.refreshCanvas();
   }
 
   ngAfterViewInit(): void {
-    this.floorplanElement = document.getElementById('floorplan-container');
+    // start observing canvas elements here
     this.resizeObserver.observe(this.floorplanElement);
-    this.svgElement = document.getElementById('canvas-container') as unknown as SVGElement;
     this.canvasGuiDataService.calcCanvasLocation();
     this.enableZoom();
     this.enablePan();
-    this.setupCursorCoorsDisplay();
+    this.mousedownUnlistener = this.renderer2.listen("document", "mousedown", (e) => this.mouseDownHandler(e));
+    this.mouseupUnlistener = this.renderer2.listen("document", "mouseup", (e) => this.mouseUpHandler(e));
+    // init cursor coords to 0
+    this.floorplanElement.style.setProperty('--cursor-x', '0px');
+    this.floorplanElement.style.setProperty('--cursor-y', '0px');
+    this.mousemoveUnlistener = this.renderer2.listen(this.floorplanElement, "mousemove", (e) => this.floorplanElementMousemoveHandler(e));
+    this.canvasElement.addEventListener('mouseover', e => {
+      this.cursorInCanvasContainer = true;
+    });
+    this.canvasElement.addEventListener('mouseout', e => {
+      this.cursorInCanvasContainer = false;
+    });
   }
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -274,30 +283,11 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
     this.draggablesUnsubscribe$.complete();
     this.unsubscribeAll.next();
     this.unsubscribeAll.complete();
-    this.resizeObserver.unobserve(this.svgElement);
-    // this.floorplanElement.removeEventListener();
-    this.unlistener0();
-    this.unlistener1();
-    this.unlistener2();
-    this.floorplanElement.removeEventListener('mousemove', (e) => this.floorplanElementMousemoveHandler(e));
-  }
-
-  private setupCursorCoorsDisplay() {
-    const fpRect = this.floorplanElement.getBoundingClientRect();
-    this.floorplanElement.style.setProperty('--cursor-x', '0px');
-    this.floorplanElement.style.setProperty('--cursor-y', '0px');
-    this.floorplanElement.style.setProperty('--fp-left', fpRect.left + 'px');
-    this.floorplanElement.style.setProperty('--fp-top', fpRect.top + 'px');
-    this.floorplanElement.style.setProperty('--fp-width', fpRect.width + 'px');
-    this.floorplanElement.style.setProperty('--fp-height', fpRect.height + 'px');
-
-    this.floorplanElement.addEventListener('mousemove', (e) => this.floorplanElementMousemoveHandler(e),false);
-    this.svgElement.addEventListener('mouseover', e => {
-      this.cursorInCanvasContainer = true;
-    });
-    this.svgElement.addEventListener('mouseout', e => {
-      this.cursorInCanvasContainer = false;
-    });
+    this.resizeObserver.unobserve(this.floorplanElement);
+    this.resizeObserver.unobserve(this.canvasElement);
+    this.mousedownUnlistener();
+    this.mouseupUnlistener();
[hunk excerpt ends; remaining lines omitted]
```
### Commit 6946d58aec43e7d2e9d77ca7aaacf830da2dff15
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-12-20T22:08:21-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-2756: optimize panning for logical canvas
Change-Ids: Ia3836a445137f541c57b6a558563e2ad73bbaf58.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -16,8 +16,8 @@
 ***************************************************************************/
 
 import { Component, OnDestroy, OnInit, AfterViewInit, ChangeDetectorRef, NgZone, Renderer2, ViewChildren, QueryList, ElementRef } from '@angular/core';
-import { fromEvent, Subject, combineLatest } from 'rxjs';
-import { filter, map, switchMap, takeUntil, tap } from 'rxjs/operators';
+import { fromEvent, Subject, combineLatest, Subscription } from 'rxjs';
+import { filter, map, switchMap, takeUntil, tap, throttleTime } from 'rxjs/operators';
 
 import { CanvasStaticDataService } from 'src/app/canvas/shared/services/canvas-static-data.service';
 import { CanvasLogicalService } from 'src/app/canvas/canvas-logical.service';
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -147,6 +147,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
 
   private measurementCanvas: HTMLCanvasElement = document.createElement('canvas');
   private measurementContext: CanvasRenderingContext2D = this.measurementCanvas.getContext('2d')!;
+  private subscriptions: Subscription = new Subscription();
 
   constructor(
     private ngZone: NgZone,
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -298,6 +299,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
     this.mousemoveUnlistener();
     // clean up the observers when the component is destroyed to avoid memory leaks
     this.mutationObservers.forEach(observer => observer.disconnect());
+    this.subscriptions.unsubscribe();
   }
 
   setCanvasInstanceDisplayLines(instances: any = this.instances) {
```
### Commit a6e5a6486e4a6be8c43e12f4245b872557c5c043
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-02-19T22:53:48-06:00; reachable from selected HEAD: True.
Subject: centralize all canvas zoom/pan logic in canvas-interaction.util.ts
Change-Ids: I2009e36fcd16edef3f956517b00722f28c5ed924.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -18,6 +18,7 @@
 import { Component, OnDestroy, OnInit, AfterViewInit, ChangeDetectorRef, NgZone, Renderer2, ViewChildren, QueryList, ElementRef } from '@angular/core';
 import { fromEvent, Subject, combineLatest, Subscription } from 'rxjs';
 import { filter, map, switchMap, takeUntil, tap, throttleTime } from 'rxjs/operators';
+import cloneDeep from 'lodash/cloneDeep';
 
 import { CanvasStaticDataService } from 'src/app/canvas/shared/services/canvas-static-data.service';
 import { CanvasLogicalService } from 'src/app/canvas/canvas-logical.service';
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -40,11 +42,17 @@ import cloneDeep from 'lodash/cloneDeep';
 })
 export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewInit, OnDestroy {
   @ViewChildren('instanceTextElement') instanceTextElements!: QueryList<ElementRef>;
-  checkView = false;
+  // canvas interaction variables
   isPanning = false;
   isZooming = false;
+  viewBox = {x: 0, y: 0, width: 100, height: 100};
+  canvasScale = 0;
+  private panSubscriptions: Subscription = new Subscription();
+  currentFloorplanType: string = null;
   floorplanElement: HTMLElement = null;
   canvasElement: SVGElement;
+  zoomHideTextTimeout: any;
+
   floorplanElementBoundingClientRect: any = null;
   canvasElementBoundingClientRect: any = null;
   removedTextElements: { element: SVGTextElement, parent: Element }[] = [];
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -148,7 +152,6 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
 
   private measurementCanvas: HTMLCanvasElement = document.createElement('canvas');
   private measurementContext: CanvasRenderingContext2D = this.measurementCanvas.getContext('2d')!;
-  private subscriptions: Subscription = new Subscription();
 
   constructor(
     private ngZone: NgZone,
```
### Commit 9d505f90c7dc30ccb87e9c0be2784d5522adb26d
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-09-25T11:39:25-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2729: GUI - 64x64 Mesh support
Change-Ids: I1973a4152d0101cc70e7a2c4f37c37d9805ce10f.
### Commit 9126ab49b5795b74f8bb61638c303f2d36e332d7
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-08-15T15:52:14-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-3468: Address interface tab memory leaks
Change-Ids: Icb83ef3c9b83a4096b9bda5e17fc9615d12b8409.
Diff excerpt, `GUI/src/app/interfaces/device-groups/ccg/ccg-group.component.ts`:
```diff
@@ -45,8 +45,6 @@ export class CcgDeviceGroupComponent implements OnInit, AfterViewInit, OnDestroy
   interfaceGroupTypeEnum = CCGType;
   interfaceGroupSub: Subscription;
   groupList: string[];
-  private resizeObserver: ResizeObserver;
-  interfaceMainElement: HTMLElement = null;
   uiFrameSubscription: Subscription;
   interfaceFrameset: any = {};
 
```
Diff excerpt, `GUI/src/app/interfaces/device-groups/ccg/ccg-group.component.ts`:
```diff
@@ -74,21 +72,6 @@ export class CcgDeviceGroupComponent implements OnInit, AfterViewInit, OnDestroy
         }
         this.cdr.detectChanges();
       });
-    this.resizeObserver = new ResizeObserver((entries: ResizeObserverEntry[]) => {
-      entries.forEach(entry => {
-        //const height = entry.contentRect.height;
-        const fieldsetElement = document.getElementById('ccg-group-fieldset-id');
-        // if(fieldsetElement !== null)
-        // fieldsetElement.style.height = height -50 + 'px';
-        if (fieldsetElement) {
-          const viewportHeight = window.innerHeight;
-          const calculatedHeight = viewportHeight - 246;
-          if (parseFloat(fieldsetElement.style.height || '0') !== calculatedHeight) {
-            fieldsetElement.style.height = `${calculatedHeight}px`;
-          }
-        }
-      });
-    });
     this.groupList = [];
     this.interfaceFrameset = this.interfaceService.uiFramework;
     this.uiFrameSubscription = this.interfaceService.uiFrameChanged
```
Diff excerpt, `GUI/src/app/interfaces/device-groups/ccg/ccg-group.component.ts`:
```diff
@@ -99,17 +82,10 @@ export class CcgDeviceGroupComponent implements OnInit, AfterViewInit, OnDestroy
     this.interfaceService.fetchDeviceGroups();
   }
 
-  ngAfterViewInit(): void {
-    this.interfaceMainElement = document.getElementById('app-interface-table-id');
-    // if (this.interfaceMainElement !== null)
-    this.resizeObserver.observe(this.interfaceMainElement);
-  }
-
   ngOnDestroy(): void {
     if (this.interfaceGroupSub) {
       this.interfaceGroupSub.unsubscribe();
     }
-    this.resizeObserver.unobserve(this.interfaceMainElement);
   }
 
   addGroup() {
```
### Commit f922795c315a0ee4816e39bbc0c2efdd6a1b36bc
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-10-01T20:57:08-05:00; reachable from selected HEAD: True.
Subject: Fix Access Maps tab memory leaks due to resize observer, implement flex layout css
Change-Ids: Ia156c896f32acd4e8283fa8dd8c014c4e3b34421.
Diff excerpt, `GUI/src/app/memory-maps/memory-map-regions/memory-map-regions.component.ts`:
```diff
@@ -46,8 +46,6 @@ export class MemoryMapRegionsComponent implements OnInit, OnDestroy, AfterViewIn
   memorySub: Subscription;
   managerSub: Subscription;
   subordinateInterfaceResolve = '';
-  private resizeObserver: ResizeObserver;
-  memoryMainElement: HTMLElement = null;
   managerSelection = '';
   subordinateIds = [];
   resolveMask = ['0', '1', '2', '3', '4', '5', '6', '7'];
```
Diff excerpt, `GUI/src/app/memory-maps/memory-map-regions/memory-map-regions.component.ts`:
```diff
@@ -111,42 +109,11 @@ export class MemoryMapRegionsComponent implements OnInit, OnDestroy, AfterViewIn
       this.cdr.detectChanges();
     });
   
-    this.resizeObserver = new ResizeObserver((entries: ResizeObserverEntry[]) => {
-      entries.forEach(entry => {
-        const height = entry.contentRect.height;
-        const fieldsetElement = document.getElementById('memory-tree-component-id');
-        const resolveId = document.getElementById('resolve-fieldset-id');
-        const treeScrollId = document.getElementById('memory-tree-scroll-id');
-        const tabElement = entry.target.children[0];
-  
-        if (fieldsetElement && resolveId && treeScrollId && tabElement) {
-          const resolveHeight = resolveId.clientHeight;
-          const newFieldsetHeight = height - tabElement.clientHeight - 115;
-          const newTreeScrollHeight = height - 32 - resolveHeight - tabElement.clientHeight - 370;
-  
-          if (
-            parseFloat(fieldsetElement.style.height || '0') !== newFieldsetHeight ||
-            parseFloat(treeScrollId.style.height || '0') !== newTreeScrollHeight
-          ) {
-            this.resizeObserver.disconnect();
-            fieldsetElement.style.height = `${newFieldsetHeight}px`;
-            treeScrollId.style.height = `${newTreeScrollHeight}px`;
-            this.resizeObserver.observe(document.body);
-          }
-        }
-      });
-    });
-
     this.hasUnusedGaps = this.detectTopLevelGaps();
 
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/memory-maps/memory-matrix-modal/memory-matrix-modal.component.ts`:
```diff
@@ -15,22 +15,19 @@
 *
 ***************************************************************************/
 
-import { Component, Output, EventEmitter, Input, ViewChild, OnInit, OnDestroy } from '@angular/core';
-
-import { DataService } from 'src/app/shared/services/data.service';
-import { ChangeDetectorRef, AfterViewInit } from '@angular/core';
+import { Component, OnInit, OnDestroy, ChangeDetectorRef } from '@angular/core';
 import { CrossingPathType, PathRelations } from 'src/app/shared/models/path-relations.model';
 import { InterfaceService } from 'src/app/interfaces/interface.service';
 import { MemoryMapService } from '../memory-map.service';
 import { MemoryServiceAPI } from '../memory-maps.service.api';
-import { Subscriber, Subscription } from 'rxjs';
+import { Subscription } from 'rxjs';
 
 @Component({
   selector: 'app-memory-map-matrix',
   templateUrl: './memory-matrix-modal.component.html',
   styleUrls: ['./memory-matrix-modal.component.css']
 })
-export class MemoryMapMatrixComponent implements OnInit, OnDestroy, AfterViewInit {
+export class MemoryMapMatrixComponent implements OnInit, OnDestroy {
   pathRelations: PathRelations = null;
   subordinateIds: string[] = [];
   memMapIds: string[] = [];
```
### Commit 63b5c1f13b94724541a9556695fa272a20524313
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-10-14T22:57:27-05:00; reachable from selected HEAD: True.
Subject: Pixi working on cluster (no GPU)
Change-Ids: I6dd9d131173d7023619f7821ae935ddc30010865.
### Commit cd3602f944118c7c6abb91506a8072cf698e46da
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-11-11T16:22:04-06:00; reachable from selected HEAD: False.
Subject: BRUNEL-3727: Improve PIXI performance on no-GPU machines
Change-Ids: I9d81fcaa166f57ca5fa46989d35a3bd6f2050c04.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -497,6 +500,185 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, A
     }
   }
 
+  private shouldEnableTelemetryOverlay(): boolean {
+    if (CanvasFloorplanLogicalComponent.diagnosticsLoggingEnabled === null) {
+      CanvasFloorplanLogicalComponent.diagnosticsLoggingEnabled = this.resolveAppDiagnosticLogging();
+    }
+    return CanvasFloorplanLogicalComponent.diagnosticsLoggingEnabled === true;
+  }
+
+  private resolveAppDiagnosticLogging(): boolean {
+    if (typeof window === 'undefined') {
+      return false;
+    }
+
+    const interpretBoolean = (value: unknown): boolean | null => {
+      if (typeof value === 'boolean') {
+        return value;
+      }
+      if (typeof value === 'string') {
+        const normalized = value.trim().toLowerCase();
+        if (!normalized) {
+          return null;
+        }
+        if (['1', 'true', 'yes', 'on'].includes(normalized)) {
+          return true;
+        }
+        if (['0', 'false', 'no', 'off'].includes(normalized)) {
+          return false;
+        }
+      }
[hunk excerpt ends; remaining lines omitted]
```
### Current source `GUI/src/app/canvas/core/services/canvas-input-interpreter.service.ts`
Snapshot: HEAD; SHA-256 `988ff113b48d53bca6bdd1a1c62590bd3aab31b02d808b6dab80809b2b8c7bb9`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 291, 'Michael Coulter': 168, 'Dustin divis': 9, 'Pawan Kakarla': 32}.
Introduction/rename-follow candidates: 2d40b3c5c155b16ac250ff34e06cdc578ebc6213 2026-02-12T21:34:47-06:00 Dustin Divis <dustin.divis@arm.com> refactor(canvas): add renderer-agnostic scene + input interpreter.
```text
85:     };
86:     const ngZone = canvasInteraction?.componentRef?.ngZone;
87: 
88:     if (ngZone?.runOutsideAngular) {
89:       ngZone.runOutsideAngular(addListeners);
90:     } else {
91:       addListeners();
92:     }
93: 
94:     return {
95:       cleanup: () => {
96:         document.removeEventListener('mousedown', onMouseDown);
97:         document.removeEventListener('mouseup', onMouseUp);
```
```text
112:     let pointerMoveFrame: number | null = null;
113: 
114:     const refreshRect = (): CachedRect => {
115:       const rect = canvas.getBoundingClientRect();
116:       cachedRect = {
117:         left: rect.left,
118:         top: rect.top,
119:         width: rect.width,
120:         height: rect.height
121:       };
122:       return cachedRect;
123:     };
```
```text
205:     const onPointerMove = (event: PointerEvent) => {
206:       pendingPointerMoveEvent = event;
207:       if (pointerMoveFrame === null) {
208:         pointerMoveFrame = requestAnimationFrame(processPointerMove);
209:       }
210:     };
211: 
212:     const onPointerUp = (event: PointerEvent) => {
213:       flushPendingPointerMove();
214:       const context = resolveContext(event);
215:       if (!context) {
216:         return;
```
```text
320:     let pointerMoveFrame: number | null = null;
321: 
322:     const refreshRect = (): CachedRect => {
323:       const rect = svgElement.getBoundingClientRect();
324:       cachedRect = {
325:         left: rect.left,
326:         top: rect.top,
327:         width: rect.width,
328:         height: rect.height
329:       };
330:       return cachedRect;
331:     };
```
### Current source `GUI/src/app/canvas/core/utils/canvas-transform.util.ts`
Snapshot: HEAD; SHA-256 `e599cd4708f0690c432593224ad793c0958ff66de90e3ce4420c5049187f78d3`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 174, 'Michael Coulter': 28}.
Introduction/rename-follow candidates: f8d0380996fe0945e720e87ab16b4c02a584e2e0 2026-02-18T10:04:28-06:00 Dustin Divis <dustin.divis@arm.com> [GUI] split core/renderers/ui and rebuild interaction layer.
```text
73:     return null;
74:   }
75:   if (context.kind === 'pixi') {
76:     const rect = cachedRect ?? context.canvas.getBoundingClientRect();
77:     const relativeX = screenX - rect.left;
78:     const relativeY = screenY - rect.top;
79:     const container = context.contentContainer;
80:     if (!container) {
81:       return null;
82:     }
83:     const worldX = (relativeX - container.position.x) / container.scale.x;
84:     const worldY = (relativeY - container.position.y) / container.scale.y;
85:     return { x: worldX, y: worldY };
86:   }
87: 
88:   const rect = cachedRect ?? context.canvas.getBoundingClientRect();
89:   const relativeX = screenX - rect.left;
90:   const relativeY = screenY - rect.top;
91:   const scale = resolveSvgScale(context, rect);
92:   const worldX = (relativeX / scale) + context.viewBox.x;
93:   const viewBoxY = (relativeY / scale) + context.viewBox.y;
94:   const worldY = context.invertY ? -viewBoxY : viewBoxY;
95:   return { x: worldX, y: worldY };
96: }
```
```text
104:     return null;
105:   }
106:   if (context.kind === 'pixi') {
107:     const rect = context.canvas.getBoundingClientRect();
108:     const relative = axis === 'x' ? screenPx - rect.left : screenPx - rect.top;
109:     const container = context.contentContainer;
110:     if (!container) {
111:       return null;
112:     }
113:     const position = axis === 'x' ? container.position.x : container.position.y;
114:     const scale = axis === 'x' ? container.scale.x : container.scale.y;
115:     return (relative - position) / scale;
116:   }
117: 
118:   const rect = context.canvas.getBoundingClientRect();
119:   const relative = axis === 'x' ? screenPx - rect.left : screenPx - rect.top;
120:   const scale = resolveSvgScale(context, rect);
121:   const viewBoxCoord = (relative / scale) + (axis === 'x' ? context.viewBox.x : context.viewBox.y);
122:   if (axis === 'y' && context.invertY) {
123:     return -viewBoxCoord;
124:   }
125:   return viewBoxCoord;
126: }
```
```text
134:     return null;
135:   }
136:   if (context.kind === 'pixi') {
137:     const rect = context.canvas.getBoundingClientRect();
138:     const container = context.contentContainer;
139:     if (!container) {
140:       return null;
141:     }
142:     const relativeX = worldX * container.scale.x + container.position.x;
143:     const relativeY = worldY * container.scale.y + container.position.y;
144:     return { x: rect.left + relativeX, y: rect.top + relativeY };
145:   }
```
### Current source `GUI/src/app/memory-maps/memory-map-regions/memory-map-regions.component.ts`
Snapshot: HEAD; SHA-256 `bcbcbba82355b4cca1590262a4d6ad0c3073975e7ba88cb32a456ff795f215a9`.
Surviving-line author counts (attribution context only): {'Ana Rescala': 66, 'Dustin divis': 132, 'Kelly Alvarez': 205, 'Dustin Divis': 15, 'Pawan Kakarla': 179, 'Michael Coulter': 41}.
Introduction/rename-follow candidates: fa401c2fc1f4865bac26dae6eeb5afc6622b3f7c 2020-06-10T10:21:09-06:00 Dustin Divis <dustin.divis@arm.com> [FE] Initial app file structure.
```text
19: import { NestedTreeControl } from '@angular/cdk/tree';
20: import { MatTreeNestedDataSource } from '@angular/material/tree';
21: 
22: import { Subscription, take } from 'rxjs';
23: import { CeMutationRequest } from 'src/app/shared/ce-policy/ce-policy';
24: 
25: import { PlaceholderDirective } from 'src/app/shared/directives/placeholder.directive';
26: import { MemoryMapService } from '../memory-map.service';
27: import { MemoryMapModalService } from '../memory.modal.service';
28: import { MemoryServiceAPI } from '../memory-maps.service.api';
29: import { InterfaceService } from 'src/app/interfaces/interface.service';
30: import { MemoryMapNode, MemoryType } from 'src/app/shared/models/memory-map-node';
```
```text
41: export class MemoryMapRegionsComponent implements OnInit, OnDestroy {
42:   @Input() periphbase: string | number;
43:   stackView = false;
44:   private readonly subscriptions = new Subscription();
45:   private destroyed = false;
46:   get saving(): boolean { return this.memoryService.isBusy('memory'); }
47: 
48:   private save(requests: CeMutationRequest[], confirmed?: () => void) {
49:     if (this.saving || this.destroyed) return;
50:     this.memoryService.mutateMaps('memory', requests).subscribe(outcome => {
51:       if (this.destroyed) return;
52:       if (outcome.success && outcome.reconciliation.status === 'refreshed') confirmed?.();
```
```text
62:   nodeSelected = false;
63:   memoryMaps: MemoryMapNode[] = [];
64:   memoryEnum = MemoryType;
65:   memorySub: Subscription;
66:   managerSub: Subscription;
67:   subordinateInterfaceResolve = '';
68:   managerSelection = '';
69:   subordinateIds = [];
70:   resolveMask = ['0', '1', '2', '3', '4', '5', '6', '7'];
71:   isChecked = { '0': false, '1': false, '2': false, '3': false, '4': false, '5': false, '6': false, '7': false };
72:   updateMemSubs = false;
73:   addingToMap = false;
74:   updateMemoryMap = false;
```
```text
145:     });
146: 
147: 
148:     this.subscriptions.add(this.memoryService.fetchConfigSize().pipe(take(1)).subscribe(size => {
149:       this.configSizeStr = addressSize(BigInt(size));
150:       this.configSize = this.memoryService.configSize;
151:       this.cdr.detectChanges();
152:     }));
153: 
154:     this.subscriptions.add(this.interfaceService.fetchInterfacesAll().pipe(take(1)).subscribe(result => {
155:       for (const subordinateInt of result[0]) {
156:         this.subordinateIds.push(subordinateInt.name);
```

## placement

### Commit 8043ff80857818dfd48a591f6f0de794dc906c13
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-01T13:24:00-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-1475: Physical auto-placement, remove HLS Floorplan
Change-Ids: I05ae15e551d88a5b0d0a0d5583d7d1dd7d93bfea.
Diff excerpt, `GUI/agent/app-docs-data.json`:
```diff
@@ -13260,982 +16815,973 @@
       }
     ],
     "reexports": [],
-    "exports": [
+    "exports": [],
+    "classes": [],
+    "functions": [
       {
-        "kind": "class",
-        "name": "CanvasAnalysisToolsComponent"
+        "name": "createComponent",
+        "modifiers": []
+      },
+      {
+        "name": "setCanvasShellWidth",
+        "modifiers": []
+      },
+      {
+        "name": "gridPanelWidths",
+        "modifiers": []
+      },
+      {
+        "name": "shiftR",
+        "modifiers": []
+      },
+      {
+        "name": "plainR",
+        "modifiers": []
       }
     ],
-    "classes": [
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/agent/app-docs-data.json`:
```diff
@@ -15306,5391 +18688,3074 @@
         "resolvedImport": null,
         "withinClass": null,
         "withinMember": null
-      }
-    ],
-    "hasDefaultExport": false
-  },
-  "canvas/canvas-design-flow/canvas-design-flow-uarch/canvas-design-flow-uarch.component.ts": {
-    "path": "canvas/canvas-design-flow/canvas-design-flow-uarch/canvas-design-flow-uarch.component.ts",
-    "isSpec": false,
-    "imports": [
+      },
       {
-        "moduleSpecifier": "@angular/core",
-        "defaultBinding": null,
-        "namedBindings": [
-          {
-            "name": "AfterContentChecked",
-            "propertyName": null
-          },
-          {
-            "name": "Component",
-            "propertyName": null
-          },
-          {
-            "name": "OnDestroy",
-            "propertyName": null
-          },
-          {
-            "name": "OnInit",
-            "propertyName": null
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/agent/app-docs-data.json`:
```diff
@@ -20699,175 +21764,180 @@
         "resolved": null
       },
       {
-        "moduleSpecifier": "./models/canvas-diff.models",
+        "moduleSpecifier": "../interfaces/interface.modal.service",
         "defaultBinding": null,
         "namedBindings": [
           {
-            "name": "CanvasDiffViewPayload",
+            "name": "InterfaceModalService",
             "propertyName": null
           }
         ],
         "namespaceImport": null,
         "isTypeOnly": false,
-        "resolved": "canvas/canvas-diff/models/canvas-diff.models.ts"
+        "resolved": "interfaces/interface.modal.service.ts"
       },
       {
-        "moduleSpecifier": "../canvas-logical.service",
+        "moduleSpecifier": "src/app/shared/services/modal.service",
         "defaultBinding": null,
         "namedBindings": [
           {
-            "name": "CanvasLogicalService",
+            "name": "ModalService",
             "propertyName": null
           }
         ],
         "namespaceImport": null,
         "isTypeOnly": false,
[hunk excerpt ends; remaining lines omitted]
```
### Current source `GUI/src/app/canvas/core/services/canvas-physical-auto-place.service.ts`
Snapshot: HEAD; SHA-256 `536163888927c31bacc28c1a3ac45ba425b5629588cac55de67e59ce7e8f3537`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1343, 'Dustin divis': 58, 'Pawan Kakarla': 2}.
Introduction/rename-follow candidates: 8043ff80857818dfd48a591f6f0de794dc906c13 2026-07-01T13:24:00-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-1475: Physical auto-placement, remove HLS Floorplan.
```text
19: import { Observable, defer, firstValueFrom } from 'rxjs';
20: import { CeInformationError, CeInformationReader, CeMutationStep, CeWorkflowOutcome, ceWorkflowNotification } from 'src/app/shared/services/ce-mutation-outcome';
21: 
22: import { CanvasAutoPlacementAllocator, CanvasAutoPlacementRect, snapPlacementToGrid } from 'src/app/canvas/core/utils/canvas-auto-placement.util';
23: import {
24:   buildLogicalRouteBucketHints,
25:   LOGICAL_LAYOUT_BUCKET_SEQUENCE,
26:   LogicalLayoutBucket,
27:   normalizeLogicalRouteNodeName,
28:   normalizeLogicalLayoutBucket,
29: } from 'src/app/canvas/core/utils/canvas-logical-layout-classifier.util';
30: import { CanvasBlockagesService } from 'src/app/canvas/core/services/canvas-blockages.service';
31: import { CanvasConfigService } from 'src/app/canvas/core/services/canvas-config.service';
32: import { CanvasConnectionsService } from 'src/app/canvas/core/services/canvas-connections.service';
33: import { CanvasInstancesService } from 'src/app/canvas/core/services/canvas-instances.service';
34: import { CanvasInterfacesService } from 'src/app/canvas/core/services/canvas-interfaces.service';
35: import { CanvasPhysicalDataService } from 'src/app/canvas/core/services/canvas-physical-data.service';
36: import { CanvasSpinnerService } from 'src/app/canvas/core/services/canvas-spinner.service';
37: import { CanvasStaticMetadataService } from 'src/app/canvas/core/services/canvas-static-metadata.service';
38: import { CanvasViewStateService } from 'src/app/canvas/core/services/canvas-view-state.service';
```
```text
58:   width: number;
59:   height: number;
60:   physical?: Coordinates | null;
61:   blockage?: string | null;
62: }
63: 
64: interface PlaceableBlock {
65:   name: string;
66:   width: number;
67:   height: number;
68:   location?: Location | null;
69:   isNew: boolean;
```
```text
75:   locationsByType: Record<string, Record<string, Coordinates>>;
76:   blockPlacements: { name: string; location: Location; isNew: boolean; interfaceNames: string[] }[];
77:   interfaceBlockByName: Record<string, string>;
78:   finalDieWidth: number;
79:   finalDieHeight: number;
80:   placedInstanceCount: number;
81:   placedInterfaceCount: number;
82:   placedBlockageCount: number;
83:   remainingUnplacedCount: number;
84: }
85: 
86: export interface PhysicalAutoPlaceResult {
87:   success: boolean;
```
### Current source `GUI/tests/ui/noc-se/physical-auto-place-layout.spec.ts`
Snapshot: HEAD; SHA-256 `df8c1254243d89989c51f0366ceb143fb256128a4650dbe773c5f625a2cf32b5`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 288, 'Liza Dayoub': 56}.
Introduction/rename-follow candidates: 8043ff80857818dfd48a591f6f0de794dc906c13 2026-07-01T13:24:00-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-1475: Physical auto-placement, remove HLS Floorplan.
```text
12: interface PhysicalPlacedItem {
13:   id: string;
14:   name: string;
15:   kind: 'instance' | 'interface' | 'blockage';
16:   type: string;
17:   x: number;
18:   y: number;
19:   width: number;
20:   height: number;
21:   blockage?: string | null;
22:   associatedInterfaces?: string[];
23: }
24: 
25: interface PhysicalAutoPlaceSnapshot {
26:   renderer: string;
27:   cellGranularity: number;
28:   die: { width: number; height: number };
29:   items: PhysicalPlacedItem[];
30:   remainingUnplaced: string[];
31: }
32: 
33: function resolveActiveRendererCase(): { mode: 'gpu' | 'cpu'; expectedRenderer: 'pixi' | 'svg' } {
34:   if (process.env.GUI_FORCE_CPU_RENDERER === '1') {
35:     return { mode: 'cpu', expectedRenderer: 'svg' };
36:   }
```
```text
69:     const snapshot = await collectPhysicalAutoPlaceSnapshot(appWindow);
70: 
71:     expect(snapshot.renderer).toBe(activeRendererCase.expectedRenderer);
72:     expect(snapshot.cellGranularity).toBeGreaterThan(0);
73:     expect(snapshot.remainingUnplaced).toEqual([]);
74:     expect(snapshot.items.length).toBeGreaterThan(20);
75: 
76:     assertGridAligned(snapshot);
77:     assertNoOverlaps(snapshot.items);
78:     assertContainedByDie(snapshot);
79:     assertCcgCombinedBlockages(snapshot);
80:     assertCcgCombinedSemanticRows(snapshot);
```

## conversion

### Commit 12c14eb478040a280bb5f8373bc296d748048b7c
Author: Michael Coulter <michael.coulter@arm.com>; author date 2023-05-04T17:23:43-05:00; reachable from selected HEAD: True.
Subject: Add first edition of nic400_to_tower_iyml.py script
Change-Ids: If5f706b89aa434a385a4493fd6ca43eec559f4c9.
Commit message:
```text
Add first edition of nic400_to_tower_iyml.py script

Change-Id: If5f706b89aa434a385a4493fd6ca43eec559f4c9
```
### Commit 6ba68516e28599638b3447891a50876d6a59602e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-04-08T21:46:33-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-1648: NIC-400 Migration
Change-Ids: I10f0d60ac1cc36b19a785fc1d2ad22d3492da4cc.
Commit message:
```text
BRUNEL-1648: NIC-400 Migration

Change-Id: I10f0d60ac1cc36b19a785fc1d2ad22d3492da4cc
```
### Commit 429a76b7e0e98b720b61065b8216e6ab2b96504a
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-04-29T16:12:51-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-1974: Add NIC-400 migration regresssion tests in Pytest
Change-Ids: I1d377ad984170b3516f7e6a47e4ff6ea65446dad.
Commit message:
```text
BRUNEL-1974: Add NIC-400 migration regresssion tests in Pytest

Change-Id: I1d377ad984170b3516f7e6a47e4ff6ea65446dad
```
### Commit f0e5bb3195676179948595be567624c872686134
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-05-08T22:51:19-05:00; reachable from selected HEAD: True.
Subject: feat(nic400): reconstruct NCI uArch and close DRCs
Change-Ids: I15aa3911678a2cbd8813735600b24e174c106989.
Commit message:
```text
feat(nic400): reconstruct NCI uArch and close DRCs

Add an integrated NIC400 XML/CCXML conversion flow that builds NCI-base IYML in memory, reconstructs source-derived uArch, preserves physical placement, and applies deterministic state-preserving DRC fixes before export.

Map NIC bus matrices to routers, CDC-capable IBs to PCDCs, width-converting IBs to SERDES, reconstruct routes from NIC architecture/connect topology, and log unsupported features plus every DRC-driven IYML mutation in nic400-to-nci.log.

Replace the legacy Tower wrapper with nic400_to_nci_iyml.py, remove obsolete helper scripts, and wire supported raw configs through CE import_design without mutating the source XML/CCXML.

Add the NIC400 pytest package, corpus audit/collection tools, curated 10 valid plus 5 invalid fixtures, standalone wrapper coverage, route/DRC diagnostics, and source-fidelity assertions for endpoint/uArch/path counts.

Validation: PYTHONPATH=CE CE/venv_3_13/bin/python -m pytest CE/pytests/nic400 -q; standalone wrapper pytest; full valid corpus audit 4130/4130 DRC-clean; invalid lane rejected 5/5 curated invalid configs.
Change-Id: I15aa3911678a2cbd8813735600b24e174c106989
```
Diff excerpt, `CE/ideas/base/nic400_conversion.py`:
```diff
@@ -0,0 +1,5935 @@
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : $State$
+#
+# ----------------------------------------------------------------------------
+"""NIC raw-config to NCI-base IYML conversion helpers."""
+
+from __future__ import annotations
+
+import html
+import logging
+import re
+import tempfile
+from collections import Counter, defaultdict, deque
+from dataclasses import dataclass, field
+from pathlib import Path
+from types import SimpleNamespace
+from typing import Any, Dict, List, Optional, Set, Tuple, Union
+import xml.etree.ElementTree as ET
+
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/pytests/nic400/audit_nic400_corpus.py`:
```diff
@@ -0,0 +1,653 @@
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : Internal
+#
+# ----------------------------------------------------------------------------
+
+"""Audit direct NIC400 conversion and CE import over a copied fixture corpus."""
+
+from __future__ import annotations
+
+import argparse
+import concurrent.futures
+import json
+import logging
+import multiprocessing
+import os
+import shutil
+import tempfile
+import traceback
+from collections import Counter
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/pytests/nic400/test_nic400_conversion.py`:
```diff
@@ -0,0 +1,990 @@
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : Internal
+#
+# ----------------------------------------------------------------------------
+
+import xml.etree.ElementTree as ET
+
+import pytest
+
+from ideas import Interconnect
+from ideas.base.nic400_conversion import Nic400Conversion, Nic400DrcFixEngine
+from tooling.general.decorators import ip
+
+from .nic400_test_utils import (
+    INVALID_FIXTURES,
+    NO_VALID_FIXTURES_REASON,
+    PRIMARY_FIXTURE,
+    REPRESENTATIVE_FIXTURES,
+    VALID_FIXTURE_DIR,
[hunk excerpt ends; remaining lines omitted]
```
### Commit d8e09fbe489d822f1e7841797f595b83ed7dc8b3
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-04T14:23:17-05:00; reachable from selected HEAD: True.
Subject: Preserve NIC400 topology during conversion
Change-Ids: I94fac5d0a1fb1317417a452c888975b6fbaf2292.
Commit message:
```text
Preserve NIC400 topology during conversion

- derive routes only from proven NIC400 graph paths and reject unresolved topology fallbacks
- keep generated endpoints, clocks, memory maps, placement, and flit sizing consistent with the source graph
- expand focused conversion and corpus diagnostics coverage for topology fidelity

Change-Id: I94fac5d0a1fb1317417a452c888975b6fbaf2292
```
Diff excerpt, `CE/ideas/base/nic400_conversion.py`:
```diff
@@ -1011,7 +1023,47 @@ class Nic400DrcFixEngine:
         if not missing_targets or not memory_maps:
             return
 
-        memory_map, region, targets_dict = self._select_data_reachability_region(memory_maps)
+        targets_by_map: Dict[str, List[str]] = defaultdict(list)
+        for target in missing_targets:
+            candidate_maps = [
+                memory_map
+                for memory_map in memory_maps
+                if self._memory_map_subscribers_reach_target(memory_map, target)
+            ]
+            if candidate_maps:
+                targets_by_map[candidate_maps[0]].append(target)
+            else:
+                self._log(
+                    f"Did not add NIC-400 manager {target} to a memory map; no subscribed source "
+                    "has a proven path to that target in the NIC-400 graph."
+                )
+
+        for memory_map, map_targets in sorted(targets_by_map.items()):
+            self._append_reachability_targets(memory_map, map_targets)
+
+    def _memory_map_subscribers_reach_target(self, memory_map: str, target: str) -> bool:
+        subscribers = self.builder.get_memory_map_subscribers(memory_map) or []
+        return bool(subscribers) and all(
+            self._uarch_path_exists(source, target)
+            for source in subscribers
+        )
+
+    def _uarch_path_exists(self, source: str, target: str) -> bool:
+        target_key = self.converter._casefold_mapping_key(self.apb_group_lookup, target)
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/base/nic400_conversion.py`:
```diff
@@ -3160,32 +3212,10 @@ class Nic400DrcFixEngine:
         return sequence
 
     def _max_route_flit_size(self, instances: List[str]) -> Optional[int]:
-        values: List[int] = []
-        for instance in instances:
-            flit_size = self.builder.get_instance_flit_size(instance, "all_rps") or {}
-            for rp_values in flit_size.values():
-                for value in rp_values.values():
-                    if isinstance(value, dict):
-                        values.extend(int(v) for v in value.values() if v is not None)
-                    elif value is not None:
-                        values.append(int(value))
-        return max(values) if values else None
+        return self.converter._max_instance_flit_size(self.builder, instances)
 
     def _raised_flit_size_dict(self, flit_size: Dict[str, Dict[str, Any]], route_max: int) -> Dict[str, Dict[str, Any]]:
-        raised: Dict[str, Dict[str, Any]] = {}
-        for rp, channel_values in flit_size.items():
-            raised[rp] = {}
-            for channel, value in channel_values.items():
-                if isinstance(value, dict):
-                    raised[rp][channel] = {
-                        side: max(int(side_value), route_max) if side_value is not None else None
-                        for side, side_value in value.items()
-                    }
-                elif value is None:
-                    raised[rp][channel] = None
-                else:
-                    raised[rp][channel] = max(int(value), route_max)
-        return raised
+        return self.converter._raise_flit_sizes(flit_size, route_max)
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/base/nic400_conversion.py`:
```diff
@@ -4730,6 +4842,161 @@ class Nic400Conversion:
             self._log(f"NIC-400 uArch features parsed but not mapped in v1: {unsupported_summary}")
         return model
 
+    def _add_generated_subordinate_to_uarch_model(
+        self,
+        model: Nic400UarchModel,
+        generated_name: str,
+    ) -> None:
+        """Represent an IA-required subordinate at each proven graph ingress."""
+        if generated_name in model.nodes:
+            return
+        external_edges = {
+            destination_name: edge
+            for edge in model.edges
+            for destination_name in [self._resolve_uarch_node_name(model, edge.dest)]
+            if edge.src.casefold() == "external" and destination_name is not None
+        }
+        internal_destinations = {
+            destination_name
+            for edge in model.edges
+            for source_name in [self._resolve_uarch_node_name(model, edge.src)]
+            for destination_name in [self._resolve_uarch_node_name(model, edge.dest)]
+            if source_name is not None and destination_name is not None
+        }
+        ingress_edges = dict(external_edges)
+        for node_name in model.nodes:
+            if node_name not in internal_destinations:
+                ingress_edges.setdefault(node_name, None)
+        if not ingress_edges:
+            if model.nodes:
+                return
[hunk excerpt ends; remaining lines omitted]
```
### Commit 0ec8ee6bddb3815016daf76faa8d38193d94cbc6
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-25T16:12:08-05:00; reachable from selected HEAD: True.
Subject: Update NIC-400 tests for channel-aware deadlock repair
Change-Ids: I864749892f171aee9c3e513d490ce7d68f715471.
Commit message:
```text
Update NIC-400 tests for channel-aware deadlock repair

Align the NIC-400 conversion tests with BRUNEL-4827 behavior by
expecting MA_74 route-cycle repairs instead of obsolete MA_14 cleanup
records. Retain final DRC-clean and duplicate-link legality checks.

Change-Id: I864749892f171aee9c3e513d490ce7d68f715471
```
Diff excerpt, `CE/pytests/nic400/test_nic400_conversion.py`:
```diff
@@ -1013,8 +1013,10 @@ def test_nic400_conversion_removes_duplicate_links_invalidated_by_wiremode_repai
     ).convert()
 
     assert log_state["drc_summary"]["clean"] is True
+    # Channel-aware deadlock analysis repairs this fixture's cycle before a
+    # separate MA_14_1 duplicate-link cleanup is needed.
     assert any(
-        fix["fixer"] == "duplicate-link-legality" and fix["rule_id"] == "MA_14_1"
+        fix["fixer"] == "route-cycle-repair" and fix["rule_id"] == "MA_74_1"
         for fix in log_state["drc_summary"]["fixes"]
     )
 
```
### Current source `CE/ideas/base/nic400_conversion.py`
Snapshot: HEAD; SHA-256 `7b292be91e74f7bd0c5f7dcab2ade72ec05280af1d8455ebc12767e37df69b18`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 6478, 'Lin Gao': 94, 'Christopher Alvarez': 156}.
Introduction/rename-follow candidates: f0e5bb3195676179948595be567624c872686134 2026-05-08T22:51:19-05:00 Michael Coulter <michael.coulter@arm.com> feat(nic400): reconstruct NCI uArch and close DRCs.
```text
47: 
48: 
49: @dataclass
50: class Nic400UarchNode:
51:     """Normalized NIC400 uArch node used only during conversion."""
52: 
53:     name: str
54:     kind: str
55:     source: dict
56:     ports: Set[str] = field(default_factory=set)
57:     master_ports: Set[str] = field(default_factory=set)
58:     slave_ports: Set[str] = field(default_factory=set)
```
```text
71: 
72: 
73: @dataclass
74: class Nic400UarchEdge:
75:     """Directed NIC400 connection edge."""
76: 
77:     index: int
78:     src: str
79:     dest: str
80:     src_port: Optional[str] = None
81:     dest_port: Optional[str] = None
82:     protocol: Optional[str] = None
```
```text
84: 
85: 
86: @dataclass
87: class Nic400UarchModel:
88:     """Normalized NIC400 uArch graph and conversion counters."""
89: 
90:     nodes: Dict[str, Nic400UarchNode] = field(default_factory=dict)
91:     edges: List[Nic400UarchEdge] = field(default_factory=list)
92:     unsupported: Counter = field(default_factory=Counter)
93:     mapping_counts: Counter = field(default_factory=Counter)
94:     placement_counts: Counter = field(default_factory=Counter)
95:     route_counts: Counter = field(default_factory=Counter)
96:     route_examples: Dict[str, List[dict]] = field(default_factory=dict)
97: 
98: 
99: @dataclass
```
### Current source `CE/pytests/nic400/audit_nic400_corpus.py`
Snapshot: HEAD; SHA-256 `a41ce94f4f87053fec0f46fefff4236f3f5de36c14b3140f0bf190cbb22c6a78`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 815, 'Lin Gao': 1}.
Introduction/rename-follow candidates: f0e5bb3195676179948595be567624c872686134 2026-05-08T22:51:19-05:00 Michael Coulter <michael.coulter@arm.com> feat(nic400): reconstruct NCI uArch and close DRCs.
```text
271:             if drc_diagnostics:
272:                 result["import"]["drc"] = normalize_drc_result(interconnect.run_drc(suppress_stdout=True))
273:                 result["import"]["drc_clean"] = result["import"]["drc"]["clean"]
274:         # Preserve the conversion result even when CE import rejects this fixture.
275:         except Exception:  # pylint: disable=broad-exception-caught
276:             result["import"] = _error_payload()
277: 
278:         result["overall_success"] = (
279:             result["conversion"].get("success") is True and result["import"].get("success") is True
280:         )
281:         return result
282:     finally:
```
```text
451:             "add_failed": {
452:                 "decision": "unemitted_topology_failure",
453:                 "rationale": (
454:                     "The NIC400 graph path was found, but IA rejected add_route. "
455:                     "The converted design therefore does not preserve that source route and "
456:                     "must be repaired before the fixture is accepted."
457:                 ),
458:             },
459:             "missing_graph_path": {
460:                 "decision": "unresolved_topology_gap",
461:                 "rationale": (
462:                     "The HLS/access metadata names the endpoint pair, but no directed path exists in the "
```

## guided

### Commit 0567531987d35ff866e312c510795b5b634707b1
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-29T13:19:56-05:00; reachable from selected HEAD: True.
Subject: Add NoC-Lite guided policy APIs
Change-Ids: I5a6a9860b323777cbc666403bfac403da76dd94b.
Diff excerpt, `CE/ideas/api/interconnect_flow.py`:
```diff
@@ -50,6 +50,8 @@ from ..flow_impl.nci_ma import create_default_microarchitecture, shorten_instanc
     get_insertable_instance_types, get_removable_instance_types
 from ..flow_impl.packet_header import get_packet_header_flit_sizes, get_gt_parameters, get_packet_header_bits, \
     get_packet_min_flit_sizes, get_fe_width, get_flit_size_requirements
+from ..flow_impl.guided_policy import apply_guided_flow_policy, check_guided_flow_compliance, minimize_latency, \
+    reduce_guided_flow_area, remove_pmu_configuration
 
 logger = logging.getLogger(__name__)
 
```
Diff excerpt, `CE/ideas/api/interconnect_flow.py`:
```diff
@@ -1364,6 +1366,121 @@ class InterconnectFlow:
         """
         return analyze_area(self, network_type, remove_b2b_routers)
 
+    def check_guided_flow_compliance(self, flow_id: str = "noc_lite", run_drc: bool = True) -> dict:
+        """
+        Check whether the active design satisfies a guided-flow policy.
+
+        Parameters
+        ----------
+        flow_id : str, optional
+            Guided-flow identifier. The first supported value is "noc_lite".
+        run_drc : bool, optional
+            If True, include HLS DRC cleanliness in the compliance result.
+
+        Returns
+        -------
+        dict :
+            Structured compliance result with status and violations.
+
+        Notes
+        -----
+        no-op: [CMN]
+        """
+        return check_guided_flow_compliance(self, flow_id, run_drc)
+
+    def apply_guided_flow_policy(self, flow_id: str = "noc_lite", dry_run: bool = False,
+                                 run_minimize_latency: bool = None) -> dict:
+        """
+        Apply guided-flow policy fixes to the active design.
+
+        Parameters
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/flow_impl/guided_policy.py`:
```diff
@@ -0,0 +1,1195 @@
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : $State$
+#
+# ----------------------------------------------------------------------------
+"""Guided-flow policy helpers for Interconnect Architect."""
+
+import copy
+import fnmatch
+import logging
+import re
+from pathlib import Path
+from typing import Any, Dict, Iterable, List, Optional, Tuple
+
+import yaml
+
+logger = logging.getLogger(__name__)
+
+GUIDED_FLOW_FEATURES_PATH = Path(__file__).resolve().parents[1] / "guided-flow-features.yaml"
+DEFAULT_PARAMS_NCI_PATH = Path(__file__).resolve().parents[1] / "default_params_nci.yaml"
[hunk excerpt ends; remaining lines omitted]
```
### Commit 3287440c76c2ab24aceaee5b73ebcc42cda052dc
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-29T13:20:27-05:00; reachable from selected HEAD: True.
Subject: Implement the NoC-Lite guided GUI flow
Change-Ids: I7bf6a7b1ed7219609f355667a0936eb4429794a2.
Diff excerpt, `GUI/src/app/app.component.ts`:
```diff
@@ -368,6 +385,124 @@ export class AppComponent implements OnInit, OnDestroy, AfterViewInit {
     });
   }
 
+  private async handleGuidedFlowProjectLoad(): Promise<boolean> {
+    let metadata: GuidedFlowMetadata | null = null;
+    try {
+      metadata = this.guidedFlowPolicyService.readMetadata();
+    } catch (error) {
+      await this.showGuidedFlowRecoveryDialog(null, error);
+      this.showAllTabs = false;
+      await this.router.navigate(['/project']);
+      return false;
+    }
+
+    if (
+      !metadata ||
+      !['active', 'starting'].includes(metadata.guidedFlow.state) ||
+      metadata.guidedFlow.retired
+    ) {
+      return true;
+    }
+
+    this.showAllTabs = false;
+    this.cdr.detectChanges();
+
+    while (true) {
+      try {
+        if (metadata.guidedFlow.state === 'starting') {
+          await this.guidedFlowPolicyService.activateAfterProjectLoad({ runMinimizeLatency: true });
+        } else {
+          await this.guidedFlowPolicyService.revalidateActiveProject();
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/app.component.ts`:
```diff
@@ -750,13 +890,36 @@ export class AppComponent implements OnInit, OnDestroy, AfterViewInit {
           //     }
           //   });
           // }
-          void this.navigateToProjectEntryRoute();
+          if (guidedReloadPending) {
+            void this.handleGuidedFlowProjectLoad()
+              .then(allowNormalEditing => {
+                if (allowNormalEditing) {
+                  void this.navigateToProjectEntryRoute();
+                } else {
+                  this.hideNavBar = false;
+                  this.cdr.detectChanges();
+                }
+              });
+          } else {
+            void this.navigateToProjectEntryRoute();
+          }
         }
       });
 
     });
   }
 
+  private shouldBlockGuidedReload(): boolean {
+    try {
+      const metadata = this.guidedFlowPolicyService.readMetadata();
+      return !!metadata &&
+        ['active', 'starting'].includes(metadata.guidedFlow.state) &&
+        !metadata.guidedFlow.retired;
+    } catch {
+      return true;
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/core/services/canvas-physical-data.service.ts`:
```diff
@@ -684,6 +705,90 @@ export class CanvasPhysicalDataService {
     return synthCompletedObserv;
   }
 
+  private saveSynthesizedProject(synthCompletedSubject: Subject<boolean>): void {
+    const savingSub = this.projectService.designSaved.subscribe(designWasSaved => {
+      savingSub.unsubscribe();
+      if (!designWasSaved) {
+        synthCompletedSubject.next(false);
+        showAppNotification('Failed to save project after SE Success!');
+        return;
+      }
+      synthCompletedSubject.next(true);
+    });
+    this.projectService.saveDesign();
+  }
+
+  private async applyGuidedPolicyAfterSynthesis(): Promise<void> {
+    if (!this.guidedFlowPolicyService.isGuidedModeActive) {
+      return;
+    }
+
+    const policyResult = await this.guidedFlowPolicyService.applyPolicy(
+      this.guidedFlowPolicyService.activeFlowId || 'noc_lite',
+      { runMinimizeLatency: true }
+    );
+    if (policyResult?.status !== 'passed') {
+      throw new Error('Guided-flow policy application failed.');
+    }
+
+    const areaResult = await this.guidedFlowPolicyService.reduceAreaAfterSynthesis();
+    if (areaResult?.status === 'failed') {
[hunk excerpt ends; remaining lines omitted]
```
### Commit 9f385e8b0fc6b8bbb2b9bef9170a43ce33d5146f
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-29T14:01:55-05:00; reachable from selected HEAD: True.
Subject: Make Guided Flow retirement atomic
Change-Ids: I91a667f2f36c84677374f8deaf8222bd7d84081a.
Diff excerpt, `GUI/src/app/shared/services/guided-flow-policy.service.ts`:
```diff
@@ -26,7 +26,7 @@ import { DataService } from './data.service';
 import { GuidedFlowLogService } from './guided-flow-log.service';
 import { StaticDataService } from './static-data.service';
 
-export type GuidedFlowState = 'not_guided' | 'starting' | 'active' | 'exit_confirmed' | 'retired';
+export type GuidedFlowState = 'not_guided' | 'starting' | 'active' | 'retired';
 export type GuidedFlowSourceType = 'example' | 'nic400_import' | 'guided_yaml_import';
 
 export interface GuidedFlowSource {
```
Diff excerpt, `GUI/src/app/shared/services/guided-flow-policy.service.ts`:
```diff
@@ -489,17 +489,14 @@ export class GuidedFlowPolicyService {
       return;
     }
 
-    metadata.guidedFlow.state = 'exit_confirmed';
-    metadata.guidedFlow.active = false;
-    this.writeMetadata(metadata);
-    this.publishMetadata(metadata);
-
-    metadata.guidedFlow.state = 'retired';
-    metadata.guidedFlow.retired = true;
-    metadata.guidedFlow.retiredAt = new Date().toISOString();
-    this.writeMetadata(metadata);
-    this.publishMetadata(metadata);
-    this.guidedFlowLogService.append(metadata.guidedFlow.flowId, 'Guided-flow mode retired.');
+    const retiredMetadata = JSON.parse(JSON.stringify(metadata)) as GuidedFlowMetadata;
+    retiredMetadata.guidedFlow.state = 'retired';
+    retiredMetadata.guidedFlow.active = false;
+    retiredMetadata.guidedFlow.retired = true;
+    retiredMetadata.guidedFlow.retiredAt = new Date().toISOString();
+    this.writeMetadataAtomically(retiredMetadata);
+    this.publishMetadata(retiredMetadata);
+    this.guidedFlowLogService.append(retiredMetadata.guidedFlow.flowId, 'Guided-flow mode retired.');
   }
 
   abandonStartingGuidedFlow(reason?: unknown): void {
```
Diff excerpt, `GUI/src/app/shared/services/guided-flow-policy.service.ts`:
```diff
@@ -600,6 +597,24 @@ export class GuidedFlowPolicyService {
     this.dataService.fs.writeFileSync(metadataPath, JSON.stringify(metadata, null, 2), 'utf8');
   }
 
+  private writeMetadataAtomically(metadata: GuidedFlowMetadata, projectDirectory?: string): void {
+    const metadataPath = this.metadataPath(projectDirectory);
+    if (!metadataPath) {
+      throw new Error('Cannot write guided-flow metadata without an active project directory.');
+    }
+    const temporaryPath = `${metadataPath}.tmp`;
+    this.dataService.fs.mkdirSync(dirname(metadataPath), { recursive: true });
+    try {
+      this.dataService.fs.writeFileSync(temporaryPath, JSON.stringify(metadata, null, 2), 'utf8');
+      this.dataService.fs.renameSync(temporaryPath, metadataPath);
+    } catch (error) {
+      if (this.dataService.fs.existsSync(temporaryPath)) {
+        this.dataService.fs.unlinkSync(temporaryPath);
+      }
+      throw error;
+    }
+  }
+
   private metadataPath(projectDirectory = this.projectService.projectDirectory): string | null {
     return projectDirectory ? join(projectDirectory, this.metadataDirectory, this.metadataFilename) : null;
   }
```
### Commit 18dc7270ca6f155cd2774eef6a4d222ad2451551
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-04T14:23:59-05:00; reachable from selected HEAD: True.
Subject: Harden Guided Flow metadata and project lifecycle
Change-Ids: I3765978eb208c7e5ea38342154cbaea3818c3d78.
Diff excerpt, `CE/ideas/flow_impl/guided_policy.py`:
```diff
@@ -1383,12 +1383,13 @@ def reduce_guided_flow_area(nci_obj: Any, remove_b2b_routers: bool = True, dry_r
     success = nci_obj.analyze_area("data", remove_b2b_routers)
     after_instances = nci_obj.get_instances()
     result["changed"] = before_instances != after_instances
-    result["changes"].append({
-        "objectPath": "dataNetwork",
-        "before": before_instances,
-        "after": after_instances,
-        "dryRun": False,
-    }) if result["changed"] else None
+    if result["changed"]:
+        result["changes"].append({
+            "objectPath": "dataNetwork",
+            "before": before_instances,
+            "after": after_instances,
+            "dryRun": False,
+        })
     if not success:
         result["status"] = "failed"
         result["errors"].append("analyze_area('data', remove_b2b_routers={}) failed.".format(remove_b2b_routers))
```
Diff excerpt, `CE/ideas/guided-flow-features.yaml`:
```diff
@@ -2,7 +2,6 @@ schemaVersion: 1
 guidedFlows:
   noc_lite:
     displayName: NoC-Lite
-    flowVersion: 1.0.0
     product_idx:
       - towernci_r0
       - towernci_r1_only
```
Diff excerpt, `CE/ideas/guided-flow-features.yaml`:
```diff
@@ -166,7 +165,7 @@ guidedFlows:
         optimizeWireMode: FlatLowWire
         maxLinkWidth: 64
       balancedAreaTiming:
-        description: Retains the minimum-area defaults unless timing closure requires relaxing timing-sensitive locks in a future flow version.
+        description: Retains the minimum-area defaults unless a future policy update relaxes timing-sensitive locks for timing closure.
 
     ceActions:
       checkCompliance:
```
### Commit 32939448d1a9a1f084701f320870daa4e0aa408e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-10-01T15:48:19-05:00; reachable from selected HEAD: True.
Subject: consolidate Guided Flow coverage across supported IPs
Change-Ids: I3c8f5ab3b48a8dd3b74a6bff6aabc93ae0630a57.
Diff excerpt, `GUI/tests/config/ip-capabilities.ts`:
```diff
@@ -95,13 +98,6 @@ const NITWAIN_LATEST_SPECS = [
   '**/hls/interfaces/data/stripe-group-duplicate-targets.spec.ts',
   '**/hls/paths/paths-edit-modal.extra-coverage.spec.ts',
   '**/hls/paths/stream-subsection-matrix.spec.ts',
-  '**/project/project.guided-badge.spec.ts',
-  '**/project/project.guided-flow-nic400-file-validation.spec.ts',
-  '**/project/project.guided-flow-adversarial.spec.ts',
-  '**/project/project.guided-flow-policy-refresh.spec.ts',
-  '**/project/project.guided-flow-latency-recovery.spec.ts',
-  '**/project/project.guided-flow-status-invalidation.spec.ts',
-  '**/project/project.guided-flow-live-unlock.spec.ts',
   '**/regression/nitwain-feature-rich-vertical.spec.ts',
   '**/regression/brunel-3059.spec.ts',
   '**/regression/brunel-4301.spec.ts',
```
Diff excerpt, `GUI/tests/config/ip-capabilities.ts`:
```diff
@@ -135,12 +131,49 @@ const CMN_SPECS_ONLY = [
   '**/user-defined-groups/*.spec.ts',
 ];
 
-const GUIDED_FLOW_SPECS_ONLY = [
-  '**/navigation/guided-navigation-persistence.spec.ts',
-  '**/project/project.guided-badge.spec.ts',
-  '**/project/project.guided-flow*.spec.ts',
+// Exact NoC-Lite support from CE/ideas/guided-flow-features.yaml. Display labels
+// (nocs3/nocs4) and other revisions of these families must not inherit coverage.
+export const GUIDED_FLOW_SUPPORTED_IPS: ReadonlySet<string> = new Set([
+  'nitwain_r1p0',
+  'towernci_r0p0',
+  'towernci_r1p3',
+  'towernci_r1p5',
+]);
+
+export const GUIDED_FLOW_SPECS_ONLY = ['**/project/project.guided-flow-*.spec.ts'];
+
+export const GUIDED_FLOW_SPEC_FILES = [
+  'project.guided-flow-launcher.spec.ts',
+  'project.guided-flow-import.spec.ts',
+  'project.guided-flow-policy.spec.ts',
+  'project.guided-flow-lifecycle.spec.ts',
 ];
 
+// Shared schema/recovery permutations run once; this does not restrict product
+// support or the common lifecycle/policy scenarios in the same spec files.
+export const GUIDED_FLOW_REPRESENTATIVE_IP = 'nitwain_r1p0';
+// Scenario ownership includes the legacy r1p3 migration exclusion check.
+export const GUIDED_FLOW_NIC400_SCENARIO_IPS = [
+  'towernci_r0p0',
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/tests/config/ip-capabilities.ts`:
```diff
@@ -659,13 +692,17 @@ export const OWO_SPEC_IPS: Readonly<Record<string, string>> = {
 export function capabilitiesForIp(ip: string): NavigationCapabilities {
   const normalized = normalizeIpKey(ip);
   const caps = IP_CAPABILITIES[normalized] ?? DEFAULT_CAPABILITIES;
+  const hasGuidedFlow = GUIDED_FLOW_SUPPORTED_IPS.has(ip);
   return {
     ...caps,
+    hasGuidedFlow,
+    grepInvert: [...(caps.grepInvert ?? []), ...guidedFlowGrepInvertForIp(ip)],
     // Playwright applies testIgnore after testMatch, so exact-version exclusions
     // also protect families whose base capabilities use an allowlist.
     testIgnore: [
       ...new Set([
         ...(caps.testIgnore ?? []),
+        ...(!hasGuidedFlow ? GUIDED_FLOW_SPECS_ONLY : []),
         ...Object.entries(OWO_SPEC_IPS)
           .filter(([, fixtureIp]) => fixtureIp !== ip)
           .map(([spec]) => spec),
```
### Commit badc593694d2ba52c12722ac5da52a934101dabc
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-10-03T20:57:55-05:00; reachable from selected HEAD: True.
Subject: Generate Nitwain NoC-Lite starter as a Guided Flow resource
Change-Ids: I059c92990262d97d4fc70d48b49fe303c0b360fe.
Diff excerpt, `CE/ideas/guided-flow-features.yaml`:
```diff
@@ -16,7 +16,7 @@ guidedFlows:
         examples:
           - id: noc_lite_min_area
             label: NoC-Lite Starter Example
-            path: resources/examples/nitwain_r1p0/socrates_yaml/example_noc_lite_min_area.yaml
+            path: resources/scripts/guided_flow/noc_lite/nitwain_r1p0/example_noc_lite_min_area.yaml
       towernci_r0p0:
         examples:
           - id: noc_lite_towernci_r0p0_4x4_axi5
```
Diff excerpt, `CE/pytests/api/test_import_export.py`:
```diff
@@ -37,7 +37,7 @@ test_dir_in = test_dir + "/input_files"
 test_dir_expected = test_dir + "/expected_files"
 NITWAIN_RESOURCE_DIR = Path(__file__).parents[3] / "resources/examples/nitwain_r1p0"
 NITWAIN_RESOURCE_EXAMPLES = (
-    NITWAIN_RESOURCE_DIR / "socrates_yaml/example_noc_lite_min_area.yaml",
+    NITWAIN_RESOURCE_DIR.parents[1] / "scripts/guided_flow/noc_lite/nitwain_r1p0/example_noc_lite_min_area.yaml",
     NITWAIN_RESOURCE_DIR / "socrates_yaml/example_1_ccg_combined.yaml",
     NITWAIN_RESOURCE_DIR / "socrates_yaml/example_2_ccg_combined.yaml",
     NITWAIN_RESOURCE_DIR / "synth/example_1_ccg_combined.yaml",
```
Diff excerpt, `CE/pytests/flow/test_noc_lite_starter.py`:
```diff
@@ -0,0 +1,95 @@
+#!/usr/bin/env python3
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : Internal
+#
+# ----------------------------------------------------------------------------
+
+"""The private Guided starter is derived from its CE construction recipe."""
+
+import importlib.util
+from pathlib import Path
+
+import pytest
+import yaml
+from tooling.general.decorators import ip
+
+CHECKOUT_ROOT = Path(__file__).resolve().parents[3]
+SCRIPT_PATH = CHECKOUT_ROOT / "resources/scripts/generate_noc_lite_starter.py"
+SPEC = importlib.util.spec_from_file_location("generate_noc_lite_starter", SCRIPT_PATH)
+starter = importlib.util.module_from_spec(SPEC)
[hunk excerpt ends; remaining lines omitted]
```
### Current source `CE/ideas/flow_impl/guided_policy.py`
Snapshot: HEAD; SHA-256 `055702068f12af5499d91560771764a94a821f54c77d251283265a5dd9c86b49`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1390, 'Lin Gao': 3}.
Introduction/rename-follow candidates: 0567531987d35ff866e312c510795b5b634707b1 2026-07-29T13:19:56-05:00 Michael Coulter <michael.coulter@arm.com> Add NoC-Lite guided policy APIs.
```text
48: def _load_features() -> Dict[str, Any]:
49:     with GUIDED_FLOW_FEATURES_PATH.open("r", encoding="utf-8") as features_file:
50:         features = yaml.safe_load(features_file) or {}
51:     if features.get("schemaVersion") != 1:
52:         raise ValueError("Unsupported guided-flow-features.yaml schemaVersion")
53:     return features
54: 
55: 
56: def _load_default_product_mapping() -> Dict[str, List[str]]:
57:     with DEFAULT_PARAMS_NCI_PATH.open("r", encoding="utf-8") as default_params_file:
58:         default_params = yaml.safe_load(default_params_file) or {}
59:     return default_params.get("product_mapping", {}) or {}
60: 
```
```text
98:     return resolved
99: 
100: 
101: def _supported_ip_versions(flow: Dict[str, Any], product_mapping: Dict[str, List[str]]) -> List[str]:
102:     if "product_idx" in flow:
103:         resolved_versions = _resolve_product_idx(flow.get("product_idx"), product_mapping)
104:     else:
105:         resolved_versions = list((flow.get("ipVersions") or {}).keys())
106:     supported_versions = flow.get("supportedIpVersions")
107:     if supported_versions is None:
108:         return resolved_versions
109:     return [ip_version for ip_version in supported_versions if ip_version in resolved_versions]
110: 
111: 
112: def _entry_supports_ip(entry: Any, ip_version: str, product_mapping: Dict[str, List[str]]) -> bool:
113:     if not isinstance(entry, dict) or "product_idx" not in entry:
114:         return True
115:     return ip_version in _resolve_product_idx(entry.get("product_idx"), product_mapping)
```
### Current source `GUI/src/app/shared/services/guided-flow-policy.service.ts`
Snapshot: HEAD; SHA-256 `216712d387303ff4fc473fb1df2f66af035b64e14d6daaf5c8c21fccd2fd71b0`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1347, 'Dustin divis': 29, 'Lin Gao': 13}.
Introduction/rename-follow candidates: 3287440c76c2ab24aceaee5b73ebcc42cda052dc 2026-07-29T13:20:27-05:00 Michael Coulter <michael.coulter@arm.com> Implement the NoC-Lite guided GUI flow.
```text
52: }
53: 
54: export interface GuidedFlowDataChange {
55:   action: 'applyPolicy' | 'minimizeLatency' | 'reduceArea';
56: }
57: 
58: interface GuidedFlowProjectContext {
59:   projectDirectory?: string;
60:   loadedIpVersion?: string;
61:   isCurrent?: () => boolean;
62: }
63: 
```
```text
124:   get isGuidedModeActive(): boolean {
125:     return this.primaryFlowMetadata?.state === 'active' &&
126:       !!this.activeMetadata?.primaryFlowId &&
127:       this.isFlowSupported(this.activeMetadata.primaryFlowId);
128:   }
129: 
130:   get activeFlowId(): string | null {
131:     return this.isGuidedModeActive ? this.activeMetadata?.primaryFlowId || null : null;
132:   }
133: 
134:   getPrimaryFlow(metadata: GuidedFlowMetadata | null | undefined): GuidedFlowProjectState | null {
135:     return getPrimaryGuidedFlow(metadata);
```
```text
155:     return this.features?.guidedFlows?.[flowId] || null;
156:   }
157: 
158:   isFlowSupported(flowId: string | null | undefined): boolean {
159:     return !!flowId && !!this.getFlow(flowId);
160:   }
161: 
162:   getSupportedIpVersions(flowId: string): string[] {
163:     const flow = this.getFlow(flowId);
164:     if (!flow) {
165:       return [];
166:     }
167:     let resolvedIpVersions: string[];
168:     if (flow.product_idx !== undefined) {
169:       resolvedIpVersions = this.resolveProductIdx(flow.product_idx);
170:     } else {
171:       resolvedIpVersions = Object.keys(flow.ipVersions || {});
172:     }
173:     if (!Array.isArray(flow.supportedIpVersions)) {
174:       return resolvedIpVersions;
175:     }
176:     return flow.supportedIpVersions.filter((ipVersion: string) => resolvedIpVersions.includes(ipVersion));
177:   }
178: 
179:   getExamples(flowId: string, ipVersion: string): any[] {
180:     return this.getFlow(flowId)?.ipVersions?.[ipVersion]?.examples || [];
181:   }
```
### Current source `GUI/src/app/shared/services/guided-flow-metadata.ts`
Snapshot: HEAD; SHA-256 `71ac6bbd171f60e1f7d757a8889726c3f00514555884d134975e1b85531c5216`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 318}.
Introduction/rename-follow candidates: 18dc7270ca6f155cd2774eef6a4d222ad2451551 2026-08-04T14:23:59-05:00 Michael Coulter <michael.coulter@arm.com> Harden Guided Flow metadata and project lifecycle.
```text
17: 
18: export const GUIDED_FLOW_METADATA_SCHEMA_VERSION = 1;
19: 
20: export type GuidedFlowState = 'not_guided' | 'starting' | 'active' | 'retired';
21: export type GuidedFlowSourcePathKind = 'repoRelative' | 'projectRelative' | 'absolute' | 'unavailable';
22: 
23: export interface GuidedFlowSource {
24:   type: string;
25:   path: string | null;
26:   pathKind: GuidedFlowSourcePathKind;
27:   originalPath?: string;
28:   sha256?: string;
```
```text
40: export interface GuidedFlowTimestamps {
41:   startedAt: string | null;
42:   activatedAt: string | null;
43:   retiredAt: string | null;
44:   [key: string]: unknown;
45: }
46: 
47: export interface GuidedFlowProjectState {
48:   state: GuidedFlowState;
49:   ipVersion: string | null;
50:   source: GuidedFlowSource;
51:   timestamps: GuidedFlowTimestamps;
```
```text
55: }
56: 
57: export interface GuidedFlowMetadata {
58:   schemaVersion: typeof GUIDED_FLOW_METADATA_SCHEMA_VERSION;
59:   primaryFlowId: string;
60:   guidedFlows: Record<string, GuidedFlowProjectState>;
61:   extensions: Record<string, unknown>;
62:   [key: string]: unknown;
63: }
64: 
65: export interface GuidedFlowMetadataNormalizationOptions {
66:   currentIpVersion?: string | null;
```
```text
70: export interface GuidedFlowMetadataNormalizationResult {
71:   metadata: GuidedFlowMetadata;
72:   migrated: boolean;
73:   sourceSchemaVersion: number | null;
74:   warnings: string[];
75: }
76: 
77: export class GuidedFlowMetadataCompatibilityError extends Error {
78:   constructor(
79:     message: string,
80:     readonly code: 'corrupt' | 'unsupported_schema' | 'unsupported_state' | 'unsupported_flow',
81:   ) {
82:     super(message);
83:     this.name = 'GuidedFlowMetadataCompatibilityError';
84:   }
85: }
86: 
87: export function normalizeGuidedFlowMetadata(
88:   rawMetadata: unknown,
```
### Current source `CE/ideas/guided-flow-features.yaml`
Snapshot: HEAD; SHA-256 `4c982f76dcb1a962b5078716f1b57a105437fe365324f3ce14323943afd0b713`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 214, 'Liza Dayoub': 6}.
Introduction/rename-follow candidates: 0567531987d35ff866e312c510795b5b634707b1 2026-07-29T13:19:56-05:00 Michael Coulter <michael.coulter@arm.com> Add NoC-Lite guided policy APIs.
```text
1: schemaVersion: 1
2: guidedFlows:
3:   noc_lite:
4:     displayName: NoC-Lite
5:     product_idx:
6:       - towernci_r0
7:       - towernci_r1_only
8:       - ni_noc_from_twain_r1p0
9:     supportedIpVersions:
10:       - nitwain_r1p0
11:       - towernci_r0p0
12:       - towernci_r1p3
13:       - towernci_r1p5
14:     ipVersions:
15:       nitwain_r1p0:
16:         examples:
17:           - id: noc_lite_min_area
18:             label: NoC-Lite Starter Example
19:             path: resources/scripts/guided_flow/noc_lite/nitwain_r1p0/example_noc_lite_min_area.yaml
20:       towernci_r0p0:
21:         examples:
22:           - id: noc_lite_towernci_r0p0_4x4_axi5
23:             label: NoC-Lite Tower NCI r0p0 4x4 AXI5 Example
24:             path: resources/examples/towernci_r0p0/socrates_yaml/example_1_4x4_axi5_combined.yaml
25:       towernci_r1p3:
26:         examples:
27:           - id: noc_lite_towernci_r1p3_4x4_axi5
```
```text
46:         parameter: useTrafficParameters
47:         product_idx: all
48:         value: Disabled
49:         reason: NoC-Lite guided mode locks this parameter for area-oriented synthesis.
50:       - scope: synthesis
51:         parameter: useTimingParameters
52:         product_idx: all
53:         value: Disabled
54:         reason: NoC-Lite guided mode disables timing-driven topology expansion for minimum area.
55:       - scope: synthesis
56:         parameter: maxLinkWidth
57:         product_idx: all
```

## owo

### Commit 9851f748f2450a96ad59aab5521b3bc157ba79db
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-29T02:44:43-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-4829: OWO Streaming Wizard
Change-Ids: Ia7a479c80a64e8fc4d1c2704dd8e17f0b0e29b50.
Diff excerpt, `GUI/src/app/canvas/canvas.component.ts`:
```diff
@@ -1449,30 +1463,101 @@ export class CanvasComponent implements OnInit, AfterViewInit, OnDestroy {
       }
       if (paramUpdate !== null) {
         if (paramUpdate.name) {
-          if (JSON.stringify(node.resourcePlane) !== JSON.stringify(paramUpdate.resourcePlane)) {
-            this.interfaceApiService.pushInterfaceResourcePlane(
-              paramUpdate.name,
-              paramUpdate.resourcePlane,
-            );
-          }
-          const param = {};
-          const option_param = {};
-          for (const field of Object.keys(paramUpdate)) {
-            if (['name', 'clkType', 'resourcePlane'].includes(field)) {
-              continue;
-            }
-            if (field.startsWith('options_'))
-              option_param[field.replace('options_', '')] = paramUpdate[field];
-            else param[field] = paramUpdate[field];
-          }
+          void this.persistCanvasInterfaceEdit(node, paramUpdate, editorResult?.owoWizardLaunch);
+        }
+      }
+    });
+  }
 
-          this.canvasInterfacesService.setInterfaceParameters(node.name, param);
+  private async persistCanvasInterfaceEdit(
+    node: InterfaceGroupNode,
+    paramUpdate: Record<string, any>,
+    owoWizardLaunch?: OwoWizardLaunchContext,
+  ): Promise<void> {
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/ui/sidebar/property-editor/canvas-interface-editor/canvas-interface-editor.component.ts`:
```diff
@@ -475,8 +472,7 @@ export class CanvasInterfaceEditorComponent implements OnInit, OnDestroy {
                                       resourcePlane: info.resourcePlane,
                                       count: 0,
                                       labels: ''};
-    const modalHost = this.canvasService.modalHost;
-    if (!modalHost) {
+    if (!this.canvasService.modalHost) {
       if (request && retryCount < 10) {
         if (this.interfaceSearchModalRetryTimeout) {
           clearTimeout(this.interfaceSearchModalRetryTimeout);
```
Diff excerpt, `GUI/src/app/interfaces/interface-inspect-node/interface-inspect-node.component.spec.ts`:
```diff
@@ -67,14 +81,38 @@ describe('InterfaceInspectModal', () => {
   let interfaceServiceSpy: InterfaceService;
   let mcnInterfaceServiceSpy: McnInterfaceService;
   let pathApiService: jasmine.SpyObj<PathServiceAPI>;
+  let appAlertServiceSpy: jasmine.SpyObj<AppAlertService>;
   beforeEach(waitForAsync(() => {
-    const interfaceService = jasmine.createSpyObj('InterfaceService', ['fetchStripes', 'fetchInterfacesAll', 'fetchInterfaceGroups',
-     'setUndoState', 'fetchClockIds', 'fetchAttributes','resetUndoState', 'setInterfaceMrpEnabled', 'filterEmptyArray']);
+    const interfaceService = jasmine.createSpyObj('InterfaceService', [
+      'fetchStripes',
+      'fetchInterfacesAll',
+      'fetchInterfaceGroups',
+      'setUndoState',
+      'fetchClockIds',
+      'fetchAttributes',
+      'resetUndoState',
+      'setInterfaceMrpEnabled',
+      'filterEmptyArray',
+    ]);
     const mcnInterfaceService = jasmine.createSpyObj('McnInterfaceService', ['fetchExternalClock']);
-    pathApiService = jasmine.createSpyObj('PathServiceAPI', ['pushAddTrafficPath', 'getPathsInfo', 'getPathsInfoSubject', 'fetchInterfaceResourcePlane']);
+    const appAlertService = jasmine.createSpyObj('AppAlertService', ['confirm']);
+    appAlertService.confirm.and.returnValue(of(false));
+    pathApiService = jasmine.createSpyObj('PathServiceAPI', [
+      'pushAddTrafficPath',
+      'getPathsInfo',
+      'getPathsInfoSubject',
+      'fetchInterfaceResourcePlane',
+    ]);
     pathApiService.getPathsInfoSubject = new ReplaySubject<any>(1);
     TestBed.configureTestingModule({
-      imports: [FormsModule, MatIconModule, MatTabsModule, MatTooltipModule, FormsModule, ReactiveFormsModule],
[hunk excerpt ends; remaining lines omitted]
```
### Commit e19a7b5a8db40056f8c3ac002504a39d3fe65383
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-10-01T15:14:02-05:00; reachable from selected HEAD: True.
Subject: OWO Streaming Wizard feedback updates
Change-Ids: I7d97964e5c0880837fe282d50e2db48a7986a7a2.
Diff excerpt, `GUI/src/app/interfaces/owo-setup/owo-setup.component.spec.ts`:
```diff
@@ -228,6 +228,11 @@ describe('OwoSetupComponent graph workflow', () => {
         preApplyFingerprint: 'base',
       }),
       createInterfaces: jasmine.createSpy('createInterfaces'),
+      ccgCreationSupported: true,
+      createOpeningCheckpoint: jasmine.createSpy('createOpeningCheckpoint').and.resolveTo({ path: '/project/checkpoint/opening.yaml', fingerprint: 'opening' }),
+      restoreOpeningCheckpoint: jasmine.createSpy('restoreOpeningCheckpoint').and.resolveTo(),
+      releaseOpeningCheckpoint: jasmine.createSpy('releaseOpeningCheckpoint').and.resolveTo(),
+      nextCcgGroupName: jasmine.createSpy('nextCcgGroupName').and.resolveTo('ccg_0'),
       createClock: jasmine.createSpy('createClock'),
       keepPartialChanges: jasmine.createSpy('keepPartialChanges').and.resolveTo(state()),
       restoreSnapshot: jasmine.createSpy('restoreSnapshot').and.resolveTo(true),
```
Diff excerpt, `GUI/src/app/interfaces/owo-setup/owo-setup.component.spec.ts`:
```diff
@@ -292,6 +297,152 @@ describe('OwoSetupComponent graph workflow', () => {
     ]);
   });
 
+  it('loads the editor independently of a delayed opening checkpoint and gates live mutations', async () => {
+    let ready!: (value: any) => void;
+    facade.createOpeningCheckpoint.and.returnValue(new Promise(resolve => ready = resolve));
+    await component.ngOnInit();
+    expect(component.loading).toBeFalse();
+    expect(component.form).toBeDefined();
+    expect(component.checkpointPending).toBeTrue();
+    expect(component.closeDisabled).toBeTrue();
+    component.onStartCreateInterface('manager');
+    await component.onStartCreateCcgGroup();
+    await component.onApply();
+    await component.onCancel();
+    expect(component.creatingInterfaceDirection).toBeNull();
+    expect(facade.applySystem).not.toHaveBeenCalled();
+    expect(facade.nextCcgGroupName).not.toHaveBeenCalled();
+    ready({ path: '/checkpoint.yaml' });
+    await Promise.resolve();
+    expect(component.closeDisabled).toBeFalse();
+    expect(component.checkpointPending).toBeFalse();
+    expect(facade.createOpeningCheckpoint).toHaveBeenCalledTimes(1);
+  });
+
+  it('offers retry after checkpoint creation fails without changing the draft', async () => {
+    facade.createOpeningCheckpoint.and.rejectWith(new Error('disk full.'));
+    await component.ngOnInit();
+    expect(component.checkpointError).toContain('disk full');
+    expect(component.checkpointError).not.toContain('..');
+    expect(component.closeDisabled).toBeTrue();
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/interfaces/owo-setup/owo-setup.component.spec.ts`:
```diff
@@ -1408,8 +1559,8 @@ describe('OwoSetupComponent graph workflow', () => {
       preApplyFingerprint: 'base',
       snapshotRestoration: { attempted: true, verified: false },
     };
-    expect(component.closeActionLabel).toBe('Close wizard (unverified state)');
-    expect(component.closeActionTooltip).toContain('could not be verified');
+    expect(component.closeActionLabel).toBe('Cancel');
+    expect(component.closeActionTooltip).toContain('checkpoint');
     component.applyResult.snapshotRestoration!.verified = true;
     expect(component.needsMutationRecovery).toBeFalse();
     expect(component.closeActionLabel).toBe('Cancel');
```
### Current source `GUI/src/app/interfaces/owo-setup/owo-setup.facade.ts`
Snapshot: HEAD; SHA-256 `9cb3399712a9f7c46d06788872ce0d5ab3d14678a39e986ff4effe41e878e13e`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 4877, 'Dustin divis': 447}.
Introduction/rename-follow candidates: 9851f748f2450a96ad59aab5521b3bc157ba79db 2026-09-29T02:44:43-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-4829: OWO Streaming Wizard.
```text
35:   ceWorkflowNotification,
36: } from 'src/app/shared/services/ce-mutation-outcome';
37: import {
38:   OWO_RESERVED_GT_RESOURCE_PLANE,
39:   OWO_STREAM_PARAMETER,
40:   OwoApplyOperationResult,
41:   OwoApplyResult,
42:   OwoClockCreationRequest,
43:   OwoChic2cLogicalLinkInfo,
44:   OwoInterfaceCreationRequest,
45:   OwoInterfaceCandidate,
46:   OwoMemoryMapState,
47:   OwoMemoryRangeDraft,
48:   OwoMemoryRegionState,
49:   OwoParameterInfo,
50:   OwoResourcePlaneAssignmentDraft,
51:   OwoResourcePlaneAssignmentMode,
52:   OwoResourcePlaneDraft,
53:   OwoReview,
54:   OwoReviewItem,
55:   OwoDestinationDraft,
56:   OwoSourceDraft,
57:   OwoSourceMapDraft,
58:   OwoStripeGroupDraft,
59:   OwoSetupDraft,
60:   OwoSetupState,
```
```text
67:   OwoOpeningCheckpoint,
68: } from './owo-setup.models';
69: import {
70:   defaultTargetWriteCapacity,
71:   destinationMembers,
72:   expandOwoRelationships,
73:   getOwoIdmParameter,
74:   getOwoParameter,
75:   isDmniProtocol,
76:   isOwoStreamingEnabled,
77:   normalizeOwoParameterInfo,
78:   numericParameterAllowsValue,
```
### Current source `GUI/src/app/interfaces/owo-setup/owo-memory-ranges.ts`
Snapshot: HEAD; SHA-256 `df84967aa5ae15ca884e552a966fdc4b3984f9fcfbd6aae7e4927fbdbc6c745c`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 79}.
Introduction/rename-follow candidates: 9851f748f2450a96ad59aab5521b3bc157ba79db 2026-09-29T02:44:43-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-4829: OWO Streaming Wizard.
### Current source `GUI/tests/ui/feature-flows/owo-setup-wizard.spec.ts`
Snapshot: HEAD; SHA-256 `5cb031abd8797335065ddcba37c1bff85fb1be75bfac40fdb4c1adfc5ca6f545`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 3391, 'Dustin divis': 72, 'Liza Dayoub': 24}.
Introduction/rename-follow candidates: 9851f748f2450a96ad59aab5521b3bc157ba79db 2026-09-29T02:44:43-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-4829: OWO Streaming Wizard.
```text
28:   label: string;
29:   sourceProtocol: string;
30:   targetProtocol: string;
31:   capacityDrc: 'MA_69_1' | 'MA_69_2';
32:   sourceKind: 'ASNI' | 'DSNI';
33: }
34: 
35: interface OpenWizardResult {
36:   sourceNames: string[];
37:   targetNames: string[];
38:   wizard: OwoSetupWizardPage;
39: }
```
```text
48: }
49: 
50: interface CcgOwoWizardOptions {
51:   clearUserResourcePlanes?: boolean;
52:   sourceChiRpCount?: number;
53: }
54: 
55: const nitwainOwoPairings: OwoPairingCase[] = [
56:   {
57:     label: 'ACE5Lite source to ACE5Lite target with AXI address metadata',
58:     sourceProtocol: 'ACE5Lite',
59:     targetProtocol: 'ACE5Lite',
60:     capacityDrc: 'MA_69_2',
61:     sourceKind: 'ASNI',
62:   },
63:   {
64:     label: 'ASNI to AMNI two-hop flow',
65:     sourceProtocol: 'AXI5',
66:     targetProtocol: 'AXI5',
67:     capacityDrc: 'MA_69_2',
68:     sourceKind: 'ASNI',
69:   },
70:   {
71:     label: 'DSNI to AMNI two-hop flow',
72:     sourceProtocol: 'CHI-H',
73:     targetProtocol: 'AXI5',
74:     capacityDrc: 'MA_69_2',
75:     sourceKind: 'DSNI',
76:   },
77:   {
78:     label: 'ASNI to DMNI three-hop flow',
79:     sourceProtocol: 'AXI5',
80:     targetProtocol: 'CHI-G',
81:     capacityDrc: 'MA_69_1',
82:     sourceKind: 'ASNI',
```

## deadlock

### Commit 5d7183cf554c64341e5b7e1c4adfa3857ee4cac8
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-10-28T12:22:22-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2900: Deadlock detection (Part 1)
Change-Ids: I66612f6cbd8f8f8b57312cac282be627075b7b51.
Diff excerpt, `GUI/src/app/canvas/canvas-design-flow/canvas-palette-u-arch/canvas-palette-u-arch.component.ts`:
```diff
@@ -116,7 +116,7 @@ export class CanvasPaletteUArchComponent implements OnInit, OnDestroy {
   }
 
   get checkNewInstacesAvaialble(): boolean {
-    return this.canvasGuiDataService.availableInstances.length === 0 
+    return this.canvasGuiDataService.availableInstances.length === 0; 
   }
 
   ngOnDestroy(): void {
```
Diff excerpt, `GUI/src/app/canvas/canvas-design-flow/canvas-toolbar/canvas-toolbar.component.ts`:
```diff
@@ -126,12 +126,12 @@ export class CanvasToolbarComponent implements OnInit, OnDestroy {
     if ((event.metaKey || event.ctrlKey) && event.key?.toLowerCase?.() === 's') {
       return;
     }
-    for (let [tool, toolInfo] of Object.entries(this.uiFrameset)) {
+    for (const [tool, toolInfo] of Object.entries(this.uiFrameset)) {
       if (!toolInfo.hasOwnProperty('hotKey')) { continue; }
       if (toolInfo['hotKey'] === event.key) {
-        for (let t of this.canvasTools) {
+        for (const t of this.canvasTools) {
           if (t['name'] === tool) {
-            let canvasTool = tool;
+            const canvasTool = tool;
             this.selectTool(canvasTool);
             if (this.uniqueTools.includes(canvasTool)) {
               t['selected'] = true;
```
Diff excerpt, `GUI/src/app/canvas/canvas-design-flow/canvas-toolbar/canvas-toolbar.component.ts`:
```diff
@@ -150,11 +150,11 @@ export class CanvasToolbarComponent implements OnInit, OnDestroy {
     if ((event.metaKey || event.ctrlKey) && event.key?.toLowerCase?.() === 's') {
       return;
     }
-    for (let [tool, toolInfo] of Object.entries(this.uiFrameset)) {
+    for (const [tool, toolInfo] of Object.entries(this.uiFrameset)) {
       if (!toolInfo.hasOwnProperty('hotKey')) { continue; }
       if (!this.uniqueTools.includes(tool)) { continue; }
       if (toolInfo['hotKey'] === event.key) {
-        for (let t of this.canvasTools) {
+        for (const t of this.canvasTools) {
           if (t['name'] === tool) {
             if (this.uniqueTools.includes(tool)) {
               t['selected'] = false;
```
### Commit a6053261023e4d20f77231c8faac995dd829a5e9
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-11-03T15:34:51-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-2900: Deadlock detection (Part 2)
Change-Ids: I1fc0c33c0fa349f18a3531778d34b85359eaca27.
Diff excerpt, `GUI/src/app/canvas/canvas-expansion.service.ts`:
```diff
@@ -122,6 +122,9 @@ export class CanvasExpansionService {
   }
 
   set sidebarTabIndex(tab: SidebarTab) {
+    if (this.sidebarTab === tab) {
+      return;
+    }
     this.sidebarTab = tab;
     this.sidebarTabChanged.next(tab);
   }
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -45,7 +46,8 @@ import {
   MeshDeadlockDeadlockedPair,
   MeshDeadlockPayload,
   MeshDeadlockTurnDetail,
-  MeshDeadlockTurnRoute
+  MeshDeadlockTurnRoute,
+  MeshDeadlockMxpsGrid
 } from 'src/app/canvas/shared/models/mesh-deadlock.model';
 
 export interface Route {
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -233,6 +252,10 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
   highlightedTargetInstanceLink: { x1:number, y1:number, x2:number, y2:number } | null = null;
   // routing submit state
   isRouteValid = false;
+  private static readonly DEADLOCK_STROKE_WIDTH = 3.5;
+  private static readonly ROUTING_HIGHLIGHT_STROKE_WIDTH_DEFAULT = 8;
+  private static readonly ROUTING_HIGHLIGHT_STROKE_WIDTH_WITH_DEADLOCK = 15;
+
   routingHighlightColor = '#39FF14'; // neon green
   invalidRoutingColor = '#FF3B30';   // red for invalid turns
   validRoutingTurns: any = {};
```
### Commit c46b9c3ca90a63169ce3ae61eaa7a7746e04658c
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-11-08T20:02:54-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-2900: Deadlock detection (Part 3)
Change-Ids: Ic8060e09fd5231d369287eec1fe2ea7d1debd313.
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -3661,6 +3661,13 @@
         uniqueLink: ["project", "mesh", "globals", "node-configuration", "canvas", "test-and-report", "build"],
         order: ["Mesh", "Globals", "User Defined Groups", "Canvas", "Test & Report", "Build"]
       },
+      features: {
+        baseRoutingTab: true,
+        meshRouteEditorSidebar: true,
+        deadlockSidebar: true,
+        canvasTileOverlayToggle: true,
+        canvasOverlayToolbar: true
+      },
       canvas: {
         floorplan: ["logicalMesh"],
         designFlow: ["canvas-mesh-configuration", "canvas-toolbar", "canvas-palette-cmn"],
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -283,6 +286,7 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
   deadlockIndicatorsDirty = false;
   deadlockHasRenderableData = false;
   deadlockOverlayVisible = true;
+  overlayToolbarEnabled = false;
   deadlockLoopKey = 'all';
   deadlockOverlayArrows: DeadlockArrowSegment[] = [];
   readonly deadlockStrokeColor = 'red';
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -290,6 +294,7 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
   readonly deadlockStrokeVectorEffect = 'non-scaling-stroke';
   readonly deadlockArrowEndPadding = 10;
   private readonly deadlockTurnAnchors = this.createDeadlockTurnAnchors();
+  deadlockIndicatorRunning = false;
 
   get routingHighlightStrokeWidth(): number {
     return (this.deadlockOverlayVisible && this.deadlockHasRenderableData)
```
### Commit 28ed79a29c52ff893ee9894357de071123c7e92e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-11-09T00:14:49-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-2900: Deadlock detection (Part 4)
Change-Ids: I6fe1ad310703efc742d44286ef4ae8cfa3eb68ff.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -2592,17 +2592,37 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
     }
     let minLabelX = Number.POSITIVE_INFINITY;
     let minLabelY = Number.POSITIVE_INFINITY;
+    let anchorSvgX: number | null = null;
+    let anchorSvgY: number | null = null;
     for (const loop of loops) {
       for (const [px, py] of loop) {
         if (px < minLabelX) { minLabelX = px; }
         if (py < minLabelY) { minLabelY = py; }
       }
     }
+    for (const coord of componentCoords) {
+      const crosspoint = this.crosspoints?.[coord.x]?.[coord.y];
+      if (!crosspoint) {
+        continue;
+      }
+      const { domainSvgX, domainSvgY } = crosspoint;
+      if (typeof domainSvgX !== 'number' || typeof domainSvgY !== 'number' || !Number.isFinite(domainSvgX) || !Number.isFinite(domainSvgY)) {
+        continue;
+      }
+      if (
+        anchorSvgY === null ||
+        domainSvgY < anchorSvgY ||
+        (domainSvgY === anchorSvgY && (anchorSvgX === null || domainSvgX < anchorSvgX))
+      ) {
+        anchorSvgX = domainSvgX;
+        anchorSvgY = domainSvgY;
+      }
+    }
     if (!Number.isFinite(minLabelX) || !Number.isFinite(minLabelY)) {
       return null;
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/shared/services/canvas-gui-data.service.ts`:
```diff
@@ -548,6 +548,10 @@ export class CanvasGuiDataService {
     return Math.round((pxVal / scale) * multiplier);
   }
 
+  cancelPendingZoom(canvasType: string, canvasId?: string): void {
+    this.clearPendingZoomEntries(canvasType, canvasId);
+  }
+
   private clearPendingZoomEntries(canvasType: string, canvasId?: string): void {
     const targetId = canvasId ?? undefined;
     const keysToRemove: string[] = [];
```
### Current source `GUI/src/app/canvas/ui/sidebar/mesh-deadlock/mesh-deadlock.component.ts`
Snapshot: HEAD; SHA-256 `2ca6b3960859a71c52d036ec5b80363cb7ee42e09d4e2c788835c89740fa136f`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1096, 'Dustin Divis': 37, 'Pawan Kakarla': 8, 'Dustin divis': 3}.
Introduction/rename-follow candidates: 5d7183cf554c64341e5b7e1c4adfa3857ee4cac8 2025-10-28T12:22:22-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-2900: Deadlock detection (Part 1).
```text
22: import { CanvasLogicalDataService, DeadlockDirtyState, normalizeCalPortValue, normalizePortValue } from 'src/app/canvas/core/services/canvas-logical-data.service';
23: import { CanvasExpansionService } from 'src/app/canvas/core/services/canvas-expansion.service';
24: import {
25:   MeshDeadlockChannelPayload,
26:   MeshDeadlockCoordinate,
27:   MeshDeadlockDeadlockedPair,
28:   MeshDeadlockPayload,
29:   MeshDeadlockTurnDetail,
30:   MeshDeadlockTurnRoute,
31:   MeshDeadlockMxpsGrid
32: } from 'src/app/canvas/core/models/mesh-deadlock.model';
33: import { MeshRouteRow } from 'src/app/canvas/ui/sidebar/mesh-route-editor/mesh-route-editor.component';
34: import { SidebarTab } from 'src/app/canvas/core/models/expansion-panel.enum';
35: import cloneDeep from 'lodash/cloneDeep';
36: 
37: interface DeadlockChannelOption {
38:   key: string;
39:   channel: string;
40:   subChannel: number;
41:   loopCount: number;
42:   disabled: boolean;
43:   isDirty: boolean;
44: }
45: 
```
### Current source `CE/ideas/flow_impl/deadlock_analysis.py`
Snapshot: HEAD; SHA-256 `26fb0c549f6dc16c010c0638beaaf78ecec34d039611704297aa365a7e69b194`.
Surviving-line author counts (attribution context only): {'Christopher Alvarez': 2, 'lingao01': 71, 'Lin Gao': 246}.
Introduction/rename-follow candidates: 4c1307f3aa52cd86cbe46ba7c9b14d866a122f81 2021-02-24T14:16:47-06:00 lingao01 <lingao01@arm.com> Move flow implementations to flow_helper directory..
```text
24: 
25: 
26: _DEADLOCK_TRANSIT_INSTANCE_TYPES = {"nrss", "pcdcs", "serdes"}
27: _HIGH_DUPLINK_CHANNELS = ("readRequest", "writeRequest", "readResponse", "writeResponse")
28: _LOW_DUPLINK_CHANNELS = ("readWriteRequest", "readWriteResponse")
29: _CHANNELS_BY_WIREMODE = {
30:     "high": _HIGH_DUPLINK_CHANNELS,
31:     "low": _LOW_DUPLINK_CHANNELS,
32: }
33: 
34: 
35: def _channels_for_wiremode(wiremode):
36:     """Return physical channels, or one route channel for a non-data wire mode."""
37:     return _CHANNELS_BY_WIREMODE.get(wiremode, (f"wireMode:{wiremode}",))
38: 
39: 
```

## latency

### Commit 519cf31c6c2c4f7cad86550de47b313f29cb7a5e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-10-07T15:20:59-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2535: Create API to get 'default_latency' from instance attributes
Change-Ids: I38f78a354574ecff012ed2df1620b2dbd0a22b4d.
Diff excerpt, `CE/ideas/api/interconnect_config.py`:
```diff
@@ -5221,6 +5221,47 @@ class InterconnectConfig:
         """
         return self._instances.get_instance_attributes()
 
+    def get_all_default_latency(self) -> dict:
+        """
+        This function returns the default_latency attribute for all instance types.
+
+        Parameters
+        ----------
+        none
+
+        Returns
+        ----------
+        dict :
+            A dictionary containing the default_latency attribute for each instance type.
+
+        Notes
+        -----
+        no-op: [CMN]
+        """
+        return self._instances.get_all_default_latency()
+
+    def get_instance_default_latency(self, instance_name: str) -> dict:
+        """
+        This function returns the default_latency attribute for the specified instance for the current instance wiremode.
+
+        Parameters
+        ----------
+        instance_name : str, required
+            Name of the instance.
+
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/base/parameter.py`:
```diff
@@ -89,7 +89,9 @@ class ParameterBase:
         orig_v = self._params_dict(is_synth)[cur_param]['value']
         final_v = 0
 
-        def extract_and_mask(orig_value, new_value, bit_offset, mask, bits):
+        def extract_and_mask(orig_value, new_value, bit_offset, mask, bits, wiremode=None):
+            if isinstance(mask, dict): # mask is in form {'high': 1, 'low': 0}
+                mask = mask[wiremode]
             a = (orig_value >> bit_offset) & ((1 << bits) - 1) & ~mask
             b = (new_value >> bit_offset) & ((1 << bits) - 1) & mask
             return (a | b) << bit_offset
```
Diff excerpt, `CE/ideas/base/parameter.py`:
```diff
@@ -125,7 +127,10 @@ class ParameterBase:
             else:
                 num_bits = bitcount - bit_start
             index += 1
-            final_v |= extract_and_mask(orig_v, new_v, bit_start, bit_mask, num_bits)
+            wm = None
+            if hasattr(self, "wireMode"):
+                wm = self.wireMode
+            final_v |= extract_and_mask(orig_v, new_v, bit_start, bit_mask, num_bits, wm)
         if final_v != new_v:
             logger.warning("%s value 0x%x has been updated to 0x%x",
                            cur_param, new_v, final_v)
```
### Commit 4c2bce6ad1f3ce33dd870f14d4e6122d256acf77
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-10-11T11:00:44-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2537: Update static latency report to use new attribute API and report new min latency info - part 1
Change-Ids: I7523f8c262bb4a9ceac2f23315ae3a26922ebd1f.
Diff excerpt, `resources/scripts/reports/report_static_latency.py`:
```diff
@@ -29,961 +28,6 @@ from html_module import html_class
 
 # asnis start pg 106 (arm_corelink_ni-tower_network-on-chip_interconnect_configuration_and_integration_manual_102770_0100_03_en.pdf) and pg 122 (arm_corelink_si_tower_system_interconnect_configuration_and_integration_manual_102772_0000_01_en.pdf)
 # all retiming is the same between NI/SI-Tower, except that SI-Tower has CMNI and NI-Tower does not.
-default_lookup = {
-    "asnis": {
-        "low": {
-            "readRequest": 0,
-            "writeRequest": 0,
-            "readResponse": 1,
-            "writeResponse": 0,
-            "readData": 0,
-            "writeData": 0,
-        },
-        "high": {
-            "readRequest": 0,
-            "writeRequest": 0,
-            "readResponse": 1,
-            "writeResponse": 0,
-            "readData": 0,
-            "writeData": 1,
-        },
-    },
-    "amnis": {
-        "low": {
-            "readRequest": 0,
-            "writeRequest": 0,
-            "readResponse": 1,
-            "writeResponse": 1,
-            "readData": 0,
-            "writeData": 0,
-        },
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `resources/scripts/reports/report_static_latency.py`:
```diff
@@ -1021,8 +72,8 @@ def instFromHop(hop):
         print("ERROR: Unable to decode hop from route")
         sys.exit()
 
-
 def calcInstLatency(inst, ch, next, prev):
+    valid_retiming_params = ["adaptor/readRetimingStages", "adaptor/writeRetimingStages", "adaptor/retimingStages"]
     l = []
     # Instance type
     t = nci.get_instance_type(inst)
```
Diff excerpt, `resources/scripts/reports/report_static_latency.py`:
```diff
@@ -1042,10 +93,9 @@ def calcInstLatency(inst, ch, next, prev):
     assert wm in default_lookup[t], ("Unexpected wire mode", wm, "for type", t)
     assert ch in default_lookup[t][wm], ("Unexpected channel", ch, "for type", t, "and wire mode", wm)
 
-    # default latency is dependent on wire mode
-
+    # default latency
+    # dependent on wire mode
     if default_lookup[t][wm][ch] > 0:
-        # add a default cycle of latency to the AMNI write request path in full wire mode.
         if t == 'serdes':
             l.append({"name": inst, "type": t, "clock": clock,
                       "reason": "Minimum latency through instance. This cycle of latency is not present if the serdes is bypassed due to the flitsizes being equal on inputs and outputs.",
```
### Commit 6e276c22916434f742b5c2c8bfe47c862af6d09a
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-10-21T01:29:06-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2537: Update static latency report to use new attribute API and report new min latency info - part 2
Change-Ids: I7304905c1a3b60d1dccf7094ed8b343232d02cf7.
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -12130,6 +12130,47 @@
             type: "integer",
             notation: "binary",
             bitcount: 9,
+            min_latency: {
+              low: {
+                readRequestPath: {
+                  min_asserted_bits: {
+                    (0, 2, 4): 1,
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the request channel in a low wire mode ASNI, you must use at least one of the following retiming options:
+                    • Write ingress register
+                    • Write internal register
+                    • Read egress register",
+                },
+                readResponsePath: {
+                  min_asserted_bits: {
+                    (1, 3, 5, 5): 1,
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the response channel for a low wire mode ASNI, you must use at least one of the following retiming options:
+                    • Read egress register (1)
+                    • Read internal register (1)
+                    • Write internal register (1)
+                    • Write ingress register
+                    You must not use the read ingress register option if the read internal register (2) option is enabled. Similarly, you must not use the read internal register (2) option if the read ingress register option is enabled.",
+                },
+              },
+              high: {
+                readRequestPath: {
+                  min_asserted_bits: {
+                    (0, 2, 4): 1,
+                  },
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -12324,6 +12365,44 @@
             type: "integer",
             notation: "binary",
             bitcount: 7,
+            min_latency: {
+              low: {
+                writeRequestPath: {
+                  min_asserted_bits: {
+                    (0, 2, 4): 1,
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the request channel in a low wire mode ASNI, you must use at least one of the following retiming options:
+                    • Write ingress register
+                    • Write internal register
+                    • Read egress register",
+                },
+                writeResponsePath: {
+                  min_asserted_bits: {
+                    (1, 3, 5, 5): 1,
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the response channel for a low wire mode ASNI, you must use at least one of the following retiming options:
+                    • Read egress register (1)
+                    • Read internal register (1)
+                    • Write internal register (1)
+                    • Write ingress register
+                    You must not use the read ingress register option if the read internal register (2) option is enabled. Similarly, you must not use the read internal register (2) option if the read ingress register option is enabled.",
+                },
+              },
+              high: {
+                writeRequestPath: {
+                  min_asserted_bits: {
+                    (0, 2, 4, 6): 1,
+                  },
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -12540,6 +12619,40 @@
             type: "integer",
             notation: "binary",
             bitcount: 7,
+            min_latency: {
+              low: {
+                readRequestPath: {
+                  min_asserted_bits: {
+                    (0, 2, 4): 1
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the AMNI read data path, you must select at least one of the following options:
+                    • Read request ingress register
+                    • Read request internal register
+                    • Read request egress register
+                    You must not select the read request internal register (2) option.",
+                },
+                readResponsePath: {
+                  min_asserted_bits: {
+                    (1, 1, 3): 1
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the AMNI read data path, you must select at least one of the following options:
+                    • Read response ingress register
+                    • Write response ingress register
+                    • Write response egress register",
+                },
+              },
+              high: {
+                readRequestPath: {
+                  min_asserted_bits: {
+                    (0, 2, 4): 1,
+                  },
+                  reason: "To prevent a zero-cycle feedthrough path on the read request path in a high wire mode AMNI, you must use at least one of the following retiming options:
[hunk excerpt ends; remaining lines omitted]
```
### Commit 2f222a1d3099f6fc092656440d256e2e4931e489
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-01-16T11:37:02-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-3749: Static latency report is not accounting for SERDES
Change-Ids: I52a0537b4de17a68ef780e24b82aae7b3e2febfa.
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -866,7 +866,7 @@
         deprecated: [ "from_tower" ],
         desc: "Number of Q channel pipeline stages. Starting from towernci_r0p0, this is replaced by retimingDepth in
         CCU.
-        
+
         \nDefault: 4."
       },
       pmuGlobalSignalStages: {
```
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -883,7 +883,7 @@
         deprecated: [ "from_tower" ],
         desc: "Number of PMU global signal pipeline stages. Starting from towernci_r0p0, this is replaced by
         retimingDepth in PMU.
-        
+
         \nDefault: 4."
       },
       dlsLogicProtection: {
```
Diff excerpt, `CE/ideas/default_params_nci.yaml`:
```diff
@@ -22349,7 +22349,7 @@
                 desc: "Read response internal retiming register (2).
                 \nIf the internal register (2) option is enabled, a retiming stage is added after the arbiter.
                 \nThis configuration reduces the logic on the address of the read buffer.
-                \nThis option also disables the read Reorder Buffer (ROB) FIFO bypass BYPASS parameter. 
+                \nThis option also disables the read Reorder Buffer (ROB) FIFO bypass BYPASS parameter.
                 \nTherefore, this option breaks up the timing path through the ROB FIFO bypass. \nDefault: 0b0."
               },
               7: {
```
### Current source `CE/ideas/api/interconnect_config.py`
Snapshot: HEAD; SHA-256 `710bbb5891b0eead17f8cbfc02ba7669113a8fc94636fab5d74af50cbedbe5bd`.
Surviving-line author counts (attribution context only): {'lingao01': 6520, 'Lin Gao': 230, 'Chris Laycock': 1, 'Christopher Alvarez': 2611, 'Tanushi Ahuja': 2369, 'Pawan Kakarla': 157, 'Jackson Petroll': 1925, 'Michael Coulter': 57, 'Chris Styles': 189, 'Dustin Divis': 5, 'Kelly Alvarez': 14, 'Kyan Kornfeld': 1}.
Introduction/rename-follow candidates: faefca7bb99f15d5c7ffd21f4544ddbb9b3e4161 2020-06-01T13:41:51-05:00 lingao01 <lingao01@arm.com> add top level api class.
```text
1279:             1. Parameters dict for updating the same parameters set on all cmni devices in the Tile Group:
1280:                 input_dict = {
1281:                     'cmnis': {
1282:                         'parameters': {'adaptor/readRetimingStages': 6},
1283:                         'interfaces': {
1284:                             'CHI5': {'chi/nidWidth': 10}
1285:                         }
1286:                     }
1287:                 }
1288:             2. Update each indexed device parameters in the Tile Group.
1289:                 input_dict = {
1290:                     'cmnis': [
1291:                         {   'parameters': {'adaptor/readRetimingStages': 7},
1292:                             'interfaces': {'CHI5': {'chi/nidWidth': 8}}},
1293:                         {   'parameters': {'adaptor/readRetimingStages': 15},
1294:                             'interfaces': {'CHI5': {'chi/nidWidth': 9}}}
1295:                     ]
1296:                 }
1297:         """
1298:         return self._tilegroups.update_tile_group_members(group_name, input_dict)
1299: 
1300:     def remove_tile_group_member(self, group_name: str) -> bool:
1301:         """
```
```text
1983:         return self._instances.get_instances(instance_type)
1984: 
1985:     def add_instances(self, instance_type: str, instance_names_list: list,
1986:                       wiremode: str = None, clk: str = None) -> list:
1987:         """
1988:         This function adds instances of the same type to the instances list.
1989: 
1990:         Parameters
1991:         ----------
1992:         instance_type : str, required
1993:             Type of instance such as "asnis", "amnis" etc. Use get_instance_attributes() to retrieve valid instance
1994:             types.
1995:         instance_names_list : list, required
1996:             List of instance names to add.
1997:         wiremode : str, optional
1998:             Common wiremode of this instance type for all instances. Use get_instance_attributes(instance_type)
1999:             to retrieve valid wire modes. For instance types that infer wiremode from connections such as NRS,
2000:             this parameter gets updated automatically when connection is made.
2001:         clk : str, optional
```
### Current source `CE/ideas/instance/instances.py`
Snapshot: HEAD; SHA-256 `cf7a6688aaeb2d7c6948a5f541e5de33e3fae34eefe4a1d1e904837e63e3f415`.
Surviving-line author counts (attribution context only): {'lingao01': 5227, 'Lin Gao': 3066, 'Chris Laycock': 1, 'Christopher Alvarez': 1715, 'Tanushi Ahuja': 2743, 'Dustin Divis': 111, 'Kyan Kornfeld': 81, 'Pawan Kakarla': 38, 'Michael Coulter': 71, 'Chris Styles': 24, 'Jackson Petroll': 331}.
Introduction/rename-follow candidates: 162614d4dac8a9eb06a3391f02ff36e267c80d9d 2020-06-12T15:28:46-05:00 lingao01 <lingao01@arm.com> add some instances code, update interface code to make the search faster..
```text
31:     INSTANCE_TYPES_MASTER_NCI, INSTANCE_TYPES_SLAVE_NCI, INSTANCE_TYPES_SLAVE, INSTANCE_TYPES_MASTER, \
32:     INSTANCE_TYPES_HAS_CLOCK, INSTANCE_TYPES_SINGLE_INTERFACE, \
33:     INSTANCES_ROUTE_DATA_HOP, INSTANCES_ROUTE_CHI_SRC, INSTANCES_ROUTE_CHI_HOP, INSTANCES_ROUTE_DVM_HOP, \
34:     CHANNEL_RP_PARAMS, PCDC_ASYNC_ONLY_PARAMS, WIREMODE_VALID_CHANNELS, RX_LINK_PARAMS, TX_LINK_PARAMS, \
35:     CHANNEL_PARAMS_NON_RP, ChannelParams, network_from_wiremode, \
36:     INSTANCE_TYPES_EXTERNAL_CLOCK, CMN700_TO_CMNCYPRUS, CMN_RESERVED_ATTRIBUTES, \
37:     INSTANCES_ROUTE_PULSE_HOP, INSTANCE_TYPES_CLOCK_CROSSING, INSTANCES_ROUTE_CXS_HOP, INSTANCES_ROUTE_DEBUG_HOP, \
38:     INSTANCES_ROUTE_DEBUG_CTRL_SRC, INSTANCES_ROUTE_DEBUG_CTRL_HOP, INSTANCE_TYPES_SIBLING_CLOCK, \
39:     INSTANCE_TYPES_CLOCK_DOMAIN, \
40:     INSTANCE_TYPES_CLOCK_OR_SIBLING_DOMAIN, INSTANCE_TYPES_CLOCK_OR_EXTERNAL_DOMAIN, INSTANCE_TYPES_ALWAYS_CLOCK, \
41:     INSTANCE_TYPES_CLOCK_OR_SIBLING, INSTANCE_TYPES_CLOCK_OR_EXTERNAL, \
42:     INSTANCE_TYPES_SUBSECTION_BRIDGE
43: from .instance import NciInstance, CmnInstance, CalInstance
```
```text
60:                                     MCN_MCI_PROTOCOLS, MCN_CHI_CDI_PROTOCOLS, MCN_CHI_NCDI_PROTOCOLS, ATB_PROTOCOLS,
61:                                     MCN_CFG_PROTOCOLS, DMNI_PROTOCOLS, AMNI_PROTOCOLS)
62: from .parameters import TYPE_COMPONENT_MAPPING, PMNI_FUSA_PARAMS
63: from .serdes import drc_serdes_tidemark_check_upstream, drc_serdes_tidemark_check_downstream
64: from ..api.interconnect_enum import PULSE_NETWORKS
65: from ..cmn.node_id import CmnNodeIdCalculator
66: 
67: logger = logging.getLogger(__name__)
68: 
69: SUBNETWORK_INSTANCES_NCI = ["asnis", "hsnis", "amnis", "hmnis", "pmnis", "cmnis", "cfgnis", "routers", "pcdcs",
70:                             "serdes", "fmus", "pmus", "ccus", "pcus", "half_pcdcs", "aub2apbs", "nrss", "half_cdbs"]
71: SUBNETWORK_INSTANCES_MCN = ["mcns"]
72: 
73: _DUPLINK_CHANNEL_BASES = {
74:     "high": {"readRequest", "writeRequest", "readResponse", "writeResponse"},
75:     "low": {"readWriteRequest", "readWriteResponse"},
76: }
77: 
78: PCIE_GEN_6_HAS_CPL = True
```
```text
217:         """ Return the boundary_manager object. """
218:         return self._boundary_manager
219: 
220:     def _create_instance(self, inst_name, instance_type, wiremode=None):
221:         """ Create an instance """
222:         if "cmn" in self._state_manager.get_ip_version():
223:             if instance_type in self.get_cmn_instance_types("ALL"):
224:                 # handle CMN instance types, dummy for now
225:                 if instance_type == "cals":
226:                     return CalInstance(self._state_manager, self, inst_name, instance_type)
227:                 if instance_type == "mxps":
228:                     # Need to check if MXP instance of inst_name already exists, and return it
```
### Current source `CE/ideas/report_impl/static_latency.py`
Snapshot: HEAD; SHA-256 `9e020aa596bd889f5ae34b16b0a27d4ed0caa869af403c63f9c4ae8c7bc5460d`.
Surviving-line author counts (attribution context only): {'Tanushi Ahuja': 593, 'Lin Gao': 14, 'Kyan Kornfeld': 14, 'Michael Coulter': 12}.
Introduction/rename-follow candidates: be7ea2b9c53a8969ebbd7aa3b9e9e67c10468b0b 2024-11-04T01:02:20-06:00 Tanushi Ahuja <tanushi.ahuja@arm.com> 1. BRUNEL-2331 - ReportStaticLatency: Converge Report Retimign Params into this report 2. BRUNEL-2616 - ReportofReports: Refactor the current report to flow API 3. added report_static_latency methods to report_impl/static_latency.py 3. Updated images in report_impl/report_html/assets - tower_retiming_diagrams from tech comms 4. Updated ip_to_reports in interconnect_report 5. Pylint fixes.
```text
103:             latency_list.append({
104:                 'name': src_intf,
105:                 'type': src_type,
106:                 'wiremode': ic.get_instance_wiremode(src_inst),
107:                 'clock': src_clock,
108:                 'reason': 'SRC has larger DataWidth than DST',
109:                 'min_cycles': '-',
110:                 'cycles': 1
111:             })
112: 
113:     # iyml has additional hops to interfaces to take care of
114:     yaml_ver2 = float(ic.get_iyml_version()) >= 2.0
```
```text
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
```

## diff

### Commit 30b70cb283e509fed0d584ba8c206a31f46c9b1b
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-10-13T10:37:32-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-3314: Present diffs on logical canvas
Change-Ids: Ia9889878b163445d7f88e77161eea7306fad90aa.
Diff excerpt, `GUI/src/app/canvas/canvas-diff/canvas-diff-pane.component.ts`:
```diff
@@ -0,0 +1,187 @@
+/***************************************************************************
+* The confidential and proprietary information contained in this file may
+* only be used by a person authorised under and to the extent permitted
+* by a subsisting licensing agreement from Arm Limited or its affiliates.
+*
+* (C) COPYRIGHT 2025 Arm Limited or its affiliates.
+* ALL RIGHTS RESERVED
+*
+* This entire notice must be reproduced on all copies of this file
+* and copies of this file may only be made by a person if such person is
+* permitted to do so under the terms of a subsisting license agreement
+* from Arm Limited or its affiliates.
+*
+* Release Information : $State$
+*
+***************************************************************************/
+
+import { Component, ElementRef, HostListener, Input, OnChanges, OnDestroy, SimpleChanges, ViewChild } from '@angular/core';
+import { CanvasDiffViewPayload } from './models/canvas-diff.models';
+import { CanvasLogicalService } from '../canvas-logical.service';
+import { CanvasGuiDataService } from '../shared/services/canvas-gui-data.service';
+import { CanvasInstancesService } from '../shared/services/canvas-instances.service';
+import { CanvasInterfacesService } from '../shared/services/canvas-interfaces.service';
+import { CanvasConnectionsRoutesService } from '../shared/services/canvas-connections-routes.service';
+import { CanvasBlockagesService } from '../shared/services/canvas-blockages.service';
+import { CanvasConfigDataService } from '../shared/services/canvas-config-data.service';
+import { CanvasSpinnerService } from '../shared/services/canvas-spinner.service';
+import { CanvasSelectorsService } from '../shared/services/canvas-selectors.service';
+import { CanvasLogicalGrpsService } from '../shared/services/canvas-logical-grps.service';
+import { SpinnerService } from '../shared/services/spinner.service';
+import cloneDeep from 'lodash/cloneDeep';
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/canvas-diff/canvas-diff.component.ts`:
```diff
@@ -0,0 +1,387 @@
+/***************************************************************************
+* The confidential and proprietary information contained in this file may
+* only be used by a person authorised under and to the extent permitted
+* by a subsisting licensing agreement from Arm Limited or its affiliates.
+*
+* (C) COPYRIGHT 2025 Arm Limited or its affiliates.
+* ALL RIGHTS RESERVED
+*
+* This entire notice must be reproduced on all copies of this file
+* and copies of this file may only be made by a person if such person is
+* permitted to do so under the terms of a subsisting license agreement
+* from Arm Limited or its affiliates.
+*
+* Release Information : $State$
+*
+***************************************************************************/
+
+import { Component, HostListener, OnDestroy, OnInit } from '@angular/core';
+import { Subscription } from 'rxjs';
+import { Router } from '@angular/router';
+import { CanvasDiffService } from './canvas-diff.service';
+import { CanvasDiffPayload } from './models/canvas-diff.models';
+import { NetworkType } from 'src/app/shared/models/connections.model';
+
+type CanvasDiffLayout = 'side-by-side' | 'stacked';
+
+@Component({
+  selector: 'app-canvas-diff',
+  templateUrl: './canvas-diff.component.html',
+  styleUrls: ['./canvas-diff.component.css']
+})
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/canvas-diff/models/canvas-diff.models.ts`:
```diff
@@ -0,0 +1,66 @@
+/***************************************************************************
+* The confidential and proprietary information contained in this file may
+* only be used by a person authorised under and to the extent permitted
+* by a subsisting licensing agreement from Arm Limited or its affiliates.
+*
+* (C) COPYRIGHT 2025 Arm Limited or its affiliates.
+* ALL RIGHTS RESERVED
+*
+* This entire notice must be reproduced on all copies of this file
+* and copies of this file may only be made by a person if such person is
+* permitted to do so under the terms of a subsisting license agreement
+* from Arm Limited or its affiliates.
+*
+* Release Information : $State$
+*
+***************************************************************************/
+
+import { InstanceAttributes } from 'src/app/canvas/shared/models/instance-attributes.model';
+
+export interface CanvasDiffViewPayload {
+  ip_version: string;
+  instance_attributes: InstanceAttributes | null;
+  instances_gui: Record<string, any>;
+  interfaces_gui: Record<string, any>;
+  route_attributes: Record<string, any>;
+  connections: Record<string, any>;
+  connections_per_instance: Record<string, any>;
+  routes: Record<string, any>;
+  pulse_routes: Record<string, any>;
+  remote_routes: Record<string, any>;
+}
[hunk excerpt ends; remaining lines omitted]
```
### Commit 76bb561f94f32624d9494b4d95c3f040807144bb
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-01-08T12:01:10-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-539: Add configuration Diff report
Change-Ids: Iff9725bb8261bb00675da7286e957bf4f4caba67.
Diff excerpt, `resources/scripts/canvas/canvas_diff.py`:
```diff
@@ -1,510 +0,0 @@
-#!/usr/bin/env python3
-# ----------------------------------------------------------------------------
-# The confidential and proprietary information contained in this file may
-# only be used by a person authorised under and to the extent permitted
-# by a subsisting licensing agreement from Arm Limited or its affiliates.
-#
-# (C) COPYRIGHT 2025 Arm Limited or its affiliates.
-# ALL RIGHTS RESERVED
-#
-# This entire notice must be reproduced on all copies of this file
-# and copies of this file may only be made by a person if such person is
-# permitted to do so under the terms of a subsisting license agreement
-# from Arm Limited or its affiliates.
-#
-# Release Information : $State$
-#
-# ----------------------------------------------------------------------------
-
-"""Generate a structured diff between two NCI iYML configurations.
-
-The script bootstraps two temporary NCI sessions, captures the logical-canvas
-view model for each, and emits a JSON payload with both raw data and
-per-entity diff annotations that the GUI can render.
-"""
-
-from __future__ import annotations
-
-import argparse
-import json
-import logging
-import os
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `resources/scripts/iyml_diff.py`:
```diff
@@ -0,0 +1,825 @@
+#!/usr/bin/env python3
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2025 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : $State$
+#
+# ----------------------------------------------------------------------------
+
+"""Generate a structured diff between two NCI iYML configurations.
+
+The script bootstraps two temporary NCI sessions, captures the logical-canvas
+view model for each, and emits a JSON payload with both raw data and
+per-entity diff annotations that the GUI can render.
+
+Usage:
+    python resources/scripts/iyml_diff.py CURRENT.iyml COMPARISON.iyml [--pretty] [--diff-only] [--report-dir DIR] [--html-report PATH]
+
+- Stdout: JSON payload (full payload by default; `--diff-only` emits just the diff blob with both view and raw YAML diffs). Use `--pretty` for formatted output.
+- Local log: appends pretty diff JSON to `resources/scripts/iyml_diff_py.log`.
+- Reports: with `--report-dir`, also writes `DIR/iyml_diff.log` (pretty diff) and `DIR/iyml_diff_report.html` (sectioned side-by-side YAML diff). `--html-report` overrides the HTML path.
+"""
[hunk excerpt ends; remaining lines omitted]
```
### Commit c23851428ffcbc041fee920acca72dc4e7ce24ca
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-17T11:19:59-05:00; reachable from selected HEAD: True.
Subject: Highlight exact YAML diff changes
Change-Ids: I4ac69adf5a95a7b7ce3f0b9ac46191c793c8c3f5.
Diff excerpt, `CE/pytests/report/test_iyml_diff.py`:
```diff
@@ -0,0 +1,194 @@
+# ----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2026 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : $State$
+#
+# ----------------------------------------------------------------------------
+
+import importlib.util
+import sys
+from pathlib import Path
+
+import pytest
+
+
+REPO_ROOT = Path(__file__).resolve().parents[3]
+SCRIPT_PATH = REPO_ROOT / "resources" / "scripts" / "iyml_diff.py"
+MODULE_SPEC = importlib.util.spec_from_file_location("iyml_diff_under_test", SCRIPT_PATH)
+if MODULE_SPEC is None or MODULE_SPEC.loader is None:
+    raise RuntimeError(f"Unable to load {SCRIPT_PATH}")
+iyml_diff = importlib.util.module_from_spec(MODULE_SPEC)
+sys.modules[MODULE_SPEC.name] = iyml_diff
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `resources/scripts/iyml_diff.py`:
```diff
@@ -33,6 +33,7 @@ Usage:
 from __future__ import annotations
 
 import argparse
+from difflib import SequenceMatcher
 import importlib.util
 import json
 import logging
```
Diff excerpt, `resources/scripts/iyml_diff.py`:
```diff
@@ -855,6 +856,142 @@ def serialize_yaml_value(value: Any) -> str:
         return str(value)
 
 
+def is_structural_line(line: str) -> bool:
+    """Return whether a serialized line contains only JSON delimiters."""
+    stripped = line.strip()
+    return bool(stripped) and all(char in "{}[]," for char in stripped)
+
+
+def render_changed_line(
+    comparison_line: str,
+    current_line: str,
+) -> Tuple[str, str]:
+    """Escape two changed lines and highlight only their differing text."""
+    if is_structural_line(comparison_line) or is_structural_line(current_line):
+        return escape(comparison_line), escape(current_line)
+
+    prefix_len = 0
+    max_prefix_len = min(len(comparison_line), len(current_line))
+    while (
+        prefix_len < max_prefix_len
+        and comparison_line[prefix_len] == current_line[prefix_len]
+    ):
+        prefix_len += 1
+
+    suffix_len = 0
+    max_suffix_len = min(
+        len(comparison_line) - prefix_len,
+        len(current_line) - prefix_len,
+    )
+    while (
[hunk excerpt ends; remaining lines omitted]
```
### Current source `resources/scripts/iyml_diff.py`
Snapshot: HEAD; SHA-256 `6f7969bb6e40190e9d66566e43b25c74acc4332afa1cf69b3511a6255b2ca5e7`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1210}.
Introduction/rename-follow candidates: 30b70cb283e509fed0d584ba8c206a31f46c9b1b 2025-10-13T10:37:32-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-3314: Present diffs on logical canvas.
```text
25: Usage:
26:     python resources/scripts/iyml_diff.py CURRENT.iyml COMPARISON.iyml [--pretty] [--diff-only] [--report-dir DIR] [--html-report PATH]
27: 
28: - Stdout: JSON payload (full payload by default; `--diff-only` emits just the diff blob with both view and raw YAML diffs). Use `--pretty` for formatted output.
29: - Local log: appends pretty diff JSON to `resources/scripts/iyml_diff_py.log`.
30: - Reports: with `--report-dir`, also writes `DIR/iyml_diff.log` (pretty diff) and `DIR/iyml_diff_report.html` (sectioned side-by-side YAML diff). `--html-report` overrides the HTML path.
31: """
32: 
33: from __future__ import annotations
34: 
35: import argparse
36: from difflib import SequenceMatcher
37: import importlib.util
38: import json
39: import logging
40: import os
41: import shutil
42: import sys
43: import tempfile
44: from dataclasses import dataclass
```
```text
58: HTML_HELPER_METHODS = (
59:     "write_header",
60:     "open_body",
61:     "close_body",
62:     "html_end",
63:     "paragraph",
64:     "headings",
65:     "table_headers",
66:     "table_data",
67:     "table_footer",
68:     "raw",
69: )
```
```text
97:         r_val = right[key]
98:         if l_val == r_val:
99:             continue
100:         if isinstance(l_val, Mapping) and isinstance(r_val, Mapping):
101:             nested_base, nested_compare = deep_diff_mappings(l_val, r_val)
102:             if nested_base or nested_compare:
103:                 base_diff[key] = nested_base
104:                 compare_diff[key] = nested_compare
105:         elif isinstance(l_val, (list, tuple)) and isinstance(r_val, (list, tuple)):
106:             nested_base, nested_compare = deep_diff_sequences(l_val, r_val)
107:             if nested_base or nested_compare:
108:                 base_diff[key] = nested_base
```
### Current source `GUI/src/app/canvas/core/services/canvas-diff-overlay.service.ts`
Snapshot: HEAD; SHA-256 `3d41809c8479fdd72d9fd1d73440ffdfc40f9bd808973d11ac67391807c00960`.
Surviving-line author counts (attribution context only): {'Dustin Divis': 497, 'Michael Coulter': 170}.
Introduction/rename-follow candidates: 415f01e20091c4e0a4345ce75c317a3880403c4c 2026-02-25T12:41:10-06:00 Dustin Divis <dustin.divis@arm.com> refactor(canvas): centralize logical layout + thin renderers.
```text
70:     pointerOffset: number;
71:     hideDelayMs: number;
72:     container: Record<string, string>;
73:     closeHeader: Record<string, string>;
74:     line: Record<string, string>;
75:     lineBackgrounds: Record<string, string>;
76:   };
77: }
78: 
79: @Injectable()
80: export class CanvasDiffOverlayService {
81:   private app: Application | null = null;
```
```text
178:     overlay.eventMode = 'none';
179:     overlay.cursor = 'default';
180:     overlay.zIndex = zIndex;
181:     const detailText = this.canvasLogicalDataService.getDiffInstanceDetail(diffKey)
182:       || this.buildDiffFallbackTooltip(nodeName, diffStatus);
183:     this.bindDiffTooltipToBase(baseGraphics, detailText, hideRegularTooltip);
184:     overlayContainer.addChild(overlay);
185:   }
186: 
187:   addConnectionOverlay(args: DiffOverlayConnectionArgs): void {
188:     const {
189:       overlayContainer,
```
```text
232:     overlay.interactiveChildren = false;
233:     overlay.cursor = 'default';
234:     overlay.zIndex = config.connection.zIndex;
235:     const detailText = this.canvasLogicalDataService.getDiffInstanceDetail(diffKey)
236:       || this.buildConnectionDiffTooltip(network, connection, diffStatus);
237:     this.bindDiffTooltipToBase(baseGraphics, detailText, hideRegularTooltip);
238: 
239:     overlayContainer.addChild(overlay);
240:   }
241: 
242:   private bindDiffTooltipToBase(
243:     baseGraphics: Container | Graphics | null | undefined,
```
```text
319:       tooltipEl.innerHTML = '';
320:       const fragment = document.createDocumentFragment();
321:       const lines = detail.split('\n');
322:       if (!tooltipEl.querySelector('#diff-popup-close-button')) {
323:         const closeContainer = document.createElement('div');
324:         closeContainer.className = 'canvas-diff-tooltip__close-header';
325:         this.applyStyleMap(closeContainer.style, config.tooltip.closeHeader);
326: 
327:         const closeIcon = document.createElement('span');
328:         closeIcon.id = 'diff-popup-close-button';
329:         closeIcon.className = 'mat-icon material-icons notranslate close-modal-icon';
330:         closeIcon.textContent = 'close';
331:         closeIcon.setAttribute('role', 'button');
```
### Current source `CE/pytests/report/test_iyml_diff.py`
Snapshot: HEAD; SHA-256 `dda2909a7c63e7b3629afb4c969bf8a0c9d46bc84a0d5335626cf689964ddae4`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 194}.
Introduction/rename-follow candidates: c23851428ffcbc041fee920acca72dc4e7ce24ca 2026-07-17T11:19:59-05:00 Michael Coulter <michael.coulter@arm.com> Highlight exact YAML diff changes.
```text
48:         self.output.append(f"<h{level}>{value}</h{level}>")
49: 
50: 
51: def test_render_yaml_text_diff_highlights_only_changed_numeric_values():
52:     comparison_html, current_html = iyml_diff.render_yaml_text_diff(
53:         '        "axi/dataWidth": 128',
54:         '        "axi/dataWidth": 256',
55:     )
56: 
57:     assert comparison_html == (
58:         "        &quot;axi/dataWidth&quot;: "
59:         '<span class="yaml-char-diff-compare">128</span>'
60:     )
61:     assert current_html == (
62:         "        &quot;axi/dataWidth&quot;: "
63:         '<span class="yaml-char-diff-current">256</span>'
64:     )
65: 
66: 
67: def test_render_yaml_text_diff_highlights_inserted_route_segment():
68:     comparison_html, current_html = iyml_diff.render_yaml_text_diff(
69:         '"amni_0": "ccg_0_dsni_0->u_r1_2155_lid21->amni_amni_0"',
70:         '"amni_0": "ccg_0_dsni_0->u_r1_2155_lid21->nrss_0->amni_amni_0"',
71:     )
72: 
73:     assert "yaml-char-diff" not in comparison_html
74:     assert (
75:         '<span class="yaml-char-diff-current">nrss_0-&gt;</span>'
```

## testing

### Commit 4985c20cf3c226569c19d4f980bb883864a15512
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-04-29T16:32:59-05:00; reachable from selected HEAD: True.
Subject: Add interfaces e2e test
Change-Ids: I015263bac0fa5ca5f47b6c7276a1a6634be4ba07.
Diff excerpt, `brunel/test/e2e_check_interface_parameters.py`:
```diff
@@ -0,0 +1,267 @@
+#----------------------------------------------------------------------------
+# The confidential and proprietary information contained in this file may
+# only be used by a person authorised under and to the extent permitted
+# by a subsisting licensing agreement from Arm Limited or its affiliates.
+#
+# (C) COPYRIGHT 2020-2021 Arm Limited or its affiliates.
+# ALL RIGHTS RESERVED
+#
+# This entire notice must be reproduced on all copies of this file
+# and copies of this file may only be made by a person if such person is
+# permitted to do so under the terms of a subsisting license agreement
+# from Arm Limited or its affiliates.
+#
+# Release Information : $State$
+#
+#----------------------------------------------------------------------------
+from ideas.api.nci import Nci
+from pathlib import Path
+import os
+import datetime
+import subprocess
+import time
+from js_library import js_library
+
+# ============================================================
+# Dummy nci, only use for fetching params
+# ============================================================
+example_dir     = str(Path(__file__).parent)
+if (example_dir[0] != "/"):
+    example_dir = "./" + example_dir
+example_dir_out = example_dir + "/interfaces"
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `brunel/test/e2e_check_parameters.py`:
```diff
@@ -1,267 +0,0 @@
-#----------------------------------------------------------------------------
-# The confidential and proprietary information contained in this file may
-# only be used by a person authorised under and to the extent permitted
-# by a subsisting licensing agreement from Arm Limited or its affiliates.
-#
-# (C) COPYRIGHT 2020-2021 Arm Limited or its affiliates.
-# ALL RIGHTS RESERVED
-#
-# This entire notice must be reproduced on all copies of this file
-# and copies of this file may only be made by a person if such person is
-# permitted to do so under the terms of a subsisting license agreement
-# from Arm Limited or its affiliates.
-#
-# Release Information : $State$
-#
-#----------------------------------------------------------------------------
-from ideas.api.nci import Nci
-from pathlib import Path
-import os
-import datetime
-import subprocess
-import time
-from js_library import js_library
-
-# ============================================================
-# Dummy nci, only use for fetching params
-# ============================================================
-example_dir     = str(Path(__file__).parent)
-if (example_dir[0] != "/"):
-    example_dir = "./" + example_dir
-example_dir_out = example_dir + "/interfaces"
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `brunel/test/e2e_interfaces.py`:
```diff
@@ -175,200 +186,209 @@ for direction,protocol_list in dirprot.items():
                     else:
 
 
-                      # this option has not been chosen
-                      print ("\n          Option: " + str(param_option))
-                      print ("          ### Running test " + str(test_name))
+                        # this option has not been chosen
+                        print ("\n          Option: " + str(param_option))
+                        print ("          ### Running test " + str(test_name))
 
-                      ## =====================================================
-                      #  Set up paths and timeouts for the testing
-                      ## =====================================================
-                      test_dir_out = example_dir_out + "/" + test_name + "/"
+                        ## =====================================================
+                        #  Set up paths and timeouts for the testing
+                        ## =====================================================
+                        test_dir_out = example_dir_out + "/" + test_name + "/"
 
-                      gui_file    = test_dir_out + test_name + ".yaml"
-                      ce_file     = test_dir_out + "ce_" + test_name + ".yaml"
-                      js_file     = test_dir_out + test_name + ".js"
-                      log_file    = test_dir_out + "logfile.txt"
-                      run_file    = test_dir_out + "run.py"
-                      timeout     = 15
+                        gui_file    = test_dir_out + test_name + ".yaml"
+                        ce_file     = test_dir_out + "ce_" + test_name + ".yaml"
+                        js_file     = test_dir_out + test_name + ".js"
+                        log_file    = test_dir_out + "logfile.txt"
+                        run_file    = test_dir_out + "run.py"
+                        timeout     = 15
[hunk excerpt ends; remaining lines omitted]
```
### Commit ca950bd508ee634fd6270dd96573b88733b7ca84
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-05-05T19:53:51-05:00; reachable from selected HEAD: True.
Subject: Run e2e tests with xvfb
Change-Ids: Icfe4a8617a938d621faeaed137c548de7f01a991.
### Commit 499876145fceb3ced61d0c11d179808094dfb9f5
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-09-04T21:19:13-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-3411: Set up a simple GUI end2end test and make it a gate for check-in
Change-Ids: Iffb5fbeb20b505c2e8eb21e765ebb944412c9817.
Diff excerpt, `CE/pytests/gui/globalparameters/js/globalparameters.spec.js`:
```diff
@@ -0,0 +1,86 @@
+// to run from ideas dir: `npx playwright test ./electron.spec.js --workers=1`
+
+const path = require('path');
+const { test, expect } = require('@playwright/test');
+const { _electron: electron } = require('playwright');
+
+const REPO_ROOT = path.resolve(__dirname, '../../../../../'); // -> ideas/
+const BRUNEL_DIR = path.join(REPO_ROOT, 'brunel');
+const ELECTRON_BIN = path.join(BRUNEL_DIR, 'node_modules', '.bin', 'electron');
+
+// Keep CLI args aligned with your Python setup
+let APP_ARGS = [
+  'confirmAppClose=false',
+  'turnOffConsole=true',
+];
+
+// Toggle headless via env: GUI_TEST_HEADLESS=0 -> headed (show GUI)
+const HEADLESS = process.env.GUI_TEST_HEADLESS !== '0';
+if (HEADLESS) {
+  APP_ARGS.push('gui-test-headless');
+}
+
+test('Electron boots and shows "Project" tab', async () => {
+  // Launch Electron.
+  const electronApp = await electron.launch({
+    executablePath: ELECTRON_BIN,     // use your project’s Electron
+    // Run headless by forwarding Chromium flags to Electron.
+    // Ensures Chromium runs headless; --disable-gpu avoids GPU init in CI.
+    // args: [BRUNEL_DIR, ...APP_ARGS, '--headless=new', '--disable-gpu'],
+    args: [BRUNEL_DIR, ...APP_ARGS],  // pass app folder and 'gui-test-headless' flags
+    cwd: BRUNEL_DIR,
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/pytests/gui/globalparameters/js/globalparameters.template.spec.js`:
```diff
@@ -0,0 +1,74 @@
+// to run from ideas dir: `npx playwright test ./CE/pytests/gui/globalparameters/js --workers=2`
+
+const path = require('path');
+const { test, expect } = require('@playwright/test');
+const { _electron: electron } = require('playwright');
+
+const REPO_ROOT = path.resolve(__dirname, '../../../../../'); // -> ideas/
+const BRUNEL_DIR = path.join(REPO_ROOT, 'brunel');
+const ELECTRON_BIN = path.join(BRUNEL_DIR, 'node_modules', '.bin', 'electron');
+
+let APP_ARGS = [
+  'confirmAppClose=false',
+  'turnOffConsole=true',
+];
+
+// Toggle headless via env: GUI_TEST_HEADLESS=0 -> headed (show GUI)
+const HEADLESS = process.env.GUI_TEST_HEADLESS !== '0';
+if (HEADLESS) {
+  APP_ARGS.push('gui-test-headless');
+}
+
+// Slightly generous timeout for parallel runs
+test.setTimeout(180_000);
+
+test('Electron shows "Clone New Project From Template" legend', async () => {
+  const electronApp = await electron.launch({
+    executablePath: ELECTRON_BIN,
+    args: [BRUNEL_DIR, ...APP_ARGS],
+    cwd: BRUNEL_DIR,
+    env: {
+      ...process.env,
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/pytests/gui/globalparameters/test_gui_global_parameters.py`:
```diff
@@ -0,0 +1,52 @@
+import os
+import pathlib
+import subprocess
+import pytest
+import shutil
+from ideas import Interconnect
+from tooling.general.decorators import ip
+
+
+@pytest.mark.pytest_tags(["gui"])
+# @ip('product_idx', 'tower_r1p1_sitwain') # will loop through: tower_r1p1_sitwain: [ "towernci_r1p2", "towernci_r1p3", "tower_r1p1", "tower_r1p2", "sitwain_r0p0" ]
+@ip('product_idx', 'nitwain_only') # will loop through: nitwain_only: [ "nitwain_r0p0" ]
+def test_gui_global_parameters(request, output_dir, ip_version):
+    # set headless mode
+    GUI_TEST_HEADLESS = "1" # "0" or "1"
+    """
+    Runs the existing Playwright JS test (electron.spec.js) from pytest,
+    so GUI E2E can execute alongside CE backend tests.
+    """
+    repo_root = pathlib.Path(__file__).resolve().parents[4]  # -> ideas/
+    if shutil.which("npx") is None:
+        pytest.skip("npx not found on PATH")
+
+    env = os.environ.copy()
+    # Default to headless unless GUI_TEST_HEADLESS=0 is explicitly set.
+    env.setdefault("GUI_TEST_HEADLESS", GUI_TEST_HEADLESS)
+    # Run the exact command from the repo root (ideas/)
+    cmd = [
+        "npx",
+        "playwright",
+        "test",
[hunk excerpt ends; remaining lines omitted]
```
### Commit 75eb348e988e2139a8c3057937bf54dfc23cd885
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-09-05T20:17:04-05:00; reachable from selected HEAD: True.
Subject: extract gui test boilerplate code into electronTestUtil.js, created playwright-reporter.js for custom test reporting/logging
Change-Ids: I37560e2492b758dbebb3850c365f9dd9725ff5e6.
Diff excerpt, `CE/pytests/gui/electronTestUtil.js`:
```diff
@@ -0,0 +1,111 @@
+'use strict';
+const path = require('path');
+const { _electron: electron } = require('playwright');
+
+// Resolve repo + app paths from this util's location: ideas/CE/pytests/gui
+const REPO_ROOT = path.resolve(__dirname, '../../..'); // -> ideas/
+const BRUNEL_DIR = path.join(REPO_ROOT, 'brunel');
+
+// Prefer native Electron binary on Linux/Windows; fall back to .bin shim (macOS or missing)
+function resolveElectronPath() {
+  const binShim = path.join(BRUNEL_DIR, 'node_modules', '.bin', 'electron');
+  let native;
+  if (process.platform === 'darwin') {
+    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'Electron.app', 'Contents', 'MacOS', 'Electron');
+  } else if (process.platform === 'win32') {
+    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'electron.exe');
+  } else {
+    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'electron');
+  }
+  try {
+    const fs = require('fs');
+    if (fs.existsSync(native)) return native;
+  } catch (_) {}
+  return binShim;
+}
+const ELECTRON_BIN = resolveElectronPath();
+
+const BASE_ARGS = ['confirmAppClose=false', 'turnOffConsole=false'];
+const HEADLESS = process.env.GUI_TEST_HEADLESS !== '0';
+const APP_ARGS = HEADLESS ? [...BASE_ARGS, 'gui-test-headless'] : BASE_ARGS;
+
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/pytests/gui/globalparameters/js/globalparameters.spec.js`:
```diff
@@ -1,122 +1,13 @@
-// to run from ideas dir: `npx playwright test ./electron.spec.js --workers=1`
-
-const path = require('path');
 const { test, expect } = require('@playwright/test');
-const { _electron: electron } = require('playwright');
-
-const REPO_ROOT = path.resolve(__dirname, '../../../../../'); // -> ideas/
-const BRUNEL_DIR = path.join(REPO_ROOT, 'brunel');
-// Prefer the native binary on Linux/Windows; use the .bin shim on macOS (and as fallback).
-function resolveElectronPath() {
-  const binShim = path.join(BRUNEL_DIR, 'node_modules', '.bin', 'electron');
-  let native;
-  if (process.platform === 'darwin') {
-    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'Electron.app', 'Contents', 'MacOS', 'Electron');
-  } else if (process.platform === 'win32') {
-    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'electron.exe');
-  } else {
-    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'electron');
-  }
-  try {
-    const fs = require('fs');
-    if (fs.existsSync(native)) return native;
-  } catch (_) {}
-  return binShim;
-}
-const ELECTRON_BIN = resolveElectronPath();
-
-// Keep CLI args aligned with your Python setup
-let APP_ARGS = [
-  'confirmAppClose=false',
-  'turnOffConsole=false',
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `CE/pytests/gui/globalparameters/js/globalparameters.template.spec.js`:
```diff
@@ -1,112 +1,13 @@
-// to run from ideas dir: `npx playwright test ./CE/pytests/gui/globalparameters/js --workers=2`
-
-const path = require('path');
 const { test, expect } = require('@playwright/test');
-const { _electron: electron } = require('playwright');
-
-const REPO_ROOT = path.resolve(__dirname, '../../../../../'); // -> ideas/
-const BRUNEL_DIR = path.join(REPO_ROOT, 'brunel');
-function resolveElectronPath() {
-  const binShim = path.join(BRUNEL_DIR, 'node_modules', '.bin', 'electron');
-  let native;
-  if (process.platform === 'darwin') {
-    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'Electron.app', 'Contents', 'MacOS', 'Electron');
-  } else if (process.platform === 'win32') {
-    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'electron.exe');
-  } else {
-    native = path.join(BRUNEL_DIR, 'node_modules', 'electron', 'dist', 'electron');
-  }
-  try {
-    const fs = require('fs');
-    if (fs.existsSync(native)) return native;
-  } catch (_) {}
-  return binShim;
-}
-const ELECTRON_BIN = resolveElectronPath();
-
-let APP_ARGS = [
-  'confirmAppClose=false',
-  'turnOffConsole=false',
-];
-
[hunk excerpt ends; remaining lines omitted]
```
### Commit e53836bfd7e883a4f43df292a25fc69b777b5262
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-01-30T10:49:08-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-3847: Migrate CMN e2e user defined group tests to playwright
Change-Ids: I040bd7f8ed1bf74ec99c33ab49205d8ace8d18fe.
Diff excerpt, `GUI/package.json`:
```diff
@@ -22,6 +22,7 @@
     "lint:tests:check": "eslint 'tests/**/*.{ts,tsx}'",
     "lint:tests": "eslint 'tests/**/*.{ts,tsx}' --fix",
     "test:playwright": "npx playwright test --config=./tests/playwright.config.ts",
+    "test:playwright:cmn": "PLAYWRIGHT_PROJECTS=$(node ./tests/scripts/list-cmn-projects.js) npx playwright test --config=./tests/playwright.config.ts --grep \"CMN example project loads\"",
     "playwright:report": "npx playwright show-report tests/test-output/playwright-report",
     "perf:summary": "node tests/scripts/perf-summary.js"
   },
```
Diff excerpt, `GUI/tests/fixtures/index.ts`:
```diff
@@ -57,7 +57,14 @@ interface WorkerFixtures {
 export const test = electronTest.extend<TestFixtures, WorkerFixtures>({
   projectSkipGuard: [
     async ({}, use, testInfo) => {
-      const { ipKey } = resolveConfig(testInfo);
+      let { ipKey } = resolveConfig(testInfo);
+      if (!ipKey || ipKey === 'nitwain') {
+        const projectName = testInfo.project?.name ?? '';
+        const baseFromProject = projectName.split('-')[0];
+        if (baseFromProject) {
+          ipKey = baseFromProject;
+        }
+      }
       const skipRule = resolveSkipRule(ipKey, testInfo);
       if (skipRule) {
         testInfo.skip(true, skipRule.reason);
```
Diff excerpt, `GUI/tests/modules/ui/interconnect-architect.ts`:
```diff
@@ -75,6 +79,8 @@ export class InterconnectArchitect {
 
     this.page = page;
     this.options = options;
+    this.navigationBar = new NavigationBar(page);
+    this.meshLabel = this.page.locator('#mesh-x-dimension-label');
 
     this.project = new ProjectPage(page);
     // View Menu
```
### Commit fff32ba2a4b6f0f5a1018df771e2ba0a6ef19439
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-06-22T23:37:36-05:00; reachable from selected HEAD: True.
Subject: Expand GUI unit test coverage and Karma harness
Change-Ids: Iec7d8cf0502450b8e968c51b0f0a94abd6ca4589.
Diff excerpt, `GUI/package-lock.json`:
```diff
@@ -45,8 +45,9 @@
         "karma": "^6.4.4",
         "karma-chrome-launcher": "^3.2.0",
         "karma-coverage": "^2.2.1",
+        "karma-coverage-istanbul-reporter": "^3.0.3",
         "karma-jasmine": "^5.1.0",
-        "karma-jasmine-html-reporter": "^2.1.0",
+        "karma-jasmine-html-reporter": "^2.2.0",
         "karma-junit-reporter": "^2.0.1",
         "nyc": "^18.0.0",
         "playwright": "1.48.1",
```
Diff excerpt, `GUI/package-lock.json`:
```diff
@@ -13009,6 +13010,139 @@
         "node": ">=10.0.0"
       }
     },
+    "node_modules/karma-coverage-istanbul-reporter": {
+      "version": "3.0.3",
+      "resolved": "https://artifactory.arm.com:443/artifactory/api/npm/mirrors.npmjs_org/karma-coverage-istanbul-reporter/-/karma-coverage-istanbul-reporter-3.0.3.tgz",
+      "integrity": "sha512-wE4VFhG/QZv2Y4CdAYWDbMmcAHeS926ZIji4z+FkB2aF/EposRb6DP6G5ncT/wXhqUfAb/d7kZrNKPonbvsATw==",
+      "dev": true,
+      "license": "MIT",
+      "dependencies": {
+        "istanbul-lib-coverage": "^3.0.0",
+        "istanbul-lib-report": "^3.0.0",
+        "istanbul-lib-source-maps": "^3.0.6",
+        "istanbul-reports": "^3.0.2",
+        "minimatch": "^3.0.4"
+      },
+      "funding": {
+        "url": "https://github.com/sponsors/mattlewis92"
+      }
+    },
+    "node_modules/karma-coverage-istanbul-reporter/node_modules/balanced-match": {
+      "version": "1.0.2",
+      "resolved": "https://artifactory.arm.com:443/artifactory/api/npm/mirrors.npmjs_org/balanced-match/-/balanced-match-1.0.2.tgz",
+      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
+      "dev": true,
+      "license": "MIT"
+    },
+    "node_modules/karma-coverage-istanbul-reporter/node_modules/brace-expansion": {
+      "version": "1.1.15",
+      "resolved": "https://artifactory.arm.com:443/artifactory/api/npm/mirrors.npmjs_org/brace-expansion/-/brace-expansion-1.1.15.tgz",
+      "integrity": "sha512-EwOCDEex4quD37XhqM3omwtMoJjr//isUZz1JopUNWms+4Z2ViyM/k1YIRePpoVNnQhENnxtFjLaxNHrT7xIUg==",
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/package.json`:
```diff
@@ -39,8 +39,10 @@
     "coverage:open": "open tests/test-output/coverage/index.html",
     "pretest": "npm run prepare:styles",
     "test": "ng test",
-    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts",
-    "test:spec:shell-synthesis": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.shell-synthesis.json --include=src/app/project --include=src/app/menu-bar/menu-bar.component.spec.ts --include=src/app/shared/services/nav-bar.utils.spec.ts --include=src/app/synthesis-constraints",
+    "test:spec:electron-karma": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts --karma-only",
+    "test:runtime:electron": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts",
+    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/canvas.component.spec.ts --include=src/app/canvas/core/interaction/canvas-interaction.controller.spec.ts --include=src/app/canvas/core/renderers/logical/logical-renderer.driver.spec.ts --include=src/app/canvas/core/renderers/physical/physical-renderer.driver.spec.ts --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-expansion.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-input-interpreter.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/canvas-physical-data.service.spec.ts --include=src/app/canvas/core/services/canvas-scene-model.service.spec.ts --include=src/app/canvas/core/services/canvas-spinner.service.spec.ts --include=src/app/canvas/core/services/canvas-static-metadata.service.spec.ts --include=src/app/canvas/core/services/canvas-tool-cursor.service.spec.ts --include=src/app/canvas/core/services/canvas-view-state.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/core/utils/canvas-transform.util.spec.ts --include=src/app/canvas/renderers/pixi/logical/pixi-logical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.draw.spec.ts --include=src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts --include=src/app/canvas/renderers/svg/physical/svg-physical-renderer.base.spec.ts --include=src/app/canvas/ui/components/component-node/instance-svg/instance-svg.component.spec.ts --include=src/app/canvas/ui/design-flow/canvas-toolbar/canvas-toolbar.component.spec.ts --include=src/app/canvas/ui/diff/canvas-diff.component.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts --include=src/app/canvas/ui/sidebar/canvas-visualizations/canvas-visualizations.component.spec.ts --include=src/app/shared/components/svg-renderer/svg-renderer.component.spec.ts",
+    "test:spec:shell-synthesis": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.shell-synthesis.json --include=src/app/app.component.spec.ts --include=src/app/status-bar/export-dialog/export-dialog.component.spec.ts --include=src/app/status-bar/status-bar.component.spec.ts --include=src/app/shared/directives/native-panel-resize.directive.spec.ts --include=src/app/project --include=src/app/menu-bar/menu-bar.component.spec.ts --include=src/app/shared/services/nav-bar.utils.spec.ts --include=src/app/synthesis-constraints",
     "lint": "eslint --fix",
     "e2e": "ng e2e",
     "ai-gui-docgen": "node agent/collect-app-docs-data.js && python agent/render-app-docs.py --skip-spec",
```
### Commit 55885d15452b3f8af975d724a94ad52095dc1784
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-07T14:01:54-05:00; reachable from selected HEAD: True.
Subject: Drive UDG Playwright coverage from live CE metadata
Change-Ids: I214d34ce5bc6444194c57e1a6304fb95cdf551d1.
Diff excerpt, `GUI/tests/fixtures/index.ts`:
```diff
@@ -4,7 +4,6 @@ import { test as electronTest } from './electron-fixtures-utils';
 import { InterconnectArchitect } from '../modules/ui/interconnect-architect';
 import { resolveIaOptions } from '../config/runtime-options';
 import { normalizeIpKey, capabilitiesForIp, NavigationCapabilities } from '../config/ip-capabilities';
-import fs from 'fs';
 import { startInactivityWatchdog, InactivityWatchdog } from '../modules/utils/inactivity-watchdog';
 
 interface IaConfig {
```
Diff excerpt, `GUI/tests/fixtures/index.ts`:
```diff
@@ -51,7 +50,6 @@ interface TestFixtures {
   };
   projectReady: InterconnectArchitect;
   projectName: string;
-  udgMeta: any;
   iaConfig: IaConfig;
   capabilities: NavigationCapabilities;
   capabilityGuard: (predicate: (caps: NavigationCapabilities) => boolean, reason: string) => void;
```
Diff excerpt, `GUI/tests/fixtures/index.ts`:
```diff
@@ -109,22 +107,6 @@ export const test = electronTest.extend<TestFixtures, WorkerFixtures>({
     await use(resolveConfigFromOptions(iaIp, iaTemplate));
   },
 
-  // eslint-disable-next-line no-empty-pattern
-  udgMeta: async ({}, use) => {
-    const metaPath = process.env.UDG_META_PATH;
-    if (metaPath && fs.existsSync(metaPath)) {
-      try {
-        const raw = fs.readFileSync(metaPath, 'utf-8');
-        const parsed = JSON.parse(raw);
-        await use(parsed);
-        return;
-      } catch (err) {
-        console.warn('[udgMeta] failed to read/parse', metaPath, err);
-      }
-    }
-    await use(undefined);
-  },
-
   capabilities: async ({ iaConfig }, use) => {
     await use(capabilitiesForIp(iaConfig.ip));
   },
```
### Commit c8120b3bc450ea5097d736bc4b746aa996826323
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-18T14:12:01-05:00; reachable from selected HEAD: True.
Subject: Add feature-rich Nitwain end-to-end regression
Change-Ids: I24b9b7dea7f7533c1354888d8be7b9c8d5a112e8.
Diff excerpt, `GUI/tests/modules/ui/project/project-page.ts`:
```diff
@@ -410,7 +410,7 @@ export class ProjectPage {
     await this.dismissExistingProjectModalIfPresent();
     await this.progressBar.waitFor();
 
-    const currentRow = this.page.locator('[data-testid="recent-project-row"].is-current').first();
+    const currentRow = this.getCurrentProjectRow();
     if (!(await currentRow.isVisible().catch(() => false))) {
       return null;
     }
```
Diff excerpt, `GUI/tests/modules/ui/project/project-page.ts`:
```diff
@@ -418,6 +418,18 @@ export class ProjectPage {
     return (await currentRow.getAttribute('data-project-name'))?.trim() ?? null;
   }
 
+  async getCurrentProjectRowTextFromCurrentView(): Promise<string | null> {
+    await this.dismissExistingProjectModalIfPresent();
+    await this.progressBar.waitFor();
+
+    const currentRow = this.getCurrentProjectRow();
+    if (!(await currentRow.isVisible().catch(() => false))) {
+      return null;
+    }
+
+    return ((await currentRow.textContent()) ?? '').replace(/\s+/g, ' ').trim();
+  }
+
   async getFirstDeletableProjectNameFromCurrentView(): Promise<string | null> {
     await this.dismissExistingProjectModalIfPresent();
     await this.progressBar.waitFor();
```
Diff excerpt, `GUI/tests/modules/ui/project/project-page.ts`:
```diff
@@ -1723,6 +1735,10 @@ export class ProjectPage {
     return this.page.locator('[data-testid="recent-project-row"][data-selected="true"]').first();
   }
 
+  private getCurrentProjectRow(): Locator {
+    return this.page.locator('[data-testid="recent-project-row"].is-current').first();
+  }
+
   private getOpenButtonForProject(projectName: string): Locator {
     return this.getProjectRow(projectName).getByTestId('recent-project-open-button');
   }
```
### Current source `GUI/tests/fixtures/index.ts`
Snapshot: HEAD; SHA-256 `c7737cb88e4ee5c9cb92e2deedc9f2e1f076cb03f377385e803aebb40d4e3a3e`.
Surviving-line author counts (attribution context only): {'Liza Dayoub': 147, 'Michael Coulter': 80, 'Dustin divis': 1}.
Introduction/rename-follow candidates: e677cf6d525c3416b32437a667bdeb0d66956f9a 2025-10-24T11:15:55-06:00 Liza Dayoub <liza.dayoub@arm.com> <BRUNEL-3624> Initial commit for Playwright GUI tests.
```text
1: // fixtures/index.ts
2: import * as path from 'path';
3: import { test as electronTest } from './electron-fixtures-utils';
4: import { InterconnectArchitect } from '../modules/ui/interconnect-architect';
5: import { resolveIaOptions } from '../config/runtime-options';
6: import { normalizeIpKey, capabilitiesForIp, NavigationCapabilities } from '../config/ip-capabilities';
7: import { startInactivityWatchdog, InactivityWatchdog } from '../modules/utils/inactivity-watchdog';
8: 
9: interface IaConfig {
10:   ip: string;
11:   template: string;
```
```text
35:   );
36: }
37: 
38: interface TestFixtures {
39:   interArchUi: InterconnectArchitect;
40:   interArchUiBare: InterconnectArchitect;
41:   interArchUiShared: InterconnectArchitect;
42:   interArchUiBareShared: InterconnectArchitect;
43:   interArchUiSharedBase: {
44:     instance: InterconnectArchitect;
45:     setSnapshotPath(fn: (...segments: string[]) => string): void;
46:   };
```
```text
48:     instance: InterconnectArchitect;
49:     setSnapshotPath(fn: (...segments: string[]) => string): void;
50:   };
51:   projectReady: InterconnectArchitect;
52:   projectName: string;
53:   iaConfig: IaConfig;
54:   capabilities: NavigationCapabilities;
55:   capabilityGuard: (predicate: (caps: NavigationCapabilities) => boolean, reason: string) => void;
56:   inactivityWatchdog: InactivityWatchdog;
57: }
58: 
59: interface WorkerFixtures {
60:   iaIp: string;
```
### Current source `GUI/tests/config/ip-capabilities.ts`
Snapshot: HEAD; SHA-256 `dd166c8fd6b6d084133158bbcb391b3503b6c6ed0c477ea0e1f736ce1c78f3b6`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 192, 'Liza Dayoub': 515, 'Dustin divis': 168, 'Pawan Kakarla': 21}.
Introduction/rename-follow candidates: ca60df32a6f896c814db8757fdcfa9b56857d5b7 2025-11-17T12:52:40-07:00 Liza Dayoub <liza.dayoub@arm.com> BRUNEL-3556.
```text
94: 
95: const NITWAIN_REGRESSION_ONLY_SPECS = [
96:   '**/rendering/canvas-selection-pan-lifecycle.spec.ts',
97:   '**/rendering/canvas-selection-metadata.spec.ts',
98:   '**/drc-waivers/drc-warning-escalation.spec.ts',
99:   '**/regression/debug_trace/twain_debugtrace1.spec.ts',
100:   '**/regression/enhanced_pmu/twain_enhancedpmu1.spec.ts',
101:   '**/regression/enhanced_pmu/twain_enhancedpmu2.spec.ts',
102: ];
103: const NITWAIN_LATEST_SPECS = [
104:   '**/feature-flows/noc-se-subsection-guard.spec.ts',
105:   '**/project/project.locking-lifecycle.spec.ts',
106:   '**/feature-flows/nitwain-r1-feature-gates.spec.ts',
107:   '**/canvas/indexed-route-editor.spec.ts',
108:   '**/canvas/indexed-sbs-connector.spec.ts',
109:   '**/canvas/non-data-route-segments.spec.ts',
110:   '**/canvas/subsection-physical-networks.spec.ts',
111:   '**/canvas/subsection-wizard.spec.ts',
112:   '**/canvas/transit-route-markers.spec.ts',
113:   '**/hls/interfaces/data/stripe-group-duplicate-targets.spec.ts',
```
```text
131: const CMNS4_DEV_ONLY_SPECS = [
132:   '**/feature-flows/cmn-route-outcomes.spec.ts',
133:   '**/feature-flows/cmn-mesh-routing-deadlock.spec.ts',
134:   '**/project/project.partial-import-outcomes.spec.ts',
135: ];
136: const CMNS4_ONLY_SPECS = [
137:   '**/feature-flows/cmn-mcs-groups.spec.ts',
138:   '**/menu-status-bar/cmn-checkpoint-restore.spec.ts',
139:   '**/project/import-migration-policy.spec.ts',
140:   '**/rendering/cmn-globals-device-counts.spec.ts',
141:   ...CMNS4_DEV_ONLY_SPECS,
142: ];
143: 
144: const CMNS4_R1P0_ONLY_SPECS = [
145:   '**/build/build-argument-outcomes.spec.ts',
146:   '**/node-configuration/user-defined-groups-safe-blank.spec.ts',
147:   '**/feature-flows/project-persistence-outcomes.spec.ts',
148: ];
149: 
150: const CMN_SPECS_ONLY = [
151:   '**/node-configuration/*.spec.ts',
152:   '**/mesh/*.spec.ts',
153:   '**/regression/brunel-4566-cmn.spec.ts',
154:   '**/regression/brunel-4568-cmn.spec.ts',
155:   '**/user-defined-groups/*.spec.ts',
```
### Current source `GUI/tests/ui/project/project.guided-flow-lifecycle.spec.ts`
Snapshot: HEAD; SHA-256 `3c3cc68f7ef19fcd7a5426ace11d294916a2453f23da0aa382158b6df407776c`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1022, 'Dustin divis': 5}.
Introduction/rename-follow candidates: 32939448d1a9a1f084701f320870daa4e0aa408e 2026-10-01T15:48:19-05:00 Michael Coulter <michael.coulter@arm.com> consolidate Guided Flow coverage across supported IPs.
```text
15:  *
16:  ***************************************************************************/
17: 
18: import { expect, test } from '../../fixtures';
19: import fs from 'fs';
20: import path from 'path';
21: import { randomUUID } from 'crypto';
22: import yaml from 'js-yaml';
23: import type { ProjectPage } from '../../modules/ui/project/project-page';
24: import { GUIDED_FLOW_REPRESENTATIVE_IP } from '../../config/ip-capabilities';
25: import { CHECKOUT_ROOT, guidedExampleForIp } from '../../utils/guided-flow-policy';
26: import { waitForFileIdle } from '../../utils/file-stability';
27: import {
28:   getPrimaryGuidedFlowMetadata,
29:   loadGuidedMetadataFixture,
30:   guidedMetadataPath,
31:   readGuidedFlowState,
32:   readGuidedMetadata,
33:   waitForGuidedFlowState,
34: } from '../../utils/guided-flow-metadata';
35: import {
36:   prepareGuidedWorkspace,
37:   startGuidedProjectFromExample,
```

## electron-karma

### Commit fa16f0019d05f3e0514f94594db9190f9fc0cbb0
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-05-18T14:44:36-05:00; reachable from selected HEAD: True.
Subject: Add Electron-bound Karma runtime workflow
Change-Ids: I92ef4a890537756aec5a807c13fa635950e0b66a.
Diff excerpt, `GUI/karma.electron.conf.js`:
```diff
@@ -0,0 +1,67 @@
+// Karma configuration for running Angular specs inside the Electron renderer.
+// The normal karma.conf.js remains Chrome/ChromeHeadless-oriented; this config
+// is captured manually by Electron through the runtime orchestration script.
+
+const path = require('path');
+
+function intFromEnv(name, fallback) {
+  const parsed = Number(process.env[name] ?? '');
+  return Number.isFinite(parsed) && parsed > 0 ? Math.floor(parsed) : fallback;
+}
+
+module.exports = function (config) {
+  const hostname = process.env.KARMA_HOSTNAME || '127.0.0.1';
+  const listenAddress = process.env.KARMA_LISTEN_ADDRESS || hostname;
+  const port = intFromEnv('KARMA_PORT', 9876);
+  const browserLogPath =
+    process.env.KARMA_ELECTRON_BROWSER_LOG ||
+    path.join(__dirname, 'tests/test-output/electron-runtime/browser-console.log');
+
+  config.set({
+    basePath: '',
+    frameworks: ['jasmine', '@angular-devkit/build-angular'],
+    plugins: [
+      require('karma-jasmine'),
+      require('karma-chrome-launcher'),
+      require('karma-jasmine-html-reporter'),
+      require('karma-coverage-istanbul-reporter'),
+      require('@angular-devkit/build-angular/plugins/karma')
+    ],
+    client: {
+      captureConsole: true,
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/package.json`:
```diff
@@ -22,6 +22,9 @@
     "coverage:open": "open tests/test-output/coverage/index.html",
     "pretest": "npm run prepare:styles",
     "test": "ng test",
+    "test:spec:electron-karma": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts --karma-only",
+    "test:runtime:electron": "ts-node --project tests/config/tsconfig.electron-runtime.json -O '{\"module\":\"commonjs\"}' tests/scripts/run-electron-karma-playwright.ts",
+    "test:spec:canvas": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.canvas.json --include=src/app/canvas/core/services/canvas-connections.service.spec.ts --include=src/app/canvas/core/services/canvas-hit-test.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-layout.service.spec.ts --include=src/app/canvas/core/services/canvas-logical-path-filter.service.spec.ts --include=src/app/canvas/core/services/logical-scene-builder.service.spec.ts --include=src/app/canvas/core/utils/canvas-logical-ccg.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-color.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-connection.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-layout-classifier.util.spec.ts --include=src/app/canvas/core/utils/canvas-logical-mcn.util.spec.ts --include=src/app/canvas/core/utils/canvas-route-hop-normalization.util.spec.ts --include=src/app/canvas/core/utils/canvas-tooltip.util.spec.ts --include=src/app/canvas/ui/sidebar/route-editor/route-editor.component.spec.ts",
     "test:spec:shell-synthesis": "ng test --watch=false --browsers ChromeHeadless --progress=false --ts-config tests/config/tsconfig.spec.shell-synthesis.json --include=src/app/project --include=src/app/menu-bar/menu-bar.component.spec.ts --include=src/app/shared/services/nav-bar.utils.spec.ts --include=src/app/synthesis-constraints",
     "lint": "eslint --fix",
     "e2e": "ng e2e",
```
Diff excerpt, `GUI/src/test-support/electron-karma-runtime.smoke.spec.ts`:
```diff
@@ -0,0 +1,7 @@
+describe('Electron-bound Karma runtime smoke', () => {
+  it('runs Angular specs inside a browser-like Electron renderer context', () => {
+    expect(typeof window).toBe('object');
+    expect(typeof document).toBe('object');
+    expect(typeof globalThis.process).toBe('object');
+  });
+});
```
### Commit fff32ba2a4b6f0f5a1018df771e2ba0a6ef19439
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-06-22T23:37:36-05:00; reachable from selected HEAD: True.
Subject: Expand GUI unit test coverage and Karma harness
Change-Ids: Iec7d8cf0502450b8e968c51b0f0a94abd6ca4589.
Diff excerpt, `GUI/karma.conf.js`:
```diff
@@ -15,6 +15,9 @@ module.exports = function (config) {
   const isHeadlessRun = requestedBrowsers.includes('Headless');
   const junitOutputDir = process.env.KARMA_JUNIT_OUTPUT_DIR || 'tests/test-output/junit';
   const junitOutputFile = process.env.KARMA_JUNIT_OUTPUT_FILE || 'unit-results.xml';
+  const karmaPort = Number.parseInt(process.env.KARMA_PORT || '9876', 10);
+  const karmaHostname = process.env.KARMA_HOSTNAME || '127.0.0.1';
+  const karmaListenAddress = process.env.KARMA_LISTEN_ADDRESS || karmaHostname;
   const reporters = ['progress', 'coverage', 'junit'];
   const plugins = [
     require('karma-jasmine'),
```
Diff excerpt, `GUI/karma.conf.js`:
```diff
@@ -51,7 +54,9 @@ module.exports = function (config) {
       useBrowserName: false
     },
     reporters,
-    port: 9876,
+    port: Number.isFinite(karmaPort) ? karmaPort : 9876,
+    hostname: karmaHostname,
+    listenAddress: karmaListenAddress,
     colors: true,
     logLevel: config.LOG_INFO,
     autoWatch: !isHeadlessRun,
```
Diff excerpt, `GUI/package-lock.json`:
```diff
@@ -45,8 +45,9 @@
         "karma": "^6.4.4",
         "karma-chrome-launcher": "^3.2.0",
         "karma-coverage": "^2.2.1",
+        "karma-coverage-istanbul-reporter": "^3.0.3",
         "karma-jasmine": "^5.1.0",
-        "karma-jasmine-html-reporter": "^2.1.0",
+        "karma-jasmine-html-reporter": "^2.2.0",
         "karma-junit-reporter": "^2.0.1",
         "nyc": "^18.0.0",
         "playwright": "1.48.1",
```
### Current source `GUI/tests/scripts/electron-karma-runtime.ts`
Snapshot: HEAD; SHA-256 `63fc2cba00443fa504d6b28c1408f2dba825e530e0373886260334b95deab216`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 190}.
Introduction/rename-follow candidates: fa16f0019d05f3e0514f94594db9190f9fc0cbb0 2026-05-18T14:44:36-05:00 Michael Coulter <michael.coulter@arm.com> Add Electron-bound Karma runtime workflow.
```text
1: import fs from 'fs';
2: import http from 'http';
3: import net from 'net';
4: import path from 'path';
5: 
6: export type ElectronRuntimeRendererMode = 'gpu' | 'cpu';
7: 
8: export interface RuntimeOutputPaths {
9:   rootDir: string;
10:   userDataDir: string;
11:   logDir: string;
12:   karmaStdoutPath: string;
13:   karmaStderrPath: string;
14:   karmaBrowserLogPath: string;
```
### Current source `GUI/tests/scripts/run-electron-karma-playwright.ts`
Snapshot: HEAD; SHA-256 `3bca4508a7d2b68e191cad55fe0ccf28d6cfe60da73a6b6b6467212bf6c944ac`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 423, 'Liza Dayoub': 46}.
Introduction/rename-follow candidates: fa16f0019d05f3e0514f94594db9190f9fc0cbb0 2026-05-18T14:44:36-05:00 Michael Coulter <michael.coulter@arm.com> Add Electron-bound Karma runtime workflow.
```text
1: import fs from 'fs';
2: import path from 'path';
3: import { createRequire } from 'module';
4: import { spawn, type ChildProcessWithoutNullStreams } from 'child_process';
5: import type { ElectronApplication, Page } from '@playwright/test';
6: 
7: import {
8:   buildElectronRuntimeEnv,
9:   buildKarmaCaptureUrl,
10:   buildKarmaRuntimeEnv,
11:   buildRuntimeRunId,
12:   ensureRuntimeOutputDirs,
13:   findFreePort,
```
### Current source `scripts/vertical-tests/test-owo-streaming.sh`
Snapshot: HEAD; SHA-256 `e73ef9ae998c0670f1b9d2a8c549ca4e2be3cbeed266bce6ea3d5c3fefce3690`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 369}.
Introduction/rename-follow candidates: 9851f748f2450a96ad59aab5521b3bc157ba79db 2026-09-29T02:44:43-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-4829: OWO Streaming Wizard.
```text
3: # OWO Streaming vertical test runner.
4: #
5: # Exercises the CE contract, Angular wizard/orchestration layer, and Electron
6: # Playwright workflows that collectively configure and validate OWO Streaming.
7: # The wizard-specific files are discovered conditionally so this runner remains
8: # useful in checkouts where only the legacy OWO flow has landed.
9: set -euo pipefail
10: 
11: SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
12: CHECKOUT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
13: GUI_DIR="${CHECKOUT_ROOT}/GUI"
14: CE_DIR="${CHECKOUT_ROOT}/CE"
15: NODE_BIN="${GUI_DIR}/node_modules/.bin"
16: CE_PYTHON="${CE_PYTHON:-${CE_DIR}/venv/bin/python}"
17: OWO_STREAMING_NODE_VERSION="${OWO_STREAMING_NODE_VERSION:-22.12.0}"
18: PLAYWRIGHT_REPORT_DIR="${GUI_DIR}/tests/test-output/playwright-report-owo-streaming"
19: PLAYWRIGHT_JUNIT_FILE="${GUI_DIR}/tests/test-output/junit-results-owo-streaming.xml"
20: 
21: RUN_CE_PYTESTS="${RUN_CE_PYTESTS:-1}"
22: RUN_ANGULAR_TESTS="${RUN_ANGULAR_TESTS:-1}"
23: RUN_PLAYWRIGHT_TESTS="${RUN_PLAYWRIGHT_TESTS:-1}"
24: RUN_GUI_BUILD="${RUN_GUI_BUILD:-1}"
25: PLAYWRIGHT_HEADED=false
26: PLAYWRIGHT_ARGS=()
27: 
28: usage() {
29:   cat <<EOF
30: Usage: $(basename "$0") [options]
31: 
32: Runs the focused OWO Streaming vertical stack:
33:   1. CE API, parameter, HLS DRC, MA DRC, path/RP, and generation pytests.
```

## lifecycle

### Commit c5250faae7ab861de53a6416406ad0708dfcbaee
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-04-17T17:55:56-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2072: Brunel GUI hangs if input config is corrupted
Change-Ids: I086377e06c9d143bc6c55a056f7a4efe4eced3b4.
### Commit 7bed6f651e4d8aca0850cac94deafe55e9ee1c33
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-04-08T22:46:11-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2634, BRUNEL-2799, BRUNEL-2801
Change-Ids: I0cf718f9f7d029798cd2100b5998ac1cb2fe4e69.
Diff excerpt, `GUI/src/app/test-and-report/logger/logger.component.ts`:
```diff
@@ -189,10 +193,18 @@ export class LoggerComponent implements OnInit, OnDestroy, AfterViewInit {
 
     // this will open the logger to the "DRC" tab when any DRC button in the app is pressed
     this.testServiceApi.loggerTabChangedSubject.pipe(takeUntil(this.unsubscribeAll)).subscribe(tab => {
-      this.loggerType = tab;
-      const i = this.loggerFiles.indexOf(tab);
-      this.sidebarTabIndex = i;
-      this.cdr.detectChanges();
+      this.loggerType = null; // force clear first
+      this.cdr.detectChanges(); // trigger Angular refresh
+      setTimeout(() => {
+        this.loggerType = tab;
+        let i = this.loggerFiles.indexOf(tab);
+        this.sidebarTabIndex = i;
+        // fetch build log file
+        this.testServiceApi.updateErrorLog(this.projectDirectory);
+        this.loggerSelect();
+        this.scrollToBotton();
+        this.cdr.detectChanges();
+      }, 0); // next tick to ensure re-render
     });
 
     // keeps track of current DRC type
```
### Commit f5881ff4e50ebf29740a2227ea34d430ca4ffe16
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-06-12T22:56:10-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-3223: Create a 'Pre-build check' API that will run lite BE/Build tab button
Change-Ids: I79039bf523b1239209a6a3c8c459afce5719fb6e.
Diff excerpt, `GUI/src/app/app.component.ts`:
```diff
@@ -20,7 +20,7 @@ import { NavigationEnd, Router } from '@angular/router';
 
 import { Subscription, Subject } from 'rxjs';
 import { takeUntil } from 'rxjs/operators';
-// import { map } from 'rxjs/operators';
+import { join } from 'path';
 
 import { DataService } from './shared/services/data.service';
 import { ProjectManagmentService } from './project/project-managment.service';
```
Diff excerpt, `GUI/src/app/build/build-service.ts`:
```diff
@@ -250,9 +250,17 @@ export class BuildService {
     return readyForBuildObservalbe;
   }
 
-  private setupBuildSpinner() {
-    this.spinnerSuccessMessage = 'RTL generation complete!';
-    this.spinnerFailureMessage = 'RTL generation failed!';
+  private setupBuildSpinner(preBuildCheck = false) {
+    let progressMsg = '';
+    if (preBuildCheck) {
+      this.spinnerSuccessMessage = 'Pre-build check complete!';
+      this.spinnerFailureMessage = 'Pre-build check failed!';
+      progressMsg = 'Running pre-build check...';
+    } else {
+      this.spinnerSuccessMessage = 'RTL generation complete!';
+      this.spinnerFailureMessage = 'RTL generation failed!';
+      progressMsg = 'Generating RTL...';
+    }
     this.spinnerDisplayPriavte = [{ status: 'inProgress', text: 'Please wait...', progressWeight: 0 }];
     this.spinnerStages = { run: 1 };
     const stagesWeights = { run: 100 };
```
### Commit 1aa44baff56d6b49bc9b39cf2b874ba3d8d22ea1
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-04-14T11:17:14-05:00; reachable from selected HEAD: True.
Subject: Project tab rework
Change-Ids: I203e63bbefbcb87e8d97e949b075c6f729b8ac94.
Diff excerpt, `GUI/src/app/app.component.ts`:
```diff
@@ -180,6 +188,21 @@ export class AppComponent implements OnInit, OnDestroy, AfterViewInit {
       this.logExpanded = state;
     });
 
+    this.projectSpinnerSub = this.projectSpinnerService.spinnerStatusChanged.subscribe(() => {
+      this.updateGlobalProjectSpinner();
+    });
+
+    this.projectTransitionSub = this.projectManagmentService.projectSpinnerActivate.subscribe(isActive => {
+      if (!isActive) {
+        return;
+      }
+
+      this.projectTransitionPending = true;
+      this.clearProjectSpinnerHideTimeout();
+      this.canvasSpinnerService.startSpinner('Loading project...');
+      this.canvasSpinnerService.updateProgress(0);
+    });
+
     this.statusBarService.loggerHeight$.pipe(takeUntil(this.unsubscribe$)).subscribe(height => {
       this.terminalHeight = height;
     });
```
Diff excerpt, `GUI/src/app/project/project.component.ts`:
```diff
@@ -113,42 +87,376 @@ export class ProjectComponent implements OnInit, CanComponentDeactivate, OnDestr
   }
 
   ngOnDestroy(): void {
-    if (this.spinnerSub) {
-      this.spinnerSub.unsubscribe();
+    if (this.launcherStateSub) {
+      this.launcherStateSub.unsubscribe();
     }
-    if (this.workspaceSub) {
-      this.workspaceSub.unsubscribe();
+    if (this.projectNameSub) {
+      this.projectNameSub.unsubscribe();
     }
     sessionStorage.removeItem('floorplan-check');
   }
 
-  private updateSpinner(isActive: boolean) {
-    this.spinnerDisplay = this.projectSpinnerService.spinnerDisplay;
-    this.spinnerProgress = this.projectSpinnerService.spinnerProgress;
-    if (this.spinnerIsActive && !isActive) {
-      this.spinnerMode = 'determinate';
-      this.cdr.detectChanges();
-      const spinnerCompleteTimeout = setTimeout(() => {
-        this.spinnerIsActive = isActive;
-        this.cdr.detectChanges();
-      }, this.spinnerDisplay[0].status === 'failure' ? 3000 : 1000);
-    } else {
-      this.spinnerMode = !this.spinnerProgress ? 'indeterminate' : 'determinate';
-      this.spinnerIsActive = isActive;
-      this.cdr.detectChanges();
+  get selectedProject(): WorkspaceProjectSummary | null {
[hunk excerpt ends; remaining lines omitted]
```
### Commit 12eb8c808c4743cc394118f0e66e8569cf1dfdc7
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-29T15:08:54-05:00; reachable from selected HEAD: True.
Subject: Isolate competing project load pipelines
Change-Ids: I284c46ad5fe141a7181afe49dcf9fb0227257db2.
Diff excerpt, `GUI/src/app/project/project-launcher.service.spec.ts`:
```diff
@@ -274,6 +277,30 @@ describe('ProjectLauncherService', () => {
     );
   });
 
+  function latestLoadCallbacks(): {
+    onMigrationReady?: (requestId: number) => void | Promise<void>;
+    onComplete?: (result: any) => void;
+  } {
+    const callbacks = projectManagmentServiceStub.loadProject.calls.mostRecent()?.args?.[3];
+    if (!callbacks) throw new Error('No request-scoped project load callbacks were registered.');
+    return callbacks;
+  }
+
+  async function signalLatestMigrationReady(requestId = 1): Promise<void> {
+    await latestLoadCallbacks().onMigrationReady?.(requestId);
+  }
+
+  function signalLatestLoadComplete(status: 'completed' | 'failed' | 'superseded', overrides: any = {}): void {
+    latestLoadCallbacks().onComplete?.({
+      requestId: 1,
+      status,
+      projectName: projectManagmentServiceStub.projectName,
+      projectDirectory: projectManagmentServiceStub.projectDir,
+      configPath: '',
+      ...overrides,
+    });
+  }
+
   it('accepts NIC XML files in Clone From Config and suggests the input basename as the default project name', async () => {
     modalServiceSpy.showInputConfirmation.and.returnValue(of(['nic400_example', 'uniq0']));
 
```
Diff excerpt, `GUI/src/app/project/project-launcher.service.ts`:
```diff
@@ -401,83 +405,83 @@ export class ProjectLauncherService implements OnDestroy {
       );
     }
 
-    const migrateSubscription = this.projectManagmentService.beginProjCloneMigrateStage.subscribe(ready => {
-      if (!ready) {
-        return;
-      }
-
-      migrateSubscription.unsubscribe();
-      this.zone.run(() => {
-        void this.applyImportMigrationPolicyOrPrompt(selectedIPVersion, guidedFlow);
-      });
-    });
-
-    const loadCompletionSubscription = this.projectManagmentService.projectLoadComplete.subscribe(complete => {
-      loadCompletionSubscription.unsubscribe();
-      if (complete) {
-        return;
-      }
-      migrateSubscription.unsubscribe();
-      if (guidedFlow?.startingIpVersion) {
-        try {
-          this.guidedFlowPolicyService.clearStartingGuidedFlow(this.projectManagmentService.projectDir);
-        } catch (error) {
-          console.error('Failed to clear Guided Flow metadata after import failure.', error);
-        }
-      }
-      if (!projectSetupResponse.existed) {
-        const cleanupResponse = this.projectManagmentService.discardFailedProjectSetup(confirmation[0]);
-        if (!cleanupResponse?.success) {
-          console.error(cleanupResponse?.error || 'Failed to discard project after import failure.');
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/project/project-launcher.service.ts`:
```diff
@@ -486,12 +490,37 @@ export class ProjectLauncherService implements OnDestroy {
         {
           reason: 'configured-import-policy',
           logMessage: `Imported YAML migrated from ${sourceIpVersion} to ${matchingRule.targetIpVersion} by configured import migration policy.`
-        }
+        },
+        loadRequestId,
       );
       return;
     }
 
-    await this.setupMigrateData(guidedFlow ? sourceIpVersion : selectedIPVersion);
+    await this.setupMigrateData(guidedFlow ? sourceIpVersion : selectedIPVersion, loadRequestId);
+  }
+
+  private handleImportLoadCompletion(
+    result: ProjectLoadResult,
+    guidedFlow: GuidedFlowImportContext | undefined,
+    projectSetupResponse: any,
+    projectName: string,
+  ): void {
+    if (result.status === 'completed') return;
+    if (guidedFlow) {
+      try {
+        this.guidedFlowPolicyService.clearStartingGuidedFlow(result.projectDirectory);
+      } catch (error) {
+        console.error('Failed to clear Guided Flow metadata after import failure.', error);
+      }
+    }
+    const canDiscardProject = result.status === 'failed'
+      || this.projectManagmentService.projectDir !== result.projectDirectory;
+    if (!projectSetupResponse.existed && canDiscardProject) {
[hunk excerpt ends; remaining lines omitted]
```
### Commit c7d43253081940a2d599647f2820bf5837ab882a
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-06T11:33:23-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-4632: Fix stale HLS and uArch DRC result handling
Change-Ids: Icf172068fec235541019f6964fa1ed279f977257.
Diff excerpt, `GUI/src/app/status-bar/drc-results/drc-results.component.spec.ts`:
```diff
@@ -126,8 +126,11 @@ describe('DrcResultsComponent', () => {
     dataService.ceErrorString = '[CE]%ERROR Instance r0 has invalid wiring';
 
     component.showDrcLogs();
+    const requestId = dataService.brunelCEApi.calls
+      .allArgs()
+      .find((args) => args[1] === 'check_micro_architecture_rules')[0];
     dataService.brunelCEResponse.next({
-      id: 'app-drc-results_rules-check',
+      id: requestId,
       res: [[27, 5]],
     });
 
```
Diff excerpt, `GUI/src/app/status-bar/drc-results/drc-results.component.spec.ts`:
```diff
@@ -140,12 +143,89 @@ describe('DrcResultsComponent', () => {
     component.drcType = DrcTypes.uArch;
 
     component.showDrcLogs();
+    const requestId = dataService.brunelCEApi.calls
+      .allArgs()
+      .find((args) => args[1] === 'check_micro_architecture_rules')[0];
     dataService.brunelCEResponse.next({
-      id: 'app-drc-results_rules-check',
+      id: requestId,
       res: true,
     });
 
     expect(canvasDrcHighlightService.clearMaDrcHighlights).toHaveBeenCalled();
     expect(canvasDrcHighlightService.handleMaDrcFailure).not.toHaveBeenCalled();
   });
+
+  it('waits for the selected DRC event instead of rerunning a stale input on initialization', () => {
+    const testServiceApi = TestBed.inject(TestAndReportServiceApi) as unknown as TestAndReportServiceApiStub;
+    component.drcType = DrcTypes.uArch;
+
+    component.ngOnInit();
+
+    expect(dataService.brunelCEApi.calls.allArgs())
+      .not.toContain(jasmine.arrayContaining(['check_micro_architecture_rules', [false]]));
+
+    testServiceApi.drcResultsChangedSubject.next(DrcTypes.HLS);
+
+    expect(dataService.brunelCEApi).toHaveBeenCalledTimes(2);
+    expect(dataService.brunelCEApi.calls.allArgs())
+      .toContain(jasmine.arrayContaining(['check_hls_rules', [false]]));
+    expect(dataService.brunelCEApi.calls.allArgs())
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/status-bar/drc-results/drc-results.component.ts`:
```diff
@@ -81,11 +85,10 @@ export class DrcResultsComponent implements OnInit, OnDestroy {
     // this might be dead code, I can't get it to execute
     this.testServiceApi.drcResultsChangedSubject.pipe(takeUntil(this.unsubscribeAll)).subscribe(drcType => {
       this.drcType = drcType;
-      this.showDrcLogs(); // calls DRCs
       this.majorResults = [{ name: 'Checking...' }];
+      this.showDrcLogs(); // calls DRCs
       this.cdr.detectChanges();
     });
-    this.showDrcLogs(); // calls DRCs
   }
 
   ngOnDestroy(): void {
```
### Commit 1ad1c93d466261afe48ee9441c42471c3fafde2e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-18T17:26:21-05:00; reachable from selected HEAD: True.
Subject: Prevent stale guided flow work across project loads
Change-Ids: If1af1a194dfed842895221350dd754d8d10a988d.
Diff excerpt, `GUI/src/app/menu-bar/menu-bar.component.spec.ts`:
```diff
@@ -707,6 +708,63 @@ describe('MenuBarComponent', () => {
     expect(component.noCLiteCheckIconColor).toBe('#ff6b00');
   });
 
+  it('should cancel a pending NoC-Lite Check as soon as a competing project name is published', async () => {
+    const guidedFlowPolicyService = TestBed.inject(
+      GuidedFlowPolicyService,
+    ) as unknown as GuidedFlowPolicyServiceStub;
+    const guidedFlowLogService = TestBed.inject(GuidedFlowLogService) as unknown as GuidedFlowLogServiceStub;
+    const projectService = TestBed.inject(ProjectService) as unknown as ProjectServiceStub;
+    let resolveCheck!: (result: any) => void;
+    guidedFlowPolicyService.isGuidedModeActive = true;
+    guidedFlowPolicyService.activeFlowId = 'noc_lite';
+    guidedFlowPolicyService.checkCompliance.and.returnValue(new Promise(resolve => {
+      resolveCheck = resolve;
+    }));
+
+    const checkPromise = component.triggerNoCLiteCheck();
+    expect(component.isNoCLiteCheckRunning).toBeTrue();
+
+    projectService.projectName = 'next-project';
+    projectService.projectNameChanged.next('next-project');
+
+    expect(component.isNoCLiteCheckRunning).toBeFalse();
+    resolveCheck({ status: 'failed', violations: [{ message: 'stale result' }] });
+    await checkPromise;
+
+    expect(guidedFlowLogService.appendNoCLiteCheckResult).not.toHaveBeenCalled();
+    expect(component.noCLiteCheckIconColor).toBe('#ff6b00');
+  });
+
+  it('should cancel a pending NoC-Lite Check when a competing project load starts', async () => {
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/menu-bar/menu-bar.component.ts`:
```diff
@@ -203,6 +203,7 @@ export class MenuBarComponent implements OnInit, OnDestroy {
   private noCLiteCheckSequence = 0;
   private activeNoCLiteCheckContext: {
     requestId: number;
+    projectName: string;
     projectDirectory: string;
     flowId: string;
   } | null = null;
```
Diff excerpt, `GUI/src/app/menu-bar/menu-bar.component.ts`:
```diff
@@ -1266,6 +1278,7 @@ export class MenuBarComponent implements OnInit, OnDestroy {
     }
     const context = {
       requestId: ++this.noCLiteCheckSequence,
+      projectName: this.projectService.projectName,
       projectDirectory,
       flowId,
     };
```
### Current source `GUI/src/app/project/project-launcher.service.ts`
Snapshot: HEAD; SHA-256 `1e1e94d1e5d525f0d69c420413062cb80a2943a6a9e2336b807acbcd29663203`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 978, 'Pawan Kakarla': 22, 'Dustin divis': 18}.
Introduction/rename-follow candidates: 1aa44baff56d6b49bc9b39cf2b874ba3d8d22ea1 2026-04-14T11:17:14-05:00 Michael Coulter <michael.coulter@arm.com> Project tab rework Add user-configurable workspace directory/path handling via GUI and also with env `BRUNEL_HOME` File menu rework for improved project navigation Delete project from project tab Recent projects access Corrupt config indication.
```text
455: 
456:     this.beginProjectTransition();
457:     this.projectManagmentService.loadProject(filePath, 'clone', undefined, {
458:       onMigrationReady: requestId => this.zone.run(
459:         () => this.applyImportMigrationPolicyOrPrompt(
460:           selectedIPVersion,
461:           guidedFlow,
462:           requestId,
463:           projectSetupResponse.projectDirectory,
464:           guidedOperation,
465:         )
466:       ),
467:       onComplete: result => this.handleImportLoadCompletion(
468:         result,
469:         guidedFlow,
470:         projectSetupResponse,
```
```text
478:   private async applyImportMigrationPolicyOrPrompt(
479:     selectedIPVersion: string,
480:     guidedFlow: GuidedFlowImportContext | undefined,
481:     loadRequestId: number,
482:     projectDirectory: string,
483:     guidedOperation?: GuidedFlowLaunchOperation,
484:   ): Promise<void> {
485:     if (!this.projectManagmentService.isLoadRequestCurrent(loadRequestId)) return;
486:     const policy = this.getIpVersionPolicy();
487:     const singleIp = policy.singleIp;
488:     let sourceIpVersion = '';
489: 
490:     if (guidedFlow) {
491:       sourceIpVersion = await this.projectManagmentService.getCurrentIPVersion();
492:       if (!this.projectManagmentService.isLoadRequestCurrent(loadRequestId)) return;
493:       if (!guidedFlow.startingIpVersion) {
494:         const metadata = await this.guidedFlowPolicyService.beginStarting(
495:           guidedFlow.flowId,
496:           sourceIpVersion,
497:           guidedFlow.source,
498:           projectDirectory,
499:           { deferIpVersionValidation: true }
500:         );
```
### Current source `GUI/src/app/status-bar/drc-results/drc-results.component.ts`
Snapshot: HEAD; SHA-256 `5d04b00df7e9de2935eb855d3edfbdbb5097c4937c42595f355f64a710d5ce8b`.
Surviving-line author counts (attribution context only): {'Kelly Alvarez': 56, 'Michael Coulter': 77, 'Dustin divis': 68, 'Dustin Divis': 34, 'Pawan Kakarla': 17, 'dusdiv01': 1}.
Introduction/rename-follow candidates: db6823b0c4c757b9a21166e5385415aff273a2a0 2020-12-01T15:20:03-06:00 Dustin Divis <dustin.divis@arm.com> [GUI/brunel] Status Bar: Phase 1 complete.
```text
19: import { ChangeDetectorRef, Component, EventEmitter, Input, OnDestroy, OnInit, Output } from '@angular/core';
20: 
21: import { Subscription, Subject } from 'rxjs';
22: import { takeUntil } from 'rxjs/operators';
23: 
24: import { CanvasConnectionsService } from 'src/app/canvas/core/services/canvas-connections.service';
25: import { ProjectService } from 'src/app/project/project.service';
26: import { DataService } from 'src/app/shared/services/data.service';
27: import { GlobalService } from 'src/app/shared/services/global.service';
28: import { TestAndReportServiceApi } from 'src/app/test-and-report/test-report-service-api';
29: import { DrcWaiverService } from 'src/app/drc-waivers/services/drc-waiver.service';
30: import { DrcTypes } from 'src/app/shared/models/drc-types.enum';
```
```text
69: 
70:   ngOnInit(): void {
71:     this.drcLog = this.dataService.drcLog;
72:     this.dataService.drcLogSubject.pipe(takeUntil(this.unsubscribeAll)).subscribe(drcLog => {
73:       this.drcLog = drcLog;
74:       this.updateMajorResults();
75:       if (this.drcType === DrcTypes.uArch && this.uArchDrcFailed) {
76:         this.canvasDrcHighlightService.handleMaDrcFailure(drcLog, false);
77:       }
78:       this.cdr.detectChanges();
79:     });
80: 
81:     // this might be dead code, I can't get it to execute
82:     this.testServiceApi.drcResultsChangedSubject.pipe(takeUntil(this.unsubscribeAll)).subscribe(drcType => {
83:       this.drcType = drcType;
84:       this.majorResults = [{ name: 'Checking...' }];
85:       this.showDrcLogs(); // calls DRCs
86:       this.cdr.detectChanges();
87:     });
88:   }
89: 
90:   ngOnDestroy(): void {
```
```text
108:     this.majorResults = [{name: 'Checking...'}];
109:     this.results = 'Checking...';
110:     this.availableNetworks = this.canvasConnectionRouteService.routeAttrs.NetworkType;
111:     this.activeResultsSubscription = this.tools.run(type, this.availableNetworks, {isCurrent: current})
112:       .pipe(takeUntil(this.unsubscribeAll)).subscribe({
113:         next: ({outcome, rules, title}) => {
114:           if (!current() || outcome.reconciliation.status === 'obsolete') return;
115:           this.modalTitle = title;
116:           this.drcRules = rules;
117:           if (!outcome.success || outcome.reconciliation.status !== 'refreshed') {
118:             const notice = ceWorkflowNotification(outcome, title);
119:             this.majorResults = [{name: notice?.message || 'The action did not complete.'}];
120:           } else {
```
### Current source `GUI/tests/ui/project/project.competing-loads.spec.ts`
Snapshot: HEAD; SHA-256 `8969361d0ddf768e9dd9308fed5c1a4293d9ffd6722144c03509af1717bbac47`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 340, 'Liza Dayoub': 41}.
Introduction/rename-follow candidates: 12eb8c808c4743cc394118f0e66e8569cf1dfdc7 2026-07-29T15:08:54-05:00 Michael Coulter <michael.coulter@arm.com> Isolate competing project load pipelines.
```text
155:   await expect(page.getByTestId('project-landing-page')).toBeHidden();
156: });
157: 
158: test('a stale Guided activation cannot cross into a subsequently opened project', async ({
159:   iaConfig,
160:   interArchUiBare,
161: }, testInfo) => {
162:   test.slow();
163:   test.skip(
164:     !SUPPORTED_TOWERNCI_IPS.has(iaConfig.ip),
165:     `Competing project Guided activation coverage only runs on towernci_r1p3 or towernci_r1p5 (current: ${iaConfig.ip}).`,
166:   );
```
```text
361:         id: responseId,
362:         res: {
363:           status: 'failed',
364:           violations: [{ message: 'STALE_PROJECT_A_RESULT' }],
365:         },
366:       },
367:     );
368:   });
369: 
370:   await expect(page.getByTestId('noc-lite-check-button')).toBeEnabled({ timeout: 30_000 });
371:   await page.waitForTimeout(1_000);
372:   expect(
```
```text
374:       const logPath = path.join(directory, 'guided-flow.log');
375:       return (
376:         fs.existsSync(logPath) &&
377:         fs.readFileSync(logPath, 'utf8').includes('STALE_PROJECT_A_RESULT')
378:       );
379:     }),
380:   ).toBe(false);
381: });
```

## console

### Commit 5b307cd1717f72d851f7807c67782659f53a05f8
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-03-30T13:28:12-05:00; reachable from selected HEAD: True.
Subject: Add ability for users to run report scripts from the GUI
Change-Ids: Ie1673ac67890711b7bb4050d6b8f1facf31a5234.
Diff excerpt, `GUI/package-lock.json`:
```diff
@@ -1,8 +1,17296 @@
 {
   "name": "ideas",
   "version": "0.0.0",
-  "lockfileVersion": 1,
+  "lockfileVersion": 2,
   "requires": true,
+  "packages": {
+    "": {
+      "name": "ideas",
+      "version": "0.0.0",
+      "dependencies": {
+        "@angular/animations": "~9.1.3",
+        "@angular/cdk": "~9.2.0",
+        "@angular/common": "~9.1.3",
+        "@angular/compiler": "~9.1.3",
+        "@angular/core": "~9.1.3",
+        "@angular/forms": "~9.1.3",
+        "@angular/material": "~9.2.0",
+        "@angular/platform-browser": "~9.1.3",
+        "@angular/platform-browser-dynamic": "~9.1.3",
+        "@angular/router": "~9.1.3",
+        "@ungap/structured-clone": "^0.3.4",
+        "angular2-draggable": "^2.3.2",
+        "ngx-electron": "^2.2.0",
+        "path": "^0.12.7",
+        "rxjs": "~6.5.4",
+        "zone.js": "~0.10.2"
+      },
+      "devDependencies": {
+        "@angular-devkit/build-angular": "~0.901.3",
+        "@angular/cli": "~9.1.3",
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/package-lock.json`:
```diff
@@ -1510,7 +18807,6 @@
       "version": "1.12.4",
       "resolved": "https://registry.npmjs.org/@electron/get/-/get-1.12.4.tgz",
       "integrity": "sha512-6nr9DbJPUR9Xujw6zD3y+rS95TyItEVM0NVjt1EehY2vUWfIgPiIPVHxCvaTS0xr2B+DRxovYVKbuOWqC35kjg==",
-      "dev": true,
       "requires": {
         "debug": "^4.1.1",
         "env-paths": "^2.2.0",
```
Diff excerpt, `GUI/package-lock.json`:
```diff
@@ -1527,7 +18823,6 @@
           "version": "8.1.0",
           "resolved": "https://registry.npmjs.org/fs-extra/-/fs-extra-8.1.0.tgz",
           "integrity": "sha512-yhlQgA6mnOJUKOsRUFsgJdQCvkKhcz8tlZG5HBQfReYZy46OwLcY+Zia0mtdHsOo9y/hP+CxMN0TU9QxoOtG4g==",
-          "dev": true,
           "requires": {
             "graceful-fs": "^4.2.0",
             "jsonfile": "^4.0.0",
```
### Commit 13108e12760abcc1f4d310ac1685901e7ba93c5b
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-11-01T13:33:08-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-2580: Capture all CE output in a logfile
Change-Ids: I788d56bcd7fa89f647be084342421b2d1f90e6f7.
Diff excerpt, `GUI/src/app/shared/services/data.service.ts`:
```diff
@@ -85,6 +87,8 @@ export class DataService {
           if (this.migratingIPVersion) {
             this.pushErrorLog(this.projectDir + '/migration.log', 'error');
             this.migratingIPVersion = false;
+          } else {
+            this.pushErrorLog(this.projectDir + '/interconnect.log', 'error');
           }
           alert(alertString);
         }
```
### Commit d99d886cb31239c71ebaa5cba2b9b12155259e8a
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-10-16T10:39:37-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-3662: Add command stream in brunel console
Change-Ids: I6f56024bb8d775753d5189b93fa2c19d0522628b.
Diff excerpt, `GUI/src/app/test-and-report/logger/logger.component.ts`:
```diff
@@ -83,6 +83,10 @@ export class LoggerComponent implements OnInit, OnDestroy, AfterViewInit {
   userDefinedScriptNames: string[] = [];
   userScriptDir = '';
   private baseUserScriptNames: string[] = [];
+  // Keep only the latest N commands in memory to avoid bloating the textarea.
+  private readonly commandStreamMaxEntries = 500;
+  commandStreamText = '';
+  private commandStreamLines: string[] = [];
   logExpanded = false;
 
   constructor(private cdr: ChangeDetectorRef,
```
Diff excerpt, `brunel/main.js`:
```diff
@@ -1018,42 +1018,77 @@ function endPythonShell(timeoutMs = 5000) {
  *************************************************************/
 let nciCmdLogger = null;
 
+/**
+ * Convert an IPC payload describing a CE API call into the textual form we append to cmds.log.
+ *
+ * The payload looks like: [requestId, 'api', 'mesh.get_mesh_info', 'channel_constraints'].
+ * We drop the first two items (metadata), detect read-only calls (`get_*`) so they do not
+ * toggle `global.hasUnsavedChanges`, and special-case `export_design` to clear the dirty flag
+ * when the export targets the active project file. Commands arrive either as
+ *   - a plain method name plus args (`['get_mesh_info', 'channel_constraints']`), or
+ *   - a preformatted string with inline args (`['mesh.get_mesh_info("channel_constraints")']`).
+ *
+ * The returned string always includes the `ic.` prefix expected by CE scripting, e.g.
+ * `ic.mesh.get_mesh_info("channel_constraints")\n`. When the command is read-only we still
+ * return it so the GUI can show it in the live command stream, but we avoid mutating
+ * the unsaved-changes state for those API calls.
+ */
 function stringifyNciCmd(cmdList) {
-  let cmdListCopy = cmdList.slice(0);
+  const cmdListCopy = cmdList.slice(0);
   cmdListCopy.shift();
   cmdListCopy.shift();
-  // Filter get_* API calls, and manage hasUnsavedChanges
-  if ((cmdListCopy.length >= 1) && (typeof cmdListCopy[0] === 'string') && (cmdListCopy[0].includes('get'))) {
-    return null
-  } else if ((cmdListCopy.length >= 1) && (typeof cmdListCopy[0] === 'string') && (cmdListCopy[0].includes('export_design') && cmdListCopy[1].includes(global.projectName + '.'))) {
-    global.hasUnsavedChanges = false;
-  } else {
-    global.hasUnsavedChanges = true;
-  }
[hunk excerpt ends; remaining lines omitted]
```
### Commit 30a56c92475007426f3404182da48c428a745957
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-11-15T00:30:44-06:00; reachable from selected HEAD: True.
Subject: Console command stream improvements
Change-Ids: I2e3f1f64b6f4cf8e1fce315940fedf5cb33e52e7.
Diff excerpt, `GUI/src/app/test-and-report/logger/logger.component.ts`:
```diff
@@ -88,6 +88,7 @@ export class LoggerComponent implements OnInit, OnDestroy, AfterViewInit {
   // Keep only the latest N commands in memory to avoid bloating the textarea.
   private readonly commandStreamMaxEntries = 500;
   commandStreamText = '';
+  showGetCommands = true;
   private commandStreamLines: string[] = [];
   logExpanded = false;
 
```
### Commit 5547a60f51c4fc6b3a6ea04e004f0ffc53c2701d
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-26T03:35:20-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-4702: fix cmd stream output to be correct Python and stabilize Pixi blockage resize tool cursors
Change-Ids: I8066f551ef2e15b045d3ac684737880590c0c362.
Diff excerpt, `GUI/src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.base.spec.ts`:
```diff
@@ -221,4 +222,26 @@ describe('PixiPhysicalRendererBase instance visibility', () => {
       matching_block: { x: 200, y: 300, width: 100, height: 200 },
     });
   });
+
+  it('defers resize-tool setup until the Pixi content container is ready', () => {
+    const renderer = createRenderer() as any;
+    renderer.canvasInteraction = { checkView: true };
+    renderer.isDestroyed = false;
+    renderer.contentContainer = null;
+    renderer.tool = CanvasTool.resize;
+    renderer.setupPixiResizeTool = jasmine.createSpy('setupPixiResizeTool');
+    renderer.transformEdgeInterfaces = jasmine.createSpy('transformEdgeInterfaces');
+
+    expect(() => renderer.ngAfterViewChecked()).not.toThrow();
+    expect(renderer.setupPixiResizeTool).not.toHaveBeenCalled();
+    expect(renderer.transformEdgeInterfaces).not.toHaveBeenCalled();
+    expect(renderer.canvasInteraction.checkView).toBeTrue();
+
+    renderer.contentContainer = { children: [] };
+    renderer.ngAfterViewChecked();
+
+    expect(renderer.setupPixiResizeTool).toHaveBeenCalledTimes(1);
+    expect(renderer.transformEdgeInterfaces).toHaveBeenCalledTimes(1);
+    expect(renderer.canvasInteraction.checkView).toBeFalse();
+  });
 });
```
Diff excerpt, `GUI/src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts`:
```diff
@@ -74,6 +74,7 @@ describe('Pixi physical renderer pointer interaction tools', () => {
       connectionStartObject: null,
       hoveredEntity: null,
       tooltipContainer: null,
+      resizeHandleHoverCount: 0,
       polygonDrawingActive: false,
       isSelecting: false,
       isPanDragging: false,
```
Diff excerpt, `GUI/src/app/canvas/renderers/pixi/physical/pixi-physical-renderer.interaction.spec.ts`:
```diff
@@ -202,6 +203,23 @@ describe('Pixi physical renderer pointer interaction tools', () => {
     expect(renderer.app.canvas.style.cursor).toBe('grab');
     expect(renderer.getCanvasCursor).toHaveBeenCalledWith(false);
   });
+
+  it('preserves the directional cursor while a resize handle is hovered', () => {
+    const renderer = createRenderer(CanvasTool.resize);
+    renderer.resizeHandleHoverCount = 1;
+    renderer.app.canvas.style.cursor = 'sw-resize';
+
+    handlePixiPhysicalPointerMove.call(renderer, context({
+      type: 'blockage',
+      data: {
+        name: 'block_0',
+      },
+    }));
+
+    expect(renderer.app.canvas.style.cursor).toBe('sw-resize');
+    expect(renderer.getInteractiveCanvasCursor).not.toHaveBeenCalled();
+    expect(renderer.syncPixiCursorStyles).not.toHaveBeenCalled();
+  });
 });
 
 describe('Pixi physical palette drops', () => {
```
### Current source `brunel/python-command.js`
Snapshot: HEAD; SHA-256 `55a933bf905d45dd2378c95309be8392886c47cbafda85051c895c89e99d9051`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 84}.
Introduction/rename-follow candidates: 5547a60f51c4fc6b3a6ea04e004f0ffc53c2701d 2026-08-26T03:35:20-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-4702: fix cmd stream output to be correct Python and stabilize Pixi blockage resize tool cursors.
```text
16: ***************************************************************************/
17: 
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
```
```text
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
```
### Current source `GUI/src/app/shared/services/data.service.ts`
Snapshot: HEAD; SHA-256 `f7b60546cb71c06e2734907c437e825f23b4d83ed345934de3c09a4cfa68f8c9`.
Surviving-line author counts (attribution context only): {'Ana Rescala': 20, 'Dustin Divis': 59, 'dusdiv01': 5, 'Dustin divis': 490, 'Pawan Kakarla': 140, 'Michael Coulter': 509, 'Kelly Alvarez': 165, 'Liza Dayoub': 56, 'Kyan Kornfeld': 11}.
Introduction/rename-follow candidates: b0c68199df9f4397c62159caf048c69b6644d570 2020-06-01T14:30:26-07:00 Kelly Alvarez <kelly.alvarez@arm.com> Initial REST api commit.
```text
24: import * as fs from 'fs';
25: import cloneDeep from 'lodash/cloneDeep';
26: import { showAppConfirmation, showAppNotification } from './app-alert.service';
27: import { bindCeRequest, CeBatchOutcome, CeLockSnapshot, CeMutationRequest, CeParameterInfo, CePolicyDecision, CeSubsectionInfo, checkCeParameterContract, evaluateCeMutation, mutationFailureReason, mutationFailureTitle, serializeCeMutation } from '../ce-policy/ce-policy';
28: import { CE_POLICY_BINDINGS } from '../ce-policy/ce-policy-bindings';
29: import { CePolicyState } from '../ce-policy/ce-policy-state';
30: import { CeInformationError, CeMutationOutcome, CeMutationStep, CeWorkflowOptions, CeWorkflowOutcome, CeWriteQueue, ceMutationOutcome, ceWorkflowNotification, executeCeMutationSteps } from './ce-mutation-outcome';
31: 
32: interface BrowserStaticData {
33:   uiInfo: any;
34:   uiFieldset: any;
35:   scripting: any;
```
```text
41: @Injectable({ providedIn: 'root' })
42: export class DataService {
43:   readonly cePolicy = new CePolicyState();
44:   subsectionRtlLockingEnabled = false;
45:   private apiManifest: Record<string, { mutator: boolean }> | null = null;
46:   private policyRequestId = 0;
47:   private policyProjectEpoch = 0;
48:   private writeQueue = new CeWriteQueue();
49:   private undoCheckpoint: Promise<CeWorkflowOutcome> | undefined;
50:   private publishedPolicy: CeLockSnapshot | null = null;
51:   private readonly policyRefreshIds = new Set<string>();
52:   private policyRefreshQueued = false;
53:   private readonly guardedRequestEpochs = new Map<string, number>();
54:   private readonly refreshedPolicyRequests = new Set<string>();
55:   private readonly workflowRequestIds = new Set<string>();
56:   private readonly workflowDiagnostics = new WeakMap<object, string>();
57:   private readonly informationReadEpochs = new Map<string, number>();
58:   readonly cePolicyChanged = new Subject<CeLockSnapshot>();
59:   readonly ceSubsectionInfoChanged = new Subject<CeSubsectionInfo>();
60: 
61:   get projectGeneration(): number { return this.policyProjectEpoch; }
62:   isCurrentProject(generation: number): boolean { return generation === this.policyProjectEpoch; }
63: 
```
### Current source `brunel/test.py`
Snapshot: HEAD; SHA-256 `2f52830cf26bc9d92d12e53553bfac0bc8cd66da7c011e7268a7deed68255e35`.
Surviving-line author counts (attribution context only): {'Kelly Alvarez': 97, 'Michael Coulter': 78, 'Christopher Alvarez': 107, 'Liza Dayoub': 7, 'Kyan Kornfeld': 15, 'Dustin divis': 17}.
Introduction/rename-follow candidates: 99aa6d04f46d85237271bd6f87da10defa6fb33b 2020-11-09T14:16:39-06:00 Dustin Divis <dustin.divis@arm.com> Brunel CE API integration:.
```text
16: 
17: 
18: class GuiDataWatchState:
19:   def __init__(self, ic, config_path=None):
20:     self.ic = ic
21:     self.methods = []
22:     self.last_signatures = {}
23:     self.config_path = Path(config_path) if config_path else Path(__file__).resolve().parent / "config" / "gui_data_watch.json"
24:     self._load_config()
25:     self._initialize_signatures()
26: 
27:   @staticmethod
28:   def enabled_from_env():
29:     value = os.getenv("BRUNEL_GUI_DATA_WATCH", "")
30:     return value.lower() in ("1", "true", "yes", "on")
31: 
32:   def _load_config(self):
33:     try:
34:       with open(self.config_path, "r") as config_file:
35:         config = json.load(config_file)
36:     except Exception as err:
37:       test_node.log(f"Failed to load GUI data watch config {self.config_path}: {err}")
38:       return
39: 
40:     for method in config.get("methods", []):
41:       if method.get("enabled", False):
42:         self.methods.append(method)
43: 
44:   def _resolve_target(self, target):
45:     resolved = self.ic
46:     for part in target.split("."):
47:       if part.startswith("_"):
48:         raise AttributeError(f"Private target path segment is not allowed: {part}")
49:       resolved = getattr(resolved, part)
```
```text
74:         args = method.get("args", [])
75:         kwargs = method.get("payload_kwargs", method.get("kwargs", {}))
76:         payload = payload_method(*args, **kwargs)
77:         if payload is not None:
78:           test_node.emit({"id": method["response_id"], "res": payload})
79:         self.last_signatures[key] = current_signature
80:       except Exception as err:
81:         test_node.log(f"Failed to refresh GUI data watch method {key}: {err}")
82: 
83: 
84: class WrapperCE:
85:   @staticmethod
```
```text
90:         product_info = yaml.safe_load(product_info_file)
91:     except Exception as err:
92:       test_node.log(f"Failed to load product info for Build Lite DRC license state: {err}")
93:       return None
94: 
95:     return (
96:       product_info.get("PRODUCT_CONFIG", {})
97:       .get("cmn", {})
98:       .get("BUILD_LITE_DRC_LICENSES", {})
99:       .get("ENV_VAR")
100:     )
101: 
```

## exports

### Commit 23f8742b677fd300b070a0209fc83cf6a7728c8b
Author: Michael Coulter <michael.coulter@arm.com>; author date 2023-11-15T14:56:57-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-1288: Export SVG of Logical/Physical canvas
Change-Ids: If4713155ed8eaa46b497b849b612c8d617272eab.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -91,6 +91,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
   calYOffset: number;
   calp0p3XOffset: number;
   calp1p3YOffset: number;
+  textFontFamily: string;
   // portStrings: any = ["p0", "p1", "p2", "p3"];
   // selection box/tool variables
   cursorCoorsElement: HTMLElement = null;
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -164,6 +165,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
     this.calYOffset = this.uiInfo.CMN.calYOffset;
     this.calp0p3XOffset = this.uiInfo.CMN.calp0p3XOffset;
     this.calp1p3YOffset = this.uiInfo.CMN.calp1p3YOffset;
+    this.textFontFamily = this.uiInfo.CMN.textFontFamily;
 
     this.canvasGuiDataService.viewBoxChanged.pipe(takeUntil(this.unsubscribe$)).subscribe(viewBox => {
       this.viewBox = viewBox;
```
Diff excerpt, `GUI/src/app/canvas/shared/services/canvas-static-data.service.ts`:
```diff
@@ -188,7 +188,7 @@ export class CanvasStaticDataService {
       });
     }
     Object.keys(searchObj).forEach(key => {
-      if (!(key === 'display' || key === 'desc' || key === 'components' || key === 'crosspoints' || key === 'links' || key === 'notFound')) {
+      if (!(key === 'display' || key === 'desc' || key === 'components' || key === 'crosspoints' || key === 'links' || key === 'textFontFamily' || key === 'notFound')) {
         this.getUiComponent(searchObj[key]);
       }
     });
```
### Commit 1a1ffed4dafa2ab389ec95a52eea19567ef1f7cd
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-09-19T12:12:32-05:00; reachable from selected HEAD: True.
Subject: export dialog modal improvements
Change-Ids: Icbdfd0fdd53f6a6fc8ce578e687d48074e652069.
Diff excerpt, `GUI/src/app/status-bar/export-dialog/export-dialog.component.ts`:
```diff
@@ -42,6 +42,8 @@ export class ExportDialogComponent implements OnInit, OnDestroy {
   fileFormat = '.yaml';
   fileTypes = ['.yaml (NoC / CMN IYML)'];
   respSub: Subscription;
+  exportFilePath: string = '';
+  formSub: Subscription;
   projectForm: UntypedFormGroup;
   ipcRenderer: any;
   isDialogOpen = false;
```
Diff excerpt, `GUI/src/app/status-bar/export-dialog/export-dialog.component.ts`:
```diff
@@ -113,23 +115,23 @@ export class ExportDialogComponent implements OnInit, OnDestroy {
     //   });
 
     this.cdr.detectChanges();
+    this.formSub = this.projectForm.valueChanges.subscribe((formValue) => this.updateExportFilePath(formValue?.exportName, formValue?.fileType));
+    this.updateExportFilePath();
   }
 
   ngOnDestroy(): void {
     if (this.respSub) {
       this.respSub.unsubscribe();
     }
+    if (this.formSub) {
+      this.formSub.unsubscribe();
+    }
   }
 
   refresh(): void {
     this.cdr.detectChanges();
   }
 
-  getFilePath() {
-    if (this.dirPath && this.projectForm.value.exportName)
-      return path.join(this.dirPath, this.projectForm.value.exportName + this.fileFormat);
-  }
-
   select(event: Event): void {
     event.preventDefault();
     if (this.isDialogOpen) return;
```
Diff excerpt, `GUI/src/app/status-bar/export-dialog/export-dialog.component.ts`:
```diff
@@ -140,6 +142,7 @@ export class ExportDialogComponent implements OnInit, OnDestroy {
         if (folderPath) {
           this.dirPath = folderPath;
           this.cdr.detectChanges();
+          this.updateExportFilePath();
         }
         this.isDialogOpen = false;
       }).catch(() => {
```
### Current source `GUI/src/app/status-bar/export-dialog/export-dialog.component.ts`
Snapshot: HEAD; SHA-256 `52dd7c04004cbaf06d34220aad409e33cfc1e8c540c70d1fcc57f027089200ca`.
Surviving-line author counts (attribution context only): {'Ana Rescala': 17, 'Pawan Kakarla': 107, 'Michael Coulter': 326, 'Dustin Divis': 49, 'dusdiv01': 2, 'Kelly Alvarez': 42}.
Introduction/rename-follow candidates: db6823b0c4c757b9a21166e5385415aff273a2a0 2020-12-01T15:20:03-06:00 Dustin Divis <dustin.divis@arm.com> [GUI/brunel] Status Bar: Phase 1 complete.
```text
27: import { UntypedFormControl, UntypedFormGroup, Validators } from '@angular/forms';
28: import { GlobalService } from 'src/app/shared/services/global.service';
29: import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
30: import { CanvasViewStateService } from 'src/app/canvas/core/services/canvas-view-state.service';
31: import { GuidedFlowPolicyService } from 'src/app/shared/services/guided-flow-policy.service';
32: import { supportsUpf, UpfService } from 'src/app/collaterals/upf.service';
33: 
34: const PYML_FILE_TYPE = '.yaml (NoC / PYML)';
35: 
36: export interface ExportDialogData {
37:   mode?: 'export' | 'checkpoint';
38: }
39: 
40: @Component({
41:     selector: 'app-export-dialog',
42:     templateUrl: './export-dialog.component.html',
43:     styleUrls: ['./export-dialog.component.css'],
44:     standalone: false
45: })
46: export class ExportDialogComponent implements OnInit, OnDestroy {
47:   @Output() closeModal = new EventEmitter<boolean>();
48:   message = 'Choose a name, format and location';
49:   dirPath: string;
50:   filePathStart = '';
```

## docs

### Commit 31a0f63e2ae554ce1afb122a2886d345c1302306
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-09-26T15:11:52-05:00; reachable from selected HEAD: True.
Subject: This change introduces and integrates a comprehensive orchestration framework under
Change-Ids: Idfbd8e2ceeff965401377b0cadf3082d1e00abf4.
Diff excerpt, `GUI/agent/app-docs-data.json`:
```diff
@@ -0,0 +1,292647 @@
+{
+  "app-routing.module.ts": {
+    "path": "app-routing.module.ts",
+    "isSpec": false,
+    "imports": [
+      {
+        "moduleSpecifier": "@angular/core",
+        "defaultBinding": null,
+        "namedBindings": [
+          {
+            "name": "NgModule",
+            "propertyName": null
+          }
+        ],
+        "namespaceImport": null,
+        "isTypeOnly": false,
+        "resolved": null
+      },
+      {
+        "moduleSpecifier": "@angular/router",
+        "defaultBinding": null,
+        "namedBindings": [
+          {
+            "name": "Routes",
+            "propertyName": null
+          },
+          {
+            "name": "RouterModule",
+            "propertyName": null
+          }
+        ],
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/agent/collect-app-docs-data.js`:
```diff
@@ -0,0 +1,388 @@
+#!/usr/bin/env node
+/*
+ * Collects static metadata for all TypeScript files under src/app.
+ * The output (by default agent/app-docs-data.json) is consumed by
+ * render-app-docs.py to produce per-directory documentation.
+ */
+
+const fs = require('fs');
+const path = require('path');
+const ts = require('typescript');
+
+const DEFAULT_APP_ROOT = path.resolve(__dirname, '../src/app');
+const DEFAULT_OUTPUT = path.resolve(__dirname, 'app-docs-data.json');
+const IGNORE_DIRS = new Set(['.git', '.angular', '.idea', '.vscode', 'build', 'dist', '__pycache__']);
+const SUPPORTED_EXTS = new Set(['.ts']);
+
+function parseArgs() {
+  const args = process.argv.slice(2);
+  const options = { appRoot: DEFAULT_APP_ROOT, output: DEFAULT_OUTPUT };
+  for (let i = 0; i < args.length; i++) {
+    const arg = args[i];
+    if ((arg === '--app-root' || arg === '-r') && args[i + 1]) {
+      options.appRoot = path.resolve(args[++i]);
+    } else if ((arg === '--output' || arg === '-o') && args[i + 1]) {
+      options.output = path.resolve(args[++i]);
+    } else if (arg === '--help' || arg === '-h') {
+      printHelp();
+      process.exit(0);
+    } else {
+      console.warn(`Unrecognised argument: ${arg}`);
+      printHelp();
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/agent/config.yaml`:
```diff
@@ -0,0 +1,23 @@
+runtime:
+  language: python
+  bootloader: runtime/bootloader.py
+  context_index: runtime/context_index.py
+  action_planner: runtime/action_planner.py
+  tools_package: runtime.tools
+
+paths:
+  repo_root: ..
+  app_source: ../src/app
+  overrides_root: manual-overrides
+  context_index: context/index.json
+
+workflows:
+  implement_task: workflows/implement_task.md
+  update_docs: workflows/update_docs.md
+  add_tests: workflows/add_tests.md
+
+policies: policies.md
+prompts:
+  system: prompts/system.md
+  code_breaker: prompts/code_breaker.md
+  doc_guard: prompts/doc_guard.md
```
### Commit 4244a7676653076be51535e15e0f2e617c38edac
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-09-29T16:32:45-05:00; reachable from selected HEAD: True.
Subject: Move nav bar to menu-bar. Extended the agent’s navigation awareness: added menu-bar keywords so the planner now picks up menu-bar.component.{ts,html,css} alongside the existing nav artifacts, and registered the menu-bar doc as a tracked nav resource (GUI/agent/runtime/action_planner.py, GUI/agent/runtime/bootloader.py). Rebuilt the agent context index so downstream tooling immediately sees the new assets and guidance (GUI/agent/context/index.json).
Change-Ids: Ida8615d1f64ce9760ca767074c0be9b9cae4b3e5.
Diff excerpt, `GUI/src/app/app.component.ts`:
```diff
@@ -15,7 +15,7 @@
 *
 ***************************************************************************/
 
-import { AfterViewInit, ChangeDetectorRef, Component, ElementRef, HostListener, NgZone, OnDestroy, OnInit, QueryList, ViewChild, ViewChildren } from '@angular/core';
+import { ChangeDetectorRef, Component, HostListener, NgZone, OnDestroy, OnInit } from '@angular/core';
 import { NavigationEnd, Router } from '@angular/router';
 
 import { Subscription, Subject } from 'rxjs';
```
Diff excerpt, `GUI/src/app/app.component.ts`:
```diff
@@ -36,16 +36,14 @@ import { StatusBarService } from './status-bar/status-bar.service';
 import { MenuService } from './menu-bar/menu.service';
 import { TestAndReportServiceApi } from './test-and-report/test-report-service-api';
 import { SynthesisToggleService } from './synthesis-constraints/synthesis-toggle-service';
+import { buildTabState } from './shared/services/nav-bar.utils';
 
 @Component({
   selector: 'app-root',
   templateUrl: './app.component.html',
   styleUrls: ['./app.component.css']
 })
-export class AppComponent implements OnInit, AfterViewInit, OnDestroy {
-  @ViewChild('docsLink', { static: false }) docsLink!: ElementRef;
-  @ViewChild('primaryNavWrapper', { static: true, read: ElementRef }) primaryNavWrapper!: ElementRef;
-  @ViewChildren('primaryTabRefs', { read: ElementRef }) primaryTabRefs!: QueryList<ElementRef>;
+export class AppComponent implements OnInit, OnDestroy {
   brunelCEOutput = '';
   brunelCECmd = '';
   cmdHistory = [''];
```
Diff excerpt, `GUI/src/app/menu-bar/menu-bar.component.spec.ts`:
```diff
@@ -1,6 +1,86 @@
 import { ComponentFixture, TestBed } from '@angular/core/testing';
+import { RouterTestingModule } from '@angular/router/testing';
+import { MatIconModule } from '@angular/material/icon';
+import { Subject, of } from 'rxjs';
 
 import { MenuBarComponent } from './menu-bar.component';
+import { MenuService } from './menu.service';
+import { GlobalService } from '../shared/services/global.service';
+import { TestAndReportServiceApi } from '../test-and-report/test-report-service-api';
+import { ProjectService } from '../project/project.service';
+import { DataService } from '../shared/services/data.service';
+import { StatusBarService } from '../status-bar/status-bar.service';
+import { ModalService } from '../shared/services/modal.service';
+import { NavigationService } from '../shared/services/navigation.service';
+import { DomainsService } from '../domains/domains.service';
+import { InterfaceService } from '../interfaces/interface.service';
+import { PathService } from '../paths/paths.service';
+import { BasicTrafficService } from '../basic-traffic/basic-traffic.service';
+import { TrafficConcurrentService } from '../traffic/traffic-concurrent.service';
+import { MemoryMapService } from '../memory-maps/memory-map.service';
+import { CanvasPhysicalService } from '../canvas/canvas-physical.service';
+
+class MenuServiceStub {
+  triggerAction = jasmine.createSpy('triggerAction');
+  navigate = jasmine.createSpy('navigate');
+}
+
+class GlobalServiceStub {
+  isCmnIp() { return false; }
+}
+
[hunk excerpt ends; remaining lines omitted]
```
### Commit fd0f07d1913dc6628280755f280a3ab6b62952d9
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-10-08T15:25:59-05:00; reachable from selected HEAD: True.
Subject: Create `GUI/agent/lessons-learned` and integrate it into the GUI agent context framework and runtime workflows
Change-Ids: I4e813828723793c51b86fe3138ba428deca17d42.
Diff excerpt, `GUI/agent/lessons-learned/build_index.py`:
```diff
@@ -0,0 +1,74 @@
+#!/usr/bin/env python3
+"""
+Regenerates the lessons catalog in index.md by scanning per-year lesson files.
+
+Usage:
+    python build_index.py
+"""
+
+from __future__ import annotations
+
+import re
+from pathlib import Path
+
+ROOT = Path(__file__).parent
+INDEX_PATH = ROOT / "index.md"
+TOC_BEGIN = "<!-- BEGIN LESSONS-TOC -->"
+TOC_END = "<!-- END LESSONS-TOC -->"
+HEADING_PATTERN = re.compile(r"#\s+(?P<title>.*?)\s+—\s+(?P<date>\d{4}-\d{2}-\d{2})")
+
+
+def collect_lessons() -> dict[str, list[tuple[str, str, Path]]]:
+    lessons: dict[str, list[tuple[str, str, Path]]] = {}
+    for year_dir in sorted(
+        [p for p in ROOT.iterdir() if p.is_dir() and p.name.isdigit()],
+        key=lambda p: p.name,
+    ):
+        entries: list[tuple[str, str, Path]] = []
+        for lesson_file in sorted(year_dir.glob("*.md")):
+            if lesson_file.name == "README.md":
+                continue
+            with lesson_file.open("r", encoding="utf-8") as fh:
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/agent/runtime/action_planner.py`:
```diff
@@ -212,6 +216,7 @@ def _infer_docs(segment: str, index: ContextIndex) -> List[str]:
         gt_doc = Path("src/app/canvas/canvas-sidebar/property-editor/canvas-instance-properties/canvas-instance-properties.md").resolve()
         if gt_doc.exists():
             notes.append(str(gt_doc))
+    notes.extend(_lesson_references(segment, index))
     return sorted(set(notes))
 
 
```
Diff excerpt, `GUI/agent/runtime/action_planner.py`:
```diff
@@ -292,3 +297,17 @@ def _mentions_drc(segment: str) -> bool:
 def _mentions_gt(segment: str) -> bool:
     lower = segment.lower()
     return any(keyword in lower for keyword in GT_SPECIFIC_KEYWORDS)
+
+
+def _lesson_references(segment: str, index: ContextIndex) -> List[str]:
+    lower = segment.lower()
+    references: List[str] = []
+    if any(keyword in lower for keyword in LESSONS_SCROLL_HINTS):
+        references.extend(index.lessons.get("lessons_index", []))
+    for keyword, slug in LESSON_SLUG_HINTS.items():
+        if keyword in lower:
+            for path in index.lessons.get("summaries", []):
+                if slug in Path(path).stem:
+                    references.append(path)
+                    break
+    return references
```
### Current source `GUI/agent/collect-app-docs-data.js`
Snapshot: HEAD; SHA-256 `df86165deedf5fbfd7b710782a59e5d8ee72c7f098df91710af6ab8fc7e9d652`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 388}.
Introduction/rename-follow candidates: 31a0f63e2ae554ce1afb122a2886d345c1302306 2025-09-26T15:11:52-05:00 Michael Coulter <michael.coulter@arm.com> This change introduces and integrates a comprehensive orchestration framework under `GUI/agent` and expands the automated documentation system for the GUI source tree. Together, these updates provide a structured foundation for planning, analysis, documentation enforcement, and curated narratives..
```text
1: #!/usr/bin/env node
2: /*
3:  * Collects static metadata for all TypeScript files under src/app.
4:  * The output (by default agent/app-docs-data.json) is consumed by
5:  * render-app-docs.py to produce per-directory documentation.
6:  */
7: 
8: const fs = require('fs');
9: const path = require('path');
10: const ts = require('typescript');
11: 
12: const DEFAULT_APP_ROOT = path.resolve(__dirname, '../src/app');
13: const DEFAULT_OUTPUT = path.resolve(__dirname, 'app-docs-data.json');
14: const IGNORE_DIRS = new Set(['.git', '.angular', '.idea', '.vscode', 'build', 'dist', '__pycache__']);
15: const SUPPORTED_EXTS = new Set(['.ts']);
16: 
17: function parseArgs() {
18:   const args = process.argv.slice(2);
```
```text
58:   return results;
59: }
60: 
61: function getDecorators(node, sourceFile) {
62:   if (!ts.canHaveDecorators(node)) return [];
63:   const decorators = ts.getDecorators(node) || [];
64:   return decorators.map((dec) => {
65:     if (ts.isCallExpression(dec.expression)) {
66:       const expr = dec.expression.expression;
67:       const name = expr.getText(sourceFile);
68:       const args = dec.expression.arguments.map((arg) => literalToValue(arg, sourceFile));
69:       return { name, args };
70:     }
71:     return { name: dec.expression.getText(sourceFile), args: [] };
```
### Current source `GUI/agent/render-app-docs.py`
Snapshot: HEAD; SHA-256 `26dc4535896b0714d857f66db706e9f2b7e77480c4761769bf0e824378603ece`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 829}.
Introduction/rename-follow candidates: 31a0f63e2ae554ce1afb122a2886d345c1302306 2025-09-26T15:11:52-05:00 Michael Coulter <michael.coulter@arm.com> This change introduces and integrates a comprehensive orchestration framework under `GUI/agent` and expands the automated documentation system for the GUI source tree. Together, these updates provide a structured foundation for planning, analysis, documentation enforcement, and curated narratives..
```text
1: #!/usr/bin/env python3
2: """Generate <folder-name>.md documentation under src/app using precomputed metadata."""
3: 
4: from __future__ import annotations
5: 
6: import argparse
7: import datetime
8: import json
9: import os
10: import re
11: from collections import defaultdict
12: from pathlib import Path
13: from typing import Any, Dict, Iterable, List
14: import subprocess
15: 
16: IGNORE_DIRS = {'.git', '.angular', '.idea', '.vscode', 'build', 'dist', '__pycache__'}
17: ALWAYS_INCLUDE_DIRS = {'build'}
```
### Current source `GUI/agent/runtime/tools/doc_guard.py`
Snapshot: HEAD; SHA-256 `437ead9147286293d8cb95b5866ba7fb46ea9736c12c2fc2b6a9292ddca93ee8`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 15}.
Introduction/rename-follow candidates: 31a0f63e2ae554ce1afb122a2886d345c1302306 2025-09-26T15:11:52-05:00 Michael Coulter <michael.coulter@arm.com> This change introduces and integrates a comprehensive orchestration framework under `GUI/agent` and expands the automated documentation system for the GUI source tree. Together, these updates provide a structured foundation for planning, analysis, documentation enforcement, and curated narratives..
```text
3: Phase 6 will populate these utilities with real comparison logic.
4: """
5: 
6: from __future__ import annotations
7: 
8: from pathlib import Path
9: from typing import List
10: 
11: 
12: def check_parity(changed_files: List[Path]) -> List[str]:
13:     """Return a list of missing documentation updates (empty for now)."""
14: 
15:     return []
```

## ai-planning

### Commit 0ab6800995f1cbf36129653ccea400b713c8d8ae
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-04-21T00:28:21-05:00; reachable from selected HEAD: True.
Subject: IA MCP capability pack initial implementation
Change-Ids: I0959221a93c0ed406fc3a86270ad41ea9eee3daf.
Commit message:
```text
IA MCP capability pack initial implementation

Change-Id: I0959221a93c0ed406fc3a86270ad41ea9eee3daf
```
Diff excerpt, `ai/ia-mcp-pack/golden_tests/requirements_to_full_clean_config/nitwain_r1p0_owo_blank.yaml`:
```diff
@@ -0,0 +1,379 @@
+case_id: requirements_to_full_clean_config/nitwain_r1p0_owo_blank
+prompt: |
+  Using ia-mcp, create a brand-new Interconnect Architect configuration for nitwain_r1p0 from a blank session. Do not clone or import an existing design. Ground the work in ideas docs/examples first. Build exactly two CCGs, ccg_0 and ccg_1, each with an OWO-enabled DSNI; exactly two ASNIs, asni_plain and asni_owo; and exactly two AMNIs, amni_plain and amni_owo. Only the _owo ASNI/AMNI pair may be OWO-enabled. Make the device routes as fully connected as the canonical gold case allows, minimize the microarchitecture, export both a final .iyml and a reproducible Python config script, and prove HLS, microarchitecture, and final DRC are all clean.
+product_version: nitwain_r1p0
+project_name: gold_nitwain_r1p0_owo_blank
+session_id_prefix: gold-nitwain-r1p0-owo-blank
+grounding:
+  docs_query: adaptor/owoStream
+  examples_query: ccg_0_dsni_if_0
+  limit: 1
+forbidden_tools:
+  - ia.ce.session_clone_example
+  - ia.ce.session_open_file
+  - ia.ce.io_import_yaml
+checkpoints:
+  initial: blank_start
+  post_hls: hls_clean
+outputs:
+  script_filename: gold_nitwain_r1p0_owo_blank.py
+  iyml_filename: gold_nitwain_r1p0_owo_blank.iyml
+  replay_iyml_filename: gold_nitwain_r1p0_owo_blank_replayed.iyml
+  replay_workspace_dirname: replay_workspace
+phases:
+  hls:
+    validation_plan:
+      - Run ia.ce.drc_check_hls and require clean status.
+      - Export the final iyml and python script after final validation.
+    operations:
+      - method: add_domains_hierarchy
+        kwargs:
+          clk_domain_name: clk0
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/build_tools.py`:
```diff
@@ -0,0 +1,69 @@
+"""Build handlers."""
+
+from __future__ import annotations
+
+from typing import Any
+
+from sysip_shared_ai_mcp.errors import ValidationArtifactUnavailableError
+from sysip_shared_ai_mcp.models import ValidationRecord
+
+from .ce_session_adapter import CESessionAdapter
+from .schemas.ce import BuildRunRequest
+from .schemas.common import GenericStatusResult
+
+
+def _adapter(runtime_context: Any) -> CESessionAdapter:
+    adapter = getattr(runtime_context, "_ia_ce_adapter", None)
+    if adapter is None:
+        adapter = CESessionAdapter(runtime_context)
+        setattr(runtime_context, "_ia_ce_adapter", adapter)
+    return adapter
+
+
+def handle_build_run(runtime_context: Any, request: BuildRunRequest) -> GenericStatusResult:
+    adapter = _adapter(runtime_context)
+    session_metadata = adapter.get_session_metadata(request.session_id)
+    if not session_metadata.get("checkpoints"):
+        raise ValidationArtifactUnavailableError(
+            "ia.ce.build_run requires an existing checkpoint created before the build action."
+        )
+    if not request.validation_plan:
+        raise ValidationArtifactUnavailableError(
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/ce_catalog.py`:
```diff
@@ -0,0 +1,73 @@
+"""Helpers for mapping curated IA tools back to checked-in CE API inventory."""
+
+from __future__ import annotations
+
+from functools import lru_cache
+from pathlib import Path
+from typing import Any, Iterable
+
+from sysip_shared_ai_mcp.models import SourceRef
+
+from .compatibility_manifest import build_api_inventory_index
+from .repo_resolver import inspect_git_state
+
+
+@lru_cache(maxsize=None)
+def _ideas_repo_state(ideas_root: str) -> dict[str, Any]:
+    return inspect_git_state("ideas", ideas_root, product_family="ia", allow_dirty=True)
+
+
+def lookup_ce_apis(ideas_root: str, api_names: Iterable[str]) -> list[dict[str, Any]]:
+    api_index = build_api_inventory_index(ideas_root)
+    entries: list[dict[str, Any]] = []
+    seen: set[str] = set()
+    for api_name in api_names:
+        if api_name in seen:
+            continue
+        seen.add(api_name)
+        entry = api_index.get(api_name)
+        if entry is not None:
+            entries.append(entry)
+    return entries
[hunk excerpt ends; remaining lines omitted]
```
### Commit 7319af553f5601a0a4365cd952f08c91fba3dd6f
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-28T09:50:21-05:00; reachable from selected HEAD: True.
Subject: Harden IA MCP transactional execution
Change-Ids: I0ad5b0540af448c8ff51c4372920f6bf701a29d7.
Commit message:
```text
Harden IA MCP transactional execution

Change-Id: I0ad5b0540af448c8ff51c4372920f6bf701a29d7
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -206,6 +224,12 @@
         "state_dependencies": [],
         "status": "pending_live_capability_snapshot"
       },
+      "callability": {
+        "authority": "pending_mcp_registration_review",
+        "blocker": null,
+        "callable": null,
+        "status": "unassessed"
+      },
       "declaring_class": "InterconnectBuild",
       "disposition": "not_implemented",
       "doc_summary": "Forcefully set build-environment-related attributes without performing validation. Intended for internal flows that need to restore a previously saved state (for example, after running a temporary build environment).",
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -718,7 +792,13 @@
         "path": "CE/ideas/api/interconnect_config.py"
       },
       "support": {
-        "evidence": {},
+        "evidence": {
+          "result_interpretation": {
+            "authority": "review",
+            "reference": "ai/ia-mcp-pack/src/ia_mcp_pack/execution_contracts.py; ai/ia-mcp-pack/tests/test_execution_contracts.py",
+            "status": "verified"
+          }
+        },
         "fully_supported": false,
         "stage": "mapped"
       }
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -923,7 +1035,13 @@
         "path": "CE/ideas/api/interconnect_config.py"
       },
       "support": {
-        "evidence": {},
+        "evidence": {
+          "result_interpretation": {
+            "authority": "review",
+            "reference": "ai/ia-mcp-pack/src/ia_mcp_pack/execution_contracts.py; ai/ia-mcp-pack/tests/test_execution_contracts.py",
+            "status": "verified"
+          }
+        },
         "fully_supported": false,
         "stage": "mapped"
       }
```
### Commit 7ba22c61f75afb5228694245af4de75f00b5fb78
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-29T19:02:12-05:00; reachable from selected HEAD: True.
Subject: Bind IA MCP capabilities to live CE
Change-Ids: I55010cb9757844a390b0389483c1142970cf6f85.
Commit message:
```text
Bind IA MCP capabilities to live CE

Change-Id: I55010cb9757844a390b0389483c1142970cf6f85
```
Diff excerpt, `ai/acceptance/direct/direct_nci.py`:
```diff
@@ -8,11 +8,19 @@ import asyncio
 import json
 import os
 from pathlib import Path
+import sys
 
 from mcp import ClientSession, StdioServerParameters
 from mcp.client.stdio import stdio_client
 
 
+ACCEPTANCE_ROOT = Path(__file__).resolve().parents[1]
+if str(ACCEPTANCE_ROOT) not in sys.path:
+    sys.path.insert(0, str(ACCEPTANCE_ROOT))
+
+from planning_contract import validate_advisory_planning_contract
+
+
 def model_data(value):
     return value.model_dump(mode="json") if hasattr(value, "model_dump") else value
 
```
Diff excerpt, `ai/acceptance/direct/direct_nci.py`:
```diff
@@ -82,10 +90,6 @@ async def run(server: str, scenario: str) -> dict:
                         "candidate_products": ["towernci_r1p3"],
                     },
                 )
-                require(
-                    recommendation["resolved_product"] == "towernci_r1p3",
-                    f"unexpected product recommendation: {recommendation['resolved_product']!r}",
-                )
                 plan = await call(
                     "ia.ce.config_plan",
                     {
```
Diff excerpt, `ai/acceptance/direct/direct_nci.py`:
```diff
@@ -96,7 +100,12 @@ async def run(server: str, scenario: str) -> dict:
                         "artifact_stem": f"direct-matrix/{scenario}",
                     },
                 )
-                require(plan["ready"] is True, f"configuration plan is not ready: {plan}")
+                validate_advisory_planning_contract(
+                    recommendation,
+                    plan,
+                    expected_product="towernci_r1p3",
+                    requirements=requirements,
+                )
                 created = await call(
                     "ia.ce.session_create",
                     {"product_version": "towernci_r1p3", "project_name": project_name},
```
### Commit 67b621ef6f366c852550ef07ee1122d336f2985e
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-30T00:56:14-05:00; reachable from selected HEAD: True.
Subject: Compile typed IA MCP design plans
Change-Ids: Ia28d9ffa2508bd4712a3c793e983a2d4de601243.
Commit message:
```text
Compile typed IA MCP design plans

Change-Id: Ia28d9ffa2508bd4712a3c793e983a2d4de601243
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/ce_session_adapter.py`:
```diff
@@ -1479,6 +1479,14 @@ class CESessionAdapter:
 
     def _unregister_session(self, session_id: str) -> None:
         self._capability_observations.pop(session_id, None)
+        plan_registry = getattr(
+            self.runtime_context,
+            "_ia_server_plan_registry",
+            None,
+        )
+        discard_plans = getattr(plan_registry, "discard_session", None)
+        if callable(discard_plans):
+            discard_plans(session_id)
         remove = getattr(self.runtime_context.session_registry, "remove", None)
         if callable(remove):
             remove(session_id)
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/config_tools.py`:
```diff
@@ -433,7 +434,10 @@ def _policy_rejection_metadata(
     return metadata
 
 
-def handle_config_recommend_changes(runtime_context: Any, request: ConfigRecommendChangesRequest) -> RecommendationResult:
+def _handle_legacy_config_recommend_changes(
+    runtime_context: Any,
+    request: ConfigRecommendChangesRequest,
+) -> RecommendationResult:
     normalized_operations: list[tuple[int, dict[str, Any]]] = []
     validations: list[ValidationRecord] = []
     for index, raw_operation in enumerate(request.operations):
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/config_tools.py`:
```diff
@@ -637,6 +641,148 @@ def handle_config_recommend_changes(runtime_context: Any, request: ConfigRecomme
     )
 
 
+def _handle_intent_recommend_changes(
+    runtime_context: Any,
+    request: ConfigRecommendChangesRequest,
+) -> RecommendationResult:
+    """Derive advisory operations only from a server-owned compiled plan."""
+
+    assert request.intent is not None
+    from .planning_tools import handle_config_plan
+
+    plan_result = handle_config_plan(
+        runtime_context,
+        ConfigPlanRequest(
+            session_id=request.session_id,
+            intent=request.intent,
+        ),
+    )
+    plan = None
+    resolution_error: str | None = None
+    if plan_result.plan_stored and plan_result.plan_id is not None:
+        try:
+            adapter = _adapter(runtime_context)
+            with adapter.idle_session_action(
+                request.session_id,
+                "resolve a server-owned intent plan for recommendation",
+            ):
+                snapshot, _cache = adapter.capability_snapshot(request.session_id)
+                from .planning_state import build_planning_state
+                from .plan_registry import server_plan_registry
[hunk excerpt ends; remaining lines omitted]
```
### Commit ad62f9ccb1382a153997636f24a9e6cd35cb096d
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-31T21:33:31-05:00; reachable from selected HEAD: True.
Subject: Prove IA MCP NCI construction vertical
Change-Ids: Ie3af23ab836d1a3f108b7544121918283a8e4bd9.
Commit message:
```text
Prove IA MCP NCI construction vertical

Change-Id: Ie3af23ab836d1a3f108b7544121918283a8e4bd9
```
Diff excerpt, `ai/acceptance/run_codex_scenario.py`:
```diff
@@ -688,6 +688,10 @@ def validate_codex_result(
     ):
         if tools.count(tool) != 1:
             raise AcceptanceError(f"Codex must call {tool} exactly once; observed {tools.count(tool)}")
+    if tools.count("ia.ce.config_execute_plan") < 1:
+        raise AcceptanceError(
+            "Codex must execute at least one exact server-owned compiled-plan phase"
+        )
     if scenario["family"] == "nci":
         for tool in ("ia.ce.drc_check_hls", "ia.ce.drc_check_microarchitecture"):
             if tools.count(tool) != 1:
```
Diff excerpt, `ai/acceptance/run_codex_scenario.py`:
```diff
@@ -761,12 +765,13 @@ def run_acceptance(args: argparse.Namespace, scenario: dict[str, Any]) -> dict[s
     if direct_only and getattr(args, "supplemental_reference", None):
         raise AcceptanceError(
             "supplemental-context acceptance is deferred with blank-context Codex acceptance "
-            "until Milestone 4; --direct-only does not consult supplemental context"
+            "until Milestone 12 broad-domain acceptance; --direct-only does not consult supplemental context"
         )
     if not direct_only:
         raise AcceptanceError(
-            "blank-context Codex acceptance is deferred until Milestone 4 provides a live-capability-validated "
-            "typed executable plan; use --direct-only for the historical deterministic regression flow"
+            "the six-scenario blank-context Codex suite is deferred until Milestone 12 expands compiler/domain "
+            "coverage; Milestone 5 typed plan execution remains available for compiler-reachable verticals, "
+            "and --direct-only runs the historical deterministic regression flow"
         )
     validate_cluster_host()
     run_root = validate_owned_root(args.run_root)
```
Diff excerpt, `ai/acceptance/run_codex_scenario.py`:
```diff
@@ -901,7 +906,7 @@ def run_acceptance(args: argparse.Namespace, scenario: dict[str, Any]) -> dict[s
             "lsf_job_id": os.environ["LSB_JOBID"],
             "acceptance_scope": "historical_deterministic_direct_regression",
             "execution_authorized_by_planning": False,
-            "codex_acceptance": "deferred_until_live_typed_planning",
+            "codex_acceptance": "deferred_until_m12_broad_domain_expansion",
             "output_root": str(output_root),
             "direct_result": str(direct_output),
             "planning_result": str(planning_output),
```
### Commit f1867d608f03207757d61e06a5abe6a35b0ac432
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-01T03:21:39-05:00; reachable from selected HEAD: True.
Subject: Prove IA MCP CMN construction vertical
Change-Ids: Ibb047f360c64610a44900cd5991f83741c005f98.
Commit message:
```text
Prove IA MCP CMN construction vertical

Change-Id: Ibb047f360c64610a44900cd5991f83741c005f98
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -8927,7 +8927,7 @@
       "name": "get_device_group_members",
       "provider_requirements": [],
       "rationale": [
-        "IA MCP exposes bounded CMN mesh, group, device, and credit state."
+        "IA MCP exposes bounded CMN mesh, group, device, and native MCS element state."
       ],
       "return_contract": {
         "annotation": "~dict_or_none",
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -15315,10 +15317,29 @@
         "status": "unassessed"
       },
       "declaring_class": "InterconnectConfig",
-      "disposition": "not_implemented",
+      "disposition": "read_only_discovery",
       "doc_summary": "Return MCS units in a native MCS wrap.",
-      "evidence": [],
-      "exposure_routes": [],
+      "evidence": [
+        "ai/ia-mcp-pack/src/ia_mcp_pack/ce_worker.py",
+        "ai/ia-mcp-pack/src/ia_mcp_pack/semantic_state.py"
+      ],
+      "exposure_routes": [
+        {
+          "id": "ia.ce.config_apply_changes",
+          "kind": "mcp_tool",
+          "relationship": "captures_transaction_semantic_pre_and_postconditions"
+        },
+        {
+          "id": "ia.ce.config_execute_plan",
+          "kind": "mcp_tool",
+          "relationship": "captures_plan_semantic_pre_and_postconditions"
+        },
+        {
+          "id": "ia_mcp_pack.ce_worker.WorkerSession.handle[command=get_semantic_snapshot]",
+          "kind": "worker_handler",
+          "relationship": "invokes_method_for_bounded_semantic_snapshot"
+        }
+      ],
       "fr_tags": null,
       "freshness": {
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -15331,15 +15352,18 @@
       "name": "get_mcs_wrap_units",
       "provider_requirements": [],
       "rationale": [
-        "No reviewed IA MCP integration route is registered."
+        "IA MCP reads these native-MCS wrap APIs only while constructing the complete bounded CMN semantic snapshot used for transaction and plan postconditions."
       ],
       "return_contract": {
         "annotation": null,
         "failure_sentinels": [],
         "normalized_success_predicate": null,
-        "review_status": "unreviewed"
+        "review_status": "current_semantic_snapshot_route_only"
       },
-      "roles": [],
+      "roles": [
+        "readback",
+        "semantic_state"
+      ],
       "route_provider_requirements": [],
       "signature": {
         "parameters": [
```
### Commit fb6764542de61d70ff7606846e5ad53e77736c31
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-03T20:41:34-05:00; reachable from selected HEAD: True.
Subject: Deliver bounded IA MCP Agentic V1
Change-Ids: I08d6a4dce0cc6b48e5a83e3d64daa6be06159f6d.
Commit message:
```text
Deliver bounded IA MCP Agentic V1

Preserve the useful M7 implementation behind a frozen certified, assisted-only, provider-gated, and fail-closed support matrix. Consolidate IA MCP runtime, setup, skills, workflow, documentation, module tooling, and tests under checkout/ai. Add repeatable validation tiers and bounded real-agent evaluations, including exact rollback and imported-session artifact authority.

Change-Id: I08d6a4dce0cc6b48e5a83e3d64daa6be06159f6d
```
Diff excerpt, `ai/acceptance/run_codex_scenario.py`:
```diff
@@ -439,6 +439,8 @@ def codex_overrides(launcher: Path) -> list[str]:
         "-c",
         "mcp_servers.ia-mcp.args=[]",
         "-c",
+        "mcp_servers.ia-mcp.startup_timeout_sec=300",
+        "-c",
         "mcp_servers.ia-mcp.enabled=true",
     ]
 
```
Diff excerpt, `ai/acceptance/run_codex_scenario.py`:
```diff
@@ -765,12 +767,12 @@ def run_acceptance(args: argparse.Namespace, scenario: dict[str, Any]) -> dict[s
     if direct_only and getattr(args, "supplemental_reference", None):
         raise AcceptanceError(
             "supplemental-context acceptance is deferred with blank-context Codex acceptance "
-            "until Milestone 12 broad-domain acceptance; --direct-only does not consult supplemental context"
+            "until post-V1 broad-domain acceptance; --direct-only does not consult supplemental context"
         )
     if not direct_only:
         raise AcceptanceError(
-            "the six-scenario blank-context Codex suite is deferred until Milestone 12 expands compiler/domain "
-            "coverage; Milestone 5 typed plan execution remains available for compiler-reachable verticals, "
+            "the six-scenario blank-context Codex suite is deferred until post-V1 work expands compiler/domain "
+            "coverage; certified typed plan execution remains available for the frozen M5/M6 verticals, "
             "and --direct-only runs the historical deterministic regression flow"
         )
     validate_cluster_host()
```
Diff excerpt, `ai/acceptance/run_codex_scenario.py`:
```diff
@@ -1080,8 +1082,8 @@ def build_parser() -> argparse.ArgumentParser:
         "--direct-only",
         action="store_true",
         help=(
-            "run only the historical deterministic direct regression while blank-context "
-            "Codex execution remains deferred pending Milestone 12 broad-domain coverage"
+            "run only the historical deterministic direct regression while broad blank-context "
+            "Codex execution remains deferred to post-V1 domain coverage"
         ),
     )
     return parser
```
### Commit e2415aae9c4951362cabb1d0607a2bf74cc9e869
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-16T17:08:36-05:00; reachable from selected HEAD: True.
Subject: Expand IA MCP configuration execution
Change-Ids: I0d6768687106afac98d25d565049b32b89949a2f.
Commit message:
```text
Expand IA MCP configuration execution

- add controlled direct-CE generation, immutable revision admission, bounded execution, recovery, validation, and replay\n- broaden typed NCI and CMN planning and operation support against reviewed live CE API evidence\n- preserve safety through identity-bound policy, checkpoint rollback, content-bound artifacts, and linear semantic comparisons\n- add focused unit, integration, and live-contract coverage for the expanded paths

Change-Id: I0d6768687106afac98d25d565049b32b89949a2f
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -920,18 +920,12 @@
             "default": "null",
             "kind": "POSITIONAL_OR_KEYWORD",
             "name": "name"
-          },
-          {
-            "annotation": "str",
-            "default": "null",
-            "kind": "POSITIONAL_OR_KEYWORD",
-            "name": "logical_group_name"
           }
         ],
         "return_annotation": "str"
       },
       "source": {
-        "line": 4590,
+        "line": 4610,
         "path": "CE/ideas/api/interconnect_config.py"
       },
       "support": {
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -1930,7 +1924,7 @@
         "return_annotation": "bool"
       },
       "source": {
-        "line": 12049,
+        "line": 12370,
         "path": "CE/ideas/api/interconnect_config.py"
       },
       "support": {
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -3498,7 +3492,7 @@
         "return_annotation": "bool"
       },
       "source": {
-        "line": 10703,
+        "line": 11024,
         "path": "CE/ideas/api/interconnect_config.py"
       },
       "support": {
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/plan_compiler.py`
Snapshot: HEAD; SHA-256 `d1eaee1c463b3973c8735be90ce397d9708c7a51a06afea598cd79197a4c3940`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 9029}.
Introduction/rename-follow candidates: 67b621ef6f366c852550ef07ee1122d336f2985e 2026-08-30T00:56:14-05:00 Michael Coulter <michael.coulter@arm.com> Compile typed IA MCP design plans.
```text
29:     canonical_cmn_mcs_type_input,
30:     canonical_cmn_device_type_input,
31: )
32: from .execution_contracts import CHECKPOINT_MATERIALIZATION_OPERATION
33: from .execution_contracts import TRUSTED_PLAN_OBSERVABLE_OPERATIONS
34: from .execution_contracts import get_execution_contract
35: from .intent_normalization import _load_trusted_design_intent, normalize_design_intent
36: from .interface_parameter_effects import NCIInterfaceParameterEffectError
37: from .interface_parameter_effects import derive_nci_interface_parameter_effects
38: from .intent_validation import (
39:     IntentValidationResultV1,
40:     _project_nci_device_group_lifecycle_intent,
```
```text
70: from .traffic_rename_lifecycle_contract import (
71:     validate_traffic_rename_authority_envelope,
72: )
73: from .plan_postconditions import (
74:     OperationPostcondition,
75:     PlanPostconditionError,
76:     SelectorItems,
77:     build_operation_postcondition_registry,
78:     canonical_operation_selector_items,
79:     mandatory_gate_definitions,
80:     semantic_phase_gate_definition,
81:     validate_provider_requirements,
82: )
83: from .planning_state import PlanningStateV1, verify_planning_state
84: from .power_domain_boundary_contract import (
85:     PowerDomainBoundaryContractError,
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/plan_execution.py`
Snapshot: HEAD; SHA-256 `720631942e251330f43b137980baff12e731ba3c0dcd110b40d728d9eca0b2aa`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 2486}.
Introduction/rename-follow candidates: ad62f9ccb1382a153997636f24a9e6cd35cb096d 2026-08-31T21:33:31-05:00 Michael Coulter <michael.coulter@arm.com> Prove IA MCP NCI construction vertical.
```text
19:     copy_to_private_file,
20:     ensure_private_dir,
21:     serialize_managed_json,
22:     stable_regular_file_sha256,
23: )
24: from ia_mcp_runtime.session_manifest import PLAN_ARTIFACT_MAX_BYTES
25: from ia_mcp_runtime.session_manifest import canonical_plan_contract_sha256
26: 
27: from .artifact_manifest import read_artifact_manifest, record_artifact
28: from .artifact_semantic_restore import build_generated_iyml_restore_authority
29: from .artifact_semantic_restore import build_obligation_iyml_restore_authority
30: from .artifact_semantic_restore import cumulative_plan_operations_from_replay
31: from .artifact_semantic_restore import source_validation_evidence_from_replay
32: from .execution_contracts import (
33:     CHECKPOINT_MATERIALIZATION_OPERATION,
34:     TRUSTED_PLAN_OBSERVABLE_OPERATIONS,
35: )
36: from .config_tools import (
37:     _adapter,
38:     _handle_config_apply_changes_locked,
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/direct_ce_fallback.py`
Snapshot: HEAD; SHA-256 `5a7741c625680fde5aa6e3ba00e2034c4267c18144d4824279e5e35b18fcfdb9`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 1616}.
Introduction/rename-follow candidates: e2415aae9c4951362cabb1d0607a2bf74cc9e869 2026-09-16T17:08:36-05:00 Michael Coulter <michael.coulter@arm.com> Expand IA MCP configuration execution.
```text
36: GAP_ID_RE = re.compile(r"^gap_[0-9a-f]{24}$")
37: GAP_BLOCK_RE = re.compile(
38:     r'(?P<indent>^[ \t]*)# <ia-mcp-gap id="(?P<gap_id>gap_[0-9a-f]{24})" '
39:     r'manifest_sha256="sha256:(?P<manifest_sha>[0-9a-f]{64})">\n'
40:     r'(?P<body>.*?)'
41:     r'(?P=indent)# </ia-mcp-gap>',
42:     re.MULTILINE | re.DOTALL,
43: )
44: SENTINEL_NAME = "ia_mcp_unresolved_gap"
45: ALLOWED_SIMPLE_CALLS = frozenset(
46:     {
47:         "all",
```
```text
100: )
101: UNMANAGED_FILESYSTEM_ROLES = frozenset(
102:     {
103:         "checkpoint_create",
104:         "checkpoint_restore",
105:         "design_export",
106:         "design_import",
107:     }
108: )
109: DOCUMENTED_FILESYSTEM_EFFECT_RE = re.compile(
110:     r"\b(?:copy|erase|inspect|load|place|read|remove|save|write)\w*\b"
111:     r"[^.]{0,160}\b(?:file|files|director(?:y|ies)|report_dir)\b",
112:     re.IGNORECASE,
```
```text
130:     """Raised when a script workflow contract is incomplete or unsafe."""
131: 
132: 
133: def canonical_bytes(value: Any) -> bytes:
134:     return json.dumps(
135:         value,
136:         sort_keys=True,
137:         separators=(",", ":"),
138:         ensure_ascii=True,
139:         allow_nan=False,
140:     ).encode("utf-8")
141: 
142: 
143: def content_sha256(value: Any) -> str:
144:     raw = value if isinstance(value, bytes) else canonical_bytes(value)
145:     return hashlib.sha256(raw).hexdigest()
146: 
147: 
148: def script_sha256(script: str) -> str:
149:     return hashlib.sha256(script.encode("utf-8")).hexdigest()
150: 
151: 
```
### Current source `ai/docs/agentic-v1-completion.md`
Snapshot: HEAD; SHA-256 `21b4b437c9cf172d6b7393a25fec11dc3f86adfcf1cedf35aec90998130fe07d`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 108}.
Introduction/rename-follow candidates: d1d5ca5a8a57e6b589a8fe7fa60f997665596edb 2026-09-04T16:12:59-05:00 Michael Coulter <michael.coulter@arm.com> Retire stale IA MCP execution guidance.
```text
18: 
19: ## Delivered Boundary
20: 
21: - Two certified end-to-end workflows: blank-session `nitwain_r1p0` NCI and
22:   blank-session `cmns4_r1p0` CMN construction.
23: - Ten exact certified operation profiles, 115 assisted-only operations, and
24:   fourteen fail-closed operations.
25: - Forty-five compiler routes classified as five certified-operation routes,
26:   37 assisted-only routes, two fail-closed routes, and one provider-gated
27:   route.
28: - Typed intent, live capability binding, strict operation schemas,
29:   deterministic plans, transactional execution, checkpoints, rollback,
30:   semantic evidence, applicable DRC, explicit CE Python, derived iYML, and
31:   replay for the exact certified profiles.
32: - Broad bounded assistance for API, schema, metadata, source, example, DRC,
33:   Python, and iYML work without turning unproved capabilities into unrestricted
34:   mutation.
35: 
36: The live CE disposition inventory closed at 450 APIs: 354 mapped, 96 unmapped,
37: 139 reviewed direct operations, and zero API-level fully-supported claims.
38: That zero is intentional: certification belongs to exact workflow and
39: operation profiles.
```

## ai-runtime

### Commit be568b8bdac01df3762f96a5d3e62dc9fa532e7b
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-19T13:03:54-05:00; reachable from selected HEAD: True.
Subject: Route IA MCP CE execution through qualified runtimes
Change-Ids: I7386fd0eecbc99516e0dc0d6c7a6a87ff7203524.
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/ce_backends.py`:
```diff
@@ -0,0 +1,620 @@
+"""CE state backends used by the Python-3.13 IA MCP worker."""
+
+from __future__ import annotations
+
+import hashlib
+import json
+import os
+import secrets
+import select
+import subprocess
+import threading
+import time
+import uuid
+from pathlib import Path
+from typing import Any, Callable, Mapping
+
+from ia_mcp_runtime.errors import ToolExecutionError
+
+from .runtime_router import _python_process_environment
+from .runtime_router import resolve_product_auxiliary_runtimes
+from .toolchain_policy import CURRENT_CE_PYTHON, LEGACY_CE_PYTHON
+from .toolchain_policy import product_toolchain_policy
+from .worker_protocol import WORKER_REQUEST_MAX_BYTES, WORKER_RESPONSE_MAX_BYTES
+
+
+_STATE_MANAGER_METHODS = frozenset(
+    {
+        "from_twain",
+        "get_supported_networks",
+        "is_deprecated_product",
+        "is_from_tower",
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/ce_session_adapter.py`:
```diff
@@ -113,7 +113,11 @@ from .route_candidate_authority import (
     validate_route_candidate_envelope,
     validate_route_candidate_request,
 )
-from .runtime_router import _python_process_environment, resolve_ce_python
+from .runtime_router import (
+    _python_process_environment,
+    resolve_control_plane_python,
+    resolve_product_ce_runtime,
+)
 from .semantic_state import (
     SemanticStateError,
     semantic_capture_profile_ids,
```
Diff excerpt, `ai/ia-mcp-pack/src/ia_mcp_pack/ce_session_adapter.py`:
```diff
@@ -5626,10 +5683,77 @@ class CESessionAdapter:
                     raise ToolExecutionError(
                         f"Unable to initialize CE session {session_id} with uniquifier={uniquifier!r}."
                     )
-        except Exception:
-            proxy.close()
-            raise
-        return proxy, python_info["python_executable"], str(audit_log)
+            runtime_profile = proxy.command("runtime_profile", {})
+            if not isinstance(runtime_profile, dict):
+                raise ToolExecutionError(
+                    "CE worker returned a malformed product runtime profile."
+                )
+            expected_profile = {
+                "backend": ce_runtime["backend"],
+                "worker_python_version": control_python["actual_version"],
+                "worker_python_executable": control_python[
+                    "resolved_executable"
+                ],
+                "ce_python_version": ce_runtime["actual_version"],
+                "ce_python_executable": ce_runtime["resolved_executable"],
+                "qualification_status": "qualified",
+            }
+            ruby_runtime = ce_runtime.get("ruby_runtime")
+            if isinstance(ruby_runtime, dict):
+                expected_profile.update(
+                    {
+                        "ruby_version": ruby_runtime["actual_version"],
+                        "ruby_executable": ruby_runtime["executable"],
+                    }
+                )
+            for field, expected in expected_profile.items():
[hunk excerpt ends; remaining lines omitted]
```
### Commit 5560c7c340a808c9b9683fe5431a795b4fbc43b4
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-19T13:04:18-05:00; reachable from selected HEAD: True.
Subject: Qualify IA MCP toolchains in setup and release gates
Change-Ids: I1616d620eb9d6b47a29b1cb47715dfeeb5421b94.
Diff excerpt, `ai/ia-mcp-pack/tests/test_init_script.py`:
```diff
@@ -54,6 +58,10 @@ def _packaged_local_module(tmp_path: Path, *, stub_runtime: bool = False) -> Pat
         _ideas_root() / "ai" / "scripts" / "ia-mcp-local-module-init.sh",
         bin_dir / "ia-mcp-local-module-init",
     )
+    shutil.copy2(
+        _ideas_root() / "ai" / "scripts" / "ia-mcp-prepare-toolchains.sh",
+        bin_dir / "ia-mcp-prepare-toolchains",
+    )
     acceptance_dir = root / "ai" / "acceptance"
     acceptance_dir.mkdir(parents=True)
     shutil.copy2(
```
Diff excerpt, `ai/ia-mcp-pack/tests/test_init_script.py`:
```diff
@@ -273,6 +281,43 @@ def test_ia_mcp_init_dry_run_is_portable_and_side_effect_free(tmp_path: Path) ->
     assert not state_root.exists()
 
 
+def test_local_toolchain_preparation_records_exact_runtime_roles(tmp_path: Path) -> None:
+    module_root = tmp_path / "module"
+    state_root = tmp_path / "state"
+    module_root.mkdir()
+
+    result = subprocess.run(
+        [
+            "bash",
+            str(_toolchain_script()),
+            "--module-root",
+            str(module_root),
+            "--state-root",
+            str(state_root),
+            "--mode",
+            "local",
+            "--python-313",
+            str(Path(sys.executable).resolve()),
+        ],
+        env={**os.environ, "IA_MCP_CE_PYTHON_37": ""},
+        capture_output=True,
+        text=True,
+        check=False,
+    )
+
+    assert result.returncode == 0, result.stderr
+    manifest = json.loads(
+        (state_root / "toolchains" / "manifest.json").read_text(encoding="utf-8")
+    )
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `ai/ia-mcp-pack/tests/test_packaging_scripts.py`:
```diff
@@ -390,6 +390,17 @@ def _write_release_manifest(
         "pack_version": "0.1.0",
         "runtime_version": "0.1.0",
         "build_environment": {"JOB_NAME": "test-release"},
+        "toolchain_policy": {
+            "schema_version": 1,
+            "runtime_roles": {
+                "ia_mcp_control_python": "3.13.9",
+                "current_ce_python": "3.13.9",
+                "legacy_ce_python": "3.7.15",
+                "cyprus_ruby": "2.6.5",
+                "current_cmn_ruby": "3.2.2",
+                "perl": "5.18.1",
+            },
+        },
         "build": {"mode": "standalone", "target_ip": None, "noc_se_hash": noc_se_hash},
         "payload": payload_paths,
         "sources": {
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/legacy_ce_sidecar.py`
Snapshot: HEAD; SHA-256 `db0c8f82bab151314e9e027154700c3abb1cda487c201b9314fac7ca92002695`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 554}.
Introduction/rename-follow candidates: be568b8bdac01df3762f96a5d3e62dc9fa532e7b 2026-09-19T13:03:54-05:00 Michael Coulter <michael.coulter@arm.com> Route IA MCP CE execution through qualified runtimes.
```text
1: #!/usr/bin/env python3
2: """Python-3.7-compatible, authenticated CE sidecar for legacy products.
3: 
4: This file intentionally imports only the standard library and CE.  IA MCP's
5: Python-3.13 dependencies, planning logic, admission policy, and evidence
6: validation stay in the parent worker.
7: """
8: 
9: import argparse
10: import contextlib
11: import hashlib
12: import hmac
13: import inspect
14: import json
```
```text
26: MAX_REQUEST_BYTES = 4 * 1024 * 1024
27: MAX_RESPONSE_BYTES = 4 * 1024 * 1024
28: MAX_ERROR_CHARS = 8 * 1024
29: TOKEN_ENV = "IA_MCP_LEGACY_SIDECAR_TOKEN"
30: EXPECTED_PYTHON = "3.7.15"
31: PRODUCT_SELECTOR_KEYWORDS = frozenset(("ip_version", "product_version", "version"))
32: STATE_MANAGER_METHODS = frozenset(
33:     (
34:         "from_twain",
35:         "get_supported_networks",
36:         "is_deprecated_product",
37:         "is_from_tower",
38:         "is_product_idx",
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/ce_backends.py`
Snapshot: HEAD; SHA-256 `13020082c9f30b89f76010170eba477f890bc2d21da6eee57b1cd82d13d3c75d`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 749}.
Introduction/rename-follow candidates: be568b8bdac01df3762f96a5d3e62dc9fa532e7b 2026-09-19T13:03:54-05:00 Michael Coulter <michael.coulter@arm.com> Route IA MCP CE execution through qualified runtimes.
```text
1: """CE state backends used by the Python-3.13 IA MCP worker."""
2: 
3: from __future__ import annotations
4: 
5: import hashlib
6: import inspect
7: import json
8: import os
9: import secrets
```
```text
52:     operation.  If it evolves compatibly, derive only a one-value call shape
53:     from the live callable and prove the result with ``get_ip_version``.  If
54:     the setter disappears, an already-correct CE default remains safe; every
55:     other case stops before the session can acquire mutation authority.
56:     """
57: 
58:     readback = getattr(interconnect, "get_ip_version", None)
59:     if not callable(readback):
60:         raise ToolExecutionError(
61:             "bootstrap_api_unavailable: current CE lacks callable "
62:             "get_ip_version identity evidence"
63:         )
```
```text
165:     )
166:     for value in (ruby, perl):
167:         if value:
168:             paths.append(str(Path(value).parent))
169:     result: dict[str, str] = {}
170:     if paths:
171:         inherited = os.environ.get("PATH", "")
172:         result["PATH"] = os.pathsep.join([*paths, inherited])
173:     if ruby:
174:         result["IA_MCP_RUBY"] = ruby
175:     if perl:
176:         result["IA_MCP_PERL"] = perl
```
```text
224:         payload = json.loads(path.read_bytes())
225:     except (OSError, ValueError, json.JSONDecodeError) as exc:
226:         raise ToolExecutionError(
227:             f"Unable to load the packaged CE API allowlist: {exc}"
228:         ) from exc
229:     methods = {
230:         entry["name"]
231:         for entry in payload.get("apis", [])
232:         if isinstance(entry, dict)
233:         and isinstance(entry.get("name"), str)
234:         and entry["name"]
235:         and not entry["name"].startswith("_")
```
```text
238:     required = {"get_products_list", "get_ip_version"}
239:     if not required.issubset(methods):
240:         raise ToolExecutionError(
241:             "Packaged CE API allowlist lacks required identity methods"
242:         )
243:     return frozenset(methods)
244: 
245: 
246: class CurrentCEBackend:
247:     """Own a current-product CE Interconnect in the Python-3.13 worker."""
248: 
249:     backend_name = "current_in_process"
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/runtime_router.py`
Snapshot: HEAD; SHA-256 `17cdcb8230d8f48e4f7ed35a10ca1eef4c37a78a8af8db7717f2017b9a8f4e00`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 812}.
Introduction/rename-follow candidates: 0ab6800995f1cbf36129653ccea400b713c8d8ae 2026-04-21T00:28:21-05:00 Michael Coulter <michael.coulter@arm.com> IA MCP capability pack initial implementation.
```text
72: 
73:     library_dirs = []
74:     for runtime_root in (
75:         resolved_executable.parent.parent,
76:         executable_path.parent.parent.resolve(strict=False),
77:     ):
78:         for directory_name in ("lib", "lib64"):
79:             candidate = runtime_root / directory_name
80:             candidate_text = str(candidate)
81:             if candidate.is_dir() and candidate_text not in library_dirs:
82:                 library_dirs.append(candidate_text)
83:     inherited_library_path = env.get("LD_LIBRARY_PATH", "")
84:     for path in inherited_library_path.split(os.pathsep):
```
```text
89:     return env
90: 
91: 
92: def _python_version(executable: Path) -> str | None:
93:     if not executable.exists():
94:         return None
95:     try:
96:         completed = subprocess.run(
97:             [str(executable), "--version"],
98:             check=True,
99:             capture_output=True,
100:             text=True,
```
```text
120: 
121: def _runtime_version(executable: Path, kind: str) -> str | None:
122:     if kind == "python":
123:         return _python_version(executable)
124:     if not executable.exists():
125:         return None
126:     command = (
127:         [str(executable), "--version"]
128:         if kind == "ruby"
129:         else [str(executable), "-e", "print $^V"]
130:     )
131:     try:
```
```text
349: 
350: 
351: def toolchain_manifest_status(ideas_root: str) -> dict[str, Any]:
352:     """Return bounded setup-manifest validity without authorizing a runtime."""
353: 
354:     configured = bool(os.environ.get("IA_MCP_TOOLCHAIN_MANIFEST"))
355:     if not configured:
356:         return {"configured": False, "valid": False, "error": "not configured"}
357:     try:
358:         manifest = _validated_toolchain_manifest(ideas_root)
359:         assert manifest is not None
360:         policy = toolchain_policy_manifest(ideas_root)
```

## release

### Commit 65e2d9081e5f6aa94b20bbbbce281999df31b713
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-13T23:52:53-05:00; reachable from selected HEAD: True.
Subject: Add isolated daily staging pipeline
Change-Ids: Ibf346fa7d1bdbeea305f4143e020c6f0763cb50e.
Commit message:
```text
Add isolated daily staging pipeline

- require an exact Gerrit patchset and disable automatic or concurrent execution
- keep staging release, buildenv, and archive outputs separate from DailyBuild
- omit NoC-SE while retaining the Brunel installer and post-installer rehearsal

Change-Id: Ibf346fa7d1bdbeea305f4143e020c6f0763cb50e
```
Diff excerpt, `jenkins/BuildReleases/Installer/daily-staging.Jenkinsfile`:
```diff
@@ -0,0 +1,391 @@
+#!/usr/bin/env groovy
+// Isolated, manual-only staging copy of DailyBuild. NoC-SE is intentionally omitted.
+// ********** DO NOT EDIT : BEGIN **********
+def config = [
+    team: 'nci',
+    displayName: 'Daily Staging',
+    description: '''Manual, isolated DailyBuild rehearsal for an exact Gerrit patchset''',
+    label: 'EUHPC2',
+    env: [],
+    lsb_defaultproject: 'PJ10000069',
+    emailEveryone: false,
+    credentialsId: 'ideasbot-creds',
+    gitCreds: 'ideasbot-creds',
+    cleanBeforeCheckout: true,
+    flow: 'other',
+    gitUrl: 'ssh://na-gerrit-1.nahpc.arm.com:29418/systems/ideas',
+    buildComment: 'No comment',
+    gerritRefspec: '',
+    gitCheckoutName: 'ideas',
+    stagingReleaseRoot: '/arm/projectscratch/ssg/pj10000069/brunel/releases/daily_staging',
+    stagingBuildenv: '/arm/projectscratch/ssg/pj10000069/brunel/releases/daily_staging_buildenv',
+    stagingArchive: '/arm/projectscratch/ssg/pj10000069/brunel/releases/daily_staging.tar.gz',
+    gitPoll: false
+]
+// ********** DO NOT EDIT : END **********
+
+pipeline {
+    agent { label config.label }
+
+    parameters {
+        string(
[hunk excerpt ends; remaining lines omitted]
```
### Commit c3335efecbb32729a04404b795725a998c0d42e1
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-17T01:25:43-05:00; reachable from selected HEAD: True.
Subject: Add a dedicated, conditional IA MCP packaging stage to installer-staging.
Change-Ids: Ib4d55573eeb87691a09b7561420b13ef7054b9f6.
Commit message:
```text
Add a dedicated, conditional IA MCP packaging stage to installer-staging.

Use includeIaMcp to select internal payload packaging or an external/customer
build with no ai/ payload, Python 3.13 wheelhouse work, or IA MCP setup.

Keep IA MCP validation in the dedicated ia-mcp Jenkins pipeline and document
the staging integration boundary.

Change-Id: Ib4d55573eeb87691a09b7561420b13ef7054b9f6
```
Diff excerpt, `ai/ia-mcp-pack/tests/test_packaging_scripts.py`:
```diff
@@ -4657,6 +4657,104 @@ def test_primary_release_jobs_are_not_ia_mcp_enabled_during_isolated_pipeline_te
         assert "build-ia-mcp-wheelhouse.sh" not in text
 
 
+def test_installer_staging_packages_ia_mcp_without_running_ia_mcp_validation() -> None:
+    ideas_root = _ideas_root()
+    text = (
+        ideas_root
+        / "jenkins"
+        / "BuildReleases"
+        / "Installer"
+        / "installer-staging.Jenkinsfile"
+    ).read_text(encoding="utf-8")
+
+    assert "booleanParam(name: 'includeIaMcp', defaultValue: true" in text
+    package_stage = text.split("stage('Package IA MCP')", 1)[1].split(
+        "stage('Post Installer')",
+        1,
+    )[0]
+    assert "expression { return params.includeIaMcp }" in package_stage
+    assert "iaMcpRuntimeWheelhouse" in package_stage
+    assert "iaMcpWheelhouseBuildPipIndexUrl" in package_stage
+    assert "controlled Python 3.13 runtime wheelhouse" in package_stage
+    assert "module load swdev python/python/3.13.9" in package_stage
+    assert 'export IA_MCP_PYTHON="${IA_MCP_PACKAGE_PYTHON}"' in package_stage
+    assert "IA_MCP_BUILD_MODE=installer-staging" in package_stage
+    assert "IA_MCP_BUILD_NOC_SE_REQUESTED=0" in package_stage
+    assert "IA_MCP_BUILD_NOC_SE_STATUS=intentionally_absent" in package_stage
+    assert (
+        'bash ai/scripts/build-ia-mcp-wheelhouse.sh --output-dir '
+        '"${IA_MCP_RUNTIME_WHEELHOUSE}"'
+    ) in package_stage
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`:
```diff
@@ -29,6 +29,12 @@
  *     created by Build Installer instead of recreating it with legacy virtualenv.
  *   - Its shell bodies use fail-fast and unset-variable checks, with narrow
  *     exceptions around legacy environment activation/deactivation scripts.
+ *   - It stages the release-owned IA MCP runtime and its exact dependencies,
+ *     but leaves IA MCP release gates, runtime proofs, and behavioral tests in
+ *     the dedicated jenkins/ia-mcp/ia-mcp.Jenkinsfile pipeline.
+ *   - The single includeIaMcp parameter controls a dedicated packaging stage.
+ *     Disabling it leaves the freshly recreated release tree free of ai/ and
+ *     performs no IA MCP dependency preparation or staging.
  *   - Its Post Installer stage generates reference.yaml and rules.xlsx, copies
  *     the params.xlsx generated during documentation, and refreshes only the
  *     isolated archive; it does not invoke the production post-installer script.
```
Diff excerpt, `jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`:
```diff
@@ -56,6 +62,8 @@ def config = [
     stagingReleaseRoot: '/arm/projectscratch/ssg/pj10000069/brunel/releases/installer_staging',
     stagingBuildenv: '/arm/projectscratch/ssg/pj10000069/brunel/releases/installer_staging_buildenv',
     stagingArchive: '/arm/projectscratch/ssg/pj10000069/brunel/releases/installer_staging.tar.gz',
+    iaMcpRuntimeWheelhouse: '/arm/projectscratch/ssg/pj10000069/brunel/releases/ia_mcp_release_wheelhouse/python3.13/runtime-lock-v1',
+    iaMcpWheelhouseBuildPipIndexUrl: 'https://artifactory.arm.com/artifactory/api/pypi/mirrors.pypi_org/simple',
     gitPoll: false
 ]
 // ********** DO NOT EDIT : END **********
```
### Commit 142665a60206f1034954bc00eb649a52be2de601
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-17T01:39:16-05:00; reachable from selected HEAD: True.
Subject: Allow installer-staging.Jenkinsfile to use both branches and gerrit refs
Change-Ids: Ia87f20d22d0de21aa1171fd185cae632a07f1ec8.
Commit message:
```text
Allow installer-staging.Jenkinsfile to use both branches and gerrit refs

Change-Id: Ia87f20d22d0de21aa1171fd185cae632a07f1ec8
```
Diff excerpt, `ai/ia-mcp-pack/tests/test_packaging_scripts.py`:
```diff
@@ -4730,6 +4730,29 @@ def test_installer_staging_packages_ia_mcp_without_running_ia_mcp_validation() -
     ) in post_stage
 
 
+def test_installer_staging_uses_branch_by_default_and_gerrit_as_override() -> None:
+    text = (
+        _ideas_root()
+        / "jenkins"
+        / "BuildReleases"
+        / "Installer"
+        / "installer-staging.Jenkinsfile"
+    ).read_text(encoding="utf-8")
+
+    assert "gitBranch: 'master'" in text
+    assert "name: 'gitBranch'" in text
+    assert "defaultValue: config.gitBranch" in text
+    assert "When set, it overrides gitBranch" in text
+    assert "config.gitBranch = (params.gitBranch ?: config.gitBranch).trim()" in text
+    assert "if (config.gerritRefspec)" in text
+    assert 'git check-ref-format --branch "$INSTALLER_STAGING_GIT_BRANCH"' in text
+    assert 'checkoutBranch = "refs/remotes/origin/${config.gitBranch}"' in text
+    assert 'checkoutRefspec = "+refs/heads/${config.gitBranch}:${checkoutBranch}"' in text
+    assert "checkoutBranch = 'refs/remotes/origin/gerrit-review'" in text
+    assert 'checkoutRefspec = "+${config.gerritRefspec}:refs/remotes/origin/gerrit-review"' in text
+    assert 'git rev-parse "$INSTALLER_STAGING_EXPECTED_REF"' in text
+
+
 def test_installer_staging_external_mode_has_no_ia_mcp_packaging_path() -> None:
     text = (
         _ideas_root()
```
Diff excerpt, `jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`:
```diff
@@ -3,16 +3,17 @@
  * Installer staging pipeline
  *
  * Purpose:
- *   Rehearse the production Brunel installer from one exact Gerrit patchset
- *   without modifying or publishing the normal DailyBuild outputs.
+ *   Rehearse the production Brunel installer from a named branch or one exact
+ *   Gerrit patchset without modifying or publishing the normal DailyBuild
+ *   outputs.
  *
  * Differences from installer.Jenkinsfile:
  *   - It is manual-only: there is no cron or SCM polling trigger, and concurrent
  *     runs of this Jenkins job are disabled.
- *   - It requires an exact refs/changes/NN/CHANGE/PATCHSET Gerrit ref. It has no
- *     branch selector, master fallback, or mirror checkout fallback.
- *   - It checks out from the primary Gerrit endpoint so the requested patchset
- *     can be fetched directly.
+ *   - It builds the selected branch (master by default), unless an exact
+ *     refs/changes/NN/CHANGE/PATCHSET Gerrit ref is supplied as an override.
+ *   - It checks out from the primary Gerrit endpoint so either source can be
+ *     fetched directly.
  *   - It does not build, copy, or publish NoC-SE, NoC_SE_DEP, or synthesis data;
  *     SYNTH_ENGINE remains unset throughout the build.
  *   - It does not run update_resource_examples.sh or recopy generated examples.
```
Diff excerpt, `jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`:
```diff
@@ -46,7 +47,7 @@
 def config = [
     team: 'nci',
     displayName: 'Installer Staging',
-    description: '''Manual, isolated installer rehearsal for an exact Gerrit patchset. NoC-SE is omitted and production DailyBuild outputs are never modified.''',
+    description: '''Manual, isolated installer rehearsal for a branch or exact Gerrit patchset. NoC-SE is omitted and production DailyBuild outputs are never modified.''',
     label: 'EUHPC2',
     env: [],
     lsb_defaultproject: 'PJ10000069',
```
### Commit 2f0f548b67be00bfaa78d481474666356a1a4131
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-21T11:45:58-05:00; reachable from selected HEAD: True.
Subject: Make CE API disposition staging contract-aware
Change-Ids: If80b2ecd3f1721513c0eeda6aae0c8f1c4008586.
Commit message:
```text
Make CE API disposition staging contract-aware
Simplify installer-staging jenkinsfile

- Preserve the tracked registry as reviewed contract authority while binding a staged canonical artifact to the current CE source.\n- Permit documentation and source-location drift only when API identities, signatures, policy digests, and dispositions remain unchanged.\n- Fail Jenkins early on real CE API contract drift and carry the reviewed/deployed binding through capability and runtime validation.\n- Add focused contract, staging, packaging, tier, and documentation coverage.

Change-Id: If80b2ecd3f1721513c0eeda6aae0c8f1c4008586
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -54313,8 +54313,8 @@
     "live_fingerprints": {
       "contract": "d38cd751201ed6573f1df2d4823ac3b114a424cb42a40b07424087e4588b9947",
       "documentation": "2093a0e4ada9aba9298baa088d2cafa3f98fb0f969cc0ae3ab4dc41ef213905d",
-      "full": "ba3e0f84e43bc9f04065222d710998a8107c7867e8aa8596dd00af25a75242c2",
-      "provenance": "7ac9f7f50f262048370e755a2ec896aa39f80990a498a4909fb9adfc12e8a9b4",
+      "full": "0eaa0752f1ead238504d27744a4bdb99e23c44594dbac405620fceb552d5e8e6",
+      "provenance": "611599992ba931ffac1c1e3c4b34201087e6dd58907bac10e8ef0c752e25777f",
       "structural": "b48760789b98dbf73f3d83b9babd1afabc092d5e0ffcc1f29460328579d38f4f"
     },
     "provenance_current": false,
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -54718,8 +54718,8 @@
       "ce_runtime_tree_file_count": null,
       "ce_runtime_tree_sha256": null,
       "ce_runtime_tree_total_bytes": null,
-      "ce_source_commit": "e045d5f750f67f1b848bb439c49b8b0c5b22c07b",
-      "ce_tree_git_object": "665efe344f2bf78ba0a45301da301754103651a0",
+      "ce_source_commit": "ddfab3c73ed75ffea3389e04c90cdc9664b7a8c6",
+      "ce_tree_git_object": "252d5378092de3a554cecdae060ec8ba561fad02",
       "ce_worktree_dirty": false,
       "ce_worktree_fingerprint": "8747a6deebd5cd8d359829c8b9b65a400ba116d571230810dcaa93d8a5d54ff7",
       "changed_input_hashes": {},
```
Diff excerpt, `ai/ia-mcp-pack/generated/ce-api-disposition-v1.json`:
```diff
@@ -54753,13 +54753,13 @@
       "provenance_hash_log_sha256": null,
       "provenance_kind": "git_checkout",
       "provenance_manifest_sha256": null,
-      "source_fingerprint": "1c07a557ac033cab4b559caa1f8e3bbae5198f61c77f29e4b246b405452023ed",
+      "source_fingerprint": "3b9ac033e1afc5bf9bfd6af068aa008455f82d88de8eff2b815f324a292e82bf",
       "untracked_input_hashes": {},
       "untracked_inputs_truncated": false
     },
-    "ce_source_commit": "e045d5f750f67f1b848bb439c49b8b0c5b22c07b",
+    "ce_source_commit": "ddfab3c73ed75ffea3389e04c90cdc9664b7a8c6",
     "ce_source_provenance_status": "verified_selected_checkout",
-    "ce_tree_git_object": "665efe344f2bf78ba0a45301da301754103651a0",
+    "ce_tree_git_object": "252d5378092de3a554cecdae060ec8ba561fad02",
     "ce_worktree_dirty": false,
     "interconnect_module": "ideas.api.interconnect",
     "interconnect_source": "CE/ideas/api/interconnect.py",
```
### Current source `jenkins/BuildReleases/Installer/installer-staging.Jenkinsfile`
Snapshot: HEAD; SHA-256 `936f3fa93aee563f536a1f47f367319d336706cdd92249dc74b1359881404eee`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 475}.
Introduction/rename-follow candidates: none.
```text
1: #!/usr/bin/env groovy
2: /*
3:  * Installer staging pipeline
4:  *
5:  * Purpose:
6:  *   Rehearse the production Brunel installer from a named branch or one exact
7:  *   Gerrit patchset without modifying or publishing the normal DailyBuild
8:  *   outputs.
9:  *
10:  * Differences from installer.Jenkinsfile:
11:  *   - It is manual-only: there is no cron or SCM polling trigger, and concurrent
12:  *     runs of this Jenkins job are disabled.
13:  *   - It builds the selected branch (master by default), unless an exact
14:  *     refs/changes/NN/CHANGE/PATCHSET Gerrit ref is supplied as an override.
15:  *   - It checks out from the primary Gerrit endpoint so either source can be
16:  *     fetched directly.
17:  *   - It does not build, copy, or publish NoC-SE, NoC_SE_DEP, or synthesis data;
18:  *     SYNTH_ENGINE remains unset throughout the build.
19:  *   - It does not run update_resource_examples.sh or recopy generated examples.
20:  *     The checked-in resources/examples/<product>/socrates_yaml payload is packaged.
21:  *   - It writes only to the isolated installer_staging module directory,
22:  *     installer_staging_buildenv symlink, and installer_staging.tar.gz archive.
```
### Current source `ai/ia-mcp-pack/src/ia_mcp_pack/api_disposition_deployment.py`
Snapshot: HEAD; SHA-256 `0e11d0318653d9190681b8e901e75397e0418b6755e776d8d5f86aeaf957d6cb`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 157}.
Introduction/rename-follow candidates: 2f0f548b67be00bfaa78d481474666356a1a4131 2026-09-21T11:45:58-05:00 Michael Coulter <michael.coulter@arm.com> Make CE API disposition staging contract-aware Simplify installer-staging jenkinsfile.
```text
1: """Check and stage a CE API disposition against reviewed contract authority."""
2: 
3: from __future__ import annotations
4: 
5: import argparse
6: import json
7: import os
8: import sys
9: import tempfile
```
```text
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
```
```text
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
```
### Current source `ai/scripts/stage-ia-mcp-runtime.sh`
Snapshot: HEAD; SHA-256 `e824b54596b3cf9f0c00f81fdb0ce71a26d2d195b603cc9360f8c1253878a7d3`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 828}.
Introduction/rename-follow candidates: eeef814840d71b16e53f87ba3c831a876527454b 2026-06-16T11:22:04-05:00 Michael Coulter <michael.coulter@arm.com> Reapply "ia-mcp is now self-contained within brunel module" with fixes; cdee3f4239a11568e885ae5bc674042e8ec2e8e2 2026-06-15T23:46:05-05:00 Michael Coulter <michael.coulter@arm.com> ia-mcp is now self-contained within brunel module.
```text
16:   IA_MCP_RUNTIME_PIP_INDEX_URL Internal Python package index for controlled vendoring.
17:   IA_MCP_PIP_INDEX_URL         Compatibility alias for IA_MCP_RUNTIME_PIP_INDEX_URL.
18:   IA_MCP_RUNTIME_PIP_EXTRA_INDEX_URL
19:                                Optional extra package index; requires a primary index.
20:   IA_MCP_PIP_EXTRA_INDEX_URL   Compatibility alias for IA_MCP_RUNTIME_PIP_EXTRA_INDEX_URL.
21:   IA_MCP_ALLOW_DEFAULT_PIP_DEP_SOURCE=1
22:                                Permit ambient pip config; intended for local tests only.
23:   IA_MCP_SKIP_DEP_VENDOR=1     Copy sources only; intended for local tests.
24:   IA_MCP_ALLOW_NON_313_PACKAGE_PYTHON=1
25:                                Permit an explicit non-3.13 packaging Python.
26: USAGE
27: }
```
```text
58: 
59:   base="$(basename "$dest")"
60:   if [[ -z "$dest" || "$dest" == "/" || "$base" != "ai" ]]; then
61:     echo "ERROR: refusing suspicious IA MCP staging destination: ${dest:-<empty>}" >&2
62:     echo "Destination must be the release payload ai directory, for example <linux64>/ai." >&2
63:     return 1
64:   fi
65: 
66:   "$python_bin" - "$dest" "$ideas_root" <<'PY'
67: from pathlib import Path
68: import sys
69: 
```
```text
77: 
78: for candidate in (dest, *dest.parents):
79:     if candidate.is_symlink():
80:         fail(f"refusing symlinked IA MCP staging destination component: {candidate}")
81:     if candidate == candidate.parent:
82:         break
83: 
84: dest_resolved = dest.resolve(strict=False)
85: if dest_resolved == ideas_ai or dest_resolved.is_relative_to(ideas_root):
86:     fail(f"refusing to stage IA MCP payload inside the source checkout: {dest}")
87: 
88: if dest.exists() and not dest.is_dir():
89:     fail(f"refusing non-directory IA MCP staging destination: {dest}")
90: 
91: if dest.exists() and any(dest.iterdir()):
92:     marker_paths = [
93:         dest / "ia-mcp-build-manifest.json",
94:         dest / "ia-mcp-pack",
95:         dest / "ia-mcp-runtime",
96:         dest / "bin" / "ia-mcp",
97:     ]
98:     if not any(path.exists() for path in marker_paths):
99:         fail(
100:             "refusing to replace a non-empty ai directory that does not look like "
101:             f"a prior IA MCP staged payload: {dest}"
```

## ip-policy

### Commit 4fb049b5c92bedb7192e7db8780eaa5b4218fa15
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-07-17T12:49:02-05:00; reachable from selected HEAD: True.
Subject: Add configurable IP version policy
Change-Ids: I4d7433de18e85396e9d1f0997e9b91b530d8a248.
Diff excerpt, `GUI/src/app/project/project-launcher.service.spec.ts`:
```diff
@@ -52,10 +52,10 @@ describe('ProjectLauncherService', () => {
     projectSpinnerActivate: Subject<boolean>;
     beginProjCloneMigrateStage: Subject<boolean>;
     fetchSuppportedIPVersions: jasmine.Spy;
-    getSingleIPVersionIfPresent: jasmine.Spy;
     setupProjectDirectory: jasmine.Spy;
     openExistingProjectFromConfigPath: jasmine.Spy;
     loadProject: jasmine.Spy;
+    getCurrentIPVersion: jasmine.Spy;
     migrateDesignIPVersion: jasmine.Spy;
     setupWorkspaceDir: jasmine.Spy;
   };
```
Diff excerpt, `GUI/src/app/project/project-launcher.service.spec.ts`:
```diff
@@ -63,10 +63,57 @@ describe('ProjectLauncherService', () => {
   const confirmationHost = {
     viewContainerRef: {},
   } as PlaceholderDirective;
+  const disabledPolicy = {
+    version: 1,
+    enabled: false,
+    singleIp: {
+      enabled: false,
+      targetIpVersion: '',
+      restrictSelectableIpVersions: true,
+      filterWorkspaceProjects: true,
+      autoMigrateImports: true,
+      autoMigrateProjectLoads: true,
+      showUiNotice: true,
+    },
+    importMigration: {
+      enabled: false,
+      rules: [],
+    },
+  };
+  const policyWithImportRules = (rules: any[]) => ({
+    ...disabledPolicy,
+    enabled: true,
+    importMigration: {
+      enabled: true,
+      rules,
+    },
+  });
+  const policyWithSingleIp = (singleIpOverrides: any = {}) => ({
+    ...disabledPolicy,
+    enabled: true,
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/project/project-launcher.service.spec.ts`:
```diff
@@ -127,6 +171,7 @@ describe('ProjectLauncherService', () => {
           uniquifier: 'uniq0',
         }),
       loadProject: jasmine.createSpy('loadProject').and.returnValue(Promise.resolve()),
+      getCurrentIPVersion: jasmine.createSpy('getCurrentIPVersion').and.resolveTo('towernci_r0p0'),
       migrateDesignIPVersion: jasmine.createSpy('migrateDesignIPVersion'),
       setupWorkspaceDir: jasmine.createSpy('setupWorkspaceDir'),
     } as unknown as ProjectManagmentService & {
```
### Commit fc81777f4faabd7a84b0bbe8ff58785298f0da90
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-09-08T22:45:25-05:00; reachable from selected HEAD: True.
Subject: Retire cmns4_r0p0 from GUI support
Change-Ids: I4744340dc45024df7a62ea1fb824e095b979c33b.
Diff excerpt, `GUI/src/app/project/project-managment.service.spec.ts`:
```diff
@@ -101,7 +101,9 @@ describe('ProjectManagmentService', () => {
       'finalizeProjectSetup',
       'rollbackProjectSetup',
       'appendConfigurationLog',
+      'getCurrentIPVersionSupport',
       'getIpVersionPolicy',
+      'getUIInfo',
     ]);
     const spinnerSpy = jasmine.createSpyObj('ProjectSpinnerService', ['setupProjectLoadSpinner', 'updateSpinner']);
     const perfLogSpy = jasmine.createSpyObj('PerfLogService', ['startRun']);
```
Diff excerpt, `GUI/src/app/project/project-managment.service.spec.ts`:
```diff
@@ -196,6 +205,26 @@ describe('ProjectManagmentService', () => {
     });
   });
 
+  it('excludes CMN versions without explicit GUI metadata while preserving NCI default metadata support', () => {
+    dataServiceSpy.getCurrentIPVersionSupport.and.returnValue([
+      'cmn_supported_r1p0',
+      'cmn_retired_r0p0',
+      'nci_without_specific_metadata',
+    ]);
+    dataServiceSpy.getUIInfo.and.returnValue({
+      ipSpecific: {
+        cmn_supported_r1p0: { display: 'Supported CMN' },
+        default: { display: '' },
+      },
+    });
+
+    expect(service.fetchSuppportedIPVersions()).toEqual([
+      'cmn_supported_r1p0',
+      'nci_without_specific_metadata',
+    ]);
+    expect(service.selectedIP).toBe('cmn_supported_r1p0');
+  });
+
   it('forwards the selected workspace path to the main process without renderer-side BrunelCE rewriting', () => {
     dataServiceSpy.setupWorkspaceDir.and.returnValue({
       path: '/workspace/custom/BrunelCE',
```
Diff excerpt, `GUI/src/app/project/project-managment.service.ts`:
```diff
@@ -266,7 +266,9 @@ export class ProjectManagmentService {
 
   fetchSuppportedIPVersions(): string[] {
     const supportedVersions = this.dataService.getCurrentIPVersionSupport();
-    const availableIPVersions = Array.isArray(supportedVersions) ? supportedVersions : [];
+    const availableIPVersions = Array.isArray(supportedVersions)
+      ? this.filterGuiSupportedIpVersions(supportedVersions)
+      : [];
 
     if (!availableIPVersions.length) {
       this.selectedIPVersion = null;
```
### Commit 48b5e3a43642b65ef99c0363937ac17d3d93c20d
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-08-13T16:21:08-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-4683, BRUNEL-4684, BRUNEL-4693: Gate GT ports and subsections to niTwain R1
Change-Ids: Iece4f0ac2013fb964c7b5379a150354ff0ae4294.
Diff excerpt, `CE/ideas/ui-info.yaml`:
```diff
@@ -5537,6 +5537,10 @@
     },
     nitwain_r1p0: {
       display: "nocs4_r1p0",
+      features: {
+        gtPorts: true,
+        subsectionBoundaries: true
+      },
       tabs: {
         uniqueLink: ["project", "domains", "globals", "interfaces",  "paths", "memory-maps", "synthesis-constraints" , "basic-traffic", "traffic", "canvas", "generate", "test-and-report", "build"],
         order: [
```
Diff excerpt, `GUI/src/app/canvas/core/services/canvas-config.service.spec.ts`:
```diff
@@ -0,0 +1,53 @@
+import { Subject } from 'rxjs';
+
+import { CanvasConfigService } from './canvas-config.service';
+
+describe('CanvasConfigService subsection feature gating', () => {
+  function createService(enabled: boolean) {
+    const dataService = {
+      brunelCEApi: jasmine.createSpy('brunelCEApi'),
+      brunelCEResponse: new Subject<any>(),
+      brunelInstantiationChanged: new Subject<void>(),
+    };
+    const projectService = {
+      ipVersionCheck: jasmine.createSpy('ipVersionCheck').and.returnValue(enabled),
+    };
+    const service = new CanvasConfigService(
+      { staticDataSync: new Subject<void>() } as any,
+      {} as any,
+      dataService as any,
+      projectService as any,
+    );
+    (service as any).bounds = {
+      subsection: { fabric: [[{ x: 0, y: 0 }]] },
+      blockage: { keep: [] },
+    };
+    return { service, dataService };
+  }
+
+  it('exposes and updates subsection boundaries when the feature is enabled', () => {
+    const { service, dataService } = createService(true);
+
+    expect(service.boundaries.subsection.fabric.length).toBe(1);
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/core/services/canvas-config.service.ts`:
```diff
@@ -149,7 +151,11 @@ export class CanvasConfigService {
   }
 
   get boundaries(): typeof this.bounds {
-    return cloneDeep(this.bounds);
+    const boundaries = cloneDeep(this.bounds);
+    if (boundaries && !this.subsectionBoundariesEnabled()) {
+      delete boundaries['subsection'];
+    }
+    return boundaries;
   }
 
   ensureBoundariesLoaded(updateSpinner: boolean): void {
```
### Current source `brunel/ip-version-policy.js`
Snapshot: HEAD; SHA-256 `5e14164d8a50cc4e216e3dbe634cddaab1c26839cd00df615bdc33ddb4b3088a`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 260}.
Introduction/rename-follow candidates: 4fb049b5c92bedb7192e7db8780eaa5b4218fa15 2026-07-17T12:49:02-05:00 Michael Coulter <michael.coulter@arm.com> Add configurable IP version policy.
```text
1: const fs = require('fs');
2: const path = require('path');
3: 
4: const IP_VERSION_POLICY_VERSION = 1;
5: 
6: function defaultIpVersionPolicy() {
7:   return {
8:     version: IP_VERSION_POLICY_VERSION,
9:     enabled: false,
10:     singleIp: {
11:       enabled: false,
12:       targetIpVersion: '',
13:       restrictSelectableIpVersions: true,
14:       filterWorkspaceProjects: true,
15:       autoMigrateImports: true,
16:       autoMigrateProjectLoads: true,
17:       showUiNotice: true,
18:     },
19:     importMigration: {
20:       enabled: false,
21:       rules: [],
22:     },
23:   };
24: }
```
### Current source `GUI/src/app/shared/services/data.service.ts`
Snapshot: HEAD; SHA-256 `f7b60546cb71c06e2734907c437e825f23b4d83ed345934de3c09a4cfa68f8c9`.
Surviving-line author counts (attribution context only): {'Ana Rescala': 20, 'Dustin Divis': 59, 'dusdiv01': 5, 'Dustin divis': 490, 'Pawan Kakarla': 140, 'Michael Coulter': 509, 'Kelly Alvarez': 165, 'Liza Dayoub': 56, 'Kyan Kornfeld': 11}.
Introduction/rename-follow candidates: b0c68199df9f4397c62159caf048c69b6644d570 2020-06-01T14:30:26-07:00 Kelly Alvarez <kelly.alvarez@arm.com> Initial REST api commit.
```text
24: import * as fs from 'fs';
25: import cloneDeep from 'lodash/cloneDeep';
26: import { showAppConfirmation, showAppNotification } from './app-alert.service';
27: import { bindCeRequest, CeBatchOutcome, CeLockSnapshot, CeMutationRequest, CeParameterInfo, CePolicyDecision, CeSubsectionInfo, checkCeParameterContract, evaluateCeMutation, mutationFailureReason, mutationFailureTitle, serializeCeMutation } from '../ce-policy/ce-policy';
28: import { CE_POLICY_BINDINGS } from '../ce-policy/ce-policy-bindings';
29: import { CePolicyState } from '../ce-policy/ce-policy-state';
30: import { CeInformationError, CeMutationOutcome, CeMutationStep, CeWorkflowOptions, CeWorkflowOutcome, CeWriteQueue, ceMutationOutcome, ceWorkflowNotification, executeCeMutationSteps } from './ce-mutation-outcome';
31: 
32: interface BrowserStaticData {
33:   uiInfo: any;
34:   uiFieldset: any;
35:   scripting: any;
36:   userScripts: string[];
37:   headDocPath: string | null;
```
```text
40: // Add working/project for back end, because -d will need to be set per access point
41: @Injectable({ providedIn: 'root' })
42: export class DataService {
43:   readonly cePolicy = new CePolicyState();
44:   subsectionRtlLockingEnabled = false;
45:   private apiManifest: Record<string, { mutator: boolean }> | null = null;
46:   private policyRequestId = 0;
47:   private policyProjectEpoch = 0;
48:   private writeQueue = new CeWriteQueue();
49:   private undoCheckpoint: Promise<CeWorkflowOutcome> | undefined;
50:   private publishedPolicy: CeLockSnapshot | null = null;
51:   private readonly policyRefreshIds = new Set<string>();
52:   private policyRefreshQueued = false;
```

## diagnostics

### Commit 44d2ae68c761b8be51a3956cab45519545eaca74
Author: Michael Coulter <michael.coulter@arm.com>; author date 2024-05-20T18:16:26-05:00; reachable from selected HEAD: True.
Subject: BRUNEL-1999: Add DRC violation tree viewer
Change-Ids: I72d7355c1bf256d24bf093d4a248c03d49323c83.
Diff excerpt, `GUI/src/app/shared/components/info-tree/info-tree.component.ts`:
```diff
@@ -0,0 +1,75 @@
+import { FlatTreeControl } from '@angular/cdk/tree';
+import { Component, OnInit, Input, OnChanges, SimpleChanges } from '@angular/core';
+import { MatTreeFlatDataSource, MatTreeFlattener, MatTreeModule } from '@angular/material/tree';
+import { MatIconModule } from '@angular/material/icon';
+import { MatButtonModule } from '@angular/material/button';
+import { InfoTreeNode } from 'src/app/shared/models/info-tree-node';
+
+/** Flat node with expandable and level information */
+interface ExampleFlatNode {
+  expandable: boolean;
+  name: string;
+  level: number;
+}
+
+@Component({
+  selector: 'app-info-tree',
+  templateUrl: './info-tree.component.html',
+  styleUrls: ['./info-tree.component.css'],
+})
+export class InfoTreeComponent implements OnInit, OnChanges {
+  @Input() inputInfo: InfoTreeNode[] = [];
+  private _transformer = (node: InfoTreeNode, level: number) => {
+    return {
+      expandable: !!node.children && node.children.length > 0,
+      name: node.name,
+      level: level,
+    };
+  };
+
+  treeControl = new FlatTreeControl<ExampleFlatNode>(
+    node => node.level,
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/shared/models/info-tree-node.ts`:
```diff
@@ -0,0 +1,25 @@
+/***************************************************************************
+* The confidential and proprietary information contained in this file may
+* only be used by a person authorised under and to the extent permitted
+* by a subsisting licensing agreement from Arm Limited or its affiliates.
+*
+* (C) COPYRIGHT 2023-2024 Arm Limited or its affiliates.
+* ALL RIGHTS RESERVED
+*
+* This entire notice must be reproduced on all copies of this file
+* and copies of this file may only be made by a person if such person is
+* permitted to do so under the terms of a subsisting license agreement
+* from Arm Limited or its affiliates.
+*
+* Release Information : $State$
+*
+***************************************************************************/
+
+/**
+ * Info with nested structure.
+ * Each node has a name and an optional list of children.
+ */
+export interface InfoTreeNode {
+  name: string;
+  children?: InfoTreeNode[];
+}
```
Diff excerpt, `GUI/src/app/shared/services/data.service.ts`:
```diff
@@ -37,11 +37,13 @@ export class DataService {
   expandLogResponse = new Subject<any>();
   nciConfigSectionResponse = new Subject<{ id: string, res: object }>();
   errorUpdate = new Subject<any>();
+  drcLogSubject = new Subject<string>();
   streamBuffer: { synth: string[], build: string[], error: string[] } = { synth: [], build: [], error: [] };
   ceErrorString: string = '';
   ceErrorStringCharLimit: number = 1395;
   private brunelNciInstantiated = false;
   private apiCallUniquifier = 0;
+  drcLog: string = "";
 
   flush() {
     this.streamBuffer = { synth: [], build: [], error: [] };
```
### Current source `GUI/src/app/shared/components/info-tree/info-tree.component.ts`
Snapshot: HEAD; SHA-256 `7c8babd5ee623ec0b23fa33131b0ecbaffa1c183c259649b83954e3744ead593`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 61, 'Pawan Kakarla': 6}.
Introduction/rename-follow candidates: 44d2ae68c761b8be51a3956cab45519545eaca74 2024-05-20T18:16:26-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-1999: Add DRC violation tree viewer.
```text
1: import { FlatTreeControl } from '@angular/cdk/tree';
2: import { Component, OnInit, Input, OnChanges, SimpleChanges } from '@angular/core';
3: import { MatTreeFlatDataSource, MatTreeFlattener } from '@angular/material/tree';
4: import { InfoTreeNode } from 'src/app/shared/models/info-tree-node';
5: 
6: /** Flat node with expandable and level information */
7: interface ExampleFlatNode {
8:   expandable: boolean;
9:   name: string;
10:   level: number;
11: }
12: 
```
```text
17:     standalone: false
18: })
19: export class InfoTreeComponent implements OnInit, OnChanges {
20:   @Input() inputInfo: InfoTreeNode[] = [];
21:   private _transformer = (node: InfoTreeNode, level: number) => {
22:     return {
23:       expandable: !!node.children && node.children.length > 0,
24:       name: node.name,
25:       level: level,
26:     };
27:   };
28: 
29:   treeControl = new FlatTreeControl<ExampleFlatNode>(
```
```text
61:     }
62:   }
63: 
64:   onInputChange(value: InfoTreeNode[]): void {
65:     this.dataSource.data = value;
66:   }
67: }
```
### Current source `GUI/src/app/status-bar/drc-results/drc-results.component.ts`
Snapshot: HEAD; SHA-256 `5d04b00df7e9de2935eb855d3edfbdbb5097c4937c42595f355f64a710d5ce8b`.
Surviving-line author counts (attribution context only): {'Kelly Alvarez': 56, 'Michael Coulter': 77, 'Dustin divis': 68, 'Dustin Divis': 34, 'Pawan Kakarla': 17, 'dusdiv01': 1}.
Introduction/rename-follow candidates: db6823b0c4c757b9a21166e5385415aff273a2a0 2020-12-01T15:20:03-06:00 Dustin Divis <dustin.divis@arm.com> [GUI/brunel] Status Bar: Phase 1 complete.
```text
28: import { TestAndReportServiceApi } from 'src/app/test-and-report/test-report-service-api';
29: import { DrcWaiverService } from 'src/app/drc-waivers/services/drc-waiver.service';
30: import { DrcTypes } from 'src/app/shared/models/drc-types.enum';
31: import { InfoTreeNode } from 'src/app/shared/models/info-tree-node';
32: import { CanvasDrcHighlightService } from 'src/app/canvas/core/services/canvas-drc-highlight.service';
33: import cloneDeep from 'lodash/cloneDeep';
34: 
35: 
36: @Component({
37:     selector: 'app-drc-results',
38:     templateUrl: './drc-results.component.html',
39:     styleUrls: ['./drc-results.component.css'],
```
```text
43:   @Input() drcType: DrcTypes = DrcTypes.none;
44:   @Output() closeModal = new EventEmitter<boolean>();
45:   modalTitle: string = null;
46:   majorResults: InfoTreeNode[] = [{ name: 'Checking...' }];
47:   indexLine = '';
48:   results = this.majorResults[0]["name"];
49:   drcRules: any;
50:   subscriptions: Subscription[] = [];
51:   private unsubscribeAll: Subject<void> = new Subject<void>();
52:   availableNetworks = [];
53:   brunelGUIDRC = false;
54:   drcTypeNone = DrcTypes.none;
55:   drcLog = "";
56:   private readonly requests = new CeRefreshScope();
57:   private uArchDrcFailed = false;
58:   private activeResultsSubscription: Subscription;
59: 
60:   constructor(private dataService: DataService,
61:     private projectService: ProjectService,
62:     private globalService: GlobalService,
63:     private canvasConnectionRouteService: CanvasConnectionsService,
```
```text
68:     private tools: DrcToolService) { }
69: 
70:   ngOnInit(): void {
71:     this.drcLog = this.dataService.drcLog;
72:     this.dataService.drcLogSubject.pipe(takeUntil(this.unsubscribeAll)).subscribe(drcLog => {
73:       this.drcLog = drcLog;
74:       this.updateMajorResults();
75:       if (this.drcType === DrcTypes.uArch && this.uArchDrcFailed) {
76:         this.canvasDrcHighlightService.handleMaDrcFailure(drcLog, false);
77:       }
78:       this.cdr.detectChanges();
79:     });
80: 
```

## routing-editors

### Commit 4d97de903fd55a58857fb69fefff10cc1909dbd6
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-02-28T10:23:03-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-2863: Enable connector tool in logical canvas
Change-Ids: I5cc6284caa25482b9022931e7f06b3d6847ca691.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -23,13 +23,14 @@ import cloneDeep from 'lodash/cloneDeep';
 import { CanvasStaticDataService } from 'src/app/canvas/shared/services/canvas-static-data.service';
 import { CanvasLogicalService } from 'src/app/canvas/canvas-logical.service';
 import { CanvasGuiDataService } from 'src/app/canvas/shared/services/canvas-gui-data.service';
+import { CanvasPhysicalService } from 'src/app/canvas/canvas-physical.service';
 import { CanvasSelectorsService } from 'src/app/canvas/shared/services/canvas-selectors.service';
 import { CanvasInstancesService } from 'src/app/canvas/shared/services/canvas-instances.service';
 import { CanvasInterfacesService } from 'src/app/canvas/shared/services/canvas-interfaces.service';
 import { CanvasBlockagesService } from 'src/app/canvas/shared/services/canvas-blockages.service';
 import { CanvasConnectionsRoutesService } from 'src/app/canvas/shared/services/canvas-connections-routes.service';
 import { UiComponent } from 'src/app/shared/models/ui-info.model';
-import { NetworkType } from 'src/app/shared/models/connections.model';
+import { CanvasConnection, ConnectionCount, Connections, NetworkType } from 'src/app/shared/models/connections.model';
 import { CanvasTool } from 'src/app/shared/models/canvas-tool.enum';
 
 import { CanvasInteraction } from 'src/app/canvas/shared/utils/canvas-interaction.util';
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -59,7 +60,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
   startRendering: boolean = false; // prevents glitchy first canvas render
   runZoomToFit: boolean = false;
   fetchedInstances: Record<string, any> = []; // defines an object where keys are strings, and values can be of any type
-  instances: any = {};
+  instancesInfo: any = {};
   interfaces: Record<string, any> = {};
   nonAssociatedInterfaces: Record<string, any> = {};
   connections: any = {};
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical/canvas-floorplan-logical.component.ts`:
```diff
@@ -148,6 +151,7 @@ export class CanvasFloorplanLogicalComponent implements OnInit, AfterViewInit, O
     });
     this.canvasGuiDataService.canvasToolChanged.pipe(takeUntil(this.unsubscribe$)).subscribe(tool => {
       this.tool = tool;
+      this.canvasInteraction.checkConnectionAndDragEnablement();
     });
     this.canvasLogicalService.setZoomToInstanceSubject.pipe(takeUntil(this.unsubscribe$)).subscribe(state => {
       this.setZoomToInstance(state);
```
### Commit 7389f6a0958aecb9e01f7708bd71fa95caa2d584
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-08-28T04:20:06-05:00; reachable from selected HEAD: True.
Subject: delphi routing
Change-Ids: I235752d4f69e7ea5db498ca6f550a226ce302b93.
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -46,7 +46,7 @@ import { CanvasInteraction } from 'src/app/canvas/shared/utils/canvas-interactio
 export interface Route {
   source: string;         // e.g. instance ID or name
   target: string;         // e.g. instance ID or name
-  hops: string[];         // list of crosspoints traversed
+  hops: Array<[number, number]>; // list of crosspoint logical coords traversed, e.g. [[0,0],[0,1],...]
 }
 
 @Component({
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -148,15 +148,33 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
   canvasGreyedOut: boolean = false;
   highlightedCrosspointIds: Set<string> = new Set();
   // live highlights for mesh links between chosen crosspoints
-  highlightedMeshLinks: Array<{x1:number,y1:number,x2:number,y2:number}> = [];
+  highlightedMeshLinks: Array<{x1:number,y1:number,x2:number,y2:number,endIndex?:number}> = [];
   isShift = false;
   isCtrl = false;
   // live highlights for source/target selections
   highlightedSourceInstanceName: string | null = null;
   highlightedTargetInstanceName: string | null = null;
+  // live highlights for instance→crosspoint links (source always; target only when route reaches target CP)
+  highlightedSourceInstanceLink: { x1:number, y1:number, x2:number, y2:number } | null = null;
+  highlightedTargetInstanceLink: { x1:number, y1:number, x2:number, y2:number } | null = null;
   // routing submit state
   isRouteValid: boolean = false;
   routingHighlightColor = '#39FF14'; // neon green
+  invalidRoutingColor = '#FF3B30';   // red for invalid turns
+  validRoutingTurns: any = {};
+  channelInfo: any = {};
+  currentRouteInfo: any = {};
+
+  // Turn-hint arrows shown around the *current* crosspoint while selecting hops
+  currentTurnHint: {
+    cpId: string | null,
+    colors: { north: string, east: string, south: string, west: string }
+  } = {
+    cpId: null,
+    colors: { north: '#FF3B30', east: '#FF3B30', south: '#FF3B30', west: '#FF3B30' }
+  };
+  turnArrowOffset = 30;   // px distance from the crosspoint box
+  turnArrowFontSize = 80; // arrow size
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `GUI/src/app/canvas/canvas-floorplan-logical-mesh/canvas-floorplan-logical-mesh.component.ts`:
```diff
@@ -271,6 +289,16 @@ export class CanvasFloorplanLogicalMeshComponent implements OnInit, AfterViewIni
     this.canvasLogicalService.refreshCanvasSubject.pipe(takeUntil(this.unsubscribe$)).subscribe(() => {
       this.refreshCanvas();
     });
+    // Listen for a route picked in Mesh Route Viewer and load it for editing
+    this.canvasLogicalService.routeSelectedSubject.pipe(takeUntil(this.unsubscribe$)).subscribe((payload: {
+      source: string;
+      target: string;
+      channel: string;
+      sub_channel: string | number;
+      hops: Array<[number, number]>;
+    }) => {
+      this.ngZone.run(() => this.loadRouteForEditing(payload));
+    });
     this.canvasSelectorsService.drawGroupMemberOutlinesSubject.pipe(takeUntil(this.unsubscribe$)).subscribe(groupName => {
       if (groupName) {
         this.drawGroupMemberOutlines(groupName);
```
### Current source `GUI/src/app/canvas/ui/sidebar/mesh-route-editor/mesh-route-editor.component.ts`
Snapshot: HEAD; SHA-256 `9ab1968c3b0810e010d35cd27efbb2906211f4d75cd34c63eb95d39a52a1383a`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 294, 'Dustin Divis': 6, 'Pawan Kakarla': 6, 'Dustin divis': 22}.
Introduction/rename-follow candidates: 7389f6a0958aecb9e01f7708bd71fa95caa2d584 2025-08-28T04:20:06-05:00 Michael Coulter <michael.coulter@arm.com> delphi routing.
```text
4: import { ProjectService } from 'src/app/project/project.service';
5: import { CanvasLogicalDataService } from 'src/app/canvas/core/services/canvas-logical-data.service';
6: 
7: type RawRoutes = Record<string, // source
8:   Record<string,               // target
9:     Record<string,             // channel (e.g. DAT/SNP/REQ/RSP)
10:       Record<string,           // sub_channel (e.g. "0", "1", ...)
11:         { route: number[][]; scheme?: string; table_entry?: string }
12:       >
13:     >
14:   >
15: >;
16: 
17: export interface MeshRouteRow {
18:   source: string;        // canonical GUI instance name
19:   target: string;        // canonical GUI instance name
20:   sourceCe?: string;     // CE-recognized instance name (key from routes payload)
21:   targetCe?: string;     // CE-recognized instance name (key from routes payload)
22:   sourceLabel: string;   // display label (rtl_name if available)
23:   targetLabel: string;   // display label (rtl_name if available)
24:   channel: string;
25:   sub_channel: string;     // keep server key name
```
### Current source `GUI/src/app/shared/components/routing-scheme-modal/routing-scheme-modal.component.ts`
Snapshot: HEAD; SHA-256 `ac16d037fdb99b63d73244f4673cbe79a7c3ce39671c595ba4a5740a0f79d449`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 125, 'Dustin Divis': 4, 'Pawan Kakarla': 8}.
Introduction/rename-follow candidates: 69c2f5290a8353a3cea9433fa77185a3f6e2ec27 2025-08-12T13:37:07-05:00 Michael Coulter <michael.coulter@arm.com> BRUNEL-3435: Create routes.
```text
1: import { Component, Inject, OnDestroy, OnInit } from '@angular/core';
2: import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
3: import { FormControl, FormGroup } from '@angular/forms';
4: import { ValidatorService } from 'src/app/shared/services/validator.service';
5: import { CanvasLogicalDataService } from 'src/app/canvas/core/services/canvas-logical-data.service';
6: import { Subject } from 'rxjs';
7: import { takeUntil } from 'rxjs/operators';
8: 
9: @Component({
10:     selector: 'app-routing-scheme-modal',
11:     templateUrl: './routing-scheme-modal.component.html',
12:     styleUrls: ['./routing-scheme-modal.component.css'],
```
```text
15: export class RoutingSchemeModalComponent implements OnInit, OnDestroy {
16:   // Hold the selected *key* (e.g., "west_first")
17:   selectedRoutingScheme: string = this.data.options?.[0]?.key;
18:   // Channel/sub-channel selections
19:   selectedChannel: string = this.data.channelInfo?.channels?.[0] ?? null;
20:   selectedSubChannels: number[] = (this.data.channelInfo?.sub_channels?.length ? [...this.data.channelInfo.sub_channels] : []);
21:   // Base path for instruction images (served from Angular assets)
22:   readonly imageBasePath = 'assets/images/valid_routing_turns';
23:   viewAll = false;
24:   baseRoutingScheme: Record<string, Record<number | string, string>> | null = null;
25: 
26:   private readonly destroy$ = new Subject<void>();
27:   private readonly schemeDisplayMap = new Map<string, string>();
28: 
29:   constructor(
30:     public dialogRef: MatDialogRef<RoutingSchemeModalComponent>,
31:     private validatorService: ValidatorService,
32:     private readonly canvasLogicalDataService: CanvasLogicalDataService,
33:     @Inject(MAT_DIALOG_DATA) public data: {
34:       options: { key: string; display: string }[],
35:       channelInfo?: { channels: string[]; sub_channels: number[] }
36:     }
37:   ) {
38:     if (Array.isArray(this.data?.options)) {
39:       for (const option of this.data.options) {
```

## desktop-dev

### Commit 91f84a5f7c53f21ede6eee30274358d3b6c5abbb
Author: Michael Coulter <michael.coulter@arm.com>; author date 2022-09-06T15:33:26-05:00; reachable from selected HEAD: True.
Subject: Add gui_setup_mac.sh script
Change-Ids: I446b43e69d8070f2a6a2795cc2a8e7458bad349b.
Diff excerpt, `gui_setup_mac.sh`:
```diff
@@ -0,0 +1,18 @@
+#!/bin/bash
+cd CE
+virtualenv venv
+source venv/bin/activate
+pip3 install -r dev_requirements.txt
+pip3 install -e .
+pip3 list
+deactivate
+cd ..
+cd brunel
+npm install
+./node_modules/.bin/electron-rebuild
+cd ../GUI
+npm install
+mkdir node_modules/arm-design-system
+mkdir node_modules/arm-design-system/core
+cp -a lib/core/ node_modules/arm-design-system/core
+npm run build
```
### Commit 1c5488ad4df90b335e39fe987368c519d5c9cac3
Author: Michael Coulter <michael.coulter@arm.com>; author date 2025-01-30T15:17:53-06:00; reachable from selected HEAD: True.
Subject: Update main.js with various GPU/rendering/JavaScript settings to increase app performance
Change-Ids: Ia8ba55d3254f9e553cbc5e2ebf0dcb637a376f29.
Diff excerpt, `brunel/main.js`:
```diff
@@ -15,13 +15,58 @@
 *
 ***************************************************************************/
 
-const electron = require('electron')
-const app = electron.app
-const BrowserWindow = electron.BrowserWindow
+const electron = require('electron');
+const app = electron.app;
+const BrowserWindow = electron.BrowserWindow;
+
+// Electron settings for increased performance
+// Graphics and GPU Optimization
+app.commandLine.appendSwitch('enable-gpu');
+app.commandLine.appendSwitch('enable-gpu-rasterization');
+// Enables "Out-of-Process Rasterization" (OOP-R), where rasterization (rendering of individual graphical elements) is performed in a dedicated GPU process instead of the main rendering process.
 app.commandLine.appendSwitch('enable-features', 'CanvasOopRasterization');
+// Ensures that all GPU features are enabled, even on systems where they are blacklisted.
+app.commandLine.appendSwitch('ignore-gpu-blacklist');
+// Optimizes GPU memory usage by enabling zero-copy rendering for images and videos.
+app.commandLine.appendSwitch('enable-zero-copy');
+// Disables the GPU shader cache to reduce memory usage.
+app.commandLine.appendSwitch('disable-gpu-program-cache');
+// Uses native GPU memory buffers for improved texture sharing.
+app.commandLine.appendSwitch('enable-native-gpu-memory-buffers');
+// Increases the number of active WebGL contexts allowed.
+app.commandLine.appendSwitch('max-active-webgl-contexts', '16');
+// Forces GPU rasterization for rendering, reducing CPU load.
 app.commandLine.appendSwitch('enable-gpu-rasterization');
-app.commandLine.appendSwitch('disable-software-rasterizer', 'false');
-const ipcMain = electron.ipcMain
+// Explicitly sets the maximum GPU memory available (adjust value as needed).
[hunk excerpt ends; remaining lines omitted]
```
Diff excerpt, `brunel/main.js`:
```diff
@@ -29,7 +74,7 @@ let fresh = false;
 
 // const options = {mode: 'json'}
 //let shell = new pythonShell.PythonShell('test.py', { mode: 'json' });
-let shell = null
+let shell = null;
 const url = require('url');
 const path = require('path');
 const fs = require('fs');
```
Diff excerpt, `brunel/main.js`:
```diff
@@ -72,12 +117,12 @@ if (global.devMode) {
 }
 
 if(process.env.STANDALONE === true){
-  let assetsPath = path.dirname(getResourceFilePath('tpip'))
-   process.env.LD_LIBRARY_PATH = assetsPath + '/python/Python-3.7.1/lib:assetsPath/python/Python-3.7.1/extlib/lib;' + assetsPath +'/../shared_lib'
-   process.env.PYTHONPATH = assetsPath + '/python_jsonschema:' + assetsPath + '/python/Python-3.7.1/lib/python3.7/site-packages:' + assetsPath + '/python/Python-3.7.1/lib/python3.7:' + assetsPath + '/CE'
-   process.env.PATH = assetsPath + '/ruby/Ruby-2.5.3/bin:' + assetsPath + '/python/Python-3.7.1/bin:' + assetsPath +'../../../../../brunel-linux-x64:' + assetsPath + '/perl/perl-5.18.1/bin:/usr/bin:/bin'
-   process.env['PATH_RUBY_3.2.2'] = assetsPath + '/ruby/Ruby-3.2.2/bin:' + assetsPath + '/python/Python-3.7.1/bin:+ ' + assetsPath + '../../../../../brunel-linux-x64:' + assetsPath + '/perl/perl-5.18.1/bin:/usr/bin:/bin'
-   process.env.PERL5LIB = assetsPath + '/perl/perl-5.18.1/lib/site_perl/5.18.1:' + assetsPath + '/perl/perl-5.18.1/lib/perl5:' + assetsPath + '/perl/perl-5.18.1/lib/5.18.1:' + assetsPath + '/5.18'
+  let assetsPath = path.dirname(getResourceFilePath('tpip'));
+  process.env.LD_LIBRARY_PATH = assetsPath + '/python/Python-3.7.1/lib:assetsPath/python/Python-3.7.1/extlib/lib;' + assetsPath +'/../shared_lib';
+  process.env.PYTHONPATH = assetsPath + '/python_jsonschema:' + assetsPath + '/python/Python-3.7.1/lib/python3.7/site-packages:' + assetsPath + '/python/Python-3.7.1/lib/python3.7:' + assetsPath + '/CE';
+  process.env.PATH = assetsPath + '/ruby/Ruby-2.5.3/bin:' + assetsPath + '/python/Python-3.7.1/bin:' + assetsPath +'../../../../../brunel-linux-x64:' + assetsPath + '/perl/perl-5.18.1/bin:/usr/bin:/bin';
+  process.env['PATH_RUBY_3.2.2'] = assetsPath + '/ruby/Ruby-3.2.2/bin:' + assetsPath + '/python/Python-3.7.1/bin:+ ' + assetsPath + '../../../../../brunel-linux-x64:' + assetsPath + '/perl/perl-5.18.1/bin:/usr/bin:/bin';
+  process.env.PERL5LIB = assetsPath + '/perl/perl-5.18.1/lib/site_perl/5.18.1:' + assetsPath + '/perl/perl-5.18.1/lib/perl5:' + assetsPath + '/perl/perl-5.18.1/lib/5.18.1:' + assetsPath + '/5.18';
 
 }
 
```
### Commit cbf07500fb644e609f85b386cdba9adfe8d295ae
Author: Michael Coulter <michael.coulter@arm.com>; author date 2026-03-02T19:48:04-06:00; reachable from selected HEAD: True.
Subject: BRUNEL-3756, BRUNEL-4050: GUI quit issues
Change-Ids: I8ab645d11211d747514dc73c60f4c160aadd0105.
Diff excerpt, `brunel/main.js`:
```diff
@@ -2098,10 +2098,15 @@ function createWindow() {
     mainWindow.webContents.openDevTools();
   }
 
+
   mainWindow.on('close', async (e) => {
-    if (global.confirmAppClose && global.hasUnsavedChanges) {
-      e.preventDefault(); // prevent the app from closing immediately
+    if (isQuitting) return; // already in quit flow
+
+    const isMac = process.platform === 'darwin';
+    const shouldConfirm = global.confirmAppClose && global.hasUnsavedChanges;
 
+    if (shouldConfirm) {
+      e.preventDefault(); // pause closing until user decides
       const { response } = await dialog.showMessageBox(mainWindow, {
         type: 'question',
         buttons: ['Yes', 'Cancel'],
```
Diff excerpt, `brunel/main.js`:
```diff
@@ -2109,30 +2114,19 @@ function createWindow() {
         title: 'Confirm Exit',
         message: 'There are unsaved changes which will be lost.\nAre you sure you want to close the application?',
       });
+      if (response !== 0) return; // user canceled; keep app open
+      // user confirmed; fall through to platform behavior
+    }
 
-      if (response === 0) {
-        // user clicked 'Yes'
-        mainWindow.destroy(); // proceed to close the window
-      }
-      // else, do nothing (cancel close)
-
-      /*
--      buttons: ['Close anyway', 'Save & Close', 'Cancel']
--      switch (choice) {
--        case 0: // 'Close anyway' - close app and lose unsaved changes
--          break;
--        case 1: // 'Save & Close' - save changes and close app
--          // TODO: Save design (export_design), then close app
--          break;
--        case 2: // 'Cancel' - do NOT close app
--          e.preventDefault();
--          break;
--        default:
--          e.preventDefault();
--      } */
+    if (isMac) {
+      e.preventDefault();    // don’t quit app, just close window
+      mainWindow.destroy();  // closes window; app stays running
+    } else {
[hunk excerpt ends; remaining lines omitted]
```
### Current source `gui_setup_mac.sh`
Snapshot: HEAD; SHA-256 `6c5cae51c0a0a0cc55473c3794dc503c8809d9bae38e9468eabf8745a0c49d78`.
Surviving-line author counts (attribution context only): {'Michael Coulter': 20, 'Liza Dayoub': 3}.
Introduction/rename-follow candidates: 91f84a5f7c53f21ede6eee30274358d3b6c5abbb 2022-09-06T15:33:26-05:00 Michael Coulter <michael.coulter@arm.com> Add gui_setup_mac.sh script.
```text
5: pip3 install -r dev_requirements.txt
6: pip3 install -e .
7: pip3 list
8: python setup.py build_ext --inplace
9: python setup.py bdist_wheel
10: deactivate
11: cd ..
12: cd brunel
13: npm install
14: ./node_modules/.bin/electron-rebuild
15: cd ../GUI
16: # clear the GUI install, but keep the lockfile so dependency resolution stays pinned
17: rm -rf node_modules/
18: npm cache clean --force
19: #
20: npm install
21: mkdir -p node_modules/arm-design-system/core
22: cp -a lib/core/. node_modules/arm-design-system/core/
23: npm run build
```
