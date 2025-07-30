# mcp/storage.py

import os
from datetime import datetime

class Storage:
    def __init__(self, base_path: str = ""):
        self.base_path = base_path

    def read_file(self, path: str) -> str:
        full_path = os.path.join(self.base_path, path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(self, path: str, content: str):
        full_path = os.path.join(self.base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    def version_file(self, path: str, content: str):
        """Save a timestamped backup before overwriting."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{path}.{timestamp}.bak"
        self.write(backup_path, content)

    def save(self, path: str, content: str):
        """Save a file with versioning."""
        try:
            old_content = self.read(path)
            self.version_file(path, old_content)
        except FileNotFoundError:
            pass  # No previous version exists
        self.write(path, content)