# EJERCICIO 4 - ELIMINAR DUPLICADOS
# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# Una lista que puede contener elementos repetidos.
# PROCESO:
# Recorrer la lista y conservar solamente la primera aparicion
# de cada elemento.
# Se utiliza un set para comprobar si el elemento ya fue visto
# y una lista para conservar el orden.
# SALIDA:
# Una lista nueva sin duplicados, conservando el orden de
# la primera aparicion.
# Ejemplo de entrada:
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Salida esperada:
# [3, 1, 4, 5, 9, 2, 6]
# 2. BOSQUEJO A MANO
# lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Crear:
#   visto = set()
#   resultado = []
# Un solo recorrido:
#   si x no esta en visto:
#     agregar x a visto
#     agregar x a resultado
# Si x ya esta en visto:
#   no agregarlo.
# Al final retornar resultado.
# 3. PATRON
# Utilizar un set para comprobar rapidamente si un elemento
# ya fue visto y una lista para conservar el orden original.
# El set permite realizar el chequeo de pertenencia de manera
# eficiente.
# 4. CODIGO
def sin_duplicados(lista):
    visto = set()
    resultado = []

    for x in lista:
        if x not in visto:
            visto.add(x)
            resultado.append(x)

    return resultado
# Alternativa (Python 3.7+): dict.fromkeys mantiene orden
def sin_duplicados_v2(lista):
    return list(dict.fromkeys(lista))
# Uso
print(sin_duplicados([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))
# 5. PRUEBA PASO A PASO
# Entrada:
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Inicio:
# visto = set()
# resultado = []
# Paso 1: x = 3
# 3 no esta en visto.
# visto = {3}
# resultado = [3]
# Paso 2: x = 1
# 1 no esta en visto.
# visto = {3, 1}
# resultado = [3, 1]
# Paso 3: x = 4
# 4 no esta en visto.
# resultado = [3, 1, 4]
# Paso 4: x = 1
# 1 ya esta en visto.
# No se agrega.
# Paso 5: x = 5
# 5 no esta en visto.
# resultado = [3, 1, 4, 5]
# Paso 6: x = 9
# 9 no esta en visto.
# resultado = [3, 1, 4, 5, 9]
# Paso 7: x = 2
# 2 no esta en visto.
# resultado = [3, 1, 4, 5, 9, 2]
# Paso 8: x = 6
# 6 no esta en visto.
# resultado = [3, 1, 4, 5, 9, 2, 6]
# Paso 9: x = 5
# 5 ya esta en visto.
# No se agrega.
# Paso 10: x = 3
# 3 ya esta en visto.
# No se agrega.
# Resultado final:
# [3, 1, 4, 5, 9, 2, 6]
