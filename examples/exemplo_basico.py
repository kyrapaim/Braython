# Example using the Braython compiler

import sys
from pathlib import Path

# Add src directory to path to import braython package
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from braython import Compiler

# Portuguese code to be compiled
codigo_portugues = '''
escreva("Olá, Mundo!")

deixe x = 10

deixe y = x + 5
deixe z = x * 2

se y > z:
    escreva("y é maior que z")
senao:
    escreva("z é maior ou igual a y")
'''

# Compile and run the code
compiler = Compiler()
print("=== Executando código em Português ===")
compiler.compile_and_run(codigo_portugues, 'pt')