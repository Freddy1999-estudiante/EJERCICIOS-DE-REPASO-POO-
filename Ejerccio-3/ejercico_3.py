# EJERCICIO 3 - GUARDAR Y CARGAR CONFIGURACION
# 1. ENTENDER EL PROBLEMA
# ENTRADA:
# Un archivo de configuracion llamado "config.json".
# Tambien se utilizan datos en forma de diccionario.
# PROCESO:
# Cargar la configuracion desde un archivo JSON.
# Si el archivo no existe, retornar un diccionario vacio.
# Luego agregar o modificar los datos de configuracion
# y guardar nuevamente el diccionario en el archivo.
# SALIDA:
# Un archivo JSON con la configuracion guardada.
# Ejemplo de entrada:
# cargar_config("config.json")
# Salida esperada:
# {'tema': 'oscuro', 'idioma': 'es'}
# 2. BOSQUEJO A MANO
# archivo = "config.json"
# Cargar:
#   comprobar si el archivo existe
#   si no existe, retornar {}
#   si existe, abrirlo y leer el JSON
#
# Modificar:
#   agregar tema = "oscuro"
#   agregar idioma = "es"
# Guardar:
#   abrir el archivo en modo escritura
#   guardar el diccionario como JSON
# Al final se obtiene la configuracion guardada.
# 3. PATRON
# Persistencia de datos utilizando archivos JSON.
# Se utiliza:
#   - os.path.exists() para comprobar si existe el archivo.
#   - json.load() para leer el archivo.
#   - json.dump() para guardar el diccionario.
# Se utiliza un diccionario para almacenar la configuracion.
# 4. CODIGO

import json
import os

def guardar_config(datos, archivo):
    with open(archivo, "w") as f:
        json.dump(datos, f, indent=2)

def cargar_config(archivo):
    if not os.path.exists(archivo):
        return {}
    with open(archivo) as f:
        return json.load(f)
# Uso
config = cargar_config("config.json")
config["tema"] = "oscuro"
config["idioma"] = "es"
guardar_config(config, "config.json")

# 5. PRUEBA PASO A PASO
# Paso 1:
# Se ejecuta cargar_config("config.json").
# Paso 2:
# Se comprueba si "config.json" existe.
# Paso 3:
# Si no existe, la funcion retorna {}.
# Paso 4:
# Se agregan los datos:
# config["tema"] = "oscuro"
# config["idioma"] = "es"
# Paso 5:
# Se ejecuta guardar_config(config, "config.json").
# Paso 6:
# El diccionario se guarda en el archivo JSON.
# Resultado esperado:
# {
#   "tema": "oscuro",
#   "idioma": "es"
# }
#
# Si el archivo ya existe y contiene la configuracion,
# cargar_config() recupera esos datos antes de modificarlos.
