# Checks whether a simulated LLM output is valid JSON containing an
# "answer" key, contrasting a well-formed structured response against a
# plain-text one that fails the check.
# Learning purpose: understand the simplest form of output validation for
# LLM responses — parsing and structure checks — as a guardrail before
# trusting a model's output downstream.

import json

def is_valid_response(text):
    try:
        data = json.loads(text)
        return "answer" in data
    except json.JSONDecodeError:
        return False

# Simulated model outputs
good_output = '{"answer": "Yes"}'
bad_output = 'Sure! The answer is yes.'

print(is_valid_response(good_output))  # True
print(is_valid_response(bad_output))   # False