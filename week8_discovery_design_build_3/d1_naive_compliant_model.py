# Baseline "model" with no safety/refusal logic — it complies with any prompt.
def naive_model(prompt):
    return f"Sure! Here's how you do it: {prompt}"

while True:
    user = input("User: ")
    print("Model:", naive_model(user))