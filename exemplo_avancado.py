from compiler import Compiler

codigo_portugues = '''
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

print("=== Executando exemplo_avancado.py ===")
Compiler().compile_and_run(codigo_portugues, 'pt')
