class MemoryStore:
    def __init__(self):
        self.data = {}

    def get(self, key: str, value):
        return self.data.get(key, None)
    
    def set(self, key: str, value):
        self.data[key] = value

    def delete(self, key: str):
        if key in self.data:
            del self.data[key]

    def all(self):
        return self.data