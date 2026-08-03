#!/usr/bin/env python3
"""
Minimal PromptLayer + OpenAI integration: wraps the OpenAI client with
promptlayer.openai.OpenAI() so a single gpt-4o-mini call is automatically
logged (with a custom tag) to the PromptLayer dashboard, instead of using
the raw OpenAI SDK with no observability.

Learning purpose: see the smallest possible setup for third-party prompt
observability/tracing tooling, as an alternative to hand-rolled trace
logging (compare week4_agents_and_safety/d4_simple_trace_logger.py).
Requires an OpenAI API key and a PromptLayer API key.
"""

from openai import OpenAI
import promptlayer  # <-- use top-level promptlayer import

# 1) Set your keys (replace with real values)
OPENAI_API_KEY = "your-openai-api-key-here"
PROMPTLAYER_API_KEY = "your-promptlayer-api-key-here"

if __name__ == "__main__":
    # 2) Create the PromptLayer-wrapped OpenAI client
    client = promptlayer.openai.OpenAI(
        api_key=OPENAI_API_KEY,
        pl_api_key=PROMPTLAYER_API_KEY,
    )

    # 3) Use the client normally â€“ this call is now tracked by PromptLayer
    prompt = "Explain machine learning in one sentence"

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4o" / other supported models
        messages=[{"role": "user", "content": prompt}],
        pl_tags=["week6-demo"],  # optional: tag this call in the dashboard
    )

    answer = completion.choices[0].message.content

    print("Prompt:", prompt)
    print("Response:", answer)
    print("\nâœ… This call is logged in your PromptLayer dashboard (tag: 'week6-demo').")