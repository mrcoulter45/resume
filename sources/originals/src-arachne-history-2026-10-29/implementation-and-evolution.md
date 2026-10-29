# Current implementations and historical attribution

PRIVATE source evidence captured 2026-10-29 at HEAD c13c1beb89b07b46afd963706bb5d941ea4d36d0.

Current excerpts are from immutable Git blobs, with original one-based source lines. SHA-256 hashes cover complete raw blobs. Non-UTF-8 bytes are escaped; source line endings are normalized in this text extraction. Surviving-line blame is context, not an ownership percentage or lifetime contribution measure.

## HEAD:AGENTS.md

Blob SHA-256: decc14c7a744de84f6341f75e3c3ccac230b88abab65f1569b3130d1f3502a1d; total source lines: 22.

```text
Source range 1-22
1: ## NoC Repo
2: The NoC is a systemverilog interconnect IP that connects masters/requesters to subordinates/slaves with a flexible topology. It supports a wide variety of protocols
3: 
4: ## Directory Structure
5: 
6: The PROJ_HOME can be found by running `git rev-parse --show-toplevel`
7: 
8: - Config locations: $PROJ_HOME/configs_iyml - this describes how the config will look like
9: - Rendered config locations: $PROJ_HOME/configs/ - this is an
10: - Top level control files: $PROJ_HOME/logical/noc_arachne/.control_files
11: - Customer facing documents (TRM, CIM) - /projects/ssg/pj10000069/docs_for_codex; use the TRM first for technical reference details such as registers, programming sequences, and architectural behavior, and use the CIM first for customer integration guidance and integration requirements.
12: - AMBA specs - use the downloaded PDFs in /projects/ssg/pj10000069/docs_for_codex/AMBA first. The directory includes a `downloaded_specs.tsv` manifest and the latest downloaded CHI, AXI, AHB, APB, AXI-Stream, CHI-C2C, LPI, and related AMBA specs. If the local files are missing or unusable, fall back to https://www.arm.com/architecture/system-architectures/amba/amba-specifications.
13: 
14: ## Top level flow
15: - Configs are rendered through the param engine step. This takes an iyaml as an input, and expands it into stitched RTL and creates ready-to-use testbench collatteral. There is a skill for this
16: 
17: ## Running commands that need environment variables/aliases
18: Use the noc-wrapper skill for commands that depend on the NoC environment, aliases, or modules.
19: The noc-wrapper skill describes a wrapper script that sources the sourceme and can be appended to other commands
20: 
21: ## Feedback
22: - If anything is surprising or difficult, especially related to infrastructure, record it in `feedback.md` with the date, task context, what was surprising, what would have helped earlier, and what to do differently next time.
```

## HEAD:logical/noc_arachne/.control_files/chariot_fault_injection.ctrl

Blob SHA-256: 4266fb2cf4de4a9b5b20ee625a9716ef6cf290e7a3907590d22dad87651a4d6b; total source lines: 15.

```text
Source range 1-15
1: Phase Param_Engine 24h
2: ae param_engine --config="brunel_1x1_ACE5Lite_AXI5_chariot" --chariot_b
3: #ae param_engine --config=partner_0_b0_multiport_flit_optimized
4: 
5: Phase get_fault_sites 24h
6: ae get_fault_sites --config="brunel_1x1_ACE5Lite_AXI5_chariot"
7: #ae get_fault_sites --config=partner_0_b0_multiport_flit_optimized
8: 
9: Phase Scenario_Generation 24h
10: ae scenario_generation --config="brunel_1x1_ACE5Lite_AXI5_chariot" --test=constrained_random --set=basic --scenario=default --junit
11: #ae scenario_generation --parse_only --config="partner_0_b0_multiport_flit_optimized" --test=constrained_random --set=basic --scenario=default --junit
12: 
13: Phase Simulation 8h
14: ae simulate --inject_fault --tb=top --config="brunel_1x1_ACE5Lite_AXI5_chariot" --test=constrained_random --set=basic --scenario=default_000 --run_time=120 --uvm=num_txs=1000 --junit --mem=16000 --maxlen=360 --chariot_b --repeat=100 --rindex=200 --fullacc
15: 
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_ahb_hang_detector.sv

Blob SHA-256: ff87cb87b0ef2b424d38407a7960d569d91cb3e03112c7869176ef9eb59f1354; total source lines: 55.

```text
Source range 1-55
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot AHB hang detector
17: //------------------------------------------------------------------------------
18: module chariot_ahb_hang_detector #(NUM_CLK_CYCLES_HANG = -1) (
19:   input clk_i,
20:   input reset_i,
21:   input ready_i,
22:   output logic error_o
23: );
24: 
25:   logic [31:0] cycle_count;
26:   logic [31:0] cycle_count_reg;
27: 
28:   always @(*) begin
29:     if (reset_i) begin
30:       cycle_count = cycle_count_reg;
31:       error_o = 0;
32:       if (~ready_i) begin
33:         cycle_count = cycle_count + 1;
34:         if (cycle_count >= NUM_CLK_CYCLES_HANG) begin
35:           error_o = 1;
36:         end
37:       end
38:       else begin
39:         cycle_count = 0;
40:       end
41:     end else begin
42:       cycle_count = 0;
43:       error_o = 0;
44:     end
45:   end
46: 
47:   always @(posedge clk_i) begin
48:     if (reset_i) begin
49:       cycle_count_reg <= cycle_count;
50:     end
51:     else begin
52:       cycle_count_reg <= 0;
53:     end
54:   end
55: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_read.sv

Blob SHA-256: 67080da6b0e315b5b3a649e49b27a9929bb2a78399059af002b4b90138cfe3b5; total source lines: 208.

```text
Source range 1-208
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot AXI hang detector
17: //------------------------------------------------------------------------------
18: module chariot_axi_hang_detector_read #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
19:   input clk_i,
20:   input resetn_i,
21:   input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] aid_i,
22:   input avalid_i,
23:   input aready_i,
24:   input [7:0] alength_i,
25:   input [2:0] asize_i,
26:   input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] id_i,
27:   input valid_i,
28:   input last_i,
29:   input ready_i,
30:   output logic error_1_o,
31:   output logic error_2_o
32: );
33: 
34:   logic [COUNTER_WIDTH-1:0] counter;
35:   logic [COUNTER_WIDTH-1:0] counter_reg;
36:   logic [TRACKER_LENGTH-1:0] tracker_valid_mask_inverted;
37:   logic [TRACKER_LENGTH-1:0] insert_index_encoded;
38:   logic [TRACKER_LENGTH-1:0] insert_index;
39:   logic remove_complete;
40:   logic [TRACKER_LENGTH-1:0] remove_index;
41:   logic [TRACKER_LENGTH-1:0] remove_mask;
42:   
43:   
44:   // a full tracker entry consists of the tracker_valid, tracker_id, and the tracker_timestamp
45:   logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids;
46:   logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids_reg;
47:   logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids [0:TRACKER_LENGTH-1];
48:   logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids_reg [0:TRACKER_LENGTH-1];
49:   logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps [0:TRACKER_LENGTH-1];
50:   logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps_reg [0:TRACKER_LENGTH-1];
51:   logic [((ID_WIDTH > 0) ? 11 : 0):0] tracker_bytecounter [0:TRACKER_LENGTH-1];
52:   logic [((ID_WIDTH > 0) ? 11 : 0):0] tracker_bytecounter_reg [0:TRACKER_LENGTH-1];
53:   logic [((ID_WIDTH > 0) ? (COUNTER_WIDTH-1) : 0):0] tracker_timeid [0:TRACKER_LENGTH-1];
54:   logic [((ID_WIDTH > 0) ? (COUNTER_WIDTH-1) : 0):0] tracker_timeid_reg [0:TRACKER_LENGTH-1];
55:   logic [((ID_WIDTH > 0) ? (COUNTER_WIDTH-1) : 0):0] oldest_transfer;
56:   integer i;
57:   integer j;
58:   integer k;
59:   integer a;
60:   integer b;
61: 
62:   // if avalid_i && aready_i, insert into a non-valid tracker entry and mark valid
63:   // if valid_i && last_i && ready_i, find the valid entries in the tracker with matching IDs, and remove the oldest one
64: 
65:   always @(*) begin
66:     error_2_o = 0;
67:     oldest_transfer = 0;
68:     if (~resetn_i) begin
69:       counter = 0;
70:       insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
71:       tracker_valid_mask_inverted = 0;
72:       remove_complete = 0;
73:       remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
74:       remove_mask = 0;
75:       tracker_valids = 0;
76:       insert_index_encoded = 0;
77: 
78:     end else begin
79:       counter = counter_reg + 1;
80:       insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
81:       tracker_valid_mask_inverted = ~tracker_valids_reg;
82:       remove_complete = 0;
83:       remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
84:       remove_mask = 0;
85:       tracker_valids = tracker_valids_reg;
86:       for (i=0; i<TRACKER_LENGTH; i=i+1) begin
87:         tracker_ids[i] = tracker_ids_reg[i];
88:         tracker_timestamps[i] = tracker_timestamps_reg[i];
89:         tracker_bytecounter[i] = tracker_bytecounter_reg[i];
90:         tracker_timeid[i] = tracker_timeid_reg[i];
91:       end
92:       // inserting into the tracker
93:       // get lowest index that is not valid
94:       insert_index_encoded = tracker_valid_mask_inverted & ~(tracker_valid_mask_inverted-1);
95:       for (i=0; i<TRACKER_LENGTH; i=i+1) begin
96:         if (insert_index_encoded[i]) begin
97:           insert_index = i;
98:         end
99:       end
100:       if (avalid_i && aready_i) begin
101:         tracker_valids[insert_index] = 1;
102:         tracker_ids[insert_index] = aid_i;
103:         tracker_timestamps[insert_index] = counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2];
104:         tracker_bytecounter[insert_index] = alength_i; // +1 here??
105:         tracker_timeid[insert_index] = counter_reg[COUNTER_WIDTH-1:0];
106:       end
107:       // removing from tracker
108:       // if multiple entries in the tracker are valid, have the same ID, and have the same timestamp, the entry with the largest index will be removed
109:       // check to see which tracker entries are valid and have a matching rid
110:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
111:         if (tracker_valids_reg[j] && tracker_ids_reg[j] == id_i) begin
112:           if(counter_reg - tracker_timeid_reg[j] > oldest_transfer) begin
113:             oldest_transfer = counter_reg - tracker_timeid_reg[j];
114:             b = j;
115:           end
116:         end
117:       end
118:       if (tracker_valids_reg[b] && tracker_ids_reg[b] == id_i) begin
119:         remove_mask[b] = 1;
120:       end
121:       // check to see which valid tracker entries with matching rids are the oldest
122:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
123:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+1)%4 && remove_mask[j]) begin
124:           remove_complete = 1;
125:           remove_index = j;
126:         end
127:       end
128:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
129:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+2)%4 && remove_mask[j] && !remove_complete) begin
130:           remove_complete = 1;
131:           remove_index = j;
132:         end
133:       end
134:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
135:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+3)%4 && remove_mask[j] && !remove_complete) begin
136:           remove_complete = 1;
137:           remove_index = j;
138:         end
139:       end
140:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
141:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+4)%4 && remove_mask[j] && !remove_complete) begin
142:           remove_index = j;
143:         end
144:       end
145:       if (valid_i && last_i && ready_i && (remove_index >= 0 && remove_index < TRACKER_LENGTH)) begin
146: 
147:         if(tracker_bytecounter_reg[remove_index] == 0) begin
148:           tracker_valids[remove_index] = 0;
149:         end
150: 
151:         if (tracker_bytecounter_reg[remove_index] < 0) begin
152:             error_2_o = 1;
153:         end
154:       end
155:       else if (valid_i && ready_i) begin
156:         tracker_bytecounter[remove_index] = tracker_bytecounter[remove_index] - 1;
157:       end
158:     end
159:   end
160: 
161:   // hang detection
162:   `define IDLE 0
163:   `define CHECK_FOR_HANG 1
164:   logic hang_detection_state;
165:   logic hang_detection_state_reg;
166: 
167:   always @(*) begin
168:     error_1_o = 0;
169:     if (~resetn_i) begin
170:       hang_detection_state = `IDLE;
171:     end else begin
172:       if (hang_detection_state_reg == `IDLE) begin
173:         hang_detection_state = `IDLE;
174:         if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
175:           hang_detection_state = `CHECK_FOR_HANG;
176:         end
177:       end else if (hang_detection_state_reg == `CHECK_FOR_HANG) begin
178:         hang_detection_state = `IDLE;
179:         for (k=0; k<TRACKER_LENGTH; k=k+1) begin
180:           // if any tracker entry is valid and has a timestamp that matches the most significant 2 bits of the counter, throw hang error
181:           if (tracker_valids_reg[k] && tracker_timestamps_reg[k]==counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
182:             error_1_o = 1;
183:           end
184:         end
185:       end
186:     end
187:   end
188: 
189:   always @(posedge clk_i or negedge resetn_i) begin
190:     if (~resetn_i) begin
191:       counter_reg <= 0;
192:       hang_detection_state_reg <= `IDLE;
193:       tracker_valids_reg <= 0;
194:       
195:     end else begin
196:       counter_reg <= counter;
197:       hang_detection_state_reg <= hang_detection_state;
198:       tracker_valids_reg <= tracker_valids;
199:       for (a=0; a<TRACKER_LENGTH; a=a+1) begin
200:         tracker_ids_reg[a] <= tracker_ids[a];
201:         tracker_timestamps_reg[a] <= tracker_timestamps[a];
202:         tracker_bytecounter_reg[a] <= tracker_bytecounter[a];
203:         tracker_timeid_reg[a] <= tracker_timeid[a];
204:       end
205:     end
206:   end
207: 
208: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_write.sv

Blob SHA-256: 348f0d6339a956a6fa90812e813e160d0a5bd438528cee5f54d41df8848799c7; total source lines: 171.

```text
Source range 1-171
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot AXI hang detector
17: //------------------------------------------------------------------------------
18: module chariot_axi_hang_detector_write #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
19:   input clk_i,
20:   input reset_i,
21:   input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] aid_i,
22:   input avalid_i,
23:   input aready_i,
24:   input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] id_i,
25:   input valid_i,
26:   input last_i,
27:   input ready_i,
28:   output logic error_o
29: );
30: 
31:   logic [COUNTER_WIDTH-1:0] counter;
32:   logic [COUNTER_WIDTH-1:0] counter_reg;
33:   logic [TRACKER_LENGTH-1:0] tracker_valid_mask_inverted;
34:   logic [TRACKER_LENGTH-1:0] insert_index_encoded;
35:   logic [TRACKER_LENGTH-1:0] insert_index;
36:   logic remove_complete;
37:   logic [TRACKER_LENGTH-1:0] remove_index;
38:   logic [TRACKER_LENGTH-1:0] remove_mask;
39:   // a full tracker entry consists of the tracker_valid, tracker_id, and the tracker_timestamp
40:   logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids;
41:   logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids_reg;
42:   logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids [0:TRACKER_LENGTH-1];
43:   logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids_reg [0:TRACKER_LENGTH-1];
44:   logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps [0:TRACKER_LENGTH-1];
45:   logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps_reg [0:TRACKER_LENGTH-1];
46:   integer i;
47:   integer j;
48:   integer k;
49:   integer a;
50: 
51:   // if avalid_i && aready_i, insert into a non-valid tracker entry and mark valid
52:   // if valid_i && last_i && ready_i, find the valid entries in the tracker with matching IDs, and remove the oldest one
53: 
54:   always @(*) begin
55:     if (reset_i) begin
56:       counter = counter_reg + 1;
57:       insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
58:       tracker_valid_mask_inverted = ~tracker_valids_reg;
59:       remove_complete = 0;
60:       remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
61:       remove_mask = 0;
62:       tracker_valids = tracker_valids_reg;
63:       for (i=0; i<TRACKER_LENGTH; i=i+1) begin
64:         tracker_ids[i] = tracker_ids_reg[i];
65:         tracker_timestamps[i] = tracker_timestamps_reg[i];
66:       end
67:       // inserting into the tracker
68:       // get lowest index that is not valid
69:       insert_index_encoded = tracker_valid_mask_inverted & ~(tracker_valid_mask_inverted-1);
70:       for (i=0; i<TRACKER_LENGTH; i=i+1) begin
71:         if (insert_index_encoded[i]) begin
72:           insert_index = i;
73:         end
74:       end
75:       if (avalid_i && aready_i) begin
76:         tracker_valids[insert_index] = 1;
77:         tracker_ids[insert_index] = aid_i;
78:         tracker_timestamps[insert_index] = counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2];
79:       end
80:       // removing from tracker
81:       // if multiple entries in the tracker are valid, have the same ID, and have the same timestamp, the entry with the largest index will be removed
82:       // check to see which tracker entries are valid and have a matching rid
83:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
84:         if (tracker_valids_reg[j] && tracker_ids_reg[j] == id_i) begin
85:           remove_mask[j] = 1;
86:         end
87:       end
88:       // check to see which valid tracker entries with matching rids are the oldest
89:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
90:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+1)%4 && remove_mask[j]) begin
91:           remove_complete = 1;
92:           remove_index = j;
93:         end
94:       end
95:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
96:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+2)%4 && remove_mask[j] && !remove_complete) begin
97:           remove_complete = 1;
98:           remove_index = j;
99:         end
100:       end
101:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
102:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+3)%4 && remove_mask[j] && !remove_complete) begin
103:           remove_complete = 1;
104:           remove_index = j;
105:         end
106:       end
107:       for (j=0; j<TRACKER_LENGTH; j=j+1) begin
108:         if (tracker_timestamps_reg[j]==(counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]+4)%4 && remove_mask[j] && !remove_complete) begin
109:           remove_index = j;
110:         end
111:       end
112:       if (valid_i && last_i && ready_i && (remove_index >= 0 && remove_index < TRACKER_LENGTH)) begin
113:         tracker_valids[remove_index] = 0;
114:       end
115:     end else begin
116:       counter = 0;
117:       insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
118:       tracker_valid_mask_inverted = 0;
119:       remove_complete = 0;
120:       remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
121:       remove_mask = 0;
122:       tracker_valids = 0;
123:       insert_index_encoded = 0;
124:     end
125:   end
126: 
127:   // hang detection
128:   `define IDLE 0
129:   `define CHECK_FOR_HANG 1
130:   logic hang_detection_state;
131:   logic hang_detection_state_reg;
132: 
133:   always @(*) begin
134:     error_o = 0;
135:     if (reset_i) begin
136:       if (hang_detection_state_reg == `IDLE) begin
137:         hang_detection_state = `IDLE;
138:         if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
139:           hang_detection_state = `CHECK_FOR_HANG;
140:         end
141:       end else if (hang_detection_state_reg == `CHECK_FOR_HANG) begin
142:         hang_detection_state = `IDLE;
143:         for (k=0; k<TRACKER_LENGTH; k=k+1) begin
144:           // if any tracker entry is valid and has a timestamp that matches the most significant 2 bits of the counter, throw hang error
145:           if (tracker_valids_reg[k] && tracker_timestamps_reg[k]==counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
146:             error_o = 1;
147:           end
148:         end
149:       end
150:     end else begin
151:       hang_detection_state = `IDLE;
152:     end
153:   end
154: 
155:   always @(posedge clk_i or negedge reset_i) begin
156:     if (reset_i) begin
157:       counter_reg <= counter;
158:       hang_detection_state_reg <= hang_detection_state;
159:       tracker_valids_reg <= tracker_valids;
160:       for (a=0; a<TRACKER_LENGTH; a=a+1) begin
161:         tracker_ids_reg[a] <= tracker_ids[a];
162:         tracker_timestamps_reg[a] <= tracker_timestamps[a];
163:       end
164:     end else begin
165:       counter_reg <= 0;
166:       hang_detection_state_reg <= `IDLE;
167:       tracker_valids_reg <= 0;
168:     end
169:   end
170: 
171: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh

Blob SHA-256: 823d82c0e53edc76b1453dfc1059e1ed50e718d31efc36da588aafd306aaa997; total source lines: 45.

```text
Source range 1-45
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2015 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot package
17: //------------------------------------------------------------------------------
18: 
19: `ifndef CHARIOT_PKG__SV
20: `define CHARIOT_PKG__SV
21: 
22: `include "chariot_wreq_parity_generator.sv"
23: `include "chariot_wreq_parity_checker.sv"
24: `include "chariot_ahb_req_parity_checker.sv"
25: `include "chariot_wdat_parity_generator.sv"
26: `include "chariot_wdat_parity_checker.sv"
27: `include "chariot_wrsp_parity_generator.sv"
28: `include "chariot_wrsp_parity_checker.sv"
29: `include "chariot_ahb_strobe_generation.sv"
30: `include "chariot_rdat_parity_generator.sv"
31: `include "chariot_rdat_parity_checker.sv"
32: `include "chariot_ahb_hang_detector.sv"
33: `include "chariot_wdat_ecc_generator.sv"
34: `include "chariot_wdat_ecc_checker.sv"
35: `include "chariot_axi_hang_detector_read.sv"
36: `include "chariot_axi_hang_detector_write.sv"
37: 
38: `include "uvm_macros.svh"
39: 
40: package chariot_pkg;
41:   import uvm_pkg::*;
42:   `include "xsni_vseq_synchronizer.sv"
43: endpackage
44: 
45: `endif
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_checker.sv

Blob SHA-256: 3e704891598e4799c6c727b253e1fab493d1702a0a9dcfa523c9379f8d3c675c; total source lines: 39.

```text
Source range 1-39
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot read data channel parity checker
17: //           This channel also carries the read response which is not yet protected
18: //------------------------------------------------------------------------------
19: module chariot_rdat_parity_checker #(DATA_WIDTH = -1, USER_WIDTH = -1, RESP_WIDTH = -1, NUM_SAFETY_BITS = -1) (
20:   input [DATA_WIDTH-1:0] data_i,
21:   input valid_i,
22:   input [USER_WIDTH+RESP_WIDTH-1:0] user_i,
23:   output error_o
24: );
25: 
26:   localparam BITS_TO_PARITY = 4 * NUM_SAFETY_BITS;
27:   localparam DATA_SIZE = DATA_WIDTH / BITS_TO_PARITY;
28:   logic [DATA_SIZE-1:0] parity_check;
29: 
30:   genvar i;
31:   generate
32:     for (i=0; i<DATA_SIZE; i=i+1) begin
33:       assign parity_check[i] = (user_i[(i*NUM_SAFETY_BITS)+(NUM_SAFETY_BITS-1)+RESP_WIDTH] == 0) ? 0 :
34:         ((~^data_i[(i*BITS_TO_PARITY)+(BITS_TO_PARITY-1):i*BITS_TO_PARITY]) == (user_i[i*NUM_SAFETY_BITS+RESP_WIDTH])) ? 0 : 1;
35:     end
36:   endgenerate
37: 
38:   assign error_o = (|parity_check) & valid_i;
39: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_generator.sv

Blob SHA-256: 63ddb92f4c5ef63ac96b72456b4620ed1d0a3998b3c94a57cfa8bdfdafd4e550; total source lines: 35.

```text
Source range 1-35
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot read data channel parity generation
17: //           This channel also carries the read response which is not yet protected
18: //------------------------------------------------------------------------------
19: module chariot_rdat_parity_generator #(DATA_WIDTH = -1, USER_WIDTH = -1, RESP_WIDTH = -1, NUM_SAFETY_BITS = -1) (
20:   input [DATA_WIDTH-1:0] data_i,
21:   input valid_i,
22:   output [USER_WIDTH-1:0] user_o
23: );
24: 
25:   localparam BITS_TO_PARITY = 4 * NUM_SAFETY_BITS;
26:   localparam DATA_SIZE = DATA_WIDTH / BITS_TO_PARITY;
27: 
28:   genvar i;
29:   generate
30:     for (i=0; i<DATA_SIZE; i=i+1) begin
31:       assign user_o[(i*NUM_SAFETY_BITS)+(NUM_SAFETY_BITS-1):(i*NUM_SAFETY_BITS)] = {{1'b1},{(NUM_SAFETY_BITS-2){1'b0}},{~^data_i[(i*BITS_TO_PARITY)+(BITS_TO_PARITY-1):i*BITS_TO_PARITY]}};
32:     end
33:   endgenerate
34: 
35: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv

Blob SHA-256: d1fe0497996139bd76d8036d16d36b40e1b46549fdcd3534d90ff1de69df8d68; total source lines: 86.

```text
Source range 1-86
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot write data ECC checker
17: //------------------------------------------------------------------------------
18: 
19: module chariot_wdat_ecc_checker #(DATA_WIDTH = -1, USER_WIDTH = -1, IS_AHB = -1) (
20:   input [DATA_WIDTH-1:0] data_i,
21:   input [USER_WIDTH-1:0] user_i,
22:   input valid_i,
23:   input [DATA_WIDTH/8-1:0] strb_i,
24:   output logic [(DATA_WIDTH/32)-1:0] uncorrectable_errs_o, // 1 error bit for each set of 32 bits
25:   output logic [(DATA_WIDTH/32)-1:0] correctable_errs_o, // 1 error bit for each set of 32 bits
26:   output logic [(DATA_WIDTH)-1:0]    correctable_bits_vector_o // bit vector that can be inverted with the recieved data to get the corrected data
27: );
28: 
29:   genvar i;
30:   generate
31:     for (i=0; i<DATA_WIDTH/32; i=i+1) begin
32:       logic [63:0] msg;
33:       logic [5:0] index_xor;
34:       integer j;
35:       always @(*) begin
36:         correctable_errs_o[i] = 0;
37:         correctable_bits_vector_o[(i*32)+31:(i*32)] = 32'd0;
38:         uncorrectable_errs_o[i] = 0;
39:         msg = 0;
40:         index_xor = 0; // this represents which bit has been corrupted
41:         j = 0;
42:         //if (valid_i && user_i[i*8+7] && (strb_i[i*4+3:i*4] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
43:         if (valid_i && (strb_i[i*4+3:i*4] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
44:           msg = {
45:             25'b0,                             //msg[63:39]
46:             data_i[(i*32)+31:(i*32)+26],       //msg[38:33]//33
47:             user_i[(i*8)+6],                   //msg[32]
48:             data_i[(i*32)+25:(i*32)+11],       //msg[31:17]
49:             user_i[(i*8)+5],                   //msg[16]
50:             data_i[(i*32)+10:(i*32)+4],        //msg[15:9]
51:             user_i[(i*8)+4],                   //msg[8]
52:             data_i[(i*32)+3:(i*32)+1],         //msg[7:5]
53:             user_i[(i*8)+3],                   //msg[4]
54:             data_i[(i*32)+0],                  //msg[3]
55:             user_i[(i*8)+2],                   //msg[2]
56:             user_i[(i*8)+1],                   //msg[1]
57:             user_i[(i*8)+0]                    //msg[0]
58:           };
59:           // this code is simple and clever, xoring the appropriate bits
60:           for (j=0; j<64; j=j+1) begin
61:             if (msg[j]) begin
62:               index_xor = index_xor ^ j;
63:             end
64:           end
65:           index_xor = ~index_xor; // invert all bits, since we're using odd parity.
66:           if ((user_i[i*8] != ~^msg[63:1]) && (user_i[i*8+7] != ^strb_i[i*4+3:i*4])) begin // if 1 bit has flipped (the lowest parity bit will not match if an odd number of bits have flipped), and strobe parity is correct
67:             correctable_errs_o[i] = 1;
68:             // this section identifies which bit needs to be corrected. 
69:             correctable_bits_vector_o[(i*32)+31:(i*32)] = (index_xor == 6'd3) ? 1       : //if bit position 3 (first data bit) is messed up, invert the first data bit
70:                           (index_xor >= 6'd5  && index_xor <= 6'd7)  ? 1<<(index_xor-4) : //subtract 4 because there are 4 bits of parity in front that need to be accounted for
71:                           (index_xor >= 6'd9  && index_xor <= 6'd15) ? 1<<(index_xor-5) : //subtract 5 because there are 4 bits of parity in front that need to be accounted for
72:                           (index_xor >= 6'd17 && index_xor <= 6'd31) ? 1<<(index_xor-6) : //subtract 6 because there are 4 bits of parity in front that need to be accounted for
73:                           (index_xor >= 6'd33 && index_xor <= 6'd38) ? 1<<(index_xor-7) : //subtract 7 because there are 4 bits of parity in front that need to be accounted for
74:                           32'b0; // error was not a data bit
75: 
76:           end else begin // no errors or 2 bit flips or strobe parity error (note - we can only check strobes in axi protocol, since AHB doesn't have strobes)
77:             if ((index_xor != 6'b0) || ((user_i[i*8+7] == ^strb_i[i*4+3:i*4]) && !IS_AHB)) begin 
78:               uncorrectable_errs_o[i] = 1;
79:             end
80:           end
81:         end
82:       end
83:     end
84:   endgenerate
85: 
86: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv

Blob SHA-256: 96c62a5511e7f72af4cfbdd91706948da38ae13031a37822a850d3029eefdda4; total source lines: 81.

```text
Source range 1-81
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot write data ECC generation
17: //------------------------------------------------------------------------------
18: 
19: module chariot_wdat_ecc_generator #(DATA_WIDTH = -1, USER_WIDTH = -1) (
20:   input [DATA_WIDTH-1:0] data_i,
21:   input [(DATA_WIDTH/8)-1:0] strb_i,
22:   output logic [USER_WIDTH-1:0] user_o
23: );
24: 
25:   parameter DATA_SIZE = DATA_WIDTH / 32;
26: 
27:   // calculate ECC for data_i
28:   genvar i;
29:   generate
30:     for (i=0; i<DATA_SIZE; i=i+1) begin
31:       logic [DATA_WIDTH-1:0] strobed_data;
32:       logic [6:0] parity_bits;
33:       logic [63:0] msg;
34:       logic [5:0] index_xor;
35:       integer j;
36:       integer k;
37:       always @(*) begin
38:         strobed_data = {
39:           ((strb_i[(i*4)+3]) ? data_i[(i*32)+31:(i*32)+24] : 8'b0),
40:           ((strb_i[(i*4)+2]) ? data_i[(i*32)+23:(i*32)+16] : 8'b0),
41:           ((strb_i[(i*4)+1]) ? data_i[(i*32)+15:(i*32)+8]  : 8'b0),
42:           ((strb_i[(i*4)])   ? data_i[(i*32)+7 :(i*32)+0]  : 8'b0)
43:         };
44: 
45:         parity_bits = 0;
46:         msg = {
47:           25'b0,
48:           strobed_data[31:26],
49:           parity_bits[6],
50:           strobed_data[25:11],
51:           parity_bits[5],
52:           strobed_data[10:4],
53:           parity_bits[4],
54:           strobed_data[3:1],
55:           parity_bits[3],
56:           strobed_data[0],
57:           parity_bits[2],
58:           parity_bits[1],
59:           parity_bits[0]
60:         };
61: 
62:         index_xor = 0;
63:         for (j=0; j<64; j=j+1) begin
64:           if (msg[j]) begin
65:             index_xor = index_xor ^ j;
66:           end
67:         end
68: 
69:         // For odd parity, if a bit in index_xor == 0, toggle the corresponding parity_bit
70:         for (k=0; k<6; k=k+1) begin // parity_bits[6:1] (user_o[6:1]) should be inverse of index_xor
71:           if (~index_xor[k]) begin
72:             parity_bits[k+1] ^= 1;
73:           end
74:         end
75:         parity_bits[0] = ~^{strobed_data[31:0],parity_bits[6:1]}; // odd parity of entire message
76:         user_o[(i*8)+7:(i*8)] = {(~^strb_i[i*4+3:i*4]),parity_bits[6:0]};
77:       end
78:     end
79:   endgenerate
80: 
81: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv

Blob SHA-256: 5fe7bcf0686a76711f0aff78a6cc343aca6653993e2cc11977e60ab0d498a32d; total source lines: 47.

```text
Source range 1-47
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot axi/ace write request parity checker
17: //           Protects most of the address, and some other small fields
18: //------------------------------------------------------------------------------
19: 
20: module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
21:     input [ADDR_WIDTH-1:0] addr_i,
22:     input valid_i,
23:     input privileged_i,
24:     input nonsec_i,
25:     input instruction_i,
26:     input bufferable_i,
27:     input modifiable_i,
28:     input allocate_i,
29:     input other_allocate_i,
30:     input [1:0] domain_i,
31:     input [USER_WIDTH-1:0] user_i,
32:     output error_o
33: );
34: 
35:     logic [USER_WIDTH-1:0] err_array;
36:     logic [USER_WIDTH-1:0] user_expected;
37:     logic shareable;
38:     logic lookup;
39: 
40:     assign lookup = allocate_i || other_allocate_i;
41:     assign shareable = (domain_i == 2'b01) || (domain_i == 2'b10);
42: 
43:     logic [ADDR_WIDTH-16:0] protectable_value;
44:     assign protectable_value = {addr_i[ADDR_WIDTH-1:15]};
45:     assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(privileged_i ^ instruction_i ^ modifiable_i ^ bufferable_i ^ allocate_i ^ lookup ^ shareable ^ (^protectable_value))}};
46:     assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
47: endmodule
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv

Blob SHA-256: 4c80de73106f025fec0f671ecbb319489b8d26119ec559fec23ae389c89d90aa; total source lines: 38.

```text
Source range 1-38
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2020 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must  be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot write request parity generation
17: //           protects most of the address, and a few other fields
18: //------------------------------------------------------------------------------
19: 
20: module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
21:     input [ADDR_WIDTH-1:0]  addr_i,
22:     input                   privileged_i,
23:     input                   nonsec_i,
24:     input                   instruction_i,
25:     input                   bufferable_i,
26:     input                   modifiable_i,
27:     input                   lookup_i,
28:     input                   allocate_i,
29:     input                   shareable_i,
30:     input [USER_WIDTH-1:0]  user_i, //currently unused, but will be required if customer wants additional user bits
31:     output [USER_WIDTH-1:0] user_o
32: );
33: 
34:     logic [ADDR_WIDTH-16:0] protectable_value;
35:     assign protectable_value = {addr_i[ADDR_WIDTH-1:15]};
36:     assign user_o = {{USER_WIDTH-1{1'b0}}, {~(privileged_i ^ instruction_i ^ bufferable_i ^ modifiable_i ^ lookup_i ^ allocate_i ^ shareable_i ^ (^protectable_value))}};
37: 
38: endmodule
```

## HEAD:logical/shared/scripts/end_to_end/load_brunel.sh

Blob SHA-256: 619806951104271a65fad85cea20505a348b83329a31d22ff970293affec7327; total source lines: 6.

```text
Source range 1-6
1: #!/bin/tcsh
2: 
3: setenv BRUNEL_VERSION "2026.02.01dev"
4: setenv SYNTH_ENGINE "/arm/tools/arm/brunel/${BRUNEL_VERSION}/linux64"
5: module load eda arm/brunel/${BRUNEL_VERSION}
6: 
```

## HEAD:logical/shared/scripts/fusa/qverify_get_flops.tcl

Blob SHA-256: a0b5da04e218b6a3c6d0058cb1077ae6dad548cd4008c0a932f3749a0fa31946; total source lines: 180.

```text
Source range 1-180
1: #proc printArray { outputFile reg_name array_size max_array_index min_array_index current_array_index } {
2: proc printArray { flopListName reg_name array_size max_array_index min_array_index current_array_index } {
3:   upvar $flopListName flopList
4: 
5:   #create the flop name
6:   set index 0
7:   set flop_name $reg_name
8:   set qverify_internal_flop_name $reg_name
9:   while { $index < $array_size } {
10:     set qverify_internal_flop_name "$qverify_internal_flop_name\[[lindex $current_array_index $index]\]"
11:     set flop_name "$flop_name\([lindex $current_array_index $index]\)"
12:     set index [expr $index + 1]
13:   }
14:   if {[Query [GetNet $qverify_internal_flop_name] isReg]} {
15:     lappend flopList $flop_name
16: #    puts $outputFile $flop_name
17:   }
18: 
19:   # pick the next entry to write
20:   set next_index $current_array_index
21:   set index 0
22:   while { $index < $array_size } {
23:     if {[lindex $current_array_index $index] == [lindex $max_array_index $index]} {
24:       lset next_index $index [lindex $min_array_index $index]
25:       set index [expr $index + 1] 
26:     } else {
27:       lset next_index $index [expr [lindex $current_array_index $index] + 1]
28: #      printArray $outputFile $reg_name $array_size $max_array_index $min_array_index $next_index
29:       printArray "flopList" $reg_name $array_size $max_array_index $min_array_index $next_index
30:       break
31:     }
32:   }
33: }
34: 
35: #proc dumpFlops { module outputFile } {
36: proc dumpFlops { module flopListName } {
37:   namespace import -force Netlist::*
38:   upvar $flopListName flopList
39:   set nets [GetNets $module]
40:   while { [set net [GetNext $nets]] != "" } {
41:     # Get flipflops - scan all nets in this instance and only dump the register nets
42:     if {[Query $net isInternal] || ![Query $net isReg] } { continue }
43: 
44:     # get information about the flop (width, name, type) and make sure it's expected
45:     # note type specifies how many dimensions it is (1 bit signal, array, 2d array, etc)
46:     set reg [GetHdlPath $net]
47:     set width [GetNetWidth $net]
48:     set type [GetNetDataTypeName $net]
49:     if {[string first "logic" $type] == -1} {
50:       if {[string first "scalar" $type] == -1} {
51:         echo "reg is $reg, width is $width, type is $type"
52:         continue
53:       }
54:     }
55:     set type_array [split $type \[]
56:     set type_array_length [llength $type_array]
57:     #echo "reg is $reg, width is $width, type is $type, type_array_length = $type_array_length"
58: 
59:     # If type is single bit wire, print to output file
60:     if {$type_array_length == 1 || $width == 1} {
61:       #puts $outputFile $reg
62:       lappend flopList $reg
63: 
64:     # If type is array, we have to expand the array to list out each flop individually
65:     } else {
66:       set max_index ""
67:       set min_index ""
68:       set index 1
69:      # set full_reg_string $reg
70:       while {$index < $type_array_length} {
71:         set array_dimensions [string trim [lindex $type_array $index]]
72:         set array_dimensions [string trim $array_dimensions \]]
73:         set array_dimensions [split $array_dimensions :]
74:         set array_1st_index  [lindex $array_dimensions 0]
75:         set array_2nd_index  [lindex $array_dimensions 1]
76:         set array_max_index   [expr max($array_1st_index, $array_2nd_index)]
77:         set array_min_index   [expr min($array_1st_index, $array_2nd_index)]
78:         lappend max_index $array_max_index
79:         lappend min_index $array_min_index
80:         set index [expr $index + 1]
81:       }
82: 
83:       # print to file
84:       #printArray $outputFile $reg [expr $type_array_length - 1] $max_index $min_index $min_index
85:       printArray "flopList" $reg [expr $type_array_length - 1] $max_index $min_index $min_index
86:     }
87:   }
88:   # now that all the flops in the module have been written, recursively decend to the next level down
89:   # and print the flops in the instances below.
90:   set insts [GetInstances $module]
91:   while { [set inst [GetNext $insts]] != "" } {
92:     set downModule [GetMasterModule $inst]
93:     # descend recursively through the instance hierarchy
94:     #dumpFlops $downModule $outputFile
95:     dumpFlops $downModule "flopList"
96:   }
97: }
98: 
99: # start from the -d top module and descend down through the design
100: # finding all the register nets
101: interp recursionlimit {} 64000
102: # The first argument is the output file
103: set flopList { }
104: if { $argc >= 1 } {
105:   set outputFileString [lindex $argv 0]
106: } else {
107:   set outputFileString "chariot_register_file.txt"
108: }
109: set outputFile [open $outputFileString w]
110: # the second argument is the module
111: if { $argc >= 2 } {
112:   set moduleArg [lindex $argv 1]
113:   set allModules [Netlist::GetModules]
114:   set mod [Netlist::GetNext $allModules]
115:   # loop through modules to identify a match
116:   while {$mod != ""} {
117:     set parentModList [list]
118:     set modName [Netlist::GetHdlName $mod]
119:     if {[string equal $moduleArg $modName]} {
120:       # if a match is found, and no other arguments exist, print flops
121:       if { $argc < 3 } {
122:         #dumpFlops $mod $outputFile
123:         dumpFlops $mod "flopList"
124:       } else {
125:         # if we have a 3rd argument, it's a parent module
126:         echo "parent argument called $modName"
127:         set modInstances [Netlist::GetModuleInstances $mod]
128:         set inst [Netlist::GetNext $modInstances]
129:         while {$inst != ""} {
130:           set parentInst [Netlist::GetParentInstance $inst]
131:           if { $argc >= 4 } {
132:             set parentInstName "[Netlist::GetName $parentInst]"
133:             set instArgument [lindex $argv 3]
134:             # if there's no match on the instance name, move to next instance
135:             if {[string first $instArgument $parentInstName] == -1} {
136:               set inst [Netlist::GetNext $modInstances]
137:               continue
138:             }
139:           }
140:           set parentMod  [Netlist::GetMasterModule $parentInst]
141:           lappend parentModList $parentMod 
142:           set inst [Netlist::GetNext $modInstances]
143:         }
144:         set parentModList [lsort -unique $parentModList]
145:         foreach parentMod $parentModList {
146:           echo "found parent mod"
147:           #dumpFlops $parentMod $outputFile
148:           dumpFlops $parentMod "flopList"
149:         } 
150:       }
151:     }
152:     set mod [Netlist::GetNext $allModules]
153:   }
154: } else {
155:   set mod [Netlist::GetTopModule]
156:   #dumpFlops $mod $outputFile
157:   dumpFlops $mod "flopList"
158: }
159: #set topMod [Netlist::GetMasterModule [Netlist::GetInstance ni700_brunel_1x1_AHB5_AHB5_chariot_b.u_s0]]
160: # increase recursion limit - tcl 8.6 has no limit, and some multi-dimensional arrays are > 1000, which is the default tcl limit
161: set flopList [lsort -unique $flopList]
162: foreach flop $flopList {
163:   puts $outputFile $flop
164: }
165: close $outputFile
166: echo "Successfully wrote flops to [pwd]/$outputFileString"
167: 
168: 
169: #set topInstance [Netlist::GetInstance testbench.dut_inst]
170: #set topInstance [Netlist::GetInstance porter.u_sbsx_nid8]
171: #set topMod [Netlist::GetMasterModule $topInstance]
172: 
173:   # if { [Query $net isInternal] || [Query $net isReg] || [Query $net isLatch] || [Query $net isMem]} { continue }
174:     #if {[GetNetWidth $net] > 1} {
175:       #set left [GetNetLeft $net]
176:       #set right [GetNetRight $net]
177:       #echo "$reg\[$left:$right\]"
178:     #} else {
179:       #echo "$reg $width $type"
180:     #}
```

## HEAD:logical/noc_arachne/validation/dynamic/top/interface_block.sv

Blob SHA-256: 0f69351edb4101c023d9b95d614d8e97f7bb326bd8e3c4661c486c76ad539985; total source lines: 7529.

```text
Source range 21-34
21: 
22: `ifndef INTERFACE_BLOCK__SV
23: `define INTERFACE_BLOCK__SV
24: 
25: `define AXI_NUM_SAFETY_BITS 2
26: `define AHB_NUM_SAFETY_BITS 2
27: `define NUM_CLK_CYCLES_HANG 2_000_000 //two million cycles
28: `define AXI_HANG_COUNTER_WIDTH 21  // two million cycles
29: 
30: `include "uvm_macros.svh"
31: `include "generic_common_nci_pkg.sv"
32: `include "local_params_pkg.sv"
33: 
34: `include "apu_intf.sv"
```

## HEAD:logical/noc_arachne/validation/dynamic/top/testbench.sv

Blob SHA-256: 602fc3ed157fc871c24ee3dce27e72af134b1f6cc920e562fa1ca52ad5d05e4b; total source lines: 3623.

```text
Source range 2476-2492
2476:   bit fault_is_being_injected; //pin for chariot random fault injection only, and set by a tcl script force statement
2477:   if(FMU_PRESENT) begin : g_fusa_interrupt_if
2478:     fusa_interrupt_if top_fusa_interrupt_if();
2479: 
2480:     assign top_fusa_interrupt_if.clk = CLK_TB[FMU_CLOCK_MAP];
2481:     assign top_fusa_interrupt_if.clk_resetn = ARESETn[FMU_CLOCK_MAP];
2482:     assign top_fusa_interrupt_if.fmu_register_resetn = SYS_RESETn[FMU_CLOCK_MAP];
2483:     assign top_fusa_interrupt_if.fault_is_being_injected = fault_is_being_injected;
2484:     assign top_fusa_interrupt_if.safety_interrupt = fmu_fault_int | fmu_err_int | fmu_cri_int;
2485: 
2486:     assign top_fusa_interrupt_if.critical_interrupt = fmu_cri_int;
2487:     assign top_fusa_interrupt_if.error_recovery_interrupt = fmu_err_int;
2488:     assign top_fusa_interrupt_if.fault_handling_interrupt = fmu_fault_int;
2489:     if (MISC_INTERFACE_PROTECTION) begin : g_fusa_interrupt_parity_c
2490:       assert property (@(posedge top_fusa_interrupt_if.clk) disable iff (!top_fusa_interrupt_if.clk_resetn) (fmu_fault_intchk == ~fmu_fault_int)) else
2491:         `uvm_error("PARITY ERROR",$sformatf("Parity generated for FMU FHI output from DUT is wrong."));
2492:       assert property (@(posedge top_fusa_interrupt_if.clk) disable iff (!top_fusa_interrupt_if.clk_resetn) (fmu_err_intchk == ~fmu_err_int)) else
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh

Blob SHA-256: 357f9a120aceef2f849d6b613a0d763eaf5170ba4d9a26ec1310b9e42c20ff2b; total source lines: 610.

```text
Source range 1-610
1: //------------------------------------------------------------------------------
2: // The confidential and proprietary information contained in this file may only
3: // be used by a person authorised under and to the extent permitted by a
4: // subsisting licensing agreement from ARM Limited.
5: //
6: //        (C) COPYRIGHT 2015 ARM Limited.
7: //            ALL RIGHTS RESERVED
8: //
9: // This entire notice must be reproduced on all copies of this file and copies
10: // of this file may only be made by a person if such person is permitted to do
11: // so under the terms of a subsisting license agreement from ARM Limited.
12: //
13: // Release Information : $State$
14: //
15: //------------------------------------------------------------------------------
16: // Purpose : Chariot Scoreboard to demote expected tb fails and fail if faults
17: //           are injected, but neither the tb and stimulus see any effects
18: //
19: //           Note: this changes the meaning of Pass/Fail
20: //
21: //------------------------------------------------------------------------------
22: 
23: `ifndef CHARIOT_INTERRUPT_SB__SVH
24: `define CHARIOT_INTERRUPT_SB__SVH
25: 
26: // The interrupt scoreboard will only check for raising interrupts. The
27: // interrupt handler will predict lowering of the interrupt
28: class chariot_fault_injection_scoreboard extends uvm_scoreboard;
29:   `uvm_component_utils(chariot_fault_injection_scoreboard)
30: 
31:   virtual fusa_interrupt_if#(MISC_INTERFACE_PROTECTION)  top_fusa_interrupt_if;
32:   // creating a local class below to demote errors
33:   typedef class demoter_t;
34:   demoter_t demoter;
35:   bit enable_interrupt_detection = 1; // set to 1 by default, so not currently disabled
36:   bit caught_safety_interrupt;
37:   bit corrected_safe_fault;
38:   string first_fail_message;
39:   string fail_messages[$];
40:   bit irq_sanitychk=0;  // default off.
41: 
42:   // Object: Class storing the inject error information
43:   fusa_err_record test_err_record;
44: 
45:   function new (string name="chariot_fault_injection_scoreboard", uvm_component parent);
46:     super.new(name, parent);
47:   endfunction
48: 
49:   function void build_phase(uvm_phase phase);
50:     super.build_phase(phase);
51:     uvm_config_db#(virtual fusa_interrupt_if)::get(uvm_root::get(), "*","fusa_interrupt_if" ,top_fusa_interrupt_if);
52:     if($test$plusargs("inject_fault")) begin
53:       demoter = new;
54:       demoter.top_fusa_interrupt_if = top_fusa_interrupt_if;
55:       demoter.parent = this;
56:     end
57:   endfunction
58: 
59:   task run_phase(uvm_phase phase);
60:     bit exp_hang_detector_fault = 0;
61:     bit poisoned = 0;
62:     bit tb_ce = 0 ;
63:     test_configuration_functions test_cfg;
64:     test_cfg = test_configuration_functions::get_instance();
65: 
66: 
67:     if($test$plusargs("IRQ_SANITYCHK_DIS"))
68:       irq_sanitychk = 0;
69:     if($test$plusargs("IRQ_SANITYCHK"))
70:       irq_sanitychk = 1;
71:     
72:     if(!uvm_config_db#(fusa_err_record)::get(null, "*", "test_err_record", test_err_record))
73:       `uvm_fatal(get_name(), $sformatf("unable to get the fusa_err_record. It should be set in func_top_test"))
74: 
75:     #1; // prevents time 0 X issues
76: 
77:     if (test_err_record.disable_fault_injection_scoreboard) begin
78:       `uvm_info(get_name(),"Disabling the chariot_fault_injection_scoreboard",UVM_NONE)
79:       return;
80:     end
81: 
82:     if($test$plusargs("inject_fault")) begin
83:       demote_errors(); // demote errors if injecting fault
84:     end
85: 
86:     fork 
87:       check_interrupt_for_X();
88:     join_none
89: 
90: 
91:     // wait for safety interrupt or correctable ecc error
92:     while (top_fusa_interrupt_if.safety_interrupt === 1'b0) begin
93:       wait(top_fusa_interrupt_if.safety_interrupt !== 1'b0);
94:       `uvm_info(get_name(), $sformatf("safety_interrupt_seen_count incremented (%0d)->(%0d)", test_err_record.safety_interrupt_seen_count, test_err_record.safety_interrupt_seen_count+1),UVM_NONE)
95:       test_err_record.safety_interrupt_seen_count++;
96:       #0; //this while loop is ugly code, but needed because idm shim component does some air-wiring that leads to X delta cycle glitches
97:     end
98: 
99:     if (top_fusa_interrupt_if.corrected_ecc_err !== 0) begin
100:       `uvm_info(get_type_name(), "Caught interrupt from corrected_ecc/deferred error", UVM_NONE)
101:        corrected_safe_fault = 1;
102:       if($test$plusargs("inject_fault")) begin
103:         `uvm_info(get_type_name(), "Corrected a safe fault", UVM_NONE)
104:       end else if((test_cfg.ip_version == "ni_only") || (test_cfg.ip_version == "converged")) begin 
105:         `uvm_info(get_type_name(), "Corrected a safe fault, or seen deferred error.", UVM_FULL)
106:       end else begin
107:          #1000ns; // leave more cycles for debug
108:          `uvm_fatal(get_type_name(), "Caught unexpected interrupt! (safe fault) ")
109:       end
110:     end
111: 
112:     while (top_fusa_interrupt_if.safety_interrupt === 1'b0) begin
113:       wait(top_fusa_interrupt_if.safety_interrupt !== 1'b0);
114:       `uvm_info(get_name(), $sformatf("safety_interrupt_seen_count incremented (%0d)->(%0d)", test_err_record.safety_interrupt_seen_count, test_err_record.safety_interrupt_seen_count+1),UVM_NONE)
115:       test_err_record.safety_interrupt_seen_count++;
116:       #0; //this while loop is ugly code, but needed because idm shim component does some air-wiring that leads to X delta cycle glitches
117:     end
118: 
119:     if(uvm_config_db#(bit)::get(null, "*", "exp_hang_detector_fault", exp_hang_detector_fault))
120:       `uvm_info(get_name(), $sformatf("Expecting Hang Detector fault... Skipping fusa_err_record::ready4chk"),UVM_NONE)
121: 
122:     if (top_fusa_interrupt_if.uncorrected_ecc_err !== 0) begin
123:       `uvm_info(get_type_name(), "Caught interrupt from uncorrected_edc", UVM_NONE)
124:       if ((exp_hang_detector_fault != 0) && (first_fail_message == "")) begin
125:         first_fail_message = "Fault caught expected from hang detector";
126:       end
127:     end else if (top_fusa_interrupt_if.corrected_ecc_err!== 0) begin
128:       `uvm_info(get_type_name(), "Caught interrupt from corrected_ecc_err/deferred error.", UVM_NONE)
129:     end else if (top_fusa_interrupt_if.sni_hang_err !== 0) begin
130:       `uvm_info(get_type_name(), "Caught interrupt from sni_hang_detector", UVM_NONE)
131:       if (first_fail_message != "") begin
132:         first_fail_message = "Hang caught by hang detector";
133:       end
134:     end else if (top_fusa_interrupt_if.pq_hang_err !== 0) begin
135:       `uvm_info(get_type_name(), "Caught interrupt from p_or_q_hang_detector", UVM_NONE)
136:     end else if (top_fusa_interrupt_if.resp_err !== 0) begin
137:       `uvm_info(get_type_name(), "Caught interrupt from resp_err", UVM_NONE)
138:     end else if (top_fusa_interrupt_if.size_err !== 0 && top_fusa_interrupt_if.size_err !== 1'hz) begin
139:       `uvm_info(get_type_name(), "Caught interrupt from size_err", UVM_NONE)
140:     end
141:     caught_safety_interrupt = 1;
142: 
143:     `uvm_info(get_name(),"Waiting for ready4chk (via set_err_record()) before starting checking poison/faults",UVM_NONE)
144:     if (((test_cfg.ip_version == "ni_only") || (test_cfg.ip_version == "converged")) && (exp_hang_detector_fault == 0)) begin 
145:       if(fusa_err_record::ready4chk==0) @fusa_err_record::ready4chk;
146:       fusa_err_record::ready4chk = 0;
147:     end
148: 
149:     sample_rtl_err_records();
150: 
151:     test_err_record.print_records();
152:     foreach(test_err_record.err_record[idx]) begin
153:       fusa_err_record_t record = test_err_record.err_record[idx];
154:       `uvm_info(get_name(), $sformatf("  err_record[%0s]: exp_addr(0x%0h), poisoned(%0d), ctrl_dui(%0d), exp_de(%0d), exp_ue(%0d), exp_ce(%0d), exp_cri(%0d), nci_node(%p)", 
155:              idx, record.exp_addr,  record.poisoned, record.ctrl_dui, record.exp_de, record.exp_ue, record.exp_ce, record.exp_cri, record.nci_node) ,UVM_NONE)
156:       if(poisoned && tb_ce) begin //{
157:         break;
158:       end //}
159:       else if(record.poisoned == 1) begin //{
160:         poisoned = 1;
161:       end //}
162:       else if(record.exp_ce == 1 ) begin //{
163:         tb_ce = 1 ;
164:       end //}
165:     end
166:     if(test_err_record.do_not_endtest_for_this_fault) begin //{
167:       poisoned = 1;
168:       `uvm_info(get_type_name(), "TB expected poison/deferred interrupt from payload/RAS prediction", UVM_NONE)
169:     end //}
170: 
171:     if($test$plusargs("inject_fault")) begin //{
172:       wait(first_fail_message != ""); // wait for tb to catch a fail
173:       `uvm_info(get_type_name(), "Seen tb checker caught error, waiting for irq seq to check fmu regs.", UVM_NONE)
174: 
175:       if((test_cfg.ip_version == "ni_only") || (test_cfg.ip_version == "converged")) begin 
176:         if(fusa_err_record::ready4endtest==0) @fusa_err_record::ready4endtest;
177:         //fusa_err_record::ready4chk = 0;
178:         `uvm_info(get_type_name(), "Ready to endtest...", UVM_NONE)
179:       end
180: 
181:       `uvm_info(get_type_name(), "Caught expected interrupt - force ending test", UVM_NONE)
182:       uvm_domain::jump_all(uvm_extract_phase::get());
183:     end //}
184:     else if(poisoned==1 || tb_ce == 1) begin //{
185:       string err_ni_name;
186:       `uvm_info(get_type_name(), "RTL seen poison defer error or CE waiting for tb to record error before checking...", UVM_NONE)
187:       poisoned = 0; // reset poisoned flag after logging.
188:       print_rtl_err_logging(err_ni_name);
189:     end //}
190:     else begin //{
191:       string err_ni_name;
192:       print_rtl_err_logging(err_ni_name);
193:       #1000ns; // leave more cycles for debug
194:       `uvm_fatal(get_type_name(), $sformatf("Caught unexpected interrupt! err_ni_name(%0s)", err_ni_name))
195:     end //}
196:   endtask : run_phase
197: 
198:   task check_interrupt_for_X();
199:     `uvm_info(get_name(), $sformatf("waiting for interrupt->X"), UVM_NONE)
200:     while(top_fusa_interrupt_if.fault_handling_interrupt!==1'bx && top_fusa_interrupt_if.error_recovery_interrupt!==1'bx && top_fusa_interrupt_if.critical_interrupt!==1'bx) begin
201:       wait(top_fusa_interrupt_if.fault_handling_interrupt===1'bx || top_fusa_interrupt_if.error_recovery_interrupt===1'bx || top_fusa_interrupt_if.critical_interrupt===1'bx);
202: 
203:       `uvm_info (get_name(), $sformatf("ERROR: FMU INTERRUPT==X, FHI(%0h), ERI(%0h), CRI(%0h)", top_fusa_interrupt_if.fault_handling_interrupt, top_fusa_interrupt_if.error_recovery_interrupt, top_fusa_interrupt_if.critical_interrupt), UVM_NONE)
204:       `uvm_error(get_name(), $sformatf("ERROR: FMU INTERRUPT==X, FHI(%0h), ERI(%0h), CRI(%0h)", top_fusa_interrupt_if.fault_handling_interrupt, top_fusa_interrupt_if.error_recovery_interrupt, top_fusa_interrupt_if.critical_interrupt))
205:       if($isunknown(top_fusa_interrupt_if.fault_handling_interrupt)|| $isunknown(top_fusa_interrupt_if.error_recovery_interrupt) || $isunknown(top_fusa_interrupt_if.critical_interrupt)) begin
206:         `uvm_info (get_name(), $sformatf("ERROR: FMU INTERRUPT==X, FHI(%0h), ERI(%0h), CRI(%0h)", top_fusa_interrupt_if.fault_handling_interrupt, top_fusa_interrupt_if.error_recovery_interrupt, top_fusa_interrupt_if.critical_interrupt), UVM_NONE)
207:         `uvm_error(get_name(), $sformatf("ERROR: FMU INTERRUPT==X, FHI(%0h), ERI(%0h), CRI(%0h)", top_fusa_interrupt_if.fault_handling_interrupt, top_fusa_interrupt_if.error_recovery_interrupt, top_fusa_interrupt_if.critical_interrupt))
208:       end
209:       #0; //this while loop is ugly code, but needed because idm shim component does some air-wiring that leads to X delta cycle glitches
210:     end
211:   endtask
212: 
213:   task print_rtl_err_logging(output string err_ni_name);
214:     nci_reg_model_pkg::nci_register_top_func  ral_;
215:     uvm_reg rg_; uvm_reg_block blk_;
216:     uvm_status_e status;
217:     string blk_name, reg_name;
218:     bit[63:0] status_data, misc0, misc1;
219:     bit[15:0] node_type, node_id;
220:     bit[9:0]  cd_id, pd_id, vd_id;
221:     int i, err_record_idx;
222:     bit[7:0] serr, ierr, ci, de, ce, mv, of, uet, ue, v;
223:     int num_of_records = 20;
224:     if (!uvm_config_db#(nci_reg_model_pkg::nci_register_top_func)::get(null, "", "reg_model", ral_))
225:       `uvm_fatal(get_name(), $sformatf("unable to get the nci_register_model"))
226: 
227:     blk_name = "fmu_registers";
228:     blk_     = ral_.get_block_by_name(blk_name);
229:     for(i=0; i<num_of_records; i++) begin
230:       reg_name = $sformatf("FMU_ERR_STATUS[%0d]", i);
231:       if(blk_!=null) begin
232:         rg_      = blk_.get_reg_by_name(reg_name);
233:         if(rg_!=null) begin
234:           status_data = 0;
235:           rg_.peek(status, status_data);
236:           serr = status_data[7:0];
237:           ierr = status_data[15:8];
238:           ci   = status_data[19:19];
239:           uet  = status_data[21:20];
240:           de   = status_data[23:23];
241:           ce   = status_data[25:24];
242:           mv   = status_data[26:26];
243:           of   = status_data[27:27];
244:           ue   = status_data[29:29];
245:           v    = status_data[30:30];
246:           err_record_idx = i;
247: 
248:           if(status_data[30]==1) begin
249:             `uvm_info(get_name(),$sformatf("RTL: Found error recorded in FMU_ERR_STATUS[%0d], err_status(0x%0h), num_of_records(%0d)", err_record_idx, status_data, num_of_records), UVM_NONE)
250:             begin : misc0_
251:               misc0 = 0;
252:               reg_name = $sformatf("FMU_ERR_MISC0[%0d]", err_record_idx);
253:               rg_      = blk_.get_reg_by_name(reg_name);
254:               rg_.peek(status, misc0);
255: 
256:               node_type = misc0[15:0];
257:               node_id   = misc0[31:16];
258:               cd_id     = misc0[41:32];
259:               pd_id     = misc0[51:42];
260:               vd_id     = misc0[61:52];
261: 
262:               case(node_type) 
263:                 'h0000 : err_ni_name = "Global domain";
264:                 'h0001 : err_ni_name = "Voltage domain";
265:                 'h0002 : err_ni_name = "Power domain";
266:                 'h0003 : err_ni_name = "Clock domain";
267:                 'h0004 : err_ni_name = "ASNI";
268:                 'h0005 : err_ni_name = "AMNI";
269:                 'h0006 : err_ni_name = "Performance Monitoring Unit (PMU)";
270:                 'h0007 : err_ni_name = "HSNI";
271:                 'h0008 : err_ni_name = "HMNI";
272:                 'h0009 : err_ni_name = "PMNI";
273:                 'h000a : err_ni_name = "DSNI";
274:                 'h000b : err_ni_name = "DMNI";
275:                 'h000c : err_ni_name = "TSNI";
276:                 'h000d : err_ni_name = "TMNI";
277:                 'h000e : err_ni_name = "CTB";
278:                 'h000f : err_ni_name = "DMNI_CHI";
279:                 'h0010 : err_ni_name = "CPL";
280:                 'h0040 : err_ni_name = "Clock controller";
281:                 'h0041 : err_ni_name = "Power controller";
282:                 'h0060 : err_ni_name = "CFGNI";
283:                 'h0061 : err_ni_name = "FMU";
284:                 default: err_ni_name = "Unknown node";
285:               endcase
286:               `uvm_info(get_name(),$sformatf("RTL: status: serr(0x%0h), ierr(0x%0h), ci(%0d), uet(0x%0h), de(0x%0h), ce(0x%0h), mv(%0d), of(%0d), ue(%0d), v(%0d)", 
287:                                                       serr,        ierr,        ci,      uet,        de,        ce,        mv,      of,      ue,      v),UVM_NONE)
288:               `uvm_info(get_name(),$sformatf("RTL: misc0:  err_ni_name(%0s), vd(%0d), pd(%0d), cd(%0d), nodeid(0x%0h), misc0=0x%0h", err_ni_name, vd_id, pd_id, cd_id, node_id, misc0),UVM_NONE)	       
289:             end: misc0_
290: 
291:             begin : misc1_
292:               bit[31:0] id;
293:               bit id_valid, attr_valid;
294:               bit[7:0] snoop, memattr, size, len;
295:               misc1 = 0;
296:               reg_name = $sformatf("FMU_ERR_MISC1[%0d]", err_record_idx);
297:               rg_      = blk_.get_reg_by_name(reg_name);
298:               rg_.peek(status, misc1);
299:               id         = misc1[31:0];
300:               id_valid   = misc1[35:35];
301:               snoop      = misc1[41:37];
302:               memattr    = misc1[48:43];
303:               size       = misc1[52:50];
304:               len        = misc1[61:54];
305:               attr_valid = misc1[63:63];
306: 
307:               `uvm_info(get_name(),$sformatf("RTL: misc1: id(0x%0h), id_valid((%0d), snoop(0x%0h), MemAttr(0x%0h), size(0x%0h), len(%0d), attr_valid(%0d), misc1(0x%0h)", 
308:                                                      id,        id_valid,       snoop,        memattr,        size,        len,      attr_valid,      misc1), UVM_NONE)
309:             end : misc1_
310: 
311:             begin : addr_
312:               bit[63:0] addr;
313:               reg_name = $sformatf("FMU_ERR_ADDR[%0d]", err_record_idx);
314:               rg_      = blk_.get_reg_by_name(reg_name);
315:               rg_.peek(status, addr);
316:               `uvm_info(get_name(),$sformatf("error record addr(0x%0h)", addr),UVM_NONE)	       
317:             end : addr_
318:           end
319:         end
320:       end
321:     end
322:   endtask : print_rtl_err_logging
323: 
324:   // Update tb w/ latest rtl err records
325:   task sample_rtl_err_records();
326:     nci_reg_model_pkg::nci_register_top_func  ral_;
327:     uvm_reg rg_; uvm_reg_block blk_;
328:     uvm_status_e status;
329:     string blk_name, reg_name;
330:     bit[63:0] status_data, misc0, misc1;
331:     bit[15:0] node_type, node_id;
332:     bit[9:0]  cd_id, pd_id, vd_id;
333:     int i, err_record_idx;
334:     bit[7:0] serr, ierr, ci, de, ce, mv, of, uet, ue, v;
335:     bit[31:0] id;
336:     bit id_valid, attr_valid;
337:     bit[7:0] snoop, memattr, size, len;
338:     bit[63:0] addr;
339:     int num_of_records; 
340:     test_configuration_functions test_cfg;
341:     test_cfg = test_configuration_functions::get_instance();
342:     num_of_records = test_cfg.nci_node_info.size();
343: 
344:     if (!uvm_config_db#(nci_reg_model_pkg::nci_register_top_func)::get(null, "", "reg_model", ral_))
345:       `uvm_fatal(get_name(), $sformatf("unable to get the nci_register_model"))
346: 
347:     blk_name = "fmu_registers";
348:     blk_     = ral_.get_block_by_name(blk_name);
349:     for(i=0; i<num_of_records; i++) begin
350:       reg_name = $sformatf("FMU_ERR_STATUS[%0d]", i);
351:       if(blk_!=null) begin
352:         rg_      = blk_.get_reg_by_name(reg_name);
353:         if(rg_!=null) begin
354:           status_data = 0;
355:           rg_.peek(status, status_data);
356:           serr = status_data[7:0];
357:           ierr = status_data[15:8];
358:           ci   = status_data[19:19];
359:           uet  = status_data[21:20];
360:           de   = status_data[23:23];
361:           ce   = status_data[25:24];
362:           mv   = status_data[26:26];
363:           of   = status_data[27:27];
364:           ue   = status_data[29:29];
365:           v    = status_data[30:30];
366:           err_record_idx = i;
367: 
368:           if(v==1) begin
369:             `uvm_info(get_name(),$sformatf("RTL: Found error recorded in FMU_ERR_STATUS[%0d], err_status(0x%0h), num_of_records(%0d)", err_record_idx, status_data, num_of_records), UVM_NONE)
370:             begin : misc0_
371:               string err_ni_name;
372:               misc0 = 0;
373:               reg_name = $sformatf("FMU_ERR_MISC0[%0d]", err_record_idx);
374:               rg_      = blk_.get_reg_by_name(reg_name);
375:               rg_.peek(status, misc0);
376: 
377:               node_type = misc0[15:0];
378:               node_id   = misc0[31:16];
379:               cd_id     = misc0[41:32];
380:               pd_id     = misc0[51:42];
381:               vd_id     = misc0[61:52];
382: 
383:               case(node_type) 
384:                 'h0000 : err_ni_name = "Global domain";
385:                 'h0001 : err_ni_name = "Voltage domain";
386:                 'h0002 : err_ni_name = "Power domain";
387:                 'h0003 : err_ni_name = "Clock domain";
388:                 'h0004 : err_ni_name = "ASNI";
389:                 'h0005 : err_ni_name = "AMNI";
390:                 'h0006 : err_ni_name = "Performance Monitoring Unit (PMU)";
391:                 'h0007 : err_ni_name = "HSNI";
392:                 'h0008 : err_ni_name = "HMNI";
393:                 'h0009 : err_ni_name = "PMNI";
394:                 'h000a : err_ni_name = "DSNI";
395:                 'h000b : err_ni_name = "DMNI";
396:                 'h000c : err_ni_name = "TSNI";
397:                 'h000d : err_ni_name = "TMNI";
398:                 'h000e : err_ni_name = "CTB";
399:                 'h000f : err_ni_name = "DMNI_CHI";
400:                 'h0010 : err_ni_name = "CPL";
401:                 'h0040 : err_ni_name = "Clock controller";
402:                 'h0041 : err_ni_name = "Power controller";
403:                 'h0060 : err_ni_name = "CFGNI";
404:                 'h0061 : err_ni_name = "FMU";
405:                 default: err_ni_name = "Unknown node";
406:               endcase
407:               `uvm_info(get_name(),$sformatf("RTL: status: serr(0x%0h), ierr(0x%0h), ci(%0d), uet(0x%0h), de(0x%0h), ce(0x%0h), mv(%0d), of(%0d), ue(%0d), v(%0d)", 
408:                                                       serr,        ierr,        ci,      uet,        de,        ce,        mv,      of,      ue,      v),UVM_NONE)
409:               `uvm_info(get_name(),$sformatf("RTL: misc0:  err_ni_name(%0s), vd(%0d), pd(%0d), cd(%0d), nodeid(0x%0h), misc0=0x%0h", err_ni_name, vd_id, pd_id, cd_id, node_id, misc0),UVM_NONE)	       
410:             end: misc0_
411: 
412:             begin : misc1_
413:               misc1 = 0;
414:               reg_name = $sformatf("FMU_ERR_MISC1[%0d]", err_record_idx);
415:               rg_      = blk_.get_reg_by_name(reg_name);
416:               rg_.peek(status, misc1);
417:               id         = misc1[31:0];
418:               id_valid   = misc1[35:35];
419:               snoop      = misc1[41:37];
420:               memattr    = misc1[48:43];
421:               size       = misc1[52:50];
422:               len        = misc1[61:54];
423:               attr_valid = misc1[63:63];
424: 
425:               `uvm_info(get_name(),$sformatf("RTL: misc1: id(0x%0h), id_valid((%0d), snoop(0x%0h), MemAttr(0x%0h), size(0x%0h), len(%0d), attr_valid(%0d), misc1(0x%0h)", 
426:                                                      id,        id_valid,       snoop,        memattr,        size,        len,      attr_valid,      misc1), UVM_NONE)
427:             end : misc1_
428: 
429:             begin : addr_
430:               reg_name = $sformatf("FMU_ERR_ADDR[%0d]", err_record_idx);
431:               rg_      = blk_.get_reg_by_name(reg_name);
432:               rg_.peek(status, addr);
433:               `uvm_info(get_name(),$sformatf("error record addr(0x%0h)", addr),UVM_NONE)	       
434:             end : addr_
435: 
436:             begin: populate_rtl_err_records
437:               // Populate rtl_err_records
438:               foreach (test_cfg.nci_node_info[node_index]) begin
439:                 if ((vd_id == test_cfg.nci_node_info[node_index].vd_id) &&
440:                     (pd_id == test_cfg.nci_node_info[node_index].pd_id) &&
441:                     (cd_id == test_cfg.nci_node_info[node_index].cd_id) &&
442:                     (node_id == test_cfg.nci_node_info[node_index].node_id) &&
443:                     (node_type == test_cfg.nci_node_info[node_index].node_type))
444:                 begin
445:                   test_err_record.rtl_err_record[node_index].node_inst = test_cfg.nci_node_info[node_index].node_inst;
446:                   // status
447:                   test_err_record.rtl_err_record[node_index].serr = serr;
448:                   test_err_record.rtl_err_record[node_index].ierr = ierr;
449:                   test_err_record.rtl_err_record[node_index].ci   = ci;
450:                   test_err_record.rtl_err_record[node_index].uet  = uet;
451:                   test_err_record.rtl_err_record[node_index].de   = de;
452:                   test_err_record.rtl_err_record[node_index].ce   = ce;
453:                   test_err_record.rtl_err_record[node_index].mv   = mv;
454:                   test_err_record.rtl_err_record[node_index].of   = of;
455:                   test_err_record.rtl_err_record[node_index].ue   = ue;
456:                   test_err_record.rtl_err_record[node_index].v    = v;
457:                   test_err_record.rtl_err_record[node_index].sm_id = ierr;
458:                   test_err_record.rtl_err_record[node_index].overflow = of;
459:                   test_err_record.rtl_err_record[node_index].rtl_ue = ue;
460:                   test_err_record.rtl_err_record[node_index].rtl_ce = |ce;
461:                   test_err_record.rtl_err_record[node_index].rtl_de = de;
462:                   test_err_record.rtl_err_record[node_index].rtl_cri = ci;
463:                   test_err_record.rtl_err_record[node_index].vd_id = vd_id;
464:                   test_err_record.rtl_err_record[node_index].pd_id = pd_id;
465:                   test_err_record.rtl_err_record[node_index].cd_id = cd_id;
466:                   // misc0
467:                   test_err_record.rtl_err_record[node_index].node_id   = node_id;
468:                   test_err_record.rtl_err_record[node_index].node_type = node_type;
469:                   // misc1
470:                   test_err_record.rtl_err_record[node_index].id         = id        ;
471:                   test_err_record.rtl_err_record[node_index].id_valid   = id_valid  ;
472:                   test_err_record.rtl_err_record[node_index].snoop      = snoop     ;
473:                   test_err_record.rtl_err_record[node_index].memattr    = memattr   ;
474:                   test_err_record.rtl_err_record[node_index].size       = size      ;
475:                   test_err_record.rtl_err_record[node_index].len        = len       ;
476:                   test_err_record.rtl_err_record[node_index].attr_valid = attr_valid;
477:                   // addr
478:                   test_err_record.rtl_err_record[node_index].rtl_addr = addr;
479:                   `uvm_info(get_name(),$sformatf("RTL: Updated rtl_err_records[%0s]", node_index), UVM_NONE)
480:                 end
481:               end // foreach
482:             end : populate_rtl_err_records
483:           end
484:         end
485:       end
486:     end
487:   endtask : sample_rtl_err_records
488: 
489: 
490:   // check if we injected a fault and caught an error.
491:   function void check_phase(uvm_phase phase);
492:     if (test_err_record.disable_fault_injection_scoreboard) begin
493:       return;
494:     end
495: 
496:     if (!$test$plusargs("disable_inject_fault_checks")) begin    
497:       if (!caught_safety_interrupt && $test$plusargs("inject_fault")) begin
498:         if (first_fail_message != "") begin
499:           `uvm_error(get_type_name, $sformatf("Missed fault ::: %s", first_fail_message)); // if the testbench finds a fail, we better have raised an uncorrectable error, otherwise print this
500:         end
501:         if (!corrected_safe_fault) begin // if we didn't correct a fault either, then none of the hardware detected anything went wrong
502:           `uvm_error(get_type_name(), "Did not catch interrupt and did not identify a testbench violation!")
503:         end
504:       end
505:     end
506:   endfunction
507: 
508:   function void report_phase(uvm_phase phase);
509:     super.report_phase(phase);
510:     if(irq_sanitychk==1 && test_err_record.safety_interrupt_seen_count>=1 && test_err_record.irq_chk_count==0) 
511:       `uvm_fatal(get_name(), $sformatf("IRQ seq (cnt=%0d) has not executed even though there were %0d safety interrupts.", test_err_record.irq_chk_count, test_err_record.safety_interrupt_seen_count))
512: 
513:     if ((first_fail_message != "") && caught_safety_interrupt && $test$plusargs("inject_fault")) begin
514:       `uvm_info(get_type_name, $sformatf("successfully caught the following error ::: %s", first_fail_message), UVM_NONE);
515:       foreach (fail_messages[i]) 
516:         `uvm_info(get_type_name, $sformatf("also successfully caught the following error ::: %s", fail_messages[i]), UVM_NONE);
517: 
518:     end else if ((first_fail_message == "") && caught_safety_interrupt && $test$plusargs("inject_fault")) begin
519:       `uvm_info(get_type_name, $sformatf("identified safety interrupt without testbench fail"), UVM_NONE);
520:     end else if ((first_fail_message == "") && corrected_safe_fault && $test$plusargs("inject_fault")) begin
521:       `uvm_info(get_type_name, $sformatf("corrected fault without testbench fail"), UVM_NONE);
522:     end
523:   endfunction
524: 
525:   function void demote_errors();
526:     // Since we're going to end the test, register the demoter!
527:     uvm_report_cb::add(null, demoter);
528:     // Since there are some random $error calls, use assertoff for now. We
529:     // should probably unify the messaging later on
530:     $assertcontrol(9); // 9 = failoff, where we turn off fails associated with assertions
531:   endfunction
532: 
533:   // Demote all error messages except the ones from this test!
534:   class demoter_t extends uvm_report_catcher;
535:     bit delay_all; // this variable delays the fatals/errors for N cycles to give time for the fusa interrupt
536:     bit allow_uvm_info;
537:     uvm_report_object permitted_reporter;
538:     int delay_count = 20_0000_000; //20 million cycles, just longer than our hang detector - revisit this
539:     virtual fusa_interrupt_if top_fusa_interrupt_if;
540:     string first_fail_message;
541:     string message_queue[$];
542:     chariot_fault_injection_scoreboard parent;
543: 
544:     function new(string name="demoter");
545:       super.new(name);
546:       delay_all = 1;
547:       allow_uvm_info = 1;
548:     endfunction
549: 
550:     function action_e catch();
551: 
552:       uvm_severity severity  = get_severity();
553:       string       id        = get_id();
554:       uvm_action   action    = get_action();
555:       string       message   = get_message();
556:       int          verbosity = get_verbosity();
557: 
558:       // Once the demoter is active, suppress all messages but our own
559:       if (allow_uvm_info && (severity == UVM_INFO || severity == UVM_WARNING)) begin
560:         // Don't mess with UVM_INFO/warning
561:         return THROW;
562:       end
563: 
564:       // always report errors from this scoreboard
565:       if (id == "chariot_fault_injection_scoreboard" || id == "fault_injection_sb" || id == "nci_top_fmu_irq_seq" || id == "test_err_record" || id == "DEMOTER") begin
566:         return THROW;
567:       end
568: 
569:       if (delay_all) begin
570: //        top_fusa_interrupt_if.tb_detected_err = 1; continuous assignment issues
571:         if (first_fail_message == "") begin
572:           // start a counter to timeout - temporarily removing, since hang detector timeout is so long. might as well wait for the end of the test
573: //          fork
574: //            begin
575: //              repeat (delay_count) @(posedge top_fusa_interrupt_if.clk);
576: //              uvm_report_error("DEMOTER", first_fail_message, UVM_NONE); // first fail is the most important
577: //              foreach (message_queue[i]) begin
578: //                if (i<100) begin // only print 100 extra fail messages to prevent logs that are too verbose
579: //                  uvm_report_error("DEMOTER", message_queue[i], UVM_NONE);
580: //                end else begin
581: //                  break;
582: //                end
583: //              end
584: //              uvm_report_fatal("DEMOTER", first_fail_message, UVM_NONE); //fatal, and report the first fail again for good measure
585: //            end
586: //          join_none
587:           first_fail_message = message;
588:           parent.first_fail_message = first_fail_message;
589:         end
590:         else 
591:           parent.fail_messages.push_front(message);
592: //        message_queue.push_back(message);
593:         return CAUGHT;
594:       end
595:       else begin //demote all except for permitted reporters
596:         if (get_client() == permitted_reporter) begin
597:           // If all messages shouldn't be demoted, then only the permitted
598:           // reporter should be allowed through
599:           return THROW;
600:         end
601:       end
602: 
603:       // if we still fall through, return throw
604:       return THROW;
605:     endfunction
606: 
607:   endclass
608: endclass
609: 
610: `endif // CHARIOT_INTERRUPT_SB__SVH
```

## HEAD:logical/noc_arachne/validation/dynamic/top/components/slaves/amba5_slave_controller_component.svh

Blob SHA-256: ecae1fad1a04e60c83d2a2de9bb55caeed0ae02432fd38d037be9876883ba3fc; total source lines: 2312.

```text
Source range 1205-1215
1205:     if(debugging_with_one_addr_flag && (req.get_axaddr() == addr_under_debug)) begin
1206:       `uvm_info("ADDR_HIT", $sformatf("Target Address: 0x%0h hit in amba5_slave_controller_component in generate_response", addr_under_debug), UVM_DEBUG)
1207:     end
1208: 
1209:     rsp.set_invalid_byte_lanes_mode(cfg.get_invalid_byte_mode());
1210:     //rsp.set_invalid_byte_lanes_mode(vip_ace5_types::INVALID_BYTE_LANES_RANDOM);
1211: 
1212:     //`uvm_info("AMBA5 SLAVE CONTROLLER COMPONENT", $sformatf("stage4: In task generate_response  for request::uid=0x%h  axaddr=0x%h axid=0x%h ",rsp.get_transaction_uid(), rsp.axaddr, rsp.axid) , UVM_HIGH)
1213:     // Get permission to access shared resource
1214:     super.get_order(p_id, p);
1215: 
```

## HEAD:logical/shared/scripts/arm_engine/services/param_engine/param_engine.sm

Blob SHA-256: 73424cc6179207b8ce61eb44244ebfb11d19cdf918009afb0ba8f14c7799b643; total source lines: 524.

```text
Source range 121-129
121: 
122:      group_sm.add_option("--ipxact_regcheck",  dest="ipxact_regcheck"    , action="store_true",  default=False, help='Check the register reset values in IPXACT against the RTL register reset values')
123:      group_sm.add_option("--hlk_check"      ,  dest="hlk_check"      , action="store_true",  default=False, help='Executes a simple check that the HLK is inline with stored version')
124:      group_sm.add_option("--remove_render"  ,  dest="remove_render"  , action="store_true",  default=False, help='Removes the rendered RTL associated with the build process')
125:      group_sm.add_option("--chariot_b"      ,  dest="chariot_b"  , action="store_true",  default=False, help='Configures design to add Chariot ASIL B safety mechanisms')
126:      group_sm.add_option("--hps_random_recipe"      ,  dest="hps_random_recipe"  , action="store_true",  default=False, help='Enables random recipe for a specific customer config')
127:      group_sm.add_option("--keep_unchanged_rtl",  dest="keep_unchanged_rtl", action="store_true",  default=False, help='Allows for a faster build by not copying RTL into bundle if unchanged from current bundle state')
128:      group_sm.add_option("--no_report_status",  dest="no_report_status", action="store_true",  default=False, help='Disables reporting of STATUS messages in Build Engine SQL')
129:      group_sm.add_option("--include_all_mcps",  dest="include_all_mcps", action="store_true",  default=False, help='Forces Build Engine to render all multicycle_path SDCs even if they are redundant or unneeded')
Source range 309-317
309:      all_opts    += " --validation " if self.options.validation  else ""
310:      all_opts    += " --external_dryrun " if self.options.external_dryrun  else ""
311:      all_opts    += " --report_colour "   if self.options.colour      else ""
312:      all_opts    += " --clean_build "     if self.options.clean_build else ""
313:      all_opts    += " --chariot_b "       if self.options.chariot_b   else ""
314:      all_opts    += " --hps_random_recipe "       if self.options.hps_random_recipe   else ""
315:      all_opts    += " --performance"      if self.options.performance else ""
316:      all_opts    += " --skip_itos"      if self.options.skip_itos else ""
317:      all_opts    += " --json_rebuild"       if self.options.json_rebuild  else ""
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_core_build.py

Blob SHA-256: 501b8929a3cab39783d054ab032830dc4811f9b33d6c150fa549636af8af5783; total source lines: 794.

```text
Source range 90-99
90:     # Sticher product HLK
91:     self.hlk_set  = kvarg_default("hlk_set", kwargs, False)
92:     self.base_hlk = sys.path[0] + "/base_hlk.json"
93: 
94:     # chariot_b boolean
95:     self.chariot_b = kvarg_default("chariot_b", kwargs, False)
96: 
97:     self.hps_random_recipe = kvarg_default("hps_random_recipe", kwargs, False)
98: 
99:     self.shallow_rtl = kvarg_default("shallow_rtl", kwargs, False)
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_internal_build.py

Blob SHA-256: ba4ed8668f85daf0006f497e251e1023e7b6c25bddc6ba7ef3f685f30c18f4db; total source lines: 287.

```text
Source range 104-112
104:       # --- DTC/DTM control assertions generation
105:       noc_external_bindings.noc_dtc_ctl_assertions.generate_binding(self.connected_rtl_file, self.build_output, tower)
106: 
107:       # --- Wrapper generation
108:       noc_external_bindings.noc_testbench_wrapper.generate_binding(self.connected_rtl_file, self.build_name, self.build_output, self.chariot_b, tower, hlk, self.build_target, False, self.dtest, self.enable_mcn_sb, self.tyaml)
109:       noc_external_bindings.noc_testbench_wrapper.generate_idm_binding(self.connected_rtl_file, self.build_name, self.build_output)
110: 
111:       # -- CDC waiver generation
112:       noc_cdc_validation.generate_cdc_binding(self.build_name, self.connected_rtl_file, self.build_output)
Source range 157-165
157:   parser.add_option("--include_all_mcps" , dest="include_all_mcps" , default=False,  action="store_true" , help="Forces Build Engine to render all multicycle_path SDCs even if they are redundant or unneeded")
158:   parser.add_option("--no_sdc" , dest="no_sdc" , default=False , action="store_true" , help="Disables SDC generation")
159:   parser.add_option("--report_output" , dest="report_output" , default=""    , action="store"      , help="Configures the report target directory - if unspecified output is used")
160:   parser.add_option("--report_colour" , dest="report_colour" , default=False , action="store_true" , help="Enables report colouring on the terminal output - useful visual feedback")
161:   parser.add_option("--chariot_b"     , dest="chariot_b"     , default=False , action="store_true" , help="Configures design to add Chariot ASIL B safety mechanisms")
162:   parser.add_option("--hps_random_recipe"     , dest="hps_random_recipe"     , default=False , action="store_true" , help="Enables random recipe for a specific customer config")
163:   parser.add_option("--performance"   , dest="performance"   , default=False , action="store_true" , help="Configure build engine to produce the perf model without generating RTL")
164: 
165:   # Argument to enable faster build by not copying unchanged RTL
Source range 198-207
198: 
199:   # Append data cleaning action
200:   kwargs["clean"] = options.clean_build
201: 
202:   # Add chariot_b option
203:   kwargs["chariot_b"] = options.chariot_b
204: 
205:   # Add random recipe for a specific customer option
206:   kwargs["hps_random_recipe"] = options.hps_random_recipe
207: 
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py

Blob SHA-256: 793b3890bda8aea06f44a83140cc2b9e8340cb5d095dbdcada22e021238fd295; total source lines: 7113.

```text
Source range 1139-1147
1139: 
1140:   # Close file upon completion
1141:   _fh.close()
1142: 
1143: def generate_binding(_dataset_file, _cfgname, _output, _chariot_b, _tower, _hlk_file, _tower_name, is_oob, dtest, _mcn_scoreboard, tyaml) :
1144: 
1145:   # declare array variables
1146:   pmni_sreset_connect = []
1147:   pmni_apu_connect = []
Source range 2284-2300
2284:         #  Diff          = ruser - wuser - buser
2285:         ruser_extra_bits = paramObj["RUSER_RESP_WIDTH"] - paramObj["BUSER_RESP_WIDTH"] # VIP-11616, see BOOKERNOC-4936 for explanation of ruser greater than/less than or equal comparision in relation to ruser/wuser/buser.
2286:         # USER WIDTH signals
2287:         if paramObj["USER_REQ_WIDTH"] > 0:
2288:           if _chariot_b:
2289:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_AWUSER                   " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wreq_err_code     "})
2290:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".rreq_err_code     "})
2291:           else:
2292:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_AWUSER                   " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.AWUSER       "})
2293:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
2294:         # WUSER
2295:         if paramObj["USER_DATA_WIDTH"] > 0:
2296:           if _chariot_b:
2297:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_WUSER                    " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wdat_err_code    "})
2298:           else:
2299:             if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
2300:               if(ruser_extra_bits>0): # note: The master vip will expect WUSER to be larger than what the design can receive, therefore in the wrapper we need to truncate wuser to the appropriate size.
Source range 2653-2666
2653:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HREADYOUT    "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HREADY       "})
2654:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HREADYIN     "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HREADY       "})
2655:       # USER WIDTH signals
2656:       if paramObj["USER_REQ_WIDTH"] > 0:
2657:         if _chariot_b:
2658:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HAUSER       "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wreq_err_code   "})
2659:         else:
2660:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HAUSER       "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HAUSER     "})
2661:       if paramObj["USER_DATA_WIDTH"] > 0:
2662:         if _chariot_b:
2663:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HWUSER       "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".wdat_err_code  "})
2664:         else:
2665:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HWUSER       "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HWUSER     "})
2666:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_HRUSER       "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.HRUSER     "})
Source range 2789-2797
2789:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_AWVALID      "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.AWVALID      "})
2790:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_AWREADY      "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.AWREADY      "})
2791:         if paramObj["INTERFACE_TYPE"] == 3 :
2792:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_WID          "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if.WID          "})
2793:         if _chariot_b:
2794:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_WDATA        "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".wdat_uncorrected  "})
2795:         else:
2796:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_WDATA        "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.WDATA        "})
2797:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_WSTRB        "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.WSTRB        "})
Source range 2953-2969
2953:               wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_WUSERCHK     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.parity_gen.parity_if.WUSERCHK"})
2954: 
2955:         # BUSER
2956:         if paramObj["BUSER_RESP_WIDTH"] > 0:
2957:           if _chariot_b:
2958:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_BUSER        " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".wrsp_err_code     "})
2959:           else:
2960:             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_BUSER        " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.BUSER        "})
2961:         # RUSER
2962:         if(ruser_extra_bits >= 0): # ruser > wuser + buser, zero-extend rtl's ruser to feed into vip's interface.
2963:           if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0:
2964:             if _chariot_b:
2965:               if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Direction" : "input", "Testbench" : "{g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rdat_err_code,g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rrsp_err_code}"})
2966:             else:
2967:               wrapper_data["AHB_User_Bits"].append("// Note: ruser > wuser + buser. RUSER not modified .  \n")
2968:               wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER                    " , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
2969:         else: # ruser < wuser + buser
Source range 3319-3327
3319:       wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HWRITE     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HWRITE     "})
3320:       wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HSIZE      "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HSIZE      "})
3321:       wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HBURST     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HBURST     "})
3322:       wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HTRANS     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HTRANS     "})
3323:       if _chariot_b:
3324:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HWDATA     " , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".wdat_uncorrected "})
3325:       else:
3326:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HWDATA     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HWDATA     "})
3327:       wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HRESP      "  , "Direction" : "input", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HRESP      "})
Source range 3347-3356
3347:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HAUSER     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HAUSER     "})
3348:       if paramObj["USER_DATA_WIDTH"] > 0:
3349:         wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HWUSER     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HWUSER     "})
3350:       if paramObj["USER_DATA_WIDTH"] > 0:
3351:         if _chariot_b:
3352:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HRUSER     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rdat_err_code   "})
3353:         else:
3354:           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_HRUSER     "  , "Direction" : "output", "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.HRUSER     "})
3355: 
3356:       if hmni_parity[instance]:
```

## HEAD:configs_iyml/brunel_1x1_ACE5Lite_AXI5_chariot.yaml

Blob SHA-256: 95acf14c9dff94855def104c8822119201c9fa200904710e73553d5a1396a702; total source lines: 418.

```text
Source range 1-27
1: ---
2: AddressRegions:
3:   mm0:
4:     cfg:
5:       endAddress: 0xffff
6:       startAddress: 0x0
7:       targets:
8:         default: CONFIGURATION_SPACE
9:     m0_if:
10:       endAddress: 0x1ffff
11:       startAddress: 0x10000
12:       targets:
13:         default: m0_if
14:     subscribers: s0
15: clockRelations:
16:   clk0:
17:     clk1: sync
18: domains:
19:   vd0:
20:     pd0:
21:       clk0: 1000
22:       clk1: 2000
23: globalParameters:
24:   PERIPHBASE: 0
25:   aub/aubRequestFlitSize: 2
26:   aub/aubRequestNumberOfChannelCredits: 1
27:   aub/aubResponseFlitSize: 2
Source range 37-55
37:   user/DATperByte: 2
38:   user/REQ: 8
39:   user/RRESP: 8
40:   user/mode: perByte
41: ipVersion: towernci_r0p0
42: iymlVersion: 0.48
43: project: brunel_1x1_ACE5Lite_AXI5_chariot
44: tooling:
45:   dieProperties:
46:     cellGranularity: 100
47:     height: 5000
48:     width: 5000
49:   paths:
50:     s0_if:
51:       CONFIGURATION_SPACE: {}
52:       m0_if:
53:         readRequest: default_profile
54:         writeRequest: default_profile
55:   profiles:
Source range 68-77
68:     maxLinkWidth: 64
69:     numberOfResourcePlanes: 4
70:     optimizeFIFOSizes: true
71:     usePreSynthTopology: false
72: uniquifier: abc123
73: units:
74:   amnis:
75:     m0:
76:       channels:
77:         readResponse:
Source range 99-107
99:       - m0_if: ~
100:       parameters:
101:         adaptor/idm: Disabled
102:         adaptor/idmDeviceId: 0
103:         adaptor/protocol: AXI5
104:         adaptor/readRetimingStages: 3
105:         adaptor/starvationAvoidancePeriod: 12
106:         adaptor/writeRetimingStages: 6
107:         axi/addressWidth: 40
Source range 143-151
143:         adaptor/burstSplitting: Enabled
144:         adaptor/enableOverridingofIncomingQoSValue: Enabled
145:         adaptor/idm: Disabled
146:         adaptor/idmDeviceId: 0
147:         adaptor/protocol: ACE5Lite
148:         adaptor/readReorderDepth: 32
149:         adaptor/readRetimingStages: 33
150:         adaptor/regulatorPresent: 3
151:         adaptor/starvationAvoidancePeriod: 7
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_configuration/decoders/asni_decoder.py

Blob SHA-256: 0e1e48f5e00d26dde97309b66443297f24b49a57cf4928ac823b5a6806fb705d; total source lines: 517.

```text
Source range 155-168
155:     for stripped_if in accessmaps.keys() :
156:       target_interfaces = noc_configuration.interfaces.interface_common.get_matching_interface_keys(
157:         _data[_instance]["write"], stripped_if
158:       )
159:       if not target_interfaces:
160:         raise ValueError("ASNI SAM unblock target '{:s}' is missing from write access map for {:s}".format(stripped_if, _instance))
161:       ublkRoute = accessmaps[stripped_if]
162:       ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
163:       for target_interface in target_interfaces:
164:         _data[_instance]["unblock"][target_interface] = {}
165:         _data[_instance]["unblock"][target_interface]["target_id"] = _data[_instance]["write"][target_interface]["target_id"]
166:         _data[_instance]["unblock"][target_interface]["decode"] = ublkVector
167: 
168:     _data[_instance]["areq"] = {}
Source range 170-183
170:     for stripped_if in accessmaps.keys() :
171:       target_interfaces = noc_configuration.interfaces.interface_common.get_matching_interface_keys(
172:         _data[_instance]["write"], stripped_if
173:       )
174:       if not target_interfaces:
175:         raise ValueError("ASNI SAM AREQ target '{:s}' is missing from write access map for {:s}".format(stripped_if, _instance))
176:       areqRoute = accessmaps[stripped_if]
177:       areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
178:       for target_interface in target_interfaces:
179:         _data[_instance]["areq"][target_interface] = {}
180:         _data[_instance]["areq"][target_interface]["target_id"] = _data[_instance]["write"][target_interface]["target_id"]
181:         _data[_instance]["areq"][target_interface]["decode"] = areqVector
182: 
183: def build_static(_instance, _dataset, _cdata, _data) :
Source range 420-449
420:       amni_16_bits = noc_configuration.configuration_functions.convert_stripe(amni_16_width)
421:       req_data[x]["split_size"] = min(amni_16_bits, req_data[x]["split_size"])
422:     if(_type == "wreq" and _debug):
423:       print("    {:14s} :".format(str(inst_target.split('/',1)[0])) + " tgtID=" + str(int(tgt_id)) + " decode=" + str(req_data[x]["decode"]) + " split_size=" + str(req_data[x]["split_size"]) + ": stripe=" + str(req_data[x]["stripe"]) + str(req_data[x]["split_size"]) + " stripe_size=" + str(req_data[x]["stripe_size"]))
424: 
425:     if owo_stream and _region in ublk_maps and _remap in ublk_maps[_region]:
426:       ublkRoute = None
427:       for route in ublk_maps[_region][_remap]['ublk']:
428:         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
429:           ublkRoute = route
430:           break
431:       ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
432:       _data[_instance]["unblock"][if_targets[x]] = {}
433:       _data[_instance]["unblock"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
434:       _data[_instance]["unblock"][if_targets[x]]["decode"] = ublkVector
435:       if _debug:
436:         print("\t      ublk - tgtID={:s} decode={:s}".format(str(_data[_instance]["unblock"][if_targets[x]]["target_id"]), str(_data[_instance]["unblock"][if_targets[x]]["decode"])))
437:     if owo_stream and _region in areq_maps and _remap in areq_maps[_region]:
438:       areqRoute = None
439:       for route in areq_maps[_region][_remap]['areq']:
440:         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
441:           areqRoute = route
442:           break
443:       areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
444:       _data[_instance]["areq"][if_targets[x]] = {}
445:       _data[_instance]["areq"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
446:       _data[_instance]["areq"][if_targets[x]]["decode"] = areqVector
447:       if _debug:
448:         print("\t      areq - tgtID={:s} decode={:s}".format(str(_data[_instance]["areq"][if_targets[x]]["target_id"]), str(_data[_instance]["areq"][if_targets[x]]["decode"])))
449: 
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_configuration/decoders/dsni_decoder.py

Blob SHA-256: e74fb0a159b02e2338b3d1a84ae7fd3e82132e55c61e3ebf9380cefb64342108; total source lines: 486.

```text
Source range 151-164
151:     for stripped_if in accessmaps.keys() :
152:       target_interfaces = noc_configuration.interfaces.interface_common.get_matching_interface_keys(
153:         _data[_instance]["write"], stripped_if
154:       )
155:       if not target_interfaces:
156:         raise ValueError("DSNI SAM unblock target '{:s}' is missing from write access map for {:s}".format(stripped_if, _instance))
157:       ublkRoute = accessmaps[stripped_if]
158:       ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
159:       for target_interface in target_interfaces:
160:         _data[_instance]["unblock"][target_interface] = {}
161:         _data[_instance]["unblock"][target_interface]["target_id"] = _data[_instance]["write"][target_interface]["target_id"]
162:         _data[_instance]["unblock"][target_interface]["decode"] = ublkVector
163: 
164:     _data[_instance]["areq"] = {}
Source range 166-179
166:     for stripped_if in accessmaps.keys() :
167:       target_interfaces = noc_configuration.interfaces.interface_common.get_matching_interface_keys(
168:         _data[_instance]["write"], stripped_if
169:       )
170:       if not target_interfaces:
171:         raise ValueError("DSNI SAM AREQ target '{:s}' is missing from write access map for {:s}".format(stripped_if, _instance))
172:       areqRoute = accessmaps[stripped_if]
173:       areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
174:       for target_interface in target_interfaces:
175:         _data[_instance]["areq"][target_interface] = {}
176:         _data[_instance]["areq"][target_interface]["target_id"] = _data[_instance]["write"][target_interface]["target_id"]
177:         _data[_instance]["areq"][target_interface]["decode"] = areqVector
178: 
179: def build_static(_instance, _dataset, _cdata, _data) :
Source range 411-440
411:       amni_16_width = str(amni_width<<4)+"B"
412:       amni_16_bits = noc_configuration.configuration_functions.convert_stripe(amni_16_width)
413:       req_data[x]["stripe_size"] = min(amni_16_bits, req_data[x]["stripe_size"])
414:     if(_type == "rreq" and _debug):
415:       print("    {:14s} :".format(str(inst_target.split('/',1)[0])) + ": tgtID=" + str(int(node_id)) + " decode=" + str(req_data[x]["decode"]) + " split_size=" + str(req_data[x]["stripe_size"]) )
416:     if owo_stream and _region in ublk_maps and _remap in ublk_maps[_region]:
417:       ublkRoute = None
418:       for route in ublk_maps[_region][_remap]['ublk']:
419:         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
420:           ublkRoute = route
421:           break
422:       ublkVector = decoder_common.int2bin(int(_cdata["connections"][ublkRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
423:       _data[_instance]["unblock"][if_targets[x]] = {}
424:       _data[_instance]["unblock"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
425:       _data[_instance]["unblock"][if_targets[x]]["decode"] = ublkVector
426:       if _debug:
427:         print("\tublk - tgt_id={:s} decode={:s}".format(str(_data[_instance]["unblock"][if_targets[x]]["target_id"]), str(_data[_instance]["unblock"][if_targets[x]]["decode"])))
428:     if owo_stream and _region in areq_maps and _remap in areq_maps[_region]:
429:       areqRoute = None
430:       for route in areq_maps[_region][_remap]['areq']:
431:         if _dataset["Routes"][route]["TargetNode"]["instanceName"] == inst_target:
432:           areqRoute = route
433:           break
434:       areqVector = decoder_common.int2bin(int(_cdata["connections"][areqRoute]["route_vector"], 2), width=_cdata["gt"]["GT_ROUTE_WIDTH"], position=2)
435:       _data[_instance]["areq"][if_targets[x]] = {}
436:       _data[_instance]["areq"][if_targets[x]]["target_id"] = req_data[x]["target_id"]
437:       _data[_instance]["areq"][if_targets[x]]["decode"] = areqVector
438:       if _debug:
439:         print("\tareq - tgt_id={:s} decode={:s}".format(str(_data[_instance]["areq"][if_targets[x]]["target_id"]), str(_data[_instance]["areq"][if_targets[x]]["decode"])))
440:   # Perform stripe aliasing
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/arachne_asni_axi_core.py

Blob SHA-256: e82c7c0ca501909c3ac6f60989d1fb7ea7adbba707b35811799fdc322a1a6353; total source lines: 1266.

```text
Source range 163-175
163: def gt_pasunknown_derivation(_dataset)              : return True, configuration_functions.data_network_params_dataset["GT_PASUNKNOWN"]
164: 
165: def sam_reg_depth_derivation(_dataset)             : return fixed_known(_dataset, 800,  "SAM_REG_DEPTH")
166: def sam_reg_width_derivation(_dataset)             : return fixed_known(_dataset, 32,  "SAM_REG_WIDTH")
167: def gt_mec_support_derivation(_dataset)            : return True, configuration_functions.data_network_params_dataset["GT_MEC_SUPPORT"]
168: def gt_mecid_width_derivation(_dataset)            : return True, configuration_functions.data_network_params_dataset["GT_MECID_WIDTH"]
169: def gt_owo_streaming_derivation(_dataset)          : return True, configuration_functions.data_network_params_dataset["GT_OWO_STREAMING"]
170: def gt_streaming_credit_derivation(_dataset)       : return True, configuration_functions.data_network_params_dataset["GT_STREAMING_CREDIT"]
171: def gt_streaming_credit_width_derivation(_dataset) : return True, configuration_functions.data_network_params_dataset["GT_STREAMING_CREDIT_WIDTH"]
172: 
173: def dtm_srcid_width_derivation(_dataset)                    : return True, configuration_functions.data_network_params_dataset["DTC_SRCID_WIDTH"]
174: def dtm_tgtid_width_derivation(_dataset)                    : return True, configuration_functions.data_network_params_dataset["DTC_TGTID_WIDTH"]
175: def dtm_route_width_derivation(_dataset)                    : return True, configuration_functions.data_network_params_dataset["DTC_ROUTE_WIDTH"]
Source range 192-215
192:   route = _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"].get("DebugRoute",None)
193:   if route == None:
194:     return True, 0
195:   result = configuration_functions.connections_dataset[route]["route_vector"]
196:   return True, result
197: 
198: def owo_streaming_map_derivation(_dataset):
199:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
200:     return True, [0]
201: 
202:   tgtid_arr = []
203:   for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
204:     inst_target = noc_configuration.configuration_functions.convert_interface(intf)
205:     tgtid = noc_configuration.interfaces.interface_common.get_comp_interface_id(_dataset["config"], intf, inst_target)
206:     tgtid_arr.append(tgtid)
207:   return True, tgtid_arr
208: 
209: def owo_streaming_tgt_type_derivation(_dataset):
210:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
211:     return True, 0
212: 
213:   aux_vec = 0
214:   for intf in reversed(noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"])):
215:     aux_vec <<= 1
Source range 218-247
218:       auxChannel = 0
219:     else:
220:       auxChannel = 1
221:     aux_vec |= auxChannel
222:   return True, aux_vec
223: 
224: def owo_streaming_max_credit_acc_derivation(_dataset):
225:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
226:     return True, [0]
227: 
228:   cred_arr = []
229:   for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
230:     cred_arr.append(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkCredits"][intf])
231:   return True, cred_arr
232: 
233: def num_owo_streaming_tgt_derivation(_dataset)             :
234:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
235:     return True, 0
236:   result = len(noc_configuration.configuration_functions.get_access_maps_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]))
237: 
238:   # Return computed value
239:   return True, result
240: 
241: def num_owo_streaming_tgt_width_derivation(_dataset)             :
242: 
243:   # Fetch required resolved parameters
244:   param_data = get_self_parameters_for_solve(_dataset, ["NUM_OWO_STREAMING_TGT"], [], "NUM_OWO_STREAMING_TGT_WIDTH")
245: 
246:   # Determine return value
247:   result = param_data["NUM_OWO_STREAMING_TGT"] if param_data["NUM_OWO_STREAMING_TGT"] > 0 else 1
```

## HEAD:logical/shared/scripts/noc_param_engine/noc_param_derivation/r0p0/component_modules/noc_dsni_core.py

Blob SHA-256: ec03a04d3923f232dbee94f2ca63a630e3f2196f2a786205854618aab8a549a1; total source lines: 1721.

```text
Source range 210-222
210: #def aub_node_pwrdid_derivation(_dataset)           : return True, configuration_functions.get_power_id(_dataset["config"], _dataset["instance_id"])
211: #def aub_cfgni_id_derivation(_dataset)              : return True, configuration_functions.get_cfgni_id(_dataset["config"], _dataset["instance_id"])
212: #def aub_cfgni_route_derivation(_dataset)           : return True, configuration_functions.get_cfgni_route(_dataset["config"], _dataset["instance_id"])
213: #def aub_flit_size_derivation(_dataset)             : return aub_flit_size_calculate(_dataset, "AUB_FLIT_SIZE")
214: #def gt_mec_support_derivation(_dataset)            : return True, configuration_functions.data_network_params_dataset["GT_MEC_SUPPORT"]
215: #def gt_mecid_width_derivation(_dataset)            : return True, configuration_functions.data_network_params_dataset["GT_MECID_WIDTH"]
216: def gt_owo_streaming_derivation(_dataset)          : return True, configuration_functions.data_network_params_dataset["GT_OWO_STREAMING"]
217: def gt_streaming_credit_derivation(_dataset)       : return True, configuration_functions.data_network_params_dataset["GT_STREAMING_CREDIT"]
218: def gt_streaming_credit_width_derivation(_dataset) : return True, configuration_functions.data_network_params_dataset["GT_STREAMING_CREDIT_WIDTH"]
219: 
220: def dtm_srcid_width_derivation(_dataset)                    : return True, configuration_functions.data_network_params_dataset["DTC_SRCID_WIDTH"]
221: def dtm_tgtid_width_derivation(_dataset)                    : return True, configuration_functions.data_network_params_dataset["DTC_TGTID_WIDTH"]
222: def dtm_route_width_derivation(_dataset)                    : return True, configuration_functions.data_network_params_dataset["DTC_ROUTE_WIDTH"]
Source range 234-246
234:   route = _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"].get("DebugRoute",None)
235:   if route == None:
236:     return True, 0
237:   result = configuration_functions.connections_dataset[route]["route_vector"]
238:   return True, result
239: 
240: def owo_streaming_tgt_type_derivation(_dataset):
241:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
242:     return True, 0
243: 
244:   aux_vec = 0
245:   for intf in reversed(noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"])):
246:     aux_vec <<= 1
Source range 260-300
260:   # Determine return value
261:   result = param_data["OWO_STREAMING_SUPPORT"]
262: 
263:   # Return computed value
264:   return True, result
265: 
266: def owo_streaming_map_derivation(_dataset):
267:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
268:     return True, [0]
269: 
270:   tgtid_arr = []
271:   for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
272:     inst_target = noc_configuration.configuration_functions.convert_interface(intf)
273:     tgtid = noc_configuration.interfaces.interface_common.get_comp_interface_id(_dataset["config"], intf, inst_target)
274:     tgtid_arr.append(tgtid)
275:   return True, tgtid_arr
276: 
277: def owo_streaming_max_credit_acc_derivation(_dataset):
278:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
279:     return True, [0]
280: 
281:   cred_arr = []
282:   for intf in noc_configuration.configuration_functions.get_access_maps_strip_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]):
283:     cred_arr.append(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkCredits"][intf])
284:   return True, cred_arr
285: 
286: def num_owo_streaming_tgt_derivation(_dataset)             :
287:   if "UblkAccessMaps" not in _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"] or len(_dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]) < 1:
288:     return True, 0
289:   result = len(noc_configuration.configuration_functions.get_access_maps_ifs(_dataset["config"], _dataset["config"]["Instances"][_dataset["instance_id"]]["componentMisc"]["UblkAccessMaps"]))
290: 
291:   # Return computed value
292:   return True, result
293: 
294: def num_owo_streaming_tgt_bus_derivation(_dataset)             :
295: 
296:   # Fetch required resolved parameters
297:   param_data = get_self_parameters_for_solve(_dataset, ["NUM_OWO_STREAMING_TGT"], [], "NUM_OWO_STREAMING_TGT_BUS")
298: 
299:   # Determine return value
300:   result = param_data["NUM_OWO_STREAMING_TGT"] if param_data["NUM_OWO_STREAMING_TGT"] > 0 else 1
```

## HEAD:logical/shared/scripts/sticho/sticho/StichoRender.py

Blob SHA-256: 39ed1cdfd4e138a700197de0ad62700189d7fb975df75a9a03b3781774e81900; total source lines: 4685.

```text
Source range 2729-2743
2729:                     else:
2730:                         self.sdc_global_iter_num_map[sdc_global_iter_lookup_str] = self.sdc_global_iter
2731:                         iter_global_view = self.sdc_global_iter
2732:                         self.sdc_global_iter += 1
2733: 
2734: 
2735:                     if (sdcObj["src_freq"] > sdcObj["dst_freq"]):
2736:                         start_end_flag = "-start"
2737:                     elif (sdcObj["dst_freq"] > sdcObj["src_freq"]):
2738:                         start_end_flag = "-end"
2739:                     else:
2740:                         # Default flag if same frequency
2741:                         start_end_flag = "-start"
2742: 
2743:                     src_cdomain = str(sdcObj["src_cDomain"])
```

## Other-author context bce47a50cf9fee013517d4bb33f71c70d4f730f1

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit bce47a50cf9fee013517d4bb33f71c70d4f730f1
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Tue Nov 3 23:18:41 2020 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Tue Nov 3 23:18:41 2020 +0000

    Initial commit of fault injection scripts
    
    includes a update to top_testbench that will be seen by the
    mainline booker nci project if merged back to dev
    
    Change-Id: I04f369e59b457f8372b8d2c9487bcec88b3455cb

diff --git a/logical/shared/scripts/fusa/qverify_get_flops.tcl b/logical/shared/scripts/fusa/qverify_get_flops.tcl
new file mode 100755
index 00000000000..dce5a952fd5
--- /dev/null
+++ b/logical/shared/scripts/fusa/qverify_get_flops.tcl
@@ -0,0 +1,116 @@
+proc dumpFlops { module outputFile} {
+    namespace import -force Netlist::*
+    set nets [GetNets $module]
+    while { [set net [GetNext $nets]] != "" } {
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
+    # One-Dimensional Arrays
+    } elseif {$type_array_length == 2} {
+
+      # get dimensions of the array
+      set type [string trim [lindex $type_array 1]]
+      set type [string trim $type \]]
+      set register_index [split $type :]
+      set register_1st_index [lindex $register_index 0]
+      set register_2nd_index [lindex $register_index 1]
+      set register_max_index [expr max($register_1st_index, $register_2nd_index)]
+      set register_min_index [expr min($register_1st_index, $register_2nd_index)]
+      if {$width != [expr $register_max_index - $register_min_index + 1]} {
+        echo "width = $width, but max = $register_max_index and min = $register_min_index"
+        exit
+      }
+
+      #print to file
+      set i $register_min_index
+      while  {$i <= $register_max_index} {
+        puts $outputFile "$reg\($i\)"
+        set i [expr $i + 1]
+      }
+    # Two dimensional arrays
+    } elseif {$type_array_length == 3} {
+
+      # get dimensions of the first array
+      set first_array_dimensions [string trim [lindex $type_array 1]]
+      set first_array_dimensions [string trim $first_array_dimensions \]]
+      set first_array_dimensions [split $first_array_dimensions :]
+      set first_array_1st_index  [lindex $first_array_dimensions 0]
+      set first_array_2nd_index  [lindex $first_array_dimensions 1]
+      set first_array_max_index   [expr max($first_array_1st_index, $first_array_2nd_index)]
+      set first_array_min_index   [expr min($first_array_1st_index, $first_array_2nd_index)]
+
+      # get dimensions of the 2nd array
+      set second_array_dimensions [string trim [lindex $type_array 2]]
+      set second_array_dimensions [string trim $second_array_dimensions \]]
+      set second_array_dimensions [split $second_array_dimensions :]
+      set second_array_1st_index  [lindex $second_array_dimensions 0]
+      set second_array_2nd_index  [lindex $second_array_dimensions 1]
+      set second_array_max_index  [expr max($second_array_1st_index, $second_array_2nd_index)]
+      set second_array_min_index  [expr min($second_array_1st_index, $second_array_2nd_index)]
+
+      # print to file
+      set i $first_array_min_index
+      while  {$i <= $first_array_max_index} {
+        set j $second_array_min_index
+        while {$j <= $second_array_max_index} {
+          puts $outputFile "$reg\($i\)\($j\)"
+          set j [expr $j + 1]
+        }
+        set i [expr $i + 1]
+      }
+
+
+    } else {
+      echo "error - length too long $type"
+      echo "net is: $reg"
+      continue
+#      exit
+    }
+
+    #echo "reg is $reg, width is $width, type is $type, type_array_length = $type_array_length"
+    }
+    set insts [GetInstances $module]
+    while { [set inst [GetNext $insts]] != "" } {
+      set downModule [GetMasterModule $inst]
+      # descend recursively through the instance hierarchy
+      dumpFlops $downModule $outputFile
+    }
+}
+
+# start from the -d top module and descend down through the design
+# finding all the register nets
+set topMod [Netlist::GetTopModule]
+set outputFile [open "chariot_register_file.txt" w]
+dumpFlops $topMod $outputFile
+close $outputFile
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

## Other-author context c53d65457f8e62c88e46411fd533cf491782caeb

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit c53d65457f8e62c88e46411fd533cf491782caeb
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Wed Nov 25 14:31:17 2020 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Wed Nov 25 22:12:53 2020 +0000

    this commit does a couple of things
    
    first, it changes the meaning of pass and fail for CHARIOT_ASIL_B tests
    2nd, it improves the coverage to the stimulus (default test) for chariot_ASIL_B tests
    
    Change-Id: I332a3dee6776e9f4be4c88da74e204de725f52f3

diff --git a/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh b/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh
new file mode 100644
index 00000000000..c6599255e40
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/scoreboards/chariot_fault_injection_scoreboard.svh
@@ -0,0 +1,190 @@
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
+// Purpose : Chariot Scoreboard to demote expected tb fails and fail if faults
+//           are injected, but neither the tb and stimulus see any effects
+//
+//           Note: this changes the meaning of Pass/Fail
+//
+//------------------------------------------------------------------------------
+
+`ifndef CHARIOT_INTERRUPT_SB__SVH
+`define CHARIOT_INTERRUPT_SB__SVH
+
+// The interrupt scoreboard will only check for raising interrupts. The
+// interrupt handler will predict lowering of the interrupt
+class chariot_fault_injection_scoreboard extends uvm_scoreboard;
+  `uvm_component_utils(chariot_fault_injection_scoreboard)
+
+  // creating a local class below to demote errors
+  typedef class demoter_t;
+  demoter_t demoter;
+  bit enable_interrupt_detection = 1; // set to 1 by default, so not currently disabled
+  bit caught_expected_error;
+  string first_fail_message;
+
+  function new (string name="chariot_fault_injection_scoreboard", uvm_component parent);
+    super.new(name, parent);
+  endfunction
+
+//  virtual por_top_misc_intf    top_misc_if[int];
+
+  function void build_phase(uvm_phase phase);
+    super.build_phase(phase);
+    demoter = new;
+//    demoter.top_misc_if = top_misc_if;
+    demoter.parent = this;
+  endfunction
+
+  task run_phase(uvm_phase phase);
+      demote_errors();
+//    if($test$plusargs("fault_injection_fatal_on_interrupt")) begin
+//            // Make the demoter suppress all errors
+//      demoter.delay_all = 1;
+//      demoter.allow_uvm_info = 1;
+//
+//      wait(enable_interrupt_detection);
+//
+//      `uvm_info(get_type_name(), "waiting for pins to be forced", UVM_NONE)
+//      demote_errors();
+//      wait((top_misc_if[0].safety_interrupt === 1'b1) || (top_misc_if[0].pins_are_being_forced === 1'b1));
+//      `uvm_info(get_type_name(), $sformatf("safety_interrupt = %d, pins_are_being_forced = %d",top_misc_if[0].safety_interrupt, top_misc_if[0].pins_are_being_forced), UVM_NONE)
+//
+//      if ((top_misc_if[0].safety_interrupt === 1'b1) && !(top_misc_if[0].pins_are_being_forced === 1'b1)) begin
+//        `uvm_error(get_type_name(), "Unexpected safety interrupt!")
+//      end
+//
+//      // if we reach this point, interrupts are expected
+//      wait(top_misc_if[0].safety_interrupt === 1'b1);
+//      caught_expected_error = 1;
+//      `uvm_info(get_type_name(), "Caught expected interrupt - force ending test", UVM_NONE)
+//
+//      uvm_domain::jump_all(uvm_extract_phase::get());
+//    end - in plusarg
+  endtask
+
+  function void check_phase(uvm_phase phase);
+//    if($test$plusargs("fault_injection_fatal_on_interrupt")) begin
+      if (!caught_expected_error) begin
+        `uvm_error(get_type_name(), "Did not catch interrupt!")
+      end
+//    end
+  endfunction
+
+  function void report_phase(uvm_phase phase);
+    super.report_phase(phase);
+    if (first_fail_message != "") begin
+      `uvm_info(get_type_name, $sformatf("successfully caught the following error : %s", first_fail_message), UVM_NONE);
+    end
+  endfunction
+
+  function void demote_errors();
+    // Since we're going to end the test, register the demoter!
+    uvm_report_cb::add(null, demoter);
+    // Since there are some random $error calls, use assertoff for now. We
+    // should probably unify the messaging later on
+//    $assertoff(); - DO this in .do file instead - otherwise, $assert($cast(xxxx,yyyy) won't even be executed
+    $assertcontrol(9); // 9 = failoff, where we turn off fails associated with assertions
+  endfunction
+
+  // Demote all error messages except the ones from this test!
+  class demoter_t extends uvm_report_catcher;
+    bit ovl_only;
+    bit demote_all;
+    bit delay_all; // this variable delays the fatals/errors for N cycles to give time for the fusa interrupt
+    bit allow_uvm_info;
+    uvm_report_object permitted_reporter;
+    int delay_count = 1000;
+//    virtual por_top_misc_intf       top_misc_if[int];
+    string first_fail_message;
+    string message_queue[$];
+    chariot_fault_injection_scoreboard parent;
+
+    function new(string name="demoter");
+      super.new(name);
+      ovl_only = 0;
+      demote_all = 0;
+      delay_all = 1;
+      allow_uvm_info = 1;
+    endfunction
+
+    function action_e catch();
+
+      uvm_severity severity  = get_severity();
+      string       id        = get_id();
+      uvm_action   action    = get_action();
+      string       message   = get_message();
+      int          verbosity = get_verbosity();
+
+      // Once the demoter is active, suppress all messages but our own
+      if (allow_uvm_info && severity == UVM_INFO) begin
+        // Don't mess with UVM_INFO
+        return THROW;
+      end
+
+      // always report errors from this scoreboard
+      if (id == "chariot_fault_injection_scoreboard" || id == "DEMOTER") begin
+        return THROW;
+      end
+
+      if (demote_all) begin
+        return CAUGHT;
+      end
+      else if (delay_all) begin
+        //delaying all a fixed number of clock cycles
+//        top_misc_if[0].fatal_occurred = 1;
+        fork
+          begin
+//            repeat (delay_count) @(posedge top_misc_if[0].TB_FREE_RUNNING_CLK);
+            #10000
+            uvm_report_error("DEMOTER", first_fail_message, UVM_NONE); // first fail is the most important
+            foreach (message_queue[i]) begin
+              if (i<100) begin // only print 100 extra fail messages to prevent logs that are too verbose
+                uvm_report_error("DEMOTER", message_queue[i], UVM_NONE);
+              end else begin
+                break;
+              end
+            end
+            uvm_report_fatal("DEMOTER", first_fail_message, UVM_NONE); //fatal, and report the first fail again for good measure
+         end
+        join_none
+        if (first_fail_message == "") begin
+          first_fail_message = message;
+          parent.first_fail_message = first_fail_message;
+        end
+        message_queue.push_back(message);
+        return CAUGHT;
+      end
+      else begin //demote all except for permitted reporters, possibly ovls
+        if (get_client() == permitted_reporter) begin
+          // If all messages shouldn't be demoted, then only the permitted
+          // reporter should be allowed through
+          return THROW;
+        end
+
+        if (ovl_only && get_id() != "OVL_ERROR") begin
+          // For the OVL suppression, don't catch other errors
+          return THROW;
+        end
+      end
+
+      // if we still fall through, return throw
+      return THROW;
+    endfunction
+
+  endclass
+endclass
+
+`endif // CHARIOT_INTERRUPT_SB__SVH
```

## Other-author context 2d1718066b9a38b5f333bf08106716ff9aa10b94

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit 2d1718066b9a38b5f333bf08106716ff9aa10b94
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Wed Jan 6 20:22:04 2021 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Wed Jan 6 20:22:04 2021 +0000

    adding support for write req/rsp channel protection
    
    Change-Id: Ic352ce040f38b73b9034409eac3cd89043bf0b50

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
new file mode 100755
index 00000000000..b72b0c85582
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
@@ -0,0 +1,36 @@
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
+// Purpose : Chariot write request parity checker
+//           Protects most of the address, and some other small fields
+//------------------------------------------------------------------------------
+
+module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
+    input [ADDR_WIDTH-1:0] addr_i,
+    input valid_i,
+    input nonsec_i,
+    input [USER_WIDTH-1:0] user_i,
+    output error_o
+);
+
+    logic [USER_WIDTH-1:0] err_array;
+    logic [USER_WIDTH-1:0] user_expected;
+
+    logic [ADDR_WIDTH-20:0] protectable_value;
+    
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
+    assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
+    assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
new file mode 100755
index 00000000000..14b5a261929
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
@@ -0,0 +1,31 @@
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
+// Purpose : Chariot write request parity generation
+//           protects most of the address, and a few other fields
+//------------------------------------------------------------------------------
+
+module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
+    input [ADDR_WIDTH-1:0]  addr_i,
+    input                   nonsec_i,
+    input [USER_WIDTH-1:0]  user_i, //currently unused, but will be required if customer wants additional user bits
+    output [USER_WIDTH-1:0] user_o
+);
+
+    logic [ADDR_WIDTH-20:0] protectable_value; 
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
+    assign user_o = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
+
+endmodule
```

## Other-author context 99937b8c02a02511fba7c67e602dce610aca453e

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit 99937b8c02a02511fba7c67e602dce610aca453e
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Wed Jan 27 18:42:44 2021 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Wed Jan 27 18:42:44 2021 +0000

    Revert "Add parity protection for read requests and responses"
    
    This reverts commit 8452bb85684afd82d80cdc2e90a7d3296dacaf4c.
    
    Change-Id: Ide0262c9518cde27c2772aa80d614ccd39bc2c5d

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
index bcf18752b04..b72b0c85582 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv
@@ -28,8 +28,9 @@ module chariot_wreq_parity_checker #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     logic [USER_WIDTH-1:0] err_array;
     logic [USER_WIDTH-1:0] user_expected;
 
-    logic [ADDR_WIDTH-10+1:0] protectable_value;
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
+    logic [ADDR_WIDTH-20:0] protectable_value;
+    
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
     assign user_expected = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
     assign error_o   = (user_expected ^ user_i) && valid_i; // only set when WVALID is high
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
index 2055fc82eb8..14b5a261929 100755
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv
@@ -24,8 +24,8 @@ module chariot_wreq_parity_generator #(ADDR_WIDTH = -1, USER_WIDTH = -1) (
     output [USER_WIDTH-1:0] user_o
 );
 
-    logic [ADDR_WIDTH-10+1:0] protectable_value;
-    assign protectable_value = {addr_i[ADDR_WIDTH-1:9],addr_i[0]};
+    logic [ADDR_WIDTH-20:0] protectable_value; 
+    assign protectable_value = {addr_i[ADDR_WIDTH-1:20]}; 
     assign user_o = {{USER_WIDTH-1{1'b0}}, {~(^protectable_value)}};
 
 endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index 14cf393f92c..2f83975d237 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -700,13 +700,10 @@ module interface_block
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
-                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
-                      logic [ARUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
                         logic parity_err_wrsp;
-                        logic parity_err_rrsp;
-                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
+                        assign parity_error = parity_err_wrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -718,27 +715,15 @@ module interface_block
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
                         );
-                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
-                          .addr_i  (u_if.ARADDR),
-                          .user_i (u_if.ARUSER),
-                          .nonsec_i (u_if.ARPROT[1]),
-                          .user_o (rreq_err_code)
-                        );
                         chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
                           .valid_i (u_if.BVALID),
                           .user_i  (u_if.BUSER),
                           .error_o (parity_err_wrsp)
                         );
-                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
-                          .valid_i (u_if.RVALID),
-                          .user_i  (u_if.RUSER),
-                          .error_o (parity_err_rrsp)
-                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
-                        logic parity_err_rreq;
                         logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
+                        assign parity_error = parity_err_wreq | parity_err_wdat;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -753,19 +738,9 @@ module interface_block
                           .valid_i (u_if.AWVALID),
                           .error_o (parity_err_wreq)
                         );
-                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
-                          .addr_i  (u_if.ARADDR),
-                          .user_i  (u_if.ARUSER),
-                          .nonsec_i  (u_if.ARPROT[1]),
-                          .valid_i (u_if.ARVALID),
-                          .error_o (parity_err_rreq)
-                        );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
                           .user_o (wrsp_err_code)
                         );
-                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
-                          .user_o (rrsp_err_code)
-                        );
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_ace4_lite
@@ -1202,13 +1177,10 @@ module interface_block
                     `ifdef CHARIOT_ASIL_B
                       logic [WUSER_WIDTH-1:0]  wdat_err_code;
                       logic [AWUSER_WIDTH-1:0] wreq_err_code;
-                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
                       logic [AWUSER_WIDTH-1:0] wrsp_err_code;
-                      logic [ARUSER_WIDTH-1:0] rrsp_err_code;
                       if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
                         logic parity_err_wrsp;
-                        logic parity_err_rrsp;
-                        assign parity_error = parity_err_wrsp | parity_err_rrsp;
+                        assign parity_error = parity_err_wrsp;
                         chariot_wdat_parity_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_gen (
                           .data_i (u_if.WDATA),
                           .strb_i (u_if.WSTRB),
@@ -1220,27 +1192,15 @@ module interface_block
                           .nonsec_i (u_if.AWPROT[1]),
                           .user_o (wreq_err_code)
                         );
-                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
-                          .addr_i  (u_if.ARADDR),
-                          .user_i (u_if.ARUSER),
-                          .nonsec_i (u_if.ARPROT[1]),
-                          .user_o (rreq_err_code)
-                        );
                         chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
                           .valid_i (u_if.BVALID),
                           .user_i  (u_if.BUSER),
                           .error_o (parity_err_wrsp)
                         );
-                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
-                          .valid_i (u_if.RVALID),
-                          .user_i  (u_if.RUSER),
-                          .error_o (parity_err_rrsp)
-                        );
                       end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
                         logic parity_err_wreq;
-                        logic parity_err_rreq;
                         logic parity_err_wdat;
-                        assign parity_error = parity_err_wreq | parity_err_wdat | parity_err_rreq;
+                        assign parity_error = parity_err_wreq | parity_err_wdat;
                         chariot_wdat_parity_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_parity_check (
                           .data_i  (u_if.WDATA),
                           .valid_i (u_if.WVALID),
@@ -1255,19 +1215,9 @@ module interface_block
                           .valid_i (u_if.AWVALID),
                           .error_o (parity_err_wreq)
                         );
-                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
-                          .addr_i  (u_if.ARADDR),
-                          .user_i  (u_if.ARUSER),
-                          .nonsec_i  (u_if.ARPROT[1]),
-                          .valid_i (u_if.ARVALID),
-                          .error_o (parity_err_rreq)
-                        );
                         chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
                           .user_o (wrsp_err_code)
                         );
-                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
-                          .user_o (rrsp_err_code)
-                        );
                       end
                     `endif // CHARIOT_ASIL_B
           end : g_axi4
@@ -1450,6 +1400,7 @@ module interface_block
       `ifdef CHARIOT_ASIL_B
         logic [WUSER_WIDTH-1:0]  wdat_err_code;
         logic [AWUSER_WIDTH-1:0] wreq_err_code;
+        logic [AWUSER_WIDTH-1:0] wrsp_err_code;
         logic [DATA_WIDTH/8-1:0] strobe; //strobe not part of the ahb protocol, so we generate it here
 
         chariot_ahb_strobe_generation #(.DATA_WIDTH(DATA_WIDTH), .ADDR_WIDTH(ADDR_WIDTH)) strobe_gen (
@@ -1491,7 +1442,7 @@ module interface_block
             .addr_i   (u_if.HADDR),
             .user_i   (u_if.HAUSER),
             .nonsec_i (u_if.HNONSEC),
-            .valid_i  (u_if.HREADY && u_if.HTRANS[1]),
+            .valid_i  (u_if.HREADY && u_if.HTRANS[1] && u_if.HWRITE),
             .error_o  (parity_err_wreq)
           );
         end
diff --git a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
index e7524cc5ae1..52c6ad86c33 100644
--- a/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
+++ b/logical/shared/scripts/noc_param_engine/noc_external_bindings/noc_testbench_wrapper.py
@@ -521,11 +521,7 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
           wrapper_data["AHB_User_Bits"].append("wire [" + str(paramObj["BUSER_RESP_WIDTH"]-1) + ":0] asni_" + str(interface_index) + "_BUSER;\n")
           wrapper_data["AHB_User_Bits"].append("assign g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.BUSER = {" + str(ruser_extra_bits) + "'b0, asni_" + str(interface_index) + "_BUSER};\n")
           wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_BUSER                    " , "Testbench" : "asni_" + str(interface_index) + "_BUSER"})
-      if paramObj["USER_REQ_WIDTH"] > 0:
-        if _chariot_b:
-          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".rreq_err_code     "})
-        else:
-          wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
+      if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_ARUSER                   " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.ARUSER       "})
       if (ruser_extra_bits >= 0): # ruser width > buser_width
         if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_SLAVE_" + str(export_id) + "_RUSER                    " , "Testbench" : "g_interface[" + str(interface_index) + "].master.u_if." + str(interface_name) + ".u_if.RUSER        "})
       else:
@@ -774,10 +770,6 @@ def generate_binding(_dataset_file, _cfgname, _output, _chariot_b) :
             wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_BUSER        " , "Testbench" : " amni_" + str(interface_index) + "_BUSER    "})
       if paramObj["USER_REQ_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_ARUSER       "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.ARUSER       "})
       # if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        "  , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
-      if _chariot_b:
-        if (ruser_extra_bits >= 0): # ruser width > buser_width
-          if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".rrsp_err_code     "})
-      else:
       if (ruser_extra_bits >= 0): # ruser width > buser_width
         if paramObj["RUSER_RESP_WIDTH"] + paramObj["USER_DATA_WIDTH"] > 0: wrapper_data["Interface"].append({"Port" : str(protocol_name) + "_MASTER_" + str(export_id) + "_RUSER        " , "Testbench" : "g_interface[" + str(interface_index) + "].slave.u_if." + str(interface_name) + ".u_if.RUSER        "})
       else:
```

## Other-author context e1382ca03cf1858b5d74e8fd472dcdadc4f59098

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit e1382ca03cf1858b5d74e8fd472dcdadc4f59098
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Mon Mar 15 19:42:30 2021 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Mon Mar 15 19:42:30 2021 +0000

    fixes for wdat_ecc checker
    
    Change-Id: I843d37cf3b8203b8824c20fd0d0901b4dd07f974

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
index 1668c626477..64968235736 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
@@ -39,7 +39,7 @@ module chariot_wdat_ecc_checker #(DATA_WIDTH = -1, USER_WIDTH = -1) (
         msg = 0;
         index_xor = 0;
         j = 0;
-        if (valid_i && user_i[i*8+7] && (strb_i[i*(DATA_WIDTH/8)+((DATA_WIDTH/8)-1):i*(DATA_WIDTH/8)] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
+        if (valid_i && user_i[i*8+7] && (strb_i[i*4+3:i*4] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
           msg = {
             25'b0,                             //msg[63:39]
             data_i[(i*32)+31:(i*32)+26],       //msg[38:33]//33
```

## Other-author context f2603804d15af6e69ba074c082ed08639c0d6195

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit f2603804d15af6e69ba074c082ed08639c0d6195
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Tue Jun 1 19:28:41 2021 +0100
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Tue Jun 1 19:28:41 2021 +0100

    Turning on error correction
    
    also adds reporting messages to say which mechanisms caught a fail
    
    Change-Id: I6e1d3c4926f677c88bb4744bd85fdeb233203b91

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
index 64968235736..34c126c476c 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv
@@ -21,9 +21,9 @@ module chariot_wdat_ecc_checker #(DATA_WIDTH = -1, USER_WIDTH = -1) (
   input [USER_WIDTH-1:0] user_i,
   input valid_i,
   input [DATA_WIDTH/8-1:0] strb_i,
-  output logic [(DATA_WIDTH/32)-1:0] error_o,
-  output logic [(32*(DATA_WIDTH/32))-1:0] errors_1_bit_o,
-  output logic [(DATA_WIDTH/32)-1:0] errors_2_bits_o
+  output logic [(DATA_WIDTH/32)-1:0] uncorrectable_errs_o, // 1 error bit for each set of 32 bits
+  output logic [(DATA_WIDTH/32)-1:0] correctable_errs_o, // 1 error bit for each set of 32 bits
+  output logic [(DATA_WIDTH)-1:0]    correctable_bits_vector_o // bit vector that can be inverted with the recieved data to get the corrected data
 );
 
   genvar i;
@@ -33,13 +33,14 @@ module chariot_wdat_ecc_checker #(DATA_WIDTH = -1, USER_WIDTH = -1) (
       logic [5:0] index_xor;
       integer j;
       always @(*) begin
-        error_o[i] = 0;
-        errors_1_bit_o[(i*32)+31:(i*32)] = 32'd0;
-        errors_2_bits_o[i] = 0;
+        correctable_errs_o[i] = 0;
+        correctable_bits_vector_o[(i*32)+31:(i*32)] = 32'd0;
+        uncorrectable_errs_o[i] = 0;
         msg = 0;
-        index_xor = 0;
+        index_xor = 0; // this represents which bit has been corrupted
         j = 0;
-        if (valid_i && user_i[i*8+7] && (strb_i[i*4+3:i*4] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
+        //if (valid_i && user_i[i*8+7] && (strb_i[i*4+3:i*4] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
+        if (valid_i && (strb_i[i*4+3:i*4] != 0)) begin // errors only thrown when valid is high, data is being written from a master device, and strb_i is not all 0s
           msg = {
             25'b0,                             //msg[63:39]
             data_i[(i*32)+31:(i*32)+26],       //msg[38:33]//33
@@ -55,25 +56,26 @@ module chariot_wdat_ecc_checker #(DATA_WIDTH = -1, USER_WIDTH = -1) (
             user_i[(i*8)+1],                   //msg[1]
             user_i[(i*8)+0]                    //msg[0]
           };
+          // this code is simple and clever, xoring the appropriate bits
           for (j=0; j<64; j=j+1) begin
             if (msg[j]) begin
               index_xor = index_xor ^ j;
             end
           end
-          if (user_i[i*8] != ~^msg[63:1]) begin // 1 bit flip
-            error_o[i] = 1;
-            index_xor = ~index_xor;
-            errors_1_bit_o[(i*32)+31:(i*32)] = (index_xor == 6'd3) ? 0 :
-                          (index_xor >= 6'd5  && index_xor <= 6'd7)  ? (index_xor-4)+(i*32) :
-                          (index_xor >= 6'd9  && index_xor <= 6'd15) ? (index_xor-5)+(i*32) :
-                          (index_xor >= 6'd17 && index_xor <= 6'd31) ? (index_xor-6)+(i*32) :
-                          (index_xor >= 6'd33 && index_xor <= 6'd38) ? (index_xor-7)+(i*32) :
-                          ~32'b0; // error was not a data bit
+          index_xor = ~index_xor; // invert all bits, since we're using odd parity.
+          if ((user_i[i*8] != ~^msg[63:1]) && (user_i[i*8+7] != ^strb_i[i*4+3:i*4])) begin // if 1 bit has flipped (the lowest parity bit will not match if an odd number of bits have flipped), and strobe parity is correct
+            correctable_errs_o[i] = 1;
+            // this section identifies which bit needs to be corrected. 
+            correctable_bits_vector_o[(i*32)+31:(i*32)] = (index_xor == 6'd3) ? 1 + (i*32) : //if bit position 3 (first data bit) is messed up, invert the first data bit
+                          (index_xor >= 6'd5  && index_xor <= 6'd7)  ? 1<<(index_xor-4)+(i*32) : //subtract 4 because there are 4 bits of parity in front that need to be accounted for
+                          (index_xor >= 6'd9  && index_xor <= 6'd15) ? 1<<(index_xor-5)+(i*32) : //subtract 5 because there are 4 bits of parity in front that need to be accounted for
+                          (index_xor >= 6'd17 && index_xor <= 6'd31) ? 1<<(index_xor-6)+(i*32) : //subtract 6 because there are 4 bits of parity in front that need to be accounted for
+                          (index_xor >= 6'd33 && index_xor <= 6'd38) ? 1<<(index_xor-7)+(i*32) : //subtract 7 because there are 4 bits of parity in front that need to be accounted for
+                          32'b0; // error was not a data bit
 
-          end else begin // no errors or 2 bit flips
-            if (index_xor != 6'b111111) begin
-              error_o[i] = 1;
-              errors_2_bits_o[i] = 1;
+          end else begin // no errors or 2 bit flips or strobe parity error
+            if ((index_xor != 6'b0) || (user_i[i*8+7] == ^strb_i[i*4+3:i*4])) begin
+              uncorrectable_errs_o[i] = 1;
             end
           end
         end
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv
index d1a0ed51eda..adbf129140a 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv
@@ -73,7 +73,7 @@ module chariot_wdat_ecc_generator #(DATA_WIDTH = -1, USER_WIDTH = -1) (
           end
         end
         parity_bits[0] = ~^{strobed_data[31:0],parity_bits[6:1]}; // odd parity of entire message
-        user_o[(i*8)+7:(i*8)] = {1'b1,parity_bits[6:0]};
+        user_o[(i*8)+7:(i*8)] = {(~^strb_i[i*4+3:i*4]),parity_bits[6:0]};
       end
     end
   endgenerate
```

## Other-author context 132198680b02ca12a89c8127c412dd48d36bd338

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit 132198680b02ca12a89c8127c412dd48d36bd338
Author:     Sean Steel <sean.steel@arm.com>
AuthorDate: Wed Mar 17 17:26:35 2021 +0000
Commit:     Sean Steel <sean.steel@arm.com>
CommitDate: Wed Mar 17 17:26:35 2021 +0000

    Fixes to the get_flops script to avoid tied-off bits in register arrays
    
    This is a big improvement to the get_flops script
    Previously, the get_flops script would not differentiate between tied-off bits
    within register arrays. For instance, in the crb_converter blocks, some registers
    would be defined as 32 bits wide, but only a few bits would actually exist as
    registers, the rest would be tied-off. The previous script would list all 32
    bits as "flops", but the new script properly only identifies the flops that
    are not tied off
    
    Change-Id: I9859db38c1bc002f23a3b0b11d306c92cbc8c9cf

diff --git a/logical/shared/scripts/fusa/qverify_get_flops.tcl b/logical/shared/scripts/fusa/qverify_get_flops.tcl
index 9c5384bbdbe..84d285c05f8 100755
--- a/logical/shared/scripts/fusa/qverify_get_flops.tcl
+++ b/logical/shared/scripts/fusa/qverify_get_flops.tcl
@@ -3,11 +3,15 @@ proc printArray { outputFile reg_name array_size max_array_index min_array_index
   #create the flop name
   set index 0
   set flop_name $reg_name
+  set qverify_internal_flop_name $reg_name
   while { $index < $array_size } {
+    set qverify_internal_flop_name "$qverify_internal_flop_name\[[lindex $current_array_index $index]\]"
     set flop_name "$flop_name\([lindex $current_array_index $index]\)"
     set index [expr $index + 1]
   }
+  if {[Query [GetNet $qverify_internal_flop_name] isReg]} {
     puts $outputFile $flop_name
+  }
 
   # pick the next entry to write
   set next_index $current_array_index
@@ -84,6 +88,7 @@ proc dumpFlops { module outputFile } {
 # start from the -d top module and descend down through the design
 # finding all the register nets
 set topMod [Netlist::GetTopModule]
+#set topMod [Netlist::GetMasterModule [Netlist::GetInstance ni700_brunel_1x1_AHB5_AHB5_chariot_b.u_s0]]
 set outputFile [open "chariot_register_file.txt" w]
 # increase recursion limit - tcl 8.6 has no limit, and some multi-dimensional arrays are > 1000, which is the default tcl limit
 interp recursionlimit {} 64000
```

## Other-author context cde13afb3503f64717b468bdd38ca846f8465063

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit cde13afb3503f64717b468bdd38ca846f8465063
Author:     Jordon Kashanchi <jorkas01@login12.euhpc2.arm.com>
AuthorDate: Fri Aug 6 22:30:44 2021 +0100
Commit:     Jordon Kashanchi <jorkas01@login12.euhpc2.arm.com>
CommitDate: Fri Aug 6 23:05:18 2021 +0100

    hang detector beat counter
    
    Change-Id: I9a8d1adb6ecdb7e5d610ec920be7b2ad077185ee

diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_read.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_read.sv
new file mode 100644
index 00000000000..07d8e84687f
--- /dev/null
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_read.sv
@@ -0,0 +1,208 @@
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
+module chariot_axi_hang_detector_read #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
+  input clk_i,
+  input resetn_i,
+  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] aid_i,
+  input avalid_i,
+  input aready_i,
+  input [7:0] alength_i,
+  input [2:0] asize_i,
+  input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] id_i,
+  input valid_i,
+  input last_i,
+  input ready_i,
+  output logic error_1_o,
+  output logic error_2_o
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
+  
+  
+  // a full tracker entry consists of the tracker_valid, tracker_id, and the tracker_timestamp
+  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids;
+  logic [((ID_WIDTH > 0) ? (TRACKER_LENGTH-1) : 0):0] tracker_valids_reg;
+  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] tracker_ids_reg [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 1 : 0):0] tracker_timestamps_reg [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 11 : 0):0] tracker_bytecounter [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? 11 : 0):0] tracker_bytecounter_reg [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? (COUNTER_WIDTH-1) : 0):0] tracker_timeid [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? (COUNTER_WIDTH-1) : 0):0] tracker_timeid_reg [0:TRACKER_LENGTH-1];
+  logic [((ID_WIDTH > 0) ? (COUNTER_WIDTH-1) : 0):0] oldest_transfer;
+  integer i;
+  integer j;
+  integer k;
+  integer a;
+  integer b;
+
+  // if avalid_i && aready_i, insert into a non-valid tracker entry and mark valid
+  // if valid_i && last_i && ready_i, find the valid entries in the tracker with matching IDs, and remove the oldest one
+
+  always @(*) begin
+    error_2_o = 0;
+    oldest_transfer = 0;
+    if (~resetn_i) begin
+      counter = 0;
+      insert_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      tracker_valid_mask_inverted = 0;
+      remove_complete = 0;
+      remove_index = TRACKER_LENGTH; // intentionally set to a number outside of tracker bounds initially
+      remove_mask = 0;
+      tracker_valids = 0;
+      insert_index_encoded = 0;
+
+    end else begin
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
+        tracker_bytecounter[i] = tracker_bytecounter_reg[i];
+        tracker_timeid[i] = tracker_timeid_reg[i];
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
+        tracker_bytecounter[insert_index] = alength_i; // +1 here??
+        tracker_timeid[insert_index] = counter_reg[COUNTER_WIDTH-1:0];
+      end
+      // removing from tracker
+      // if multiple entries in the tracker are valid, have the same ID, and have the same timestamp, the entry with the largest index will be removed
+      // check to see which tracker entries are valid and have a matching rid
+      for (j=0; j<TRACKER_LENGTH; j=j+1) begin
+        if (tracker_valids_reg[j] && tracker_ids_reg[j] == id_i) begin
+          if(counter_reg - tracker_timeid_reg[j] > oldest_transfer) begin
+            oldest_transfer = counter_reg - tracker_timeid_reg[j];
+            b = j;
+          end
+        end
+      end
+      if (tracker_valids_reg[b] && tracker_ids_reg[b] == id_i) begin
+        remove_mask[b] = 1;
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
+
+        if(tracker_bytecounter_reg[remove_index] == 0) begin
+          tracker_valids[remove_index] = 0;
+        end
+
+        if (tracker_bytecounter_reg[remove_index] < 0) begin
+            error_2_o = 1;
+        end
+      end
+      else if (valid_i && ready_i) begin
+        tracker_bytecounter[remove_index] = tracker_bytecounter[remove_index] - 1;
+      end
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
+    error_1_o = 0;
+    if (~resetn_i) begin
+      hang_detection_state = `IDLE;
+    end else begin
+      if (hang_detection_state_reg == `IDLE) begin
+        hang_detection_state = `IDLE;
+        if (counter[COUNTER_WIDTH-1:COUNTER_WIDTH-2] != counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
+          hang_detection_state = `CHECK_FOR_HANG;
+        end
+      end else if (hang_detection_state_reg == `CHECK_FOR_HANG) begin
+        hang_detection_state = `IDLE;
+        for (k=0; k<TRACKER_LENGTH; k=k+1) begin
+          // if any tracker entry is valid and has a timestamp that matches the most significant 2 bits of the counter, throw hang error
+          if (tracker_valids_reg[k] && tracker_timestamps_reg[k]==counter_reg[COUNTER_WIDTH-1:COUNTER_WIDTH-2]) begin
+            error_1_o = 1;
+          end
+        end
+      end
+    end
+  end
+
+  always @(posedge clk_i or negedge resetn_i) begin
+    if (~resetn_i) begin
+      counter_reg <= 0;
+      hang_detection_state_reg <= `IDLE;
+      tracker_valids_reg <= 0;
+      
+    end else begin
+      counter_reg <= counter;
+      hang_detection_state_reg <= hang_detection_state;
+      tracker_valids_reg <= tracker_valids;
+      for (a=0; a<TRACKER_LENGTH; a=a+1) begin
+        tracker_ids_reg[a] <= tracker_ids[a];
+        tracker_timestamps_reg[a] <= tracker_timestamps[a];
+        tracker_bytecounter_reg[a] <= tracker_bytecounter[a];
+        tracker_timeid_reg[a] <= tracker_timeid[a];
+      end
+    end
+  end
+
+endmodule
diff --git a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_write.sv
similarity index 98%
rename from logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
rename to logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_write.sv
index fbc506180d8..c040df5fe8e 100644
--- a/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector.sv
+++ b/logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_write.sv
@@ -15,7 +15,7 @@
 //------------------------------------------------------------------------------
 // Purpose : Chariot AXI hang detector
 //------------------------------------------------------------------------------
-module chariot_axi_hang_detector #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
+module chariot_axi_hang_detector_write #(ID_WIDTH = -1, TRACKER_LENGTH = -1, COUNTER_WIDTH = -1) (
   input clk_i,
   input reset_i,
   input [((ID_WIDTH > 0) ? (ID_WIDTH-1) : 0):0] aid_i,
```

## Other-author context 15ec8b7621ebc26393d82bbf335293b7058f1f95

Not attributed to Michael. Selected path diff, ignoring whitespace-only changes.

```diff
commit 15ec8b7621ebc26393d82bbf335293b7058f1f95
Author:     lingao01 <lin.gao@arm.com>
AuthorDate: Thu May 19 21:49:46 2022 +0100
Commit:     lingao01 <lin.gao@arm.com>
CommitDate: Thu May 19 21:57:40 2022 +0100

    Switch to Brunel modules in end_2_end tests
    
    Change-Id: I3f6c28ef707ccaba254764d68af4b26195a02541

diff --git a/logical/shared/scripts/end_to_end/load_brunel.sh b/logical/shared/scripts/end_to_end/load_brunel.sh
new file mode 100644
index 00000000000..eb015c4893a
--- /dev/null
+++ b/logical/shared/scripts/end_to_end/load_brunel.sh
@@ -0,0 +1,5 @@
+#!/bin/tcsh
+
+module load swdev python/python/3.7.2 python/pyyaml_py3.7.2
+module load core perl/perl/5.12.3
+module load eda arm/brunel/2022.05.03dev
```

## History and surviving-line context logical/noc_arachne/.control_files/chariot_fault_injection.ctrl

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
09d46bb1145ce13626725ad3b45806f8af95e8be 2021-09-27T17:15:39+01:00 Sean Steel adding get ports script to Asil-D
4aa2acc078502afa4acaff78b22245f0a532a3f5 2021-02-24T17:26:38Z Sean Steel updates to regressions to waive checks for user bits
22827d3471f874c5e7609b8c48c907d1c9dbfcd3 2020-12-10T20:12:11Z Sean Steel merge commit -merging dev into chariot-b
4ce7802d1d9d0037f6b86cc83da390b168d6431b 2020-12-10T15:52:10Z Sean Steel additional control_file fixes
492593a8f1b7a15c8f12174cda9bcf7cfd7f6c8b 2020-12-09T10:34:44Z Michael Coulter Add chariot package that includes the chariot_parity_generation and the chariot_parity_checker modules Add brunel_1x1_ACE5Lite_AXI5_chariot iyaml and corresponding generated syaml, and update chariot_fault_injection.ctrl to use new config Add --fullacc arg to ae simulate command in chariot_fault_injection.ctrl Add CHARIOT_ASIL_B defines and check_user condition to amba5_payload_checker_component.svh Modify testbench to instantiate parity read modules and associated signals Modify noc_testbench_wrapper.py to connect err_detection_code to ACELITE_SLAVE_S0_IF_WUSER Modify param_engine scripts to conditionally modify noc_testbench_wrapper.py for chariot by supplying the ae param_engine command with the '--chariot_b' flag large commit
0758416876564cb5d14aa3ebda85b1c173096482 2020-11-27T20:53:36Z Sean Steel adding +acc into chariot_fault_injection regression
c53d65457f8e62c88e46411fd533cf491782caeb 2020-11-25T14:31:17Z Sean Steel this commit does a couple of things
a8a7f9c1d538632db2acf330e0e51438adac1264 2020-11-25T21:02:32Z Sean Steel minor fixes to fault injection control file
3902fe3fb3feca6e2f06eb1424bb4c554cef2e42 2020-11-25T14:31:17Z Sean Steel this commit does a couple of things
23bcb2e434c8dfb1f10a24fcc590d8960b43a5d8 2020-11-09T16:06:16Z Sean Steel add --inject_faults as an option to ae simulate
Surviving-line author counts: {"Michael Coulter": 1, "Sean Steel": 14}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_ahb_hang_detector.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
3ba56bea53a1b7e239c7f609ef88bf8b60e83829 2021-02-19T07:01:29Z Michael Coulter Add chariot_ahb_hang_detector.sv (hang_error fires if HREADY is low for >=1000 cycles) Change delay_count to 5000 in chariot_fault_injection_scoreboard.svh
Surviving-line author counts: {"Michael Coulter": 55}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_read.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
a4866358adcf90898708e7b68f6ffba801db24d4 2021-09-21T22:15:33-05:00 swetalina Merging origin/dev to tower/dev
Surviving-line author counts: {"Michael Coulter": 145, "swetalina": 63}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_axi_hang_detector_write.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
a4866358adcf90898708e7b68f6ffba801db24d4 2021-09-21T22:15:33-05:00 swetalina Merging origin/dev to tower/dev
Surviving-line author counts: {"Michael Coulter": 170, "swetalina": 1}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_pkg.svh

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
a4866358adcf90898708e7b68f6ffba801db24d4 2021-09-21T22:15:33-05:00 swetalina Merging origin/dev to tower/dev
c22154dd2c2f91d60d1f15c6b83053be63a708eb 2021-04-07T22:05:34+01:00 Michael Coulter Generalize the AXI hang detector to work for both reads and writes
5d88abb380368baa73f3e9e2b8b6f4d2033aa398 2021-03-26T22:00:06Z Michael Coulter Adding AXI read hang detector
9a1baceb97022342da39d95f0aaf39c1e227b87c 2021-03-22T18:05:10Z Sean Steel Improving the direct_ta scenario with several features
2cb79d4081f5d79cd0aba93217e2c121b4e6348f 2021-02-24T21:34:22Z Michael Coulter Replace chariot_wdat_parity_generator/chariot_wdat_parity_checker with chariot_wdat_ecc_generator/chariot_wdat_ecc_checker
3ba56bea53a1b7e239c7f609ef88bf8b60e83829 2021-02-19T07:01:29Z Michael Coulter Add chariot_ahb_hang_detector.sv (hang_error fires if HREADY is low for >=1000 cycles) Change delay_count to 5000 in chariot_fault_injection_scoreboard.svh
ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012 2021-01-29T20:24:33Z Michael Coulter Add rdat parity generation and checker. 2 bits of user (1 valid bit, 1 parity bit) per 8 bits of data for both AXI and AHB. Set the 'invalid_byte_lanes_mode' on the transaction item in the testbench to 'INVALID_BYTE_LANES_RANDOM' to send random 0s and 1s instead of Xs for invalid read data.
2d1718066b9a38b5f333bf08106716ff9aa10b94 2021-01-06T20:22:04Z Sean Steel adding support for write req/rsp channel protection
806c7e9bb3d54d51e8af5c568d98ccb4f4364dc0 2021-01-03T19:41:16Z Sean Steel fixes for ahb configs
492593a8f1b7a15c8f12174cda9bcf7cfd7f6c8b 2020-12-09T10:34:44Z Michael Coulter Add chariot package that includes the chariot_parity_generation and the chariot_parity_checker modules Add brunel_1x1_ACE5Lite_AXI5_chariot iyaml and corresponding generated syaml, and update chariot_fault_injection.ctrl to use new config Add --fullacc arg to ae simulate command in chariot_fault_injection.ctrl Add CHARIOT_ASIL_B defines and check_user condition to amba5_payload_checker_component.svh Modify testbench to instantiate parity read modules and associated signals Modify noc_testbench_wrapper.py to connect err_detection_code to ACELITE_SLAVE_S0_IF_WUSER Modify param_engine scripts to conditionally modify noc_testbench_wrapper.py for chariot by supplying the ae param_engine command with the '--chariot_b' flag large commit
Surviving-line author counts: {"Michael Coulter": 31, "Sean Steel": 11, "swetalina": 3}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_checker.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012 2021-01-29T20:24:33Z Michael Coulter Add rdat parity generation and checker. 2 bits of user (1 valid bit, 1 parity bit) per 8 bits of data for both AXI and AHB. Set the 'invalid_byte_lanes_mode' on the transaction item in the testbench to 'INVALID_BYTE_LANES_RANDOM' to send random 0s and 1s instead of Xs for invalid read data.
Surviving-line author counts: {"Michael Coulter": 39}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_rdat_parity_generator.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
ff3fcf4dd41f5f0b212b2d6b3ef653b7b5b69012 2021-01-29T20:24:33Z Michael Coulter Add rdat parity generation and checker. 2 bits of user (1 valid bit, 1 parity bit) per 8 bits of data for both AXI and AHB. Set the 'invalid_byte_lanes_mode' on the transaction item in the testbench to 'INVALID_BYTE_LANES_RANDOM' to send random 0s and 1s instead of Xs for invalid read data.
Surviving-line author counts: {"Michael Coulter": 35}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_checker.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
8e334abdefabadf66d4bf72040ca3c16ebfde876 2021-06-16T22:10:35+01:00 Sean Steel fixes for chariot wdat ecc correction
44793ed9c17389e739907a2e90c0fb8f0cf5d7a1 2021-06-02T21:54:34+01:00 Sean Steel fixes for error correction
cd82fd7e8e7896fb522af1608f3e5e93a83bc2db 2021-06-02T01:18:05+01:00 Sean Steel removed incorrect parity checking on AHB wdat channel
f2603804d15af6e69ba074c082ed08639c0d6195 2021-06-01T19:28:41+01:00 Sean Steel Turning on error correction
e1382ca03cf1858b5d74e8fd472dcdadc4f59098 2021-03-15T19:42:30Z Sean Steel fixes for wdat_ecc checker
2cb79d4081f5d79cd0aba93217e2c121b4e6348f 2021-02-24T21:34:22Z Michael Coulter Replace chariot_wdat_parity_generator/chariot_wdat_parity_checker with chariot_wdat_ecc_generator/chariot_wdat_ecc_checker
Surviving-line author counts: {"Michael Coulter": 62, "Sean Steel": 24}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wdat_ecc_generator.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
f2603804d15af6e69ba074c082ed08639c0d6195 2021-06-01T19:28:41+01:00 Sean Steel Turning on error correction
2cb79d4081f5d79cd0aba93217e2c121b4e6348f 2021-02-24T21:34:22Z Michael Coulter Replace chariot_wdat_parity_generator/chariot_wdat_parity_checker with chariot_wdat_ecc_generator/chariot_wdat_ecc_checker
Surviving-line author counts: {"Michael Coulter": 80, "Sean Steel": 1}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_checker.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
a4866358adcf90898708e7b68f6ffba801db24d4 2021-09-21T22:15:33-05:00 swetalina Merging origin/dev to tower/dev
d8e7d9edefe1c18d2cb15669cc682d7375d6c900 2021-02-02T04:21:30Z Michael Coulter Num unprotected bits = 15
0061d5b19fa53c919287bfa6ccc9150edba032df 2021-01-29T16:34:51Z Michael Coulter Reduce number of protected address bits to 21
41d2221e7973c21437e040d51dbe75cbf73ed3c0 2021-01-28T17:05:15Z Michael Coulter Revert "Revert "Add parity protection for read requests and responses""
99937b8c02a02511fba7c67e602dce610aca453e 2021-01-27T18:42:44Z Sean Steel Revert "Add parity protection for read requests and responses"
8452bb85684afd82d80cdc2e90a7d3296dacaf4c 2021-01-25T18:21:50Z Michael Coulter Add parity protection for read requests and responses Increase number of protected address bits for write and read requests
2d1718066b9a38b5f333bf08106716ff9aa10b94 2021-01-06T20:22:04Z Sean Steel adding support for write req/rsp channel protection
Surviving-line author counts: {"Michael Coulter": 2, "Sean Steel": 31, "swetalina": 14}
```

## History and surviving-line context logical/noc_arachne/validation/dynamic/top/components/chariot/chariot_wreq_parity_generator.sv

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
a4866358adcf90898708e7b68f6ffba801db24d4 2021-09-21T22:15:33-05:00 swetalina Merging origin/dev to tower/dev
d8e7d9edefe1c18d2cb15669cc682d7375d6c900 2021-02-02T04:21:30Z Michael Coulter Num unprotected bits = 15
0061d5b19fa53c919287bfa6ccc9150edba032df 2021-01-29T16:34:51Z Michael Coulter Reduce number of protected address bits to 21
41d2221e7973c21437e040d51dbe75cbf73ed3c0 2021-01-28T17:05:15Z Michael Coulter Revert "Revert "Add parity protection for read requests and responses""
99937b8c02a02511fba7c67e602dce610aca453e 2021-01-27T18:42:44Z Sean Steel Revert "Add parity protection for read requests and responses"
8452bb85684afd82d80cdc2e90a7d3296dacaf4c 2021-01-25T18:21:50Z Michael Coulter Add parity protection for read requests and responses Increase number of protected address bits for write and read requests
2d1718066b9a38b5f333bf08106716ff9aa10b94 2021-01-06T20:22:04Z Sean Steel adding support for write req/rsp channel protection
Surviving-line author counts: {"Michael Coulter": 2, "Sean Steel": 28, "swetalina": 8}
```

## History and surviving-line context logical/shared/scripts/end_to_end/load_brunel.sh

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
a2fba8dd81bfd1f69c6cf9c6978da22ea6f58251 2026-02-06T11:04:37-06:00 Kyan Kornfeld Brunel version update for Kelly
319a710f837348a4fd2b97358cdd5d6c726b649c 2025-04-30T18:46:05-05:00 Julian Mendoza fixes and checks for DRC_ASNI_022
a7e4ab5000308e4d058fc6fcd11c8fcf4b229ea4 2024-06-18T13:23:15+01:00 lingao01 Update brunel module to rc0
7b3ccc898e1bc50c5f47d8d47c44ee790be76be2 2024-06-13T20:42:34+01:00 lingao01 Update Brunel to 2024.06.01Fdev
0b81d26d38b4c875a5565af3025d718291a8a54d 2024-06-07T14:49:42+01:00 lingao01 Update Brunel to 2024.06.01Bdev
add7b4569e7b3c2d915514491e72151395e2c582 2024-06-05T02:22:52+01:00 lingao01 Update Brunel to 2024.06.01dev
88a70303c1ce04a175f9ea7ae62bac39ed10cb16 2024-05-29T02:59:19+01:00 lingao01 Update Brunel module to the latest
01ac770d804b44792bdc65821431658f01d6cd79 2024-05-09T20:50:18+01:00 lingao01 Update Brunel to 2024.05.01dev
2003760621179877ca61abdae7d91d15ec247f20 2024-04-09T00:02:39+01:00 lingao01 Update Brunel module used in end2end tests
fcd6b083726da9ef18da2071f4e724ecd7358024 2024-04-04T17:32:27+01:00 lingao01 Add header size compare step to end2end tests
23383cc220ae89254b20151e8d310d8231541496 2024-02-29T23:41:17-06:00 keerav01 Resolved DEV to EAC merge conflicts - misc
7d0f09aabf2efe515fd298227efd17b5a726f4b8 2024-02-29T10:34:47-06:00 keerav01 Checking in conflicts after merge
ac9c81b9122a9aecce2580da09b53b4ab23e190a 2024-02-21T14:29:04Z Chris Laycock TOWER-4115: Updating E2E tests to use brunel RC
405831aba40c0096ef96377d46c182edfc1c2caf 2024-02-10T00:59:39Z Christopher Alvarez updated load_brunel.sh to module 2024.02.01dev
eab9edfbb28764b947b58edcf4505db87ed1fb77 2024-02-02T20:45:55-06:00 Lin Gao Update Brunel module for end2end, fix tests
b22a71c91ba4f3ac4a39ad77d7c6c7d7ca18fc53 2024-02-02T11:53:06-06:00 keerav01 squash commit - dev to eac merge 1_29_2024
838062f078ce6fad83be327cf38ce736ee642f05 2024-01-31T16:06:45-06:00 Lin Gao Update brunel module for end2end, update end2end tests to skip gen_syml on si tower configs
860348c51f718d3d33eb09636e7b314edf38846d 2024-01-26T23:01:10Z lingao01 Update end2end Brunel module and tests
7ed3b9018698489bbb1f357a2e4f1860bdf9f9a4 2024-01-23T02:17:16Z lingao01 Update brunel module to 2024.01.02dev
6490fb21be08348132d63aa43d9af4ca2c83f972 2023-09-05T15:42:21-05:00 Ramesh Bodakunta Partner Configs Updates
b660dc668b562544c104eb0d9a213177ffd89742 2023-07-29T17:21:24+01:00 lingao01 Update brunel module for end2end
79aa4bb18cd456798ed2f77a2aea94c534a875aa 2023-05-24T09:38:39-05:00 Eser Unlu Resolving conflicts during releases/CHARIOT_R0P0_EAC_122422 to origin/dev merge
f9ee94d12bc73a69acdb7c56c59043dbff1c9884 2023-05-22T17:14:59-05:00 Eser Unlu Checking in conflicts after merge
1ee0f621128262c24e1e301468dea94f30d006bd 2023-05-16T15:26:56+01:00 lingao01 Update kronos config with a pipeline router, upgrade Brunel module
53973e81f61d68153ed0eb82265918623580b29f 2023-04-30T15:49:55+01:00 Chris Laycock Updating brunel version in e2e tests to match release version
0f99b87adcce6f221d3b4ec0b7fb2187848027bf 2023-04-25T00:29:29+01:00 Chris Laycock Adding optimized versions of LEM and Kronos configs with updates to the error network (both) and config netowrk (Kronos) based on physcial requirements
740e394c1daaaab35dbbf82675348bb08b638151 2023-04-18T14:14:01+01:00 Chris Laycock Updateing brunel e2e testing to use latest release candidate
d5fce03fc5f91ac00fffeac6cc67a2f28598695a 2023-04-17T17:34:54+01:00 Chris Laycock Updating Brunel version for e2e tests
f6b291bbda13c46fa41d45e60d4fc6bde844efa6 2023-03-27T14:59:00+01:00 lingao01 Upgrade Brunel version
5259fdf0d7672e73d01742eb06b5a5a25b701f18 2023-03-06T16:10:02Z lingao01 Update Brunel module for end2end testing
141cf253ec471b606fd71d24b78d2528973ff276 2023-02-27T15:33:53Z lingao01 Update Brunel module to lac RC4
e80315f9f8db4ff03d5e695ea62c77866bb11770 2023-02-15T02:18:39Z lingao01 Update Brunel to RC6
6227ee1edc2b4e4dd7c59535a36fe39d3c479e09 2023-02-01T15:52:23Z lingao01 Update Brunel module to the latest
39fa9cc60eaffc43824ad752a7a1a8cb90829daf 2023-01-26T16:50:21Z lingao01 Update Brunel module to the latest
91e7c4c771a860781f7bf6f1b44f37aa2909b000 2023-01-20T22:59:29Z lingao01 Update brunel to the latest
2554712082cf0981e504959b66af75990c2eee34 2023-01-20T22:34:43Z lingao01 Upgrade Brunel module, add brunel_pipeline test
51e4bf942a7f51274cf98583807c96c2c4de04e0 2023-01-12T15:16:09-06:00 lingao01 Upgrade brunel module for e2e tests
8086fe8f0c7dc94be5c6c594c22d98706d93b1f1 2023-01-06T19:59:34-06:00 lingao01 Update Brunel to the latest
a70b75bb661f3b59ebe16a9a8abed689426451a8 2022-12-19T09:01:10-06:00 lingao01 Update Brunel for end2end
9a37d5a4b0b756db9b730aa13dffec9f4e0f6463 2022-12-03T13:58:12-06:00 lingao01 Update brunel for end2end
d4f21ee3e58042d21d9a375a872c5dd42b3f22c9 2022-11-02T13:46:06-05:00 lingao01 Fix bcfggen_tower_tormore_apu configs, upgrade brunel and perl version
cb7247c896498bfd5b24829bd62cd015e5383b81 2022-10-20T15:56:34-05:00 lingao01 Update brunel module to 2022.10.02dev
8350f7b5bbc913dfb13156a9ee3cb524dd52716d 2022-10-13T22:38:47-05:00 lingao01 Update brunel module for e2e tests
a6a47bf54364e4daf9173884e287c742f19bd4b0 2022-09-30T18:03:26+01:00 Chris Laycock Updating e2e tests to use brunel 2022.09.03dev.
587b4d0befd994e909f7ec313bd475c641ef5d93 2022-09-19T08:46:03-05:00 Chris Laycock Updating brunel version to 2022.09.02dev
d4dd385c346480c7afd489b898fd21696c636cb1 2022-08-19T02:30:50+01:00 lingao01 Update Brunel module
bb39b3b3ed6a4922053e701192bf91b92995c9d7 2022-08-04T15:00:43-05:00 lingao01 Upgrade brunel module for e2e tests
6acbd740bcd4bd7bc8888a673999a8009a08a6eb 2022-07-27T21:36:21+01:00 Naveen Anumalla Update from Lin: Fix Brunel e2e tests
9ed6e83ab500c6dbbabc8ea333bdabfeb651af43 2022-07-23T17:21:21+01:00 lingao01 Update Brunel module, add R52 and R52P IP path
46e7ed9f7fb6d89a3a6f61b656f7531afda5fe5b 2022-06-23T12:10:56-05:00 lingao01 Upgrade brunel module in end2end tests
15ec8b7621ebc26393d82bbf335293b7058f1f95 2022-05-19T21:49:46+01:00 lingao01 Switch to Brunel modules in end_2_end tests
Surviving-line author counts: {"Kyan Kornfeld": 1, "Naveen Anumalla": 3, "lingao01": 2}
```

## History and surviving-line context logical/shared/scripts/fusa/qverify_get_flops.tcl

History below disables rename inference. Counts include comments/blank lines and are not authorship shares.

```text
c93c38388e3cce1973b4a4b30367da0f1b05c6a2 2024-11-24T22:48:00-06:00 jacpet01 Enable Pinata flow for DSNI/DMNI/CTB configs
a29f164b33c4fd231d7fb9a5fa5c55624c463e4d 2022-01-26T22:18:28Z Sean Steel improvements to get minifmu pinata task working
0469f78275941f8da434e51a634f53086e89f594 2021-11-24T20:19:37Z Sean Steel pinata updates for amni flops
09d46bb1145ce13626725ad3b45806f8af95e8be 2021-09-27T17:15:39+01:00 Sean Steel adding get ports script to Asil-D
132198680b02ca12a89c8127c412dd48d36bd338 2021-03-17T17:26:35Z Sean Steel Fixes to the get_flops script to avoid tied-off bits in register arrays
4df3354cc2c16df21f6cfeddf2cb3bcef3efac32 2020-11-05T16:57:56Z Michael Coulter Update qverify_get_flops.tcl to list regs in 3D arrays
bce47a50cf9fee013517d4bb33f71c70d4f730f1 2020-11-03T23:18:41Z Sean Steel Initial commit of fault injection scripts
Surviving-line author counts: {"Michael Coulter": 88, "Sean Steel": 91, "jacpet01": 1}
```

## Later removal of legacy top-level model bindings cb3d526eb8f49e7ed3e09fcb146aea535587417a

Other-author lifecycle evidence. Retained files do not imply current top-level use.

```diff
commit cb3d526eb8f49e7ed3e09fcb146aea535587417a
Author:     Ariel Paling <aripal01@login2.nahpc2.arm.com>
AuthorDate: Wed Aug 10 16:16:42 2022 -0500
Commit:     Ariel Paling <aripal01@login2.nahpc2.arm.com>
CommitDate: Wed Aug 10 16:18:22 2022 -0500

    Updated func_top for chariot_fault_injection only when FMU present
    
    Change-Id: I2ef1f1178283c97b0030dcbf6bcd46cf00b8b419

diff --git a/logical/noc_arachne/validation/dynamic/top/interface_block.sv b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
index aadc374c7cd..f996cc42d64 100755
--- a/logical/noc_arachne/validation/dynamic/top/interface_block.sv
+++ b/logical/noc_arachne/validation/dynamic/top/interface_block.sv
@@ -283,15 +283,6 @@ module interface_block
   logic                        cov_rvalid;
   logic                        cov_rready;
 
-  `ifdef CHARIOT_ASIL_B
-    logic parity_error;
-    logic hang_error;
-    logic resp_error;
-    logic size_error;
-    logic uncorrectable_ecc_error;
-    logic correctable_ecc_error;
-  `endif // CHARIOT_ASIL_B
-
   typedef virtual apu_intf #(
      .IF_NO(IF_NO),
      .APU_NUM_CHANNELS(APU_CHANNELS),
@@ -1541,169 +1532,6 @@ module interface_block
                         uvm_config_db#(idm_signal_if_wrapper_base)::set(uvm_root::get(),"uvm_test_top",$sformatf("idm_signal_interface_wrapper%0d", IF_NO),idm_signal_vif_wrapper);
                       end
                     end : g_idm
-
-                    `ifdef CHARIOT_ASIL_B
-                      logic [WUSER_WIDTH-1:0]  wdat_err_code;
-                      logic [WUSER_WIDTH-1:0]  rdat_err_code;
-                      logic [AWUSER_WIDTH-1:0] wreq_err_code;
-                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
-                      logic [AWUSER_WIDTH-1:0] wrsp_err_code;
-
-                      logic [ DATA_WIDTH-1:0] wdat_uncorrected;
-                      logic [RUSER_WIDTH-WUSER_WIDTH-1:0] rrsp_err_code;
-
-                      if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
-                        logic parity_err_rdat;
-                        logic parity_err_wrsp;
-                        logic parity_err_rrsp;
-                        logic hang_err_axi_write;
-                        logic hang_err_axi_read;
-                        logic size_err_axi_write;
-                        logic size_err_axi_read;
-                        assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
-                        assign hang_error = hang_err_axi_write | hang_err_axi_read;
-                        assign resp_error = (u_if.RRESP[1] && u_if.RVALID) || (u_if.BRESP[1] && u_if.BVALID);
-                        assign size_error = size_err_axi_read;
-                        assign uncorrectable_ecc_error = 0;
-                        assign correctable_ecc_error   = 0;
-                        assign wdat_uncorrected = 0;
-                        chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
-                          .data_i (u_if.WDATA),
-                          .strb_i (u_if.WSTRB),
-                          .user_o (wdat_err_code)
-                        );
-                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_gen (
-                          .addr_i           (u_if.AWADDR),
-                          .user_i           (u_if.AWUSER),
-                          .privileged_i     (u_if.AWPROT[0]),
-                          .nonsec_i         (u_if.AWPROT[1]),
-                          .instruction_i    (u_if.AWPROT[2]),
-                          .bufferable_i     (u_if.AWCACHE[0] && !(u_if.AWCACHE[3:1] == 3'b001)), //awcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.AWCACHE[1]),
-                          .lookup_i         (u_if.AWCACHE[2] || u_if.AWCACHE[3]),
-                          .allocate_i       (u_if.AWCACHE[3]),
-                          .shareable_i      ((u_if.AWDOMAIN == 2'b01) || (u_if.AWDOMAIN == 2'b10)),
-                          .user_o           (wreq_err_code)
-                        );
-                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
-                          .addr_i           (u_if.ARADDR),
-                          .user_i           (u_if.ARUSER),
-                          .privileged_i     (u_if.ARPROT[0]),
-                          .nonsec_i         (u_if.ARPROT[1]),
-                          .instruction_i    (u_if.ARPROT[2]),
-                          .bufferable_i     (u_if.ARCACHE[0] && !(u_if.ARCACHE[3:1] == 3'b001)), //arcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.ARCACHE[1]),
-                          .lookup_i         (u_if.ARCACHE[2] || u_if.ARCACHE[3]),
-                          .allocate_i       (u_if.ARCACHE[2]),
-                          .shareable_i      ((u_if.ARDOMAIN == 2'b01) || (u_if.ARDOMAIN == 2'b10)),
-                          .user_o           (rreq_err_code)
-                        );
-                        chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
-                          .valid_i (u_if.BVALID),
-                          .user_i  (u_if.BUSER),
-                          .error_o (parity_err_wrsp)
-                        );
-                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
-                          .valid_i (u_if.RVALID),
-                          .user_i  (u_if.RUSER),
-                          .error_o (parity_err_rrsp)
-                        );
-                        chariot_rdat_parity_checker #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_check (
-                          .data_i (u_if.RDATA),
-                          .valid_i (u_if.RVALID),
-                          .user_i (u_if.RUSER),
-                          .error_o (parity_err_rdat)
-                        );
-                        chariot_axi_hang_detector_write #(.ID_WIDTH(WID_WIDTH), .TRACKER_LENGTH(MAX_WRITES_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_write_hang_detector (
-                          .clk_i(ACLK),
-                          .reset_i(u_if.ARESETn),
-                          .aid_i(u_if.AWID),
-                          .avalid_i(u_if.AWVALID),
-                          .aready_i(u_if.AWREADY),
-                          .id_i(u_if.BID),
-                          .valid_i(u_if.BVALID),
-                          .last_i(1),
-                          .ready_i(u_if.BREADY),
-                          .error_o(hang_err_axi_write)
-                        );
-                        chariot_axi_hang_detector_read #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
-                          .clk_i(ACLK),
-                          .resetn_i(u_if.ARESETn),
-                          .aid_i(u_if.ARID),
-                          .avalid_i(u_if.ARVALID),
-                          .aready_i(u_if.ARREADY),
-                          .alength_i(u_if.ARLEN),
-                          .asize_i(u_if.ARSIZE),
-                          .id_i(u_if.RID),
-                          .valid_i(u_if.RVALID),
-                          .last_i(u_if.RLAST),
-                          .ready_i(u_if.RREADY),
-                          .error_1_o(hang_err_axi_read),
-                          .error_2_o(size_err_axi_read)
-                        );
-                      end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
-                        logic parity_err_wreq;
-                        logic parity_err_rreq;
-                        logic [(DATA_WIDTH/32)-1:0] uncorrectable_ecc_err_wdat;
-                        logic [(DATA_WIDTH/32)-1:0] correctable_ecc_err_wdat;
-                        logic [ DATA_WIDTH-1:0] correctable_bits_vector;
-                        assign parity_error = parity_err_wreq | parity_err_rreq;
-                        assign hang_error = 0;
-                        assign size_error = 0;
-                        assign resp_error = 0;
-                        assign uncorrectable_ecc_error = |uncorrectable_ecc_err_wdat;
-                        assign correctable_ecc_error   = |correctable_ecc_err_wdat;
-                        assign u_if.WDATA = wdat_uncorrected ^ correctable_bits_vector;
-                        chariot_wdat_ecc_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .IS_AHB(0)) wdat_ecc_check (
-                          .data_i  (wdat_uncorrected),
-                          .user_i  (u_if.WUSER),
-                          .valid_i (u_if.WVALID),
-                          .strb_i  (u_if.WSTRB),
-                          .uncorrectable_errs_o(uncorrectable_ecc_err_wdat),
-                          .correctable_errs_o(correctable_ecc_err_wdat),
-                          .correctable_bits_vector_o (correctable_bits_vector)
-                        );
-                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_check (
-                          .addr_i           (u_if.AWADDR),
-                          .user_i           (u_if.AWUSER),
-                          .privileged_i     (u_if.AWPROT[0]),
-                          .nonsec_i         (u_if.AWPROT[1]),
-                          .instruction_i    (u_if.AWPROT[2]),
-                          .bufferable_i     (u_if.AWCACHE[0] && !(u_if.AWCACHE[3:1] == 3'b001)), //arcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.AWCACHE[1]),
-                          .allocate_i       (u_if.AWCACHE[3]),
-                          .other_allocate_i (u_if.AWCACHE[2]),
-                          .domain_i         (u_if.AWDOMAIN),
-                          .valid_i          (u_if.AWVALID),
-                          .error_o          (parity_err_wreq)
-                        );
-                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
-                          .addr_i           (u_if.ARADDR),
-                          .user_i           (u_if.ARUSER),
-                          .privileged_i     (u_if.ARPROT[0]),
-                          .nonsec_i         (u_if.ARPROT[1]),
-                          .instruction_i    (u_if.ARPROT[2]),
-                          .bufferable_i     (u_if.ARCACHE[0] && !(u_if.ARCACHE[3:1] == 3'b001)), //arcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.ARCACHE[1]),
-                          .allocate_i       (u_if.ARCACHE[2]),
-                          .other_allocate_i (u_if.ARCACHE[3]),
-                          .domain_i         (u_if.ARDOMAIN),
-                          .valid_i          (u_if.ARVALID),
-                          .error_o          (parity_err_rreq)
-                        );
-                        chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
-                          .user_o (wrsp_err_code)
-                        );
-                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
-                          .user_o (rrsp_err_code)
-                        );
-                        chariot_rdat_parity_generator #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_gen (
-                          .data_i (u_if.RDATA),
-                          .valid_i (u_if.RVALID),
-                          .user_o (rdat_err_code)
-                        );
-                      end
-                    `endif // CHARIOT_ASIL_B
           end : g_ace4_lite
 
 //REVISIT_PRIYANKA: ADD DELAYED_MODE_EN ifdef from dev
@@ -2430,168 +2258,6 @@ module interface_block
                         uvm_config_db#(idm_signal_if_wrapper_base)::set(uvm_root::get(),"uvm_test_top",$sformatf("idm_signal_interface_wrapper%0d", IF_NO),idm_signal_vif_wrapper);
                       end
                     end : g_idm
-
-                    `ifdef CHARIOT_ASIL_B
-                      logic [WUSER_WIDTH-1:0]  wdat_err_code;
-                      logic [WUSER_WIDTH-1:0]  rdat_err_code;
-                      logic [AWUSER_WIDTH-1:0] wreq_err_code;
-                      logic [ARUSER_WIDTH-1:0] rreq_err_code;
-                      logic [AWUSER_WIDTH-1:0] wrsp_err_code;
-                      logic [ DATA_WIDTH-1:0]  wdat_uncorrected;
-                      logic [RUSER_WIDTH-WUSER_WIDTH-1:0] rrsp_err_code;
-                      if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
-                        logic parity_err_rdat;
-                        logic parity_err_wrsp;
-                        logic parity_err_rrsp;
-                        logic hang_err_axi_write;
-                        logic hang_err_axi_read;
-                        logic size_err_axi_write;
-                        logic size_err_axi_read;
-                        assign parity_error = parity_err_rdat | parity_err_wrsp | parity_err_rrsp;
-                        assign hang_error = hang_err_axi_write | hang_err_axi_read;
-                        assign size_error = size_err_axi_read;
-                        assign resp_error = (u_if.RRESP[1] && u_if.RVALID) || (u_if.BRESP[1] && u_if.BVALID);
-                        assign uncorrectable_ecc_error = 0;
-                        assign correctable_ecc_error   = 0;
-                        assign wdat_uncorrected = 0;
-                        chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
-                          .data_i (u_if.WDATA),
-                          .strb_i (u_if.WSTRB),
-                          .user_o (wdat_err_code)
-                        );
-                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_gen (
-                          .addr_i           (u_if.AWADDR),
-                          .user_i           (u_if.AWUSER),
-                          .privileged_i     (u_if.AWPROT[0]),
-                          .nonsec_i         (u_if.AWPROT[1]),
-                          .instruction_i    (u_if.AWPROT[2]),
-                          .bufferable_i     (u_if.AWCACHE[0] && !(u_if.AWCACHE[3:1] == 3'b001)), //awcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.AWCACHE[1]),
-                          .lookup_i         (u_if.AWCACHE[2] || u_if.AWCACHE[3]),
-                          .allocate_i       (u_if.AWCACHE[3]),
-                          .shareable_i      (1'b0),
-                          .user_o           (wreq_err_code)
-                        );
-                        chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_gen (
-                          .addr_i           (u_if.ARADDR),
-                          .user_i           (u_if.ARUSER),
-                          .privileged_i     (u_if.ARPROT[0]),
-                          .nonsec_i         (u_if.ARPROT[1]),
-                          .instruction_i    (u_if.ARPROT[2]),
-                          .bufferable_i     (u_if.ARCACHE[0] && !(u_if.ARCACHE[3:1] == 3'b001)), //arcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.ARCACHE[1]),
-                          .lookup_i         (u_if.ARCACHE[2] || u_if.ARCACHE[3]),
-                          .allocate_i       (u_if.ARCACHE[2]),
-                          .shareable_i      (1'b0),
-                          .user_o           (rreq_err_code)
-                        );
-                        chariot_wrsp_parity_checker #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_check (
-                          .valid_i (u_if.BVALID),
-                          .user_i  (u_if.BUSER),
-                          .error_o (parity_err_wrsp)
-                        );
-                        chariot_wrsp_parity_checker #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_check (
-                          .valid_i (u_if.RVALID),
-                          .user_i  (u_if.RUSER),
-                          .error_o (parity_err_rrsp)
-                        );
-                        chariot_rdat_parity_checker #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_check (
-                          .data_i (u_if.RDATA),
-                          .valid_i (u_if.RVALID),
-                          .user_i (u_if.RUSER),
-                          .error_o (parity_err_rdat)
-                        );
-                        chariot_axi_hang_detector_write #(.ID_WIDTH(WID_WIDTH), .TRACKER_LENGTH(MAX_WRITES_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_write_hang_detector (
-                          .clk_i(ACLK),
-                          .reset_i(u_if.ARESETn),
-                          .aid_i(u_if.AWID),
-                          .avalid_i(u_if.AWVALID),
-                          .aready_i(u_if.AWREADY),
-                          .id_i(u_if.BID),
-                          .valid_i(u_if.BVALID),
-                          .last_i(1),
-                          .ready_i(u_if.BREADY),
-                          .error_o(hang_err_axi_write)
-                        );
-                        chariot_axi_hang_detector_read #(.ID_WIDTH(RID_WIDTH), .TRACKER_LENGTH(MAX_READS_OUTSTANDING), .COUNTER_WIDTH(`AXI_HANG_COUNTER_WIDTH)) axi_read_hang_detector (
-                          .clk_i(ACLK),
-                          .resetn_i(u_if.ARESETn),
-                          .aid_i(u_if.ARID),
-                          .avalid_i(u_if.ARVALID),
-                          .aready_i(u_if.ARREADY),
-                          .alength_i(u_if.ARLEN),
-                          .asize_i(u_if.ARSIZE),
-                          .id_i(u_if.RID),
-                          .valid_i(u_if.RVALID),
-                          .last_i(u_if.RLAST),
-                          .ready_i(u_if.RREADY),
-                          .error_1_o(hang_err_axi_read),
-                          .error_2_o(size_err_axi_read)
-                        );
-                      end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
-                        logic parity_err_wreq;
-                        logic parity_err_rreq;
-                        logic [(DATA_WIDTH/32)-1:0] uncorrectable_ecc_err_wdat;
-                        logic [(DATA_WIDTH/32)-1:0]   correctable_ecc_err_wdat;
-                        logic [ DATA_WIDTH-1:0] correctable_bits_vector;
-                        assign parity_error = parity_err_wreq | parity_err_rreq;
-                        assign hang_error = 0;
-                        assign size_error = 0;
-                        assign resp_error = 0;
-                        assign uncorrectable_ecc_error = |uncorrectable_ecc_err_wdat;
-                        assign correctable_ecc_error   = |correctable_ecc_err_wdat;
-                        assign u_if.WDATA = wdat_uncorrected ^ correctable_bits_vector;
-
-                        chariot_wdat_ecc_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .IS_AHB(0)) wdat_ecc_check (
-                          .data_i  (wdat_uncorrected),
-                          .user_i  (u_if.WUSER),
-                          .valid_i (u_if.WVALID),
-                          .strb_i  (u_if.WSTRB),
-                          .uncorrectable_errs_o(uncorrectable_ecc_err_wdat),
-                          .correctable_errs_o(correctable_ecc_err_wdat),
-                          .correctable_bits_vector_o (correctable_bits_vector)
-                        );
-                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_check (
-                          .addr_i           (u_if.AWADDR),
-                          .user_i           (u_if.AWUSER),
-                          .privileged_i     (u_if.AWPROT[0]),
-                          .nonsec_i         (u_if.AWPROT[1]),
-                          .instruction_i    (u_if.AWPROT[2]),
-                          .bufferable_i     (u_if.AWCACHE[0] && !(u_if.AWCACHE[3:1] == 3'b001)), //awcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.AWCACHE[1]),
-                          .allocate_i       (u_if.AWCACHE[3]),
-                          .other_allocate_i (u_if.AWCACHE[2]),
-                          .domain_i         (2'b0),
-                          .valid_i          (u_if.AWVALID),
-                          .error_o          (parity_err_wreq)
-                        );
-                        chariot_wreq_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(ARUSER_WIDTH)) rreq_parity_check (
-                          .addr_i           (u_if.ARADDR),
-                          .user_i           (u_if.ARUSER),
-                          .privileged_i     (u_if.ARPROT[0]),
-                          .nonsec_i         (u_if.ARPROT[1]),
-                          .instruction_i    (u_if.ARPROT[2]),
-                          .bufferable_i     (u_if.ARCACHE[0] && !(u_if.ARCACHE[3:1] == 3'b001)), //arcache [4'b0011] is converted to -non-bufferable in AHB protocol, so it can't be protected here
-                          .modifiable_i     (u_if.ARCACHE[1]),
-                          .allocate_i       (u_if.ARCACHE[2]),
-                          .other_allocate_i (u_if.ARCACHE[3]),
-                          .domain_i         (2'b0),
-                          .valid_i          (u_if.ARVALID),
-                          .error_o          (parity_err_rreq)
-                        );
-                        chariot_wrsp_parity_generator #(.USER_WIDTH(BUSER_WIDTH)) wrsp_parity_gen (
-                          .user_o (wrsp_err_code)
-                        );
-                        chariot_wrsp_parity_generator #(.USER_WIDTH(RUSER_WIDTH-WUSER_WIDTH)) rrsp_parity_gen (
-                          .user_o (rrsp_err_code)
-                        );
-                        chariot_rdat_parity_generator #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AXI_NUM_SAFETY_BITS)) rdat_parity_gen (
-                          .data_i (u_if.RDATA),
-                          .valid_i (u_if.RVALID),
-                          .user_o (rdat_err_code)
-                        );
-                      end
-                    `endif // CHARIOT_ASIL_B
           end : g_axi4
 
       generic_types::PROTOCOL__AXI3:
@@ -3246,127 +2912,6 @@ module interface_block
         end
 
       end : g_idm
-      `ifdef CHARIOT_ASIL_B
-        logic [WUSER_WIDTH-1:0]  wdat_err_code;
-        logic [AWUSER_WIDTH-1:0] wreq_err_code;
-        logic [RUSER_WIDTH-1:0]  rdat_err_code;
-        logic [ DATA_WIDTH-1:0]  wdat_uncorrected;
-        logic [DATA_WIDTH/8-1:0] strobe; //strobe not part of the ahb protocol, so we generate it here
-        logic [1:0] htrans_previous; // saving htrans from address phase so it can be used in the data phase
-        logic hwrite_previous; // saving hwrite from address phase so it can be used in the data phase
-
-        chariot_ahb_strobe_generation #(.DATA_WIDTH(DATA_WIDTH), .ADDR_WIDTH(ADDR_WIDTH)) strobe_gen (
-          .HCLK     (ACLK),
-          .HRESETn  (AHB_RESETn_final),
-          .hsize_i  (u_if.HSIZE),
-          .htrans_i (u_if.HTRANS),
-          .hwrite_i (u_if.HWRITE),
-          .hready_i (u_if.HREADY),
-          .haddr_i  (u_if.HADDR),
-          .strobe_o (strobe),
-          .htrans_previous_o (htrans_previous),
-          .hwrite_previous_o (hwrite_previous)
-        );
-
-        if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__MASTER) begin
-          logic parity_err_rdat;
-          logic hang_err_ahb;
-          logic lookup;
-          logic shareable;
-          logic bufferable;
-          logic allocate;
-          //logic other_allocate;
-          //logic [1:0] domain;
-          assign parity_error = parity_err_rdat; // no buser on this interface
-          assign hang_error = hang_err_ahb;
-          assign size_error = 0;
-          assign resp_error = u_if.HRESP;
-          assign uncorrectable_ecc_error = 0;
-          assign correctable_ecc_error   = 0;
-          assign wdat_uncorrected = 0;
-          assign bufferable     = EXTENDED_MEMORY_TYPES ? (u_if.HPROT[4] & u_if.HPROT[3] & u_if.HPROT[2]) : u_if.HPROT[2];
-          assign lookup         = EXTENDED_MEMORY_TYPES ? u_if.HPROT[4] : u_if.HPROT[3];
-          assign allocate       = EXTENDED_MEMORY_TYPES ? u_if.HPROT[5] : 0;
-          assign shareable      = EXTENDED_MEMORY_TYPES ? (u_if.HPROT[6] & ~u_if.HEXCL) : 0; // only shareable if modifiable, shareable, and not exclusive. modifiable is implied by shareable
-//          assign other_allocate = EXTENDED_MEMORY_TYPES ? (u_if.HPROT[5] &  u_if.HWRITE & u_if.HMASTLOCK) : 0;
-//          assign domain[1]      = EXTENDED_MEMORY_TYPES ? (~u_if.HPROT[3] | u_if.HPROT[6] & !u_if.HEXCL) : ~u_if.HPROT[3];
-//          assign domain[0]      = ~u_if.HPROT[3];
-          chariot_wdat_ecc_generator #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH)) wdat_ecc_gen (
-            .data_i (u_if.HWDATA),
-            .strb_i (strobe),
-            .user_o (wdat_err_code)
-          );
-          chariot_wreq_parity_generator #(.ADDR_WIDTH(ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) wreq_parity_gen (
-            .addr_i           (u_if.HADDR),
-            .user_i           (u_if.HAUSER),
-            .privileged_i     (u_if.HPROT[1]),
-            .nonsec_i         (u_if.HNONSEC),
-            .instruction_i    (~u_if.HPROT[0]),
-            .bufferable_i     (bufferable),
-            .modifiable_i     (u_if.HPROT[3]),
-            .lookup_i         (lookup),
-            .allocate_i       (allocate),
-            .shareable_i      (shareable),
-            .user_o           (wreq_err_code)
-          );
-          chariot_rdat_parity_checker #(.DATA_WIDTH(DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AHB_NUM_SAFETY_BITS)) rdat_parity_check (
-            .data_i (u_if.HRDATA),
-            .valid_i (u_if.HREADY && htrans_previous[1] && !hwrite_previous),
-            .user_i (u_if.HRUSER),
-            .error_o (parity_err_rdat)
-          );
-          chariot_ahb_hang_detector #(.NUM_CLK_CYCLES_HANG(`NUM_CLK_CYCLES_HANG)) ahb_hang_detector (
-            .clk_i (u_if.HCLK),
-            .reset_i (u_if.HRESET_N),
-            .ready_i (u_if.HREADY),
-            .error_o(hang_err_ahb)
-          );
-        end else if (generic_types::device_t'(DEVICE) == generic_types::DEVICE__SLAVE) begin
-          logic parity_err_req; //checks read and write
-          logic [(DATA_WIDTH/32)-1:0] uncorrectable_ecc_err_wdat;
-          logic [(DATA_WIDTH/32)-1:0] correctable_ecc_err_wdat;
-          logic [ DATA_WIDTH-1:0] correctable_bits_vector;
-          logic bufferable;
-          logic lookup;
-          logic shareable;
-          assign parity_error = parity_err_req;
-          assign hang_error = 0;
-          assign size_error = 0;
-          assign resp_error = 0;
-          assign uncorrectable_ecc_error = |uncorrectable_ecc_err_wdat;
-          assign correctable_ecc_error   = |correctable_ecc_err_wdat;
-          assign u_if.HWDATA = wdat_uncorrected ^ correctable_bits_vector;
-          chariot_wdat_ecc_checker #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .IS_AHB(1)) wdat_ecc_check (
-            .data_i  (wdat_uncorrected),
-            .user_i  (u_if.HWUSER),
-            .valid_i (|strobe), // no valid on ahb, but this should be fine because strobes will compensate - they factor in HTRANS, which is the ahb equivalent
-            .strb_i  (strobe),
-            .uncorrectable_errs_o(uncorrectable_ecc_err_wdat),
-            .correctable_errs_o(correctable_ecc_err_wdat),
-            .correctable_bits_vector_o (correctable_bits_vector)
-          );
-          chariot_ahb_req_parity_checker #(.ADDR_WIDTH (ADDR_WIDTH), .USER_WIDTH(AWUSER_WIDTH)) req_parity_check ( //checks read and write requests
-            .addr_i           (u_if.HADDR),
-            .user_i           (u_if.HAUSER),
-            .hwrite_i         (u_if.HWRITE),
-            .hnonsec_i        (u_if.HNONSEC),
-            .hprot_0_i        (u_if.HPROT[0]),
-            .hprot_1_i        (u_if.HPROT[1]),
-            .hprot_2_i        (u_if.HPROT[2]),
-            .hprot_3_i        (u_if.HPROT[3]),
-            .hprot_4_i        (EXTENDED_MEMORY_TYPES ? u_if.HPROT[4] : 0),
-            .hprot_5_i        (EXTENDED_MEMORY_TYPES ? u_if.HPROT[5] : 0),
-            .hprot_6_i        (EXTENDED_MEMORY_TYPES ? u_if.HPROT[6] : 0),
-            .valid_i          (u_if.HREADY && u_if.HTRANS[1]),
-            .error_o          (parity_err_req)
-          );
-          chariot_rdat_parity_generator #(.DATA_WIDTH (DATA_WIDTH), .USER_WIDTH(WUSER_WIDTH), .RESP_WIDTH(RUSER_WIDTH-WUSER_WIDTH), .NUM_SAFETY_BITS(`AHB_NUM_SAFETY_BITS)) rdat_parity_gen (
-            .data_i (u_if.HRDATA),
-            .valid_i (u_if.HREADY && htrans_previous[1] && !hwrite_previous),
-            .user_o (rdat_err_code)
-          );
-        end
-      `endif // CHARIOT_ASIL_B
     end : g_ahb
 
     // Interface is APB4
@@ -3523,16 +3068,6 @@ module interface_block
           uvm_config_db#(idm_signal_if_wrapper_base)::set(uvm_root::get(),"uvm_test_top",$sformatf("idm_signal_interface_wrapper%0d", IF_NO),idm_signal_vif_wrapper);
         end
       end : g_idm
-
-    `ifdef CHARIOT_ASIL_B
-      assign parity_error = 0; // no parity on APB yet - todo once apb gets user bits
-      assign hang_error = 0;
-      assign size_error = 0;
-      assign resp_error = 0;
-      assign uncorrectable_ecc_error = 0;
-      assign correctable_ecc_error   = 0;
-    `endif // CHARIOT_ASIL_B
-
     end : g_apb
     default:
         begin : g_default
diff --git a/logical/noc_arachne/validation/dynamic/top/testbench.sv b/logical/noc_arachne/validation/dynamic/top/testbench.sv
index 513301f4c8a..4055304d506 100755
--- a/logical/noc_arachne/validation/dynamic/top/testbench.sv
+++ b/logical/noc_arachne/validation/dynamic/top/testbench.sv
@@ -41,9 +41,6 @@
 `include "sva/arachne_crb_converter_scov_sva.sv"
 `include "components/scov/arachne_qch_dbgmsg.sv"
 `include "vip_apb5_uvc_pkg.sv"
-`ifdef CHARIOT_ASIL_B
-  `include "components/chariot/chariot_pkg.svh"
-`endif // CHARIOT_ASIL_B
 `include "vip_reset_if.sv"
 
 module testbench;
@@ -54,9 +51,6 @@ module testbench;
   `ifdef POWER_AWARE
     import UPF::*;
   `endif
-  `ifdef CHARIOT_ASIL_B
-    import chariot_pkg::*;
-  `endif // CHARIOT_ASIL_B
 
   `include "configuration_local_params.svh"
 
@@ -111,60 +105,6 @@ module testbench;
 
 
   // all things chariot_b
-  `ifdef CHARIOT_ASIL_B
-    logic          parity_error;
-    logic          hang_error;
-    logic          size_error;
-    logic          pch_hang_error;
-    logic          qch_hang_error; //added for qch
-    logic          resp_error;
-    logic          uncorrectable_ecc_error;
-    logic          correctable_ecc_error;
-    logic [NUM_IF-1:0] if_parity_error;
-    logic [NUM_IF-1:0] if_hang_error;
-    logic [NUM_IF-1:0] if_size_error;
-    logic [NUM_PD-1:0] if_pch_hang_error;
-    logic [NUM_CD-1:0] if_qch_hang_error; //added for qch # Q-Channels = # Clock Domains
-    logic [NUM_IF-1:0] if_resp_error;
-    logic [NUM_IF-1:0] if_ecc_uncorrectable_err;
-    logic [NUM_IF-1:0] if_ecc_correctable_err;
-
-    logic  APU_ENABLE_RESET_STRAP;
-    logic  APU_ENABLE_RESET_STRAPCHK;
-    logic  APUID;
-    logic  APUIDCHK;   
-   
-   //      
-    fusa_interrupt_if top_fusa_interrupt_if();
-    bit fault_is_being_injected; //pin for chariot random fault injection only, and set by a tcl script force statement
-
-    assign parity_error            = |if_parity_error;
-    assign hang_error              = |if_hang_error;
-    assign size_error              = |if_size_error;
-    assign pch_hang_error          = 0; //|if_pch_hang_error;
-    assign qch_hang_error          = 0; //|if_qch_hang_error; //added for qch
-    assign resp_error              = |if_resp_error;
-    assign uncorrectable_ecc_error = |if_ecc_uncorrectable_err;
-    assign correctable_ecc_error   = |if_ecc_correctable_err;
-    assign top_fusa_interrupt_if.clk = TB_SYS_CLK;
-    assign top_fusa_interrupt_if.fault_is_being_injected = fault_is_being_injected;
-    assign top_fusa_interrupt_if.safety_interrupt = parity_error | uncorrectable_ecc_error | hang_error | pch_hang_error | resp_error | qch_hang_error | size_error;
-    assign top_fusa_interrupt_if.correctable_safety_interrupt = correctable_ecc_error;
-
-    // details about which mechanisms caught the fail
-    assign top_fusa_interrupt_if.corrected_ecc_err   = correctable_ecc_error;
-    assign top_fusa_interrupt_if.uncorrected_ecc_err = parity_error | uncorrectable_ecc_error;
-    assign top_fusa_interrupt_if.resp_err            = resp_error;
-    assign top_fusa_interrupt_if.sni_hang_err        = hang_error;
-    assign top_fusa_interrupt_if.pq_hang_err         = pch_hang_error;
-    assign top_fusa_interrupt_if.size_err            = size_error;
-
-
-    initial begin
-      uvm_config_db#(virtual fusa_interrupt_if)::set(uvm_root::get(), "*","fusa_interrupt_if" ,top_fusa_interrupt_if);
-    end
-  `endif // CHARIOT_ASIL_B
-
   test_configuration_functions tst_cfg;
   `ifdef POWER_AWARE
     //power aware
@@ -400,23 +340,6 @@ module testbench;
      assign testbench.nISOLATE[a] = u_pa_domain.pa_vif.iso_n;
    `endif
   
-   `ifdef CHARIOT_ASIL_B
-     logic [31:0] preq_counter;
-     logic [31:0] preq_counter_next; 
-
-     
-     assign preq_counter_nxt = (u_p_domain.preq && !(u_p_domain.paccept || u_p_domain.pdeny)) ? preq_counter + 1 : 0;
-     assign if_pch_hang_error[a] = (preq_counter > 4000) ? 1 : 0;
-     always @(posedge PD_CLK[a] or negedge PD_RESETn[a]) begin
-       if (~PD_RESETn[a]) begin
-         preq_counter <= 0;
-       end else begin
-         preq_counter <= preq_counter_nxt;
-       end
-     end
-
-   `endif // CHARIOT_ASIL_B
-
  end : g_p_domain
 
  // Create the sideband interface for each clock domain excluding combiner
@@ -531,24 +454,6 @@ module testbench;
 
    end : g_not_comb
 
-   `ifdef CHARIOT_ASIL_B
-    //qch hang detector code
-     logic [31:0] qreq_counter;
-     logic [31:0] qreq_counter_next;
-
-    
-     assign qreq_counter_nxt = (!u_q_domain.qreqn && !(!u_q_domain.qacceptn || u_q_domain.qdeny)) ? qreq_counter + 1 : 0;
-     assign if_qch_hang_error[a] = (qreq_counter > 4000) ? 1 : 0;
-     always @(posedge ACLK[a] or negedge ARESETn[a]) begin
-       if (~ARESETn[a]) begin
-         qreq_counter <= 0;
-       end else begin
-         qreq_counter <= qreq_counter_nxt;
-       end
-     end
-     
-  `endif // CHARIOT_ASIL_B
-    
     //**
 
  end : g_q_domain
@@ -771,15 +676,6 @@ module testbench;
            `endif
         end
 
-        `ifdef CHARIOT_ASIL_B
-          assign if_parity_error[a] = u_if.parity_error;
-          assign if_hang_error[a] = u_if.hang_error;
-          assign if_resp_error[a] = u_if.resp_error;
-          assign if_size_error[a] = u_if.size_error;
-          assign if_ecc_uncorrectable_err[a] = u_if.uncorrectable_ecc_error;
-          assign if_ecc_correctable_err[a]   = u_if.correctable_ecc_error;
-        `endif // CHARIOT_ASIL_B
- 
      end : master
      generic_types::DEVICE__SLAVE:
      begin : slave
@@ -906,15 +802,6 @@ module testbench;
            `endif
         end
 
-        `ifdef CHARIOT_ASIL_B
-          assign if_parity_error[a] = u_if.parity_error;
-          assign if_hang_error[a] = u_if.hang_error;
-          assign if_resp_error[a] = u_if.resp_error;
-          assign if_size_error[a] = u_if.size_error;
-          assign if_ecc_uncorrectable_err[a] = u_if.uncorrectable_ecc_error;
-          assign if_ecc_correctable_err[a]   = u_if.correctable_ecc_error;
-        `endif // CHARIOT_ASIL_B
-
       end : slave
     endcase
 
```

