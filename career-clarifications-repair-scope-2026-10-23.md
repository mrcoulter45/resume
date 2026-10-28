# repair-jenkins scope clarification - October 23, 2026

Michael directly clarified the scope in the resume chat and requested changing only the repair-jenkins bullet and the ia-mcp runtime bullet's opening verb.

repair-jenkins handles flaky tests, legitimate defects in test code, and actual failing tests that require targeted fixes in application/source code. The same Codex workflow identifies the failing tests and can address these categories together; it is not limited to flakiness.

The existing repeat-pass requirement, human patch review, reported hours-to-days manual-debugging baseline and user-scoped cluster-write/LSF policies remain supported by their earlier sources. This clarification supplies no new metric or independent test execution.

Michael also explicitly requested changing “Run ia-mcp on Python 3.13” to “Built ia-mcp on Python 3.13”, preserving the rest of the runtime statement. Existing IA and DUAL_RUNTIME evidence already describes his implementation of this architecture.
