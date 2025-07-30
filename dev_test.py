# devtest.py

from agents.orchestrator import Orchestrator
from models.ollama_client import OllamaClient
from mcp.memory import MemoryStore
from mcp.storage import Storage

# --- SETUP ---
model = OllamaClient()
memory = MemoryStore()
storage = Storage("/Users/andrew/Developer/Modular")

orchestrator = Orchestrator(model, memory, storage)

# --- PATH TO TEST ---
file_path = "examples/simple_app.py"

# --- RUN TEST ---
print(f"\n🔧 Registering file: {file_path}")
orchestrator.register_file(file_path)

print("File agents:", orchestrator.file_agents)

print(f"\n🧠 Summarizing {file_path}")
print(storage.base_path)
summary = orchestrator.summarize_all()
print(f"\n📋 Summary:\n{summary}")

instruction = "Generate a plan for another AI agent that will carry out the task: Implement the add function provided. Write only valid Python code. Do not include markdown formatting or explanations."
print(f"\n🛠️ Refactoring {file_path} with instruction {instruction}...")
result = orchestrator.refactor_all(instruction, file_path)
print(f"\n✅ Refactor Result:\n{result}")