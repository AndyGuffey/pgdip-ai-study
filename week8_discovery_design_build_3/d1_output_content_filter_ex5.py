# A fifth guardrail variant: filters the model's output for banned words
# after generation, complementing the input-side sanitization in
# d1_prompt_sanitization_ex4.py.
def filter_output(response):
    banned_words = ["violence", "explosive"]

    for word in banned_words:
        if word in response.lower():
            return "I can't provide that information safely."

    return response

model_output = "This could lead to violence if misused."
safe_output = filter_output(model_output)

print("Final output:", safe_output)