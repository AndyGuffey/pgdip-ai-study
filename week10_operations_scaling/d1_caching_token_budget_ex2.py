# Response caching + token budget guard demo.
# Caches responses by prompt to avoid repeat model calls, and rejects any
# request whose (rough, word-count) token estimate exceeds a fixed budget —
# two simple cost-control mechanisms for AI request handling.
cache = {}
TOKEN_BUDGET = 3

def estimate_tokens(text):
    return len(text.split())

def ai_call(prompt):
    return f"Processed response for: {prompt}"

def handle_request(prompt):

    # --- Cache Check ---
    if prompt in cache:
        print("Cache HIT → returning cached response")
        return cache[prompt]

    # --- Token Budget Check ---
    tokens = estimate_tokens(prompt)
    if tokens > TOKEN_BUDGET:
        return "Request exceeds token budget"

    # --- Simulated AI Call ---
    response = ai_call(prompt)

    # Store in cache
    cache[prompt] = response
    print("Cache MISS → calling model")

    return response


# Simulate requests
queries = [
    "Explain token budgeting",
    "Explain token budgeting",
    "Summarize caching strategies in AI"
]

for q in queries:
    print(handle_request(q))