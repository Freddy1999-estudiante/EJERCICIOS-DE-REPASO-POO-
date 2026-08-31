
# EJERCICIO 1 - ESTADISTICAS DE UNA LISTA
# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# Una lista de enteros.
# PROCESO:
# Recorrer una vez, acumular varios contadores y retornar un dict.
# SALIDA:
# Un diccionario con las estadisticas.
# Ejemplo de entrada:
# [8, 5, 12, 7, 3, 10]
# Salida esperada:
# {"total": 45, "promedio": 7.5, "max": 12, "min": 3, "pares": 3}

# 2. BOSQUEJO 
# nums = [8, 5, 12, 7, 3, 10]
# Un solo recorrido:
#   suma acumula: 8, 13, 25, 32, 35, 45
#   maximo se actualiza si es mayor
#   minimo se actualiza si es menor
#   pares: incrementa contador si n % 2 == 0
#
# Al final construyo el diccionario con los 5 valores.
# 3. PATRON
# Recorrido unico de una lista utilizando:
# un acumulador para la suma,
# una variable para el maximo,
# una variable para el minimo
# y un contador para los numeros pares.


# 4. CODIGO

def estadisticas(numeros):
    if not numeros:
        return {
            "total": 0,
            "promedio": 0,
            "max": None,
            "min": None,
            "pares": 0
        }

    total = 0
    maximo = numeros[0]
    minimo = numeros[0]
    pares = 0

    for n in numeros:
        total += n

        if n > maximo:
            maximo = n

        if n < minimo:
            minimo = n

        if n % 2 == 0:
            pares += 1

    return {
        "total": total,
        "promedio": total / len(numeros),
        "max": maximo,
        "min": minimo,
        "pares": pares
    }
# 5. PRUEBA
# Entrada:
# [8, 5, 12, 7, 3, 10]
# Paso 1: n = 8
# total = 8
# maximo = 8
# minimo = 8
# pares = 1
# Paso 2: n = 5
# total = 13
# maximo = 8
# minimo = 5
# pares = 1
# Paso 3: n = 12
# total = 25
# maximo = 12
# minimo = 5
# pares = 2
# Paso 4: n = 7
# total = 32
# maximo = 12
# minimo = 5
# pares = 2
# Paso 5: n = 3
# total = 35
# maximo = 12
# minimo = 3
# pares = 2
# Paso 6: n = 10
# total = 45
# maximo = 12
# minimo = 3
# pares = 3
# Resultado final:
# {"total": 45, "promedio": 7.5, "max": 12, "min": 3, "pares": 3}
# USO
#r = estadisticas([8, 5, 12, 7, 3, 10])
#print(r)
#print(f"Promedio: {r['promedio']:.2f}")
