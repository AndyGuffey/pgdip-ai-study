# Runs a local LLM (Phi, via Ollama) over Ollama's HTTP API instead of
# loading the model in-process like week5_strategy_risk_governance/d1_example1.py does.
# Ollama must already be running locally (`ollama serve`, with the `phi`
# model pulled) - this script just POSTs a prompt to it and prints the
# generated response, with error handling for the server being down,
# the request timing out, or the call being interrupted.
import requests
import json

print("🦙 Ollama Local LLM Demo")
print("=" * 40)

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_ollama(prompt, model="phi"):
    """Call Ollama API with error handling"""
    try:
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
        
        return response.json()["response"]
    
    except (requests.exceptions.ConnectionError, ConnectionRefusedError):
        return "❌ Error: Ollama server not running. Please start Ollama first with 'ollama serve'"
    
    except requests.exceptions.Timeout:
        return "⏰ Error: Request timed out. Model might be loading or busy."
    
    except KeyboardInterrupt:
        return "⛔ Operation cancelled by user."
    
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Demo 1: Technical Explanation
print("\n📚 Demo 1: Technical Explanation")
print("-" * 35)
prompt1 = "Explain what python is?"
response1 = call_ollama(prompt1)
print(response1)