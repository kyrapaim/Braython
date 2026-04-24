"""
Braython - A Portuguese/Spanish to Python Compiler

This package provides tools to write programs in Portuguese or Spanish
and automatically compile them to Python.

Main Components:
- Lexer: Tokenizes Portuguese/Spanish source code
- Parser: Builds abstract syntax trees (placeholder for future use)
- Compiler: Orchestrates the lexer and translator to convert to Python
- Messages: Provides localized error messages and translations
"""

from .compiler import Compiler
from .lexer import Lexer, TipoToken
from .parser import ASTParser

__all__ = ['Compiler', 'Lexer', 'TipoToken', 'ASTParser']
__version__ = '1.0.0'
