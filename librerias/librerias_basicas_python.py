import os, json, math


# Obtenemos la ruta actual del directorio de trabajo:
ruta = os.getcwd()
print(f"Mi ruta actual de trabajo es: {ruta}")

# Crear una nueva carpeta en el directorio actual de trabajo:
ruta_carpeta = "C:\Users\airs8\Desktop"
os.system("mkdir " + ruta_carpeta + "\severa_carpeta")

# # # Guardamos un archivo en la nueva carpeta que creamos:
# with open("nueva_carpeta_2/rutas_PC.txt", "w+") as archivo:
#     archivo.write(ruta)

# ***********************************
# datos_cliente = {
#     'id': 101,
#     'nombre': "Juan",
#     'apellido': "Alvarez",
#     'correo': "ja@correo.com"
# }

# with open("nueva_carpeta_2/clientes.json", "w") as archivo:
#     json.dump(datos_cliente, archivo)

# with open("nueva_carpeta_2/clientes.json", "r+") as archivo2:
#     lectura_json = json.load(archivo2)

# print("contenido del archivo clientes.json:")
# print(lectura_json)