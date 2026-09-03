# Edge/cloud request routing demo.
# Routes short prompts to a fast, free "edge" template answer and longer
# ones to a real OpenAI cloud call — a simple cost-aware routing pattern
# that avoids paying for cloud inference on trivial requests.
import os
from openai import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in the environment.")

client = OpenAI(api_key=OPENAI_API_KEY)

def edge_answer(prompt: str) -> str:
    # Very fast, cheap, template-based local answer
    return f"[EDGE] Quick answer: {prompt[:50]}..."

def cloud_answer(prompt: str) -> str:
    # Use OpenAI in the cloud for richer answers
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def route_request(prompt: str) -> str:
    # Simple routing rule: very short prompts to edge, others to cloud
    if len(prompt) < 5:
        return edge_answer(prompt)
    else:
        return cloud_answer(prompt)

if __name__ == "__main__":
    prompt = "Explain machine learning in one sentence"
    answer = route_request(prompt)
    print("Prompt:", prompt)
    print("Response:", answer)