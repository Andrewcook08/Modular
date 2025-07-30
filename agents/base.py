class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def plan(self, task: str) -> str:
        raise NotImplementedError
    
    def act(self, task: str) -> str:
        raise NotImplementedError