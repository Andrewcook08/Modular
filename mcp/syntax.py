import ast

def extract_ast_summary(code: str) -> str:
    try:
        tree = ast.parse(code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        return (
            f"Classes: {', '.join(classes) if classes else 'None'}\n"
            f"Functions: {', '.join(functions) if functions else 'None'}"
        )
    except Exception as e:
        return f"[Error parsing code AST] {e}"