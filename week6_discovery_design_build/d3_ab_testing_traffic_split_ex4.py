# Randomly routes 100 requests roughly 50/50 between a "new" and "old"
# prompt version and tallies how many went to each, with no LLM call
# involved.
# Learning purpose: understand the basic mechanics of A/B testing traffic
# splitting for prompts — randomly assigning requests to a variant and
# counting the split — as groundwork before comparing variant quality.

import random

def route_request(prompt):
    if random.random() < 0.5:
        return "New_Prompt", f"[new_prompt]{prompt}"
    else:
        return "Old_Prompt", f"[old_prompt]{prompt}"
    
counter = {"New_Prompt": 0, "Old_Prompt": 0}

for _ in range(100):
    version, _ = route_request("Hello")
    counter["New_Prompt" if version == "New_Prompt" else "Old_Prompt"] += 1
    
print(counter)