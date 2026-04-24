#!/usr/bin/env python3
"""
Simple runner script for Braython examples.
Use this to easily run different examples without editing files.
"""

import sys
from pathlib import Path

# Add src directory to path to import braython package
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from braython import Compiler

def run_basic_example():
    """Run the basic example: variables and conditionals"""
    codigo = '''
escreva("Olá, Mundo!")

deixe x = 10
deixe y = x + 5
deixe z = x * 2

se y > z:
    escreva("y é maior que z")
senao:
    escreva("z é maior ou igual a y")
'''
    print("=== Exemplo Básico ===\n")
    Compiler().compile_and_run(codigo, 'pt')

def run_advanced_example():
    """Run advanced example: functions and loops"""
    codigo = '''
funcao soma(a, b):
    retorna a + b

deixe resultado = soma(3, 4)
escreva("Soma:", resultado)

deixe total = 0
para i em alcance(1, 5):
    deixe total = total + i

se total > 10:
    escreva("Total maior que 10")
senao:
    escreva("Total:", total)
'''
    print("=== Exemplo Avançado ===\n")
    Compiler().compile_and_run(codigo, 'pt')

def run_custom_code():
    """Allow user to input custom Portuguese code"""
    print("=== Código Customizado ===")
    print("Digite seu código em Português (termine com uma linha vazia):\n")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    
    codigo = '\n'.join(lines)
    if codigo.strip():
        Compiler().compile_and_run(codigo, 'pt')
    else:
        print("Nenhum código fornecido.")

def main():
    print("Braython - Compilador Português → Python\n")
    print("Opções:")
    print("1 - Exemplo Básico")
    print("2 - Exemplo Avançado")
    print("3 - Código Customizado")
    print("0 - Sair\n")
    
    choice = input("Escolha uma opção (0-3): ").strip()
    
    if choice == '1':
        run_basic_example()
    elif choice == '2':
        run_advanced_example()
    elif choice == '3':
        run_custom_code()
    elif choice == '0':
        print("Até logo!")
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
