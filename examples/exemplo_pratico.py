import sys
from pathlib import Path

# Add src directory to path to import braython package
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from braython import Compiler

# Practical example: Simple grade calculator
codigo_portugues = '''
funcao media(nota1, nota2, nota3):
    deixe soma = nota1 + nota2 + nota3
    retorna soma / 3

escreva("=== Calculadora de Notas ===")

deixe nota1 = 8
deixe nota2 = 9
deixe nota3 = 7

deixe media_final = media(nota1, nota2, nota3)

se media_final >= 7:
    escreva("Aprovado!")
senao:
    escreva("Reprovado!")

escreva("Média: " + str(media_final))
'''

print("=== Exemplo Prático: Calculadora de Notas ===\n")
Compiler().compile_and_run(codigo_portugues, 'pt')
