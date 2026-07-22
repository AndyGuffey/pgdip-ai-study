# Runs a local, offline LLM (Phi-2, quantized as a .gguf file) through
# llama-cpp-python. Unlike the OpenAI/langchain demos elsewhere in this repo,
# no API key or network call is involved - the model weights and inference
# both live on this machine.
from llama_cpp import Llama

print("🚀 Local LLM Demo with Phi-2 Model")
print("=" * 50)

# Initialize the model once
llm = Llama(model_path="./phi-2.Q4_K_M.gguf", verbose=False)

# Demo 1: Code Explanation
print("\n📝 Demo 1: Code Explanation")
print("-" * 30)
code_prompt = """Explain this Python code in simple terms:

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

Answer:"""

resp = llm(code_prompt, max_tokens=100, temperature=0.3)
print(resp["choices"][0]["text"].strip())

# Demo 2: Technical Q&A
print("\n🤖 Demo 2: Technical Question")
print("-" * 30)
tech_prompt = "Q: What is the difference between AI and Machine Learning?\nA:"

resp = llm(tech_prompt, max_tokens=150, temperature=0.5)
print(resp["choices"][0]["text"].strip())

# Demo 3: Creative Writing
print("\n✨ Demo 3: Creative Writing")
print("-" * 30)
creative_prompt = "Write a short story about a programmer who discovers their code can predict the future. Start with: Once upon a time,"

resp = llm(creative_prompt, max_tokens=200, temperature=0.8)
print(resp["choices"][0]["text"].strip())

# Demo 4: Problem Solving
print("\n🧠 Demo 4: Problem Solving")
print("-" * 30)
problem_prompt = """Problem: A company wants to reduce their cloud computing costs. List 3 practical solutions.

Solutions:
1."""

resp = llm(problem_prompt, max_tokens=150, temperature=0.4)
print("1." + resp["choices"][0]["text"].strip())

print("\n" + "=" * 50)
print("✅ Demo Complete! Local LLM successfully handled:")
print("   • Code explanation")
print("   • Technical Q&A") 
print("   • Creative writing")
print("   • Problem solving")
print("\n💡 All processing done locally - no internet required!")