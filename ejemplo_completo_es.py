# ejemplo_completo_es.py
# Ejemplo completo de Braython en Español.
# Ejecutar con: python compiler.py ejemplo_completo_es.py
#
# Uso mediante API:
#   from compiler import Compiler
#   c = Compiler()
#   c.compile_and_run(open('ejemplo_completo_es.py').read(), 'es')

# ---------- importaciones ----------
de os importar path

# ---------- variables básicas ----------
nombre = "Braython"
version = 1
activo = verdadero
ninguno = nulo

# ---------- salida ----------
escribe("Bienvenido a", nombre, "versión", version)

# ---------- condicional ----------
si version > 0:
    escribe("Versión válida")
sino:
    escribe("Versión inválida")

# ---------- bucle mientras ----------
contador = 0
mientras contador < 3:
    escribe("contador:", contador)
    contador = contador + 1

# ---------- bucle para ----------
para i en rango(5):
    si i == 2:
        continua
    si i == 4:
        rompe
    escribe("i =", i)

# ---------- función ----------
función saludo(persona):
    retorna "¡Hola, " + persona + "!"

escribe(saludo("Mundo"))

# ---------- operadores lógicos ----------
x = 10
z = 20
si x < z y x > 0:
    escribe("x está entre 0 y z")

si x == 5 o z == 20:
    escribe("al menos una condición es verdadera")

si no activo == falso:
    escribe("activo está definido correctamente")

# ---------- clase ----------
clase Animal:
    función __init__(self, nombre_animal):
        self.nombre_animal = nombre_animal

    función hablar(self):
        retorna self.nombre_animal + " hace algún sonido"

perro = Animal("Rex")
escribe(perro.hablar())

# ---------- manejo de excepciones ----------
intenta:
    resultado = 10 / 0
excepto ZeroDivisionError:
    escribe("Error: ¡división por cero!")
finalmente:
    escribe("Bloque finalmente ejecutado")

# ---------- gestor de contexto ----------
# con open("archivo.txt", "w") como f:
#     f.write("prueba")

# ---------- built-ins ----------
numeros = lista(rango(1, 6))
escribe("Lista:", numeros)
escribe("Tamaño:", tamaño(numeros))
escribe("Tipo:", tipo(numeros))

texto_num = "42"
escribe("Entero:", entero(texto_num))
escribe("Flotante:", flotante("3.14"))

# ---------- lambda ----------
doblar = lambda n: n * 2
escribe("Doble de 7:", doblar(7))

# ---------- pass (pasa) ----------
clase Base:
    pasa

# ---------- verificación de identidad ----------
a = nulo
si a es nulo:
    escribe("a es nulo")

# ---------- diccionario y conjunto ----------
datos = diccionario()
datos["clave"] = "valor"
escribe("Diccionario:", datos)

unicos = conjunto([1, 2, 2, 3])
escribe("Conjunto:", unicos)
