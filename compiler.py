import re

from lexer import Lexer, TipoToken
from parser import ASTParser
from messages import msg, translate_exception

class Compiler:
    def __init__(self):
        # Portuguese to Python translations (order matters - more specific first)
        self._pt_translations = [
            # Import statements
            (r'\bde\b([\s\w.]+)\bimportar\b', r'from\1import'),
            (r'\bimportar\b', 'import'),
            # Enum support
            (r'\bEnumeracao\b', 'Enum'),
            (r'\benumeracao\b', 'enum'),
            # Print
            (r'\bescreva\b', 'print'),
            # Variable assignment (remove keyword)
            (r'\bdeixe\b\s*', ''),
            # Control flow (senao_se/senão_se before senao/senão, then se)
            (r'\bsen[aã]o_se\b', 'elif'),
            (r'\bsen[aã]o\b', 'else'),
            (r'\bse\b', 'if'),
            (r'\benquanto\b', 'while'),
            # For loop
            (r'\bpara\b', 'for'),
            (r'\bem\b', 'in'),
            (r'\balcance\b', 'range'),
            # Function definition (funcao, função, funçao, funcão)
            (r'\bfun[cç][aã]o\b', 'def'),
            # Return
            (r'\bretorna\b', 'return'),
            # Booleans / None
            (r'\bverdadeiro\b', 'True'),
            (r'\bfalso\b', 'False'),
            (r'\bnulo\b', 'None'),
            # Loop control
            (r'\bcontinua\b', 'continue'),
            (r'\bquebra\b', 'break'),
            # Logical operators
            (r'\bou\b', 'or'),
            (r'\be\b', 'and'),
        ]

        # Spanish to Python translations (order matters - more specific first)
        self._es_translations = [
            # Import statements
            (r'\bde\b([\s\w.]+)\bimportar\b', r'from\1import'),
            (r'\bimportar\b', 'import'),
            # Enum support
            (r'\bEnumeracion\b', 'Enum'),
            (r'\benumeracion\b', 'enum'),
            # Print
            (r'\bescribe\b', 'print'),
            # Variable assignment (remove keyword)
            (r'\bdeja\b\s*', ''),
            # Control flow (sino_si before sino, then si)
            (r'\bsino_si\b', 'elif'),
            (r'\bsino\b', 'else'),
            (r'\bsi\b', 'if'),
            (r'\bmientras\b', 'while'),
            # For loop
            (r'\bpara\b', 'for'),
            (r'\ben\b', 'in'),
            (r'\brango\b', 'range'),
            # Function definition (funcion, función)
            (r'\bfunci[oó]n\b', 'def'),
            # Return
            (r'\bretorna\b', 'return'),
            # Booleans / None
            (r'\bverdadero\b', 'True'),
            (r'\bfalso\b', 'False'),
            (r'\bnulo\b', 'None'),
            # Loop control
            (r'\bcontinua\b', 'continue'),
            (r'\brompe\b', 'break'),
        ]

    def _split_code_and_strings(self, line: str):
        """Split a line into alternating ('code', text) and ('string', text) segments."""
        parts = []
        in_string = False
        string_char = None
        current = ""
        i = 0
        while i < len(line):
            char = line[i]
            if not in_string:
                if char in ('"', "'"):
                    if current:
                        parts.append(('code', current))
                        current = ""
                    in_string = True
                    string_char = char
                    current = char
                else:
                    current += char
            else:
                current += char
                if char == '\\' and i + 1 < len(line):
                    i += 1
                    current += line[i]
                elif char == string_char:
                    parts.append(('string', current))
                    current = ""
                    in_string = False
                    string_char = None
            i += 1
        if current:
            parts.append(('code' if not in_string else 'string', current))
        return parts

    def _translate_line(self, line: str, translations: list) -> str:
        """Translate a single line, leaving string literals and comments untouched."""
        stripped = line.lstrip()
        if stripped.startswith('#'):
            return line
        parts = self._split_code_and_strings(line)
        result = ""
        for part_type, text in parts:
            if part_type == 'code':
                for pattern, replacement in translations:
                    text = re.sub(pattern, replacement, text)
            result += text
        return result

    def compile(self, code: str, language: str) -> str:
        """ Convert code from Portuguese/Spanish to Python. """
        if language == 'pt':
            translations = self._pt_translations
        elif language == 'es':
            translations = self._es_translations
        else:
            raise ValueError("Unsupported language. Use 'pt' for Portuguese or 'es' for Spanish.")
        lines = code.split('\n')
        translated = [self._translate_line(line, translations) for line in lines]
        return '\n'.join(translated)

    def compile_and_run(self, code: str, language: str):
        """ Compile the code and execute the generated Python."""
        python_code = self.compile(code, language)
        try:
            exec(python_code)
        except Exception as e:
            # Localized runtime error message and translated detail when possible
            try:
                print(f"{msg('runtime_error', language)}: {e}")
                translated = translate_exception(e, language)
                if translated:
                    print(f"{translated}")
            except Exception:
                # Fallback if message localization fails
                print(f"Runtime error: {e}")

    def compile_to_file(self, input_file: str, output_file: str, language: str):
        """ Read code from input_file, compile it, and save to output_file. """
        with open(input_file, 'r') as infile:
            code = infile.read()
        python_code = self.compile(code, language)
        with open(output_file, 'w') as outfile:
            outfile.write(python_code)
