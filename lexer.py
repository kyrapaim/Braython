import re
from enum import Enum, auto

class TokenType(Enum):
    # Keywords - Portuguese
    SE = auto()           # if
    SENAO = auto()        # else
    ENQUANTO = auto()     # while
    PARA = auto()         # for
    FUNCAO = auto()       # function/def
    RETORNA = auto()      # return
    VERDADEIRO = auto()   # True
    FALSO = auto()        # False
    NULO = auto()         # None
    ESCREVA = auto()      # print
    DEIXE = auto()        # let/var
    E = auto()            # and
    OU = auto()           # or
    NAO = auto()          # not
    CLASSE = auto()       # class
    TENTE = auto()        # try
    EXCETO = auto()       # except
    FINALMENTE = auto()   # finally
    COM = auto()          # with
    COMO = auto()         # as
    DE = auto()           # from
    IMPORTAR = auto()     # import
    LAMBDA = auto()       # lambda
    PASSE = auto()        # pass
    QUEBRA = auto()       # break
    CONTINUA = auto()     # continue
    EM = auto()           # in
    EH = auto()           # is

    # Operators
    IGUAL = auto()        # =
    MAIS = auto()         # +
    MENOS = auto()        # -
    MULT = auto()         # *
    DIV = auto()          # /
    MODULO = auto()       # %
    IGUAL_IGUAL = auto()  # ==
    DIFERENTE = auto()    # !=
    MAIOR = auto()        # >
    MENOR = auto()        # <
    MAIOR_IGUAL = auto()  # >=
    MENOR_IGUAL = auto()  # <=
    
    # Literals
    NUMERO = auto()
    TEXTO = auto()
    IDENTIFICADOR = auto()
    
    # Delimiters
    LPAREN = auto()       # (
    RPAREN = auto()       # )
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    VIRG = auto()         # ,
    DOIS_PONTOS = auto()  # :
    PONTO_VIRG = auto()   # ;
    
    EOF = auto()

class Lexer:
    def __init__(self, code, language='pt'):
        self.code = code
        self.language = language  # 'pt' for Portuguese, 'es' for Spanish
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        # Define keywords for both languages
        self.keywords = {
            'pt': {
                'se': TokenType.SE,
                'senão': TokenType.SENAO,
                'senao': TokenType.SENAO,
                'enquanto': TokenType.ENQUANTO,
                'para': TokenType.PARA,
                'função': TokenType.FUNCAO,
                'funcao': TokenType.FUNCAO,
                'retorna': TokenType.RETORNA,
                'verdadeiro': TokenType.VERDADEIRO,
                'falso': TokenType.FALSO,
                'nulo': TokenType.NULO,
                'escreva': TokenType.ESCREVA,
                'deixe': TokenType.DEIXE,
                'e': TokenType.E,
                'ou': TokenType.OU,
                'não': TokenType.NAO,
                'nao': TokenType.NAO,
                'classe': TokenType.CLASSE,
                'tente': TokenType.TENTE,
                'exceto': TokenType.EXCETO,
                'finalmente': TokenType.FINALMENTE,
                'com': TokenType.COM,
                'como': TokenType.COMO,
                'de': TokenType.DE,
                'importar': TokenType.IMPORTAR,
                'lambda': TokenType.LAMBDA,
                'passe': TokenType.PASSE,
                'quebra': TokenType.QUEBRA,
                'continua': TokenType.CONTINUA,
                'em': TokenType.EM,
                'é': TokenType.EH,
                'eh': TokenType.EH,
            },
            'es': {
                'si': TokenType.SE,
                'sino': TokenType.SENAO,
                'mientras': TokenType.ENQUANTO,
                'para': TokenType.PARA,
                'función': TokenType.FUNCAO,
                'funcion': TokenType.FUNCAO,
                'retorna': TokenType.RETORNA,
                'verdadero': TokenType.VERDADEIRO,
                'falso': TokenType.FALSO,
                'nulo': TokenType.NULO,
                'escribe': TokenType.ESCREVA,
                'deja': TokenType.DEIXE,
                'y': TokenType.E,
                'o': TokenType.OU,
                'no': TokenType.NAO,
                'clase': TokenType.CLASSE,
                'intenta': TokenType.TENTE,
                'excepto': TokenType.EXCETO,
                'finalmente': TokenType.FINALMENTE,
                'con': TokenType.COM,
                'como': TokenType.COMO,
                'de': TokenType.DE,
                'importar': TokenType.IMPORTAR,
                'lambda': TokenType.LAMBDA,
                'pasa': TokenType.PASSE,
                'rompe': TokenType.QUEBRA,
                'continúa': TokenType.CONTINUA,
                'continua': TokenType.CONTINUA,
                'en': TokenType.EM,
                'es': TokenType.EH,
            }
        }
    
    def tokenize(self):
        while self.pos < len(self.code):
            self._skip_whitespace()
            
            if self.pos >= len(self.code):
                break
            
            char = self.code[self.pos]
            
            # Skip comments
            if char == '#':
                self._skip_comment()
                continue
            
            # Numbers
            if char.isdigit():
                self._read_number()
            # Strings
            elif char in ('"', "'"):
                self._read_string(char)
            # Identifiers and keywords
            elif char.isalpha() or char == '_':
                self._read_identifier()
            # Operators and delimiters
            elif char == '=' and self.peek() == '=':
                self.tokens.append({'type': TokenType.IGUAL_IGUAL, 'value': '==', 'line': self.line, 'column': self.column})
                self.pos += 2
                self.column += 2
            elif char == '!':
                if self.peek() == '=':
                    self.tokens.append({'type': TokenType.DIFERENTE, 'value': '!=', 'line': self.line, 'column': self.column})
                    self.pos += 2
                    self.column += 2
                else:
                    self.pos += 1
                    self.column += 1
            elif char == '<':
                if self.peek() == '=':
                    self.tokens.append({'type': TokenType.MENOR_IGUAL, 'value': '<=', 'line': self.line, 'column': self.column})
                    self.pos += 2
                    self.column += 2
                else:
                    self.tokens.append({'type': TokenType.MENOR, 'value': '<', 'line': self.line, 'column': self.column})
                    self.pos += 1
                    self.column += 1
            elif char == '>':
                if self.peek() == '=':
                    self.tokens.append({'type': TokenType.MAIOR_IGUAL, 'value': '>=', 'line': self.line, 'column': self.column})
                    self.pos += 2
                    self.column += 2
                else:
                    self.tokens.append({'type': TokenType.MAIOR, 'value': '>', 'line': self.line, 'column': self.column})
                    self.pos += 1
                    self.column += 1
            elif char == '=':
                self.tokens.append({'type': TokenType.IGUAL, 'value': '=', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '+':
                self.tokens.append({'type': TokenType.MAIS, 'value': '+', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '-':
                self.tokens.append({'type': TokenType.MENOS, 'value': '-', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '*':
                self.tokens.append({'type': TokenType.MULT, 'value': '*', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '/':
                self.tokens.append({'type': TokenType.DIV, 'value': '/', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '%':
                self.tokens.append({'type': TokenType.MODULO, 'value': '%', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '(':  
                self.tokens.append({'type': TokenType.LPAREN, 'value': '(', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == ')':
                self.tokens.append({'type': TokenType.RPAREN, 'value': ')', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '{':
                self.tokens.append({'type': TokenType.LBRACE, 'value': '{', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == '}':
                self.tokens.append({'type': TokenType.RBRACE, 'value': '}', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == ',':
                self.tokens.append({'type': TokenType.VIRG, 'value': ',', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == ':':
                self.tokens.append({'type': TokenType.DOIS_PONTOS, 'value': ':', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            elif char == ';':
                self.tokens.append({'type': TokenType.PONTO_VIRG, 'value': ';', 'line': self.line, 'column': self.column})
                self.pos += 1
                self.column += 1
            else:
                self.pos += 1
                self.column += 1
        
        self.tokens.append({'type': TokenType.EOF, 'value': '', 'line': self.line, 'column': self.column})
        return self.tokens
    
    def peek(self):
        if self.pos + 1 < len(self.code):
            return self.code[self.pos + 1]
        return '\0'
    
    def _skip_whitespace(self):
        while self.pos < len(self.code) and self.code[self.pos].isspace():
            if self.code[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def _skip_comment(self):
        while self.pos < len(self.code) and self.code[self.pos] != '\n':
            self.pos += 1
    
    def _read_number(self):
        start = self.pos
        start_column = self.column
        
        while self.pos < len(self.code) and (self.code[self.pos].isdigit() or self.code[self.pos] == '.'): 
            self.pos += 1
            self.column += 1
        
        value = self.code[start:self.pos]
        self.tokens.append({'type': TokenType.NUMERO, 'value': value, 'line': self.line, 'column': start_column})
    
    def _read_string(self, quote):
        start_column = self.column
        self.pos += 1
        self.column += 1
        start = self.pos
        
        while self.pos < len(self.code) and self.code[self.pos] != quote:
            if self.code[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
        
        value = self.code[start:self.pos]
        self.tokens.append({'type': TokenType.TEXTO, 'value': value, 'line': self.line, 'column': start_column})
        
        if self.pos < len(self.code):
            self.pos += 1
            self.column += 1
    
    def _read_identifier(self):
        start = self.pos
        start_column = self.column
        
        while self.pos < len(self.code) and (self.code[self.pos].isalnum() or self.code[self.pos] == '_'):
            self.pos += 1
            self.column += 1
        
        value = self.code[start:self.pos]
        
        # Check if it's a keyword
        keywords = self.keywords.get(self.language, {})
        token_type = keywords.get(value.lower(), TokenType.IDENTIFICADOR)
        self.tokens.append({'type': token_type, 'value': value, 'line': self.line, 'column': start_column})