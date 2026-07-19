# Agent observability/tracing: a sample trace record showing what should be
# logged when an agent decides to call a tool — timestamp, role, the
# decision type, which tool was chosen and with what arguments, and a
# run_id to correlate it with the rest of that session's trace.

{
    "timestamp": "2026-06-20T12:00:00Z",
    "role": "assistant",
    "decision": "tool_call",
    "tool":"get_weather",
    "arguments": {
        "city": "Auckland"
    },
    "run_id": "session_abc123"
}