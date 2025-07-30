from mcp.memory import MemoryStore

class Agent:
    def __init__(self, name: str, llm_client, memory: MemoryStore = None):
        self.name = name
        self.llm = llm_client
        self.memory = memory or MemoryStore()

    def plan(self, task: str) -> str:
        prompt = """You are an agent that reasons and makes decisions. Your task is: {task}"""
        print(f"task for planning: {task}")
        plan = self.llm.chat(prompt)
        self.remember("last_plan", plan)
        return plan
    
    def act(self, plan: str, context: str = "") -> str:
        prompt = f"""Act on the following plan: {plan} \n\n context: {context} Write only valid Python code. Do not include markdown formatting or explanations."""
        print(f"prompt for action: {prompt}")
        action_output = self.llm.chat(prompt)
        self.remember("last_action", action_output)
        return action_output
    
    def remember(self, key: str, value):
        self.memory.set(f"{self.name}:{key}", value)
    
    def recall(self, key: str):
        return self.memory.get(f"{self.name}:{key}")