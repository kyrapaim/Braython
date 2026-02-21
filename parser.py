import ast

class ASTParser:
    def __init__(self, language: str):
        self.language = language

    def parse(self, code: str):
        try:
            tree = ast.parse(code)
            return tree
        except SyntaxError as e:
            return f"Syntax Error: {e}"

    def handle_portuguese(self, code: str):
        # Implementation for parsing Portuguese syntax
        return self.parse(code)

    def handle_spanish(self, code: str):
        # Implementation for parsing Spanish syntax
        return self.parse(code)

    def parse_code(self, code: str):
        if self.language.lower() == 'portuguese':
            return self.handle_portuguese(code)
        elif self.language.lower() == 'spanish':
            return self.handle_spanish(code)
        else:
            return "Unsupported language"

# Example usage:
if __name__ == "__main__":
    code = """
    def hello():
        print("Olá" if language == "portuguese" else "Hola")
    """
    parser = ASTParser(language="portuguese")
    result = parser.parse_code(code)
    print(result)