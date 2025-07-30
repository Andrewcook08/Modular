from agents.base import Agent
from mcp.storage import Storage as storage
from mcp.syntax import extract_ast_summary

class FileAgent(Agent):
    def __init__(self, file_path: str, llm_client, memory = None, storage=None):
        super().__init__(f"file:{file_path}", llm_client, memory)
        self.file_path = file_path
        self.storage = storage
        self.memory = memory

    def summarize(self):
        code = storage.read_file(self.storage, self.file_path)
        ast_summary = extract_ast_summary(code)
        prompt = f"Summarize this Python file based on its AST:\n\n{ast_summary}"
        return self.llm.chat(prompt)
    
    def plan_refactor(self, instruction: str):
        print("planning refactor ...")
        return self.plan(f"Refactor this file at {self.file_path} with instructions: {instruction}")
    
    def act_on_file(self, plan: str):
        code = storage.read_file(self.storage, self.file_path)
        return self.act(plan, context=code)
    
    def show_diff(self, new_code: str):
        old_code = storage.read_file(self.storage, self.file_path)
        return f"--- OLD ---\n{old_code}\n\n--- NEW ---\n{new_code}"