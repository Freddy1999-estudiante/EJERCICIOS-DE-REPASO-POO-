# EJERCICIO 5 - DISPATCH TABLE
# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# Un operador (+, -, * o /) y dos numeros.
# PROCESO:
# Utilizar un diccionario donde cada operador sea una clave
# y la funcion que realiza la operacion sea su valor.
# De esta manera se evita utilizar una cascada de if/elif.
# SALIDA:
# El resultado de la operacion seleccionada.
# Ejemplo de entrada:
# op = "+"
# a = 8
# b = 3
# Salida esperada:
# 11
# 2. BOSQUEJO
# Crear un diccionario de operaciones:
#   "+" → suma
#   "-" → resta
#   "*" → multiplicacion
#   "/" → division
# Pedir al usuario la operacion.
# Si escribe "q":
#   salir del programa.
# Si el operador no existe:
#   mostrar operador invalido.
# Pedir los valores de a y b.
# Buscar la operacion en el diccionario
# y ejecutarla con a y b.
# Mostrar el resultado.
# 3. PATRON
# Dispatch Table:
# utilizar un diccionario para relacionar cada opcion
# con la funcion que debe ejecutarse.
# De esta manera se evita una cascada de if/elif.
# Cada clave representa una operacion y su valor
# representa la funcion que la implementa.
# 4. CODIGO
def calculadora():
    operaciones = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else None,
    }

    while True:
        op = input("Operador (+ - * / o q para salir): ")
        if op == "q":
            break
        if op not in operaciones:
            print("Operador inválido")
            continue

        a = float(input("a: "))
        b = float(input("b: "))
        r = operaciones[op](a, b)
        print(f"Resultado: {r}")
# Uso
# calculadora()
# 5. PRUEBA PASO A PASO
# Entrada:
# op = "+"
# a = 8
# b = 3
# Paso 1:
# El usuario ingresa el operador "+".
# Paso 2:
# Se busca "+" dentro del diccionario operaciones.
# Paso 3:
# "+" corresponde a:
# lambda a, b: a + b
# Paso 4:
# Se ingresan los valores:
# a = 8
# b = 3
# Paso 5:
# Se ejecuta:
# operaciones["+"](8, 3)
# Paso 6:
# Se realiza:
# 8 + 3 = 11
# Resultado final:
# 11
# Prueba adicional:
# Si el usuario ingresa "q", el programa termina.
# Si ingresa un operador que no existe,
# muestra "Operador inválido".
# Si se intenta dividir para cero, el resultado es None.
