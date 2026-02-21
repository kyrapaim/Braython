from lexer import Lexer, TipoToken
from parser import ASTParser

class Compiler:
    def __init__(self):
        # Initialize lexer, parser, and translator here
        self.lexer = None
        self.parser = None

    def compile(self, code: str, language: str) -> str:
        """ Convert code from Portuguese/Spanish to Python. """  
        if language not in ['pt', 'es']:
            raise ValueError("Unsupported language. Use 'pt' for Portuguese or 'es' for Spanish.")
        
        # Tokenize
        lexer = Lexer(code, idioma=language)
        tokens = lexer.obter_tokens()
        
        # Parse and translate to Python
        python_code = self._translate_to_python(tokens, language)
        return python_code

    def _translate_to_python(self, tokens: list, language: str) -> str:
        """ Translate tokens to Python code. """
        # Group tokens by source line so we can preserve basic block structure
        lines = {}
        for t in tokens:
            lineno = t.get('linha', 0)
            lines.setdefault(lineno, []).append(t)

        def tok_to_src(t):
            tt = t['tipo']
            v = t['valor']
            if tt == TipoToken.TEXTO:
                return repr(v)
            if tt == TipoToken.NUMERO:
                return str(v)
            if tt == TipoToken.ESCREVA:
                return 'print'
            if tt == TipoToken.DEIXE:
                return ''
            if tt == TipoToken.SE:
                return 'if'
            if tt == TipoToken.SENAO:
                return 'else'
            if tt == TipoToken.PARA:
                return 'for'
            if tt == TipoToken.FUNCAO:
                return 'def'
            if tt == TipoToken.RETORNA:
                return 'return'
            if tt == TipoToken.VERDADEIRO:
                return 'True'
            if tt == TipoToken.FALSO:
                return 'False'
            if tt == TipoToken.NULO:
                return 'None'
            # operators and punctuation: value already holds symbol
            return str(v)

        python_lines = []
        for lineno in sorted(k for k in lines.keys() if k > 0):
            toks = lines[lineno]
            if not toks:
                continue
            indent_spaces = max(0, toks[0].get('coluna', 1) - 1)
            indent = ' ' * indent_spaces

            first = toks[0]['tipo']

            # Assignment: "deixe x = expr" -> "x = expr"
            if first == TipoToken.DEIXE:
                src_parts = [tok_to_src(t) for t in toks[1:]]
                # simple join, collapse extra spaces
                line_src = ' '.join(p for p in src_parts if p)
                python_lines.append(f"{indent}{line_src}")
                continue

            # If statement: "se COND :" -> "if COND :"
            if first == TipoToken.SE:
                # take everything after SE up to ':'
                parts = []
                for t in toks[1:]:
                    if t['tipo'] == TipoToken.DOIS_PONTOS:
                        break
                    parts.append(tok_to_src(t))
                cond = ' '.join(p for p in parts if p)
                python_lines.append(f"{indent}if {cond}:")
                continue

            # Else
            if first == TipoToken.SENAO:
                python_lines.append(f"{indent}else:")
                continue

            # Function
            if first == TipoToken.FUNCAO:
                parts = [tok_to_src(t) for t in toks[1:]]
                line_src = ' '.join(p for p in parts if p)
                python_lines.append(f"{indent}def {line_src}")
                continue

            # For loop: translate Portuguese flavors -> Python
            if first == TipoToken.PARA:
                # reconstruct and replace common words
                parts = [tok_to_src(t) for t in toks[1:]]
                line = ' '.join(p for p in parts if p)
                # replace Portuguese keywords
                line = line.replace(' em ', ' in ')
                line = line.replace('alcance', 'range')
                python_lines.append(f"{indent}for {line}")
                continue

            # Default: map tokens to source and join
            parts = [tok_to_src(t) for t in toks]
            line_src = ' '.join(p for p in parts if p)
            python_lines.append(f"{indent}{line_src}")

        return "\n".join(python_lines) if python_lines else "# Empty code"

    def compile_and_run(self, code: str, language: str):
        """ Compile the code and execute the generated Python."""
        python_code = self.compile(code, language)
        try:
            exec(python_code)
        except Exception as e:
            print(f"Error executing code: {e}")

    def compile_to_file(self, input_file: str, output_file: str, language: str):
        """ Read code from input_file, compile it, and save to output_file. """
        with open(input_file, 'r') as infile:
            code = infile.read()
        python_code = self.compile(code, language)
        with open(output_file, 'w') as outfile:
            outfile.write(python_code)


if __name__ == "__main__":
    compiler = Compiler()
    
    # Test with Portuguese code
    test_code = 'escreva("Olá, Mundo!")'
    print("Compiling Portuguese code...")
    result = compiler.compile(test_code, 'pt')
    print(result)
