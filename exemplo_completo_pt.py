# exemplo_completo_pt.py
# Exemplo completo de Braython em Português.
# Execute com: python compiler.py exemplo_completo_pt.py
#
# Uso via API:
#   from compiler import Compiler
#   c = Compiler()
#   c.compile_and_run(open('exemplo_completo_pt.py').read(), 'pt')

# ---------- importações ----------
de os importar path

# ---------- variáveis básicas ----------
nome = "Braython"
versao = 1
ativo = verdadeiro
nenhum = nulo

# ---------- saída ----------
escreva("Bem-vindo ao", nome, "versão", versao)

# ---------- condicional ----------
se versao > 0:
    escreva("Versão válida")
senão:
    escreva("Versão inválida")

# ---------- laço enquanto ----------
contador = 0
enquanto contador < 3:
    escreva("contador:", contador)
    contador = contador + 1

# ---------- laço para ----------
para i em intervalo(5):
    se i == 2:
        continua
    se i == 4:
        quebra
    escreva("i =", i)

# ---------- função ----------
função saudacao(pessoa):
    retorna "Olá, " + pessoa + "!"

escreva(saudacao("Mundo"))

# ---------- operadores lógicos ----------
x = 10
y = 20
se x < y e x > 0:
    escreva("x está entre 0 e y")

se x == 5 ou y == 20:
    escreva("pelo menos uma condição é verdadeira")

se não ativo == falso:
    escreva("ativo está definido corretamente")

# ---------- classe ----------
classe Animal:
    função __init__(self, nome_animal):
        self.nome_animal = nome_animal

    função falar(self):
        retorna self.nome_animal + " faz algum som"

cachorro = Animal("Rex")
escreva(cachorro.falar())

# ---------- tratamento de exceções ----------
tente:
    resultado = 10 / 0
exceto ZeroDivisionError:
    escreva("Erro: divisão por zero!")
finalmente:
    escreva("Bloco finalmente executado")

# ---------- gerenciador de contexto ----------
# com open("arquivo.txt", "w") como f:
#     f.write("teste")

# ---------- built-ins ----------
numeros = lista(intervalo(1, 6))
escreva("Lista:", numeros)
escreva("Tamanho:", tamanho(numeros))
escreva("Tipo:", tipo(numeros))

texto_num = "42"
escreva("Inteiro:", inteiro(texto_num))
escreva("Decimal:", decimal("3.14"))

# ---------- lambda ----------
dobrar = lambda n: n * 2
escreva("Dobro de 7:", dobrar(7))

# ---------- pass (passe) ----------
classe Base:
    passe

# ---------- verificação de identidade ----------
a = nulo
se a é nulo:
    escreva("a é nulo")

# ---------- dicionário e conjunto ----------
dados = dicionario()
dados["chave"] = "valor"
escreva("Dicionário:", dados)

unicos = conjunto([1, 2, 2, 3])
escreva("Conjunto:", unicos)
