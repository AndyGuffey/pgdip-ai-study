# Agent observability/tracing: wraps an OpenAI chat completion call so the
# model's decision (which tool it chose to call, or that it responded
# directly) gets logged as a trace event alongside the raw response.

from openai import OpenAI
from w4_d4_simple_trace_logger import log_event

client = OpenAI()

def call_model(messages, tools=None):
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools or []
    )
    msg = resp.choices[0].message
    log_event({
        "role": "assistant",
        "decision": msg.tool_calls[0].function.name if msg.tool_calls else "respond",
        "content": msg.content
    })
    return msg