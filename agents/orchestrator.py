from agents.file_agent import FileAgent
from mcp.memory import MemoryStore
from mcp.storage import Storage
import os

def no_markdown(text):
        return "".join([line for line in text.split('\n') if not line.strip().startswith('```')])

class Orchestrator:
    def __init__(self, llm_client, memory = None, storage = None):
        self.llm = llm_client
        self.memory = memory or MemoryStore()
        self.file_agents = {}
        self.storage = storage

    def register_file(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found.")
        agent = FileAgent(path, self.llm, self.memory, self.storage)
        self.file_agents[path] = agent
        return agent
    
    def summarize_all(self):
        return {path: agent.summarize() for path, agent in self.file_agents.items()}

    def refactor_all(self, instruction: str, path):
        results = {}
        for path, agent in self.file_agents.items():
            plan = agent.plan_refactor(instruction)
            result = agent.act_on_file(plan)
            # formatted_result = self.llm.chat(f"strip this so that there is no markdown formatting, do not give me any words in your response, just the formatted code. ensure all indentations are correct. Code: {result}")
        lines = result.strip().splitlines()
        formatted_result = ""
    # If it starts with a markdown fence like ``` or ```python, remove first and last line
        if lines and lines[0].strip().startswith("```") and lines[-1].strip().startswith("```"):
            formatted_result =  "\n".join(lines[1:-1])
        self.storage.write_file(path, formatted_result)
        print(result)
        results[path] = agent.show_diff(result)
        return results