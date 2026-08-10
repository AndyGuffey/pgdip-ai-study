# Adds a simple keyword-based refusal check on top of the naive baseline
# in d1_naive_compliant_model.py.
BANNED_KEYWORDS = ["hack", "kill"]

def safe_model(prompt):
    for word in BANNED_KEYWORDS:
        if word in prompt.lower():
            return "I can't help with that request."
    return f"I can help explain this safely: {prompt}"

while True:
    user = input("User: ")
    print("Model:", safe_model(user))