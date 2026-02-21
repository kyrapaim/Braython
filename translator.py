import re


class Translator:
    """Translates Braython source code (Portuguese or Spanish) into standard Python."""

    # Portuguese keyword/built-in -> Python mapping
    PT_MAP = {
        # Control flow
        'se': 'if',
        'senão': 'else',
        'senao': 'else',
        'enquanto': 'while',
        'para': 'for',
        # Functions / classes
        'função': 'def',
        'funcao': 'def',
        'retorna': 'return',
        'classe': 'class',
        'lambda': 'lambda',
        # Boolean / None
        'verdadeiro': 'True',
        'falso': 'False',
        'nulo': 'None',
        # Logic operators
        'e': 'and',
        'ou': 'or',
        'não': 'not',
        'nao': 'not',
        # Exception handling
        'tente': 'try',
        'exceto': 'except',
        'finalmente': 'finally',
        # Context managers
        'com': 'with',
        'como': 'as',
        # Imports
        'de': 'from',
        'importar': 'import',
        # Loop control
        'passe': 'pass',
        'quebra': 'break',
        'continua': 'continue',
        # Membership / identity
        'em': 'in',
        'é': 'is',
        'eh': 'is',
        # Built-in functions
        'escreva': 'print',
        'tamanho': 'len',
        'tipo': 'type',
        'intervalo': 'range',
        'entrada': 'input',
        'inteiro': 'int',
        'texto': 'str',
        'decimal': 'float',
        'lista': 'list',
        'tupla': 'tuple',
        'dicionario': 'dict',
        'conjunto': 'set',
    }

    # Spanish keyword/built-in -> Python mapping
    ES_MAP = {
        # Control flow
        'si': 'if',
        'sino': 'else',
        'mientras': 'while',
        'para': 'for',
        # Functions / classes
        'función': 'def',
        'funcion': 'def',
        'retorna': 'return',
        'clase': 'class',
        'lambda': 'lambda',
        # Boolean / None
        'verdadero': 'True',
        'falso': 'False',
        'nulo': 'None',
        # Logic operators
        'y': 'and',
        'o': 'or',
        'no': 'not',
        # Exception handling
        'intenta': 'try',
        'excepto': 'except',
        'finalmente': 'finally',
        # Context managers
        'con': 'with',
        'como': 'as',
        # Imports
        'de': 'from',
        'importar': 'import',
        # Loop control
        'pasa': 'pass',
        'rompe': 'break',
        'continúa': 'continue',
        'continua': 'continue',
        # Membership / identity
        'en': 'in',
        'es': 'is',
        # Built-in functions
        'escribe': 'print',
        'tamaño': 'len',
        'tipo': 'type',
        'rango': 'range',
        'entrada': 'input',
        'entero': 'int',
        'texto': 'str',
        'flotante': 'float',
        'lista': 'list',
        'tupla': 'tuple',
        'diccionario': 'dict',
        'conjunto': 'set',
    }

    # Matches triple-quoted strings, single-quoted strings, comments, or identifiers.
    # Order matters: longer/more-specific patterns come first.
    _TOKEN_PATTERN = re.compile(
        r'"""(?:[^"\\]|\\.)*"""|'
        r"'''(?:[^'\\]|\\.)*'''|"
        r'"(?:[^"\\]|\\.)*"|'
        r"'(?:[^'\\]|\\.)*'|"
        r'#[^\n]*|'
        r'[^\W\d]\w*',
        re.DOTALL | re.UNICODE,
    )

    def translate(self, code: str, language: str) -> str:
        """Return *code* rewritten as valid Python.

        Parameters
        ----------
        code:
            Source code written using Portuguese (``'pt'``) or Spanish (``'es'``)
            Braython keywords.
        language:
            ``'pt'`` for Portuguese or ``'es'`` for Spanish.
        """
        if language == 'pt':
            mapping = self.PT_MAP
            var_keyword = 'deixe'
        elif language == 'es':
            mapping = self.ES_MAP
            var_keyword = 'deja'
        else:
            raise ValueError(f"Unsupported language '{language}'. Use 'pt' or 'es'.")

        # Remove variable-declaration keywords (deixe/deja) together with the
        # horizontal whitespace that separates them from the variable name, so
        # that the indentation of the line is preserved.
        code = re.sub(
            r'(?<!\w)' + re.escape(var_keyword) + r'(?!\w)[ \t]+',
            '',
            code,
        )

        # Replace every identifier-like token that appears in the mapping while
        # leaving string literals and comments untouched.
        def _replace(match: re.Match) -> str:
            token = match.group(0)
            if token[0] in ('"', "'", '#'):
                return token
            return mapping.get(token, token)

        return self._TOKEN_PATTERN.sub(_replace, code)
