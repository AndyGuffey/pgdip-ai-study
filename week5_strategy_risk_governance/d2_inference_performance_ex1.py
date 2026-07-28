# Sends a single prompt to OpenAI's gpt-4o-mini model and measures the
# end-to-end latency of the API call, from request to full response.
# Learning purpose: understand how to measure LLM inference performance
# (response time) as a factor in model/strategy evaluation, ahead of
# comparing this against other inference setups (e.g. local models).

import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

start = time.time()
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":"I need a python code that prints the first 10 Fibonacci numbers."}],
)
print(resp.choices[0].message.content)

print("Latency:", time.time() - start, "seconds")