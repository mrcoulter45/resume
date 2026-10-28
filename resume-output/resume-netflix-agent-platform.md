# Michael Remington Coulter

Buda, TX | [mrcoulter45@gmail.com](mailto:mrcoulter45@gmail.com) | (760) 694-6310
[linkedin.com/in/michael-coulter-164868153](https://www.linkedin.com/in/michael-coulter-164868153/) | [github.com/mrcoulter45](https://github.com/mrcoulter45)

Senior Software Engineer with nearly 8 years shipping and maintaining production engineering software. Built a shared Codex harness and MCP tool used in Arm engineering workflows.

## Professional Experience

**Arm - Austin, TX**

### Senior Software Engineer | Apr 2023 - Present

Ship and maintain Interconnect Architect, Arm's Angular/TypeScript and Python SoC configuration tool. The product has about six years of customer releases and ships internally twice a month.

**Recognition:** Most Innovative Award, Engineering AI Showcase (Dec 2025): multi-agent system.

- Designed and built a shared Codex harness used by several Arm engineers, with reusable tools/skills, project context and automatic capture/retrieval of persistent engineering memory.
    - Created `repair-jenkins`, a team-used Codex skill to identify failing Playwright tests and autonomously fix flakiness, test-code defects and underlying source bugs; requires three consecutive passes and human patch review. Replaces hours-to-days manual debugging; cluster skills use user-scoped write policies and LSF scheduling.
    - Developed a Rust/Tauri 2 workbench with React UI and shared desktop/CLI core.
- Designed and built `ia-mcp`, an internal Python MCP interface used by several engineers for configuration, with typed plans, checkpoints, semantic validation and backend fallback.
    - Implemented Codex-driven NCI/CMN evaluations on installed modules, checking valid builds, DRC, artifacts and cleanup; verified exact configuration-hash restoration in rollback. Separately passed 92 real-engine contract/integration cases.
    - Built `ia-mcp` on Python 3.13; product-aware routing runs current backends directly and legacy Python 3.7 in an isolated, authenticated subprocess with exact-version checks.
- CMN GUI Lead: created and own all coherent-mesh GUI tooling from CMN-800 onward. Deliver features requested by licensees and technical leads; contribute to shared Python backend APIs in a product supporting Arm interconnect licensing.

### Software Engineer | Apr 2020 - Apr 2023

- Built Flask services for Pelion's Jupyter notebooks, persisting files through Kubernetes storage backed by AWS EFS; designed PostgreSQL schemas and end-to-end tests.

### Graduate Software Engineer | Jan 2019 - Apr 2020

- Built Verilog I/O test modules and C++ firmware for the Arm Mbed OS FPGA Test Shield.

## Technical Skills

**Languages:** Python, Rust, TypeScript/JavaScript, C++, SQL  
**Agent systems:** MCP, tool integration, persistent memory, semantic validation, checkpointing, rollback  
**Platform:** Python packaging; Angular, React, Flask, PostgreSQL; Kubernetes, Jenkins/LSF, CI/CD  

## Education

**The University of Texas at Austin**
Bachelor of Science, Electrical and Computer Engineering | Dec 2018
Primary focus: Computer Architecture and Embedded Systems | Secondary: Integrated Circuits
