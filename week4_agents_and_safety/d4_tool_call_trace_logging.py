# Agent observability/tracing: wraps a tool (get_weather) so every call and
# its result are logged as trace events via log_event, showing where trace
# logging hooks into a real tool rather than just the log entry shape.

from d4_simple_trace_logger import log_event


def get_weather(city):
    log_event({
        "role": "tool",
        "tool": "get_weather",
        "arguments": {"city": city}
    })
    return f"The weather in {city} is sunny."

# Example usage
result = get_weather("Auckland")
log_event({"role": "tool_result", "tool": "get_weather", "output": result})