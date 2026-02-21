# Example using the Braython compiler

from compiler import Compiler

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