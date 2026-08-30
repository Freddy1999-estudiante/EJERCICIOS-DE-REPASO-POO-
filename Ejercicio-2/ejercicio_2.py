# EJERCICIO 2 - CONTAR PALABRAS
# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# Una cadena de texto.
# PROCESO:
# Convertir el texto a minusculas, eliminar los signos de
# puntuacion basicos, separar las palabras y contar sus apariciones.
# SALIDA:
# Un diccionario con cada palabra y su cantidad de apariciones.
# Ejemplo de entrada:
# "Python es genial. Python es potente. Python es simple."
# Salida esperada:
# {"python": 3, "es": 3, "genial": 1, "potente": 1, "simple": 1}
# 2. BOSQUEJO A MANO
# texto = "Python es genial. Python es potente. Python es simple."
# Primero convertir todo a minusculas.
# Luego eliminar los signos de puntuacion.
# Separar el texto en palabras.
# Un solo recorrido:
#   si la palabra no existe, iniciar su cantidad en 1
#   si ya existe, aumentar su cantidad en 1
# Al final retorno el diccionario con las frecuencias.
# 3. PATRON
# Usar un diccionario para almacenar las frecuencias.
# Recorrer las palabras una sola vez.
# Utilizar get() para obtener la cantidad actual de cada palabra
# y aumentar en 1.
# 4. CODIGO

def contar_unicas(texto):
    # Normalizamos
    texto = texto.lower()
    for signo in ".,;:!?\"'()":
        texto = texto.replace(signo, "")
    # Contamos con dict
    frecuencias = {}
    for palabra in texto.split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias
# Uso
texto = "Python es genial. Python es potente. Python es simple."
r = contar_unicas(texto)
for palabra, cant in r.items():
    print(f"{palabra}: {cant}")
# 5. PRUEBA PASO A PASO
# Entrada:
# Python es genial. Python es potente. Python es simple.
# Paso 1: Convertimos todo a minusculas.
# python es genial. python es potente. python es simple.
# Paso 2: Eliminamos los signos de puntuacion.
# python es genial python es potente python es simple
# Paso 3: Separamos las palabras.
# python, es, genial, python, es, potente, python, es, simple
# Paso 4: Contamos las apariciones.
# python -> 3
# es -> 3
# genial -> 1
# potente -> 1
# simple -> 1
# Resultado final:
# {"python": 3, "es": 3, "genial": 1, "potente": 1, "simple": 1}
