import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "deepseek-coder-v2:16b")
print(f"Using model: {OLLAMA_MODEL}")

class OllamaClient:
    def __init__(self, model: str = OLLAMA_MODEL):
        self.model = model

    def chat(self, prompt: str) -> str:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json = {"model": self.model, "prompt": prompt, "stream": False},
        )
        if(response.ok):
            return response.json()["response"]
        else:
            raise RuntimeError(f"Ollama error: {response.status_code}, {response.text}")