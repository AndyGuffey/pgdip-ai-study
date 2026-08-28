# Token cost estimation & prompt-shortening cost optimization demo.
# Uses tiktoken to count exact tokens for a model, estimates $ cost per
# request from a per-1K-token price, and applies a simple optimization
# (truncating prompt/response to a token cap) to show the resulting token
# and cost savings.
COST_PER_1K_TOKENS = 0.002  # example pricing

import tiktoken

# Use a concrete model name whose tokenizer you want to match
ENCODING_NAME = "gpt-4o-mini"

encoding = tiktoken.encoding_for_model(ENCODING_NAME)

def estimate_tokens(text: str) -> int:
    # Exact token count according to the model's tokenizer
    return len(encoding.encode(text))

def estimate_cost(prompt, response):
    input_tokens = estimate_tokens(prompt)
    output_tokens = estimate_tokens(response)
    total_tokens = input_tokens + output_tokens
    cost = (total_tokens / 1000) * COST_PER_1K_TOKENS
    return total_tokens, cost

def shorten_text(text: str, max_tokens: int) -> str:
    """
    Simple cost-optimization helper:
    - If text exceeds max_tokens, truncate it at that many tokens.
    - Otherwise, return as-is.
    """
    tokens = encoding.encode(text)
    if len(tokens) <= max_tokens:
        return text
    trimmed = tokens[:max_tokens]
    return encoding.decode(trimmed)

# Simulate requests
prompts = [
    "Explain continual learning in simple terms",
    "Summarize cost optimization strategies in AI systems, including caching, batching, model routing, "
    "and prompt shortening techniques for large-scale deployments.",
]

responses = [
    "Continual learning allows models to adapt over time without forgetting previous knowledge.",
    "Cost optimization focuses on reducing token usage by shortening prompts, limiting response length, "
    "using cheaper models for simple tasks, and caching frequent answers.",
]

# Apply a very simple optimization: cap each prompt/response to 30 tokens
MAX_PROMPT_TOKENS = 10
MAX_RESPONSE_TOKENS = 20

for p, r in zip(prompts, responses):
    optimized_prompt = shorten_text(p, MAX_PROMPT_TOKENS)
    optimized_response = shorten_text(r, MAX_RESPONSE_TOKENS)

    tokens_before, cost_before = estimate_cost(p, r)
    tokens_after, cost_after = estimate_cost(optimized_prompt, optimized_response)

    print("\n--- Request ---")
    print("Original tokens:", tokens_before, "| Cost: ${:.6f}".format(cost_before))
    print("Optimized tokens:", tokens_after, "| Cost: ${:.6f}".format(cost_after))