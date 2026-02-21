import re

from enum import Enum, auto

class TipoToken(Enum):
    # Palavras-chave - Português
    SE = auto()           # se
    SENAO = auto()        # senao
    ENQUANTO = auto()     # enquanto
    PARA = auto()         # para
    FUNCAO = auto()       # função/def
    RETORNA = auto()      # retorna
    VERDADEIRO = auto()   # Verdadeiro
    FALSO = auto()        # Falso
    NULO = auto()         # Nulo
    ESCREVA = auto()      # escreva
    DEIXE = auto()        # deixe
    
    # Operadores
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
    
    # Literais
    NUMERO = auto()
    TEXTO = auto()
    IDENTIFICADOR = auto()
    
    # Delimitadores
    LPAREN = auto()       # (
    RPAREN = auto()       # )
    LBRACE = auto()       # {
    RBRACE = auto()       # }
    VIRG = auto()         # ,
    DOIS_PONTOS = auto()  # :
    PONTO_VIRG = auto()   # ;
    
    EOF = auto()

class Lexer:
    def __init__(self, codigo, idioma='pt'):
        self.codigo = codigo
        self.idioma = idioma  # 'pt' para Português, 'es' para Espanhol
        self.pos = 0
        self.linha = 1
        self.coluna = 1
        self.tokens = []
        
        # Define palavras-chave para ambos idiomas
        self.palavras_chave = {
            'pt': {
                'se': TipoToken.SE,
                'senao': TipoToken.SENAO,
                'senão': TipoToken.SENAO,
                'enquanto': TipoToken.ENQUANTO,
                'para': TipoToken.PARA,
                'função': TipoToken.FUNCAO,
                'funcao': TipoToken.FUNCAO,
                'retorna': TipoToken.RETORNA,
                'verdadeiro': TipoToken.VERDADEIRO,
                'falso': TipoToken.FALSO,
                'nulo': TipoToken.NULO,
                'escreva': TipoToken.ESCREVA,
                'escreve': TipoToken.ESCREVA,
                'deixe': TipoToken.DEIXE,
            },
            'es': {
                'si': TipoToken.SE,
                'sino': TipoToken.SENAO,
                'mientras': TipoToken.ENQUANTO,
                'para': TipoToken.PARA,
                'función': TipoToken.FUNCAO,
                'funcion': TipoToken.FUNCAO,
                'retorna': TipoToken.RETORNA,
                'verdadero': TipoToken.VERDADEIRO,
                'falso': TipoToken.FALSO,
                'nulo': TipoToken.NULO,
                'escribe': TipoToken.ESCREVA,
                'escriba': TipoToken.ESCREVA,
                'deja': TipoToken.DEIXE,
            }
        }
    
    def tokenizar(self):
        while self.pos < len(self.codigo):
            self._pular_espacos_brancos()
            
            if self.pos >= len(self.codigo):
                break
            
            char = self.codigo[self.pos]
            
            # Tratar comentários
            if char == '#':
                self._pular_comentario()
                continue
            
            # Tratar strings
            if char in ('"', "'"):
                self._ler_string()
            # Tratar números
            elif char.isdigit():
                self._ler_numero()
            # Tratar identificadores e palavras-chave
            elif char.isalpha() or char == '_':
                self._ler_identificador()
            # Tratar operadores e delimitadores
            else:
                self._ler_operador()
    
    def _pular_espacos_brancos(self):
        while self.pos < len(self.codigo) and self.codigo[self.pos].isspace():
            if self.codigo[self.pos] == '\n':
                self.linha += 1
                self.coluna = 1
            else:
                self.coluna += 1
            self.pos += 1
    
    def _pular_comentario(self):
        while self.pos < len(self.codigo) and self.codigo[self.pos] != '\n':
            self.pos += 1
    
    def _ler_string(self):
        aspas = self.codigo[self.pos]
        self.pos += 1
        valor = ""
        
        while self.pos < len(self.codigo) and self.codigo[self.pos] != aspas:
            if self.codigo[self.pos] == '\\':
                self.pos += 1
                if self.pos < len(self.codigo):
                    valor += self.codigo[self.pos]
                    self.pos += 1
            else:
                valor += self.codigo[self.pos]
                self.pos += 1
        
        if self.pos < len(self.codigo):
            self.pos += 1
        
        self.tokens.append({
            'tipo': TipoToken.TEXTO,
            'valor': valor,
            'linha': self.linha,
            'coluna': self.coluna
        })
    
    def _ler_numero(self):
        valor = ""
        while self.pos < len(self.codigo) and (self.codigo[self.pos].isdigit() or self.codigo[self.pos] == '.'): 
            valor += self.codigo[self.pos]
            self.pos += 1
        
        self.tokens.append({
            'tipo': TipoToken.NUMERO,
            'valor': float(valor) if '.' in valor else int(valor),
            'linha': self.linha,
            'coluna': self.coluna
        })
    
    def _ler_identificador(self):
        valor = ""
        while self.pos < len(self.codigo) and (self.codigo[self.pos].isalnum() or self.codigo[self.pos] == '_'):
            valor += self.codigo[self.pos]
            self.pos += 1
        
        palavras = self.palavras_chave[self.idioma]
        tipo = palavras.get(valor.lower(), TipoToken.IDENTIFICADOR)
        
        self.tokens.append({
            'tipo': tipo,
            'valor': valor,
            'linha': self.linha,
            'coluna': self.coluna
        })
    
    def _ler_operador(self):
        char = self.codigo[self.pos]
        proximo = self.codigo[self.pos + 1] if self.pos + 1 < len(self.codigo) else ""
        
        dois_caracteres = char + proximo
        
        if dois_caracteres == "==":
            self.tokens.append({'tipo': TipoToken.IGUAL_IGUAL, 'valor': '==', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 2
        elif dois_caracteres == "!=":
            self.tokens.append({'tipo': TipoToken.DIFERENTE, 'valor': '!=', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 2
        elif dois_caracteres == ">=":
            self.tokens.append({'tipo': TipoToken.MAIOR_IGUAL, 'valor': '>=', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 2
        elif dois_caracteres == "<=":
            self.tokens.append({'tipo': TipoToken.MENOR_IGUAL, 'valor': '<=', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 2
        elif char == '=':
            self.tokens.append({'tipo': TipoToken.IGUAL, 'valor': '=', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '+':
            self.tokens.append({'tipo': TipoToken.MAIS, 'valor': '+', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '-':
            self.tokens.append({'tipo': TipoToken.MENOS, 'valor': '-', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '*':
            self.tokens.append({'tipo': TipoToken.MULT, 'valor': '*', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '/':
            self.tokens.append({'tipo': TipoToken.DIV, 'valor': '/', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '%':
            self.tokens.append({'tipo': TipoToken.MODULO, 'valor': '%', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '>':
            self.tokens.append({'tipo': TipoToken.MAIOR, 'valor': '>', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '<':
            self.tokens.append({'tipo': TipoToken.MENOR, 'valor': '<', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '(': 
            self.tokens.append({'tipo': TipoToken.LPAREN, 'valor': '(', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == ')':
            self.tokens.append({'tipo': TipoToken.RPAREN, 'valor': ')', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '{':
            self.tokens.append({'tipo': TipoToken.LBRACE, 'valor': '{', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == '}':
            self.tokens.append({'tipo': TipoToken.RBRACE, 'valor': '}', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == ',':
            self.tokens.append({'tipo': TipoToken.VIRG, 'valor': ',', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == ':':
            self.tokens.append({'tipo': TipoToken.DOIS_PONTOS, 'valor': ':', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        elif char == ';':
            self.tokens.append({'tipo': TipoToken.PONTO_VIRG, 'valor': ';', 'linha': self.linha, 'coluna': self.coluna})
            self.pos += 1
        else:
            self.pos += 1
        
        self.coluna += 1
    
    def obter_tokens(self):
        self.tokenizar()
        self.tokens.append({'tipo': TipoToken.EOF, 'valor': '', 'linha': self.linha, 'coluna': self.coluna})
        return self.tokens