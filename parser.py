# parser.py

class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        return f"<{self.node_type}: {self.value}>"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        return self.program()

    def program(self):
        nodes = []
        while self.current < len(self.tokens):
            nodes.append(self.statement())
        return ASTNode('Program', children=nodes)

    def statement(self):
        # This is a placeholder for various statement types
        if self.match('IDENTIFIER'):
            return self.variable_declaration()
        raise Exception('Unexpected token')

    def variable_declaration(self):
        identifier = self.consume('IDENTIFIER')
        return ASTNode('VariableDeclaration', value=identifier)

    def match(self, token_type):
        if self.check(token_type):
            self.current += 1
            return True
        return False

    def check(self, token_type):
        if self.is_at_end():
            return False
        return self.tokens[self.current]['type'] == token_type

    def consume(self, token_type):
        if self.check(token_type):
            return self.tokens[self.current]['value']
        raise Exception(f'Expected token type: {token_type}')

    def is_at_end(self):
        return self.current >= len(self.tokens)

# Example usage
# tokens = [{'type': 'IDENTIFIER', 'value': 'x'}]
# parser = Parser(tokens)
# ast = parser.parse()
# print(ast)