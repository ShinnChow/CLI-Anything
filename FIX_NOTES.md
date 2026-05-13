# PR-245 Fix Notes

## DAP Attach Smoke

Result: real LLDB-backed DAP client smoke was not run in this environment because
`lldb` is not installed on PATH. `gcc` is available, but the LLDB Python/runtime
backend required by `cli-anything-lldb-dap` is unavailable.

Checklist for an environment with LLDB installed:

1. Start `cli-anything-lldb-dap` as a stdio DAP server.
2. Send `initialize` and verify a successful response followed by `initialized`.
3. Start a long-running helper process.
4. Send `attach` with only `{"processId": <pid>}` and no `program` or `executable`.
5. Send `configurationDone` and verify the adapter attaches, then emits a stopped
   or continued execution event without an attach validation error.
6. Repeat with `{"processName": "<helper-basename>", "waitFor": false}` and no
   `program` or `executable`.
7. Verify the existing launch path still accepts `{"program": "<helper-path>"}` and
   reaches `configurationDone` without requiring the new empty-target path.

