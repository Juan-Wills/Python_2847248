"""
PERSISTENCIA DE DATOS:
Guardar información para que no se borre cuando apagamos el/la PC, para esto
hacemos uso de los métodos de Python para lectura y escritura de datos.

En este caso hacemos uso del método open(), el cual devuelve el archivo solicitado
como un objeto con propiedades de lectura y escritura. Ej:

f = open('archivo_de_trabajo', 'modo', encoding='utf-8')

El primer argumento es el archivo de trabajo con su respectiva extension y localización, el segundo 
argumento es el modo de trabajo (lectura, escritura, ambos) y el tercer argumento
es la codificación a usar con el archivo final.

Modos de trabajo:
1. Lectura:                 'r'
2. Lectura y escritura:     'r+'
3. Escritura:               'w'
4. Escritura y lectura:     'w+'
5. Concatenación (Append):  'a'
6. Concatenación y lectura: 'a+'
7. Modo binario:            'b'

"""


# Ejemplo 1:
# Escritura de datos:
# nombres = ["Juan", "Sonia", "Pedro", "Camila"]


# # archivo = open("nombres.txt", 'w', encoding='utf-8')
# archivo = open("nombres.txt", 'a')
# # mensaje = "Los nombres en lista son:\n" + nombres[0] + "\n" + nombres[1] + "\n" + nombres[2] + "\n" + nombres[3]
# mensaje = "\n" + "Daniel"
# archivo.write(mensaje)
# archivo.close()

# # Lectura de datos:
# archivo = open("nombres.txt", 'r')
# mensaje_leido = archivo.read()
# archivo.close()
# print(mensaje_leido)


# Ejemplo 2:
# nombres = ['Oscar', 'Andres', 'Milena']
# # Escritura de datos:
# with open("persistencia_datos/nombres.csv", 'w') as archivo2:
#     for nombre in nombres:
#         mensaje = "Hola, " + nombre + " . Bienvenido a Python\n"
#         archivo2.write(mensaje)


# # Lectura de datos:
# with open("persistencia_datos/nombres.csv", 'r') as archivo3:
#     datos = archivo3.read()
#     print(datos)

# print(type(datos))

# with open("persistencia_datos/nombres.csv", 'a') as file:
#     file.write("Es es un nuevo mensaje")

# """
# Métodos de escritura:
# 1. write():         Escribe en una sola línea la infromación indicada.
# 2. writelines():    Escribe la información en líneas independientes mientras estén separadas por '\n'

# Métodos de lectura:
# 1. read():      Lee la infromación del archivo en una sola instruccón (línea de trabajo)
# 2. readline():  Lee un número determinado de líneas y no todo el archivo a la vez. Cada vez que
#                 se llama a la función readline() se lee una línea de información diferente.
# 3. readlines(): Devuelve una lista donde cada elemento es una línea de información del archivo leído.

# """

# # Ejemplo 3:
# frutas = ["manzana\n", "pera\n", "mango\n", "banano\n"]
# with open('ejemplo.txt', 'w+', encoding='utf-8') as archivo:
#     archivo.writelines(frutas)


# with open('ejemplo.txt', 'r') as archivo:
#     linea = archivo.readline()
#     while linea != '':
#         print(linea, end='')
#         linea = archivo.readline()



# # Ejemplo 4:
mascotas = [
    {
        'nombre': 'copito',
        'tipo': 'gato',
        'raza': 'N/A',
        'edad': 6
    },
    {
        'nombre': 'Toby',
        'tipo': 'perro',
        'raza': 'pomerania',
        'edad': 18
    },
    {
        'nombre': 'Diomedez',
        'tipo': 'loro',
        'raza': 'N/A',
        'edad': 20
    },
    {
        'nombre': 'Juanita',
        'tipo': 'conejo',
        'raza': 'N/A',
        'edad': 24
    },
]

def leer_db():
    with open("persistencia_datos/mascotas.txt", 'r') as file:
        datos = file.read()
    
    return datos

def actualizar_db(mensage_inicial, ruta, mascotas):
    i = 1
    with open(ruta, 'w') as file:
        file.write(mensage_inicial)

        for mascota in mascotas:
            nombre = mascota['nombre']
            tipo = mascota['tipo']
            edad = str(mascota['edad'])
            raza = mascota['raza']

            file.write(f"mascota No: {i}\n")
            
            mensaje_temp = "\tnombre mascota: " + nombre + "\n" + "\ttipo mascota: " + tipo + "\n" + "\tedad mascota: " + edad + "\n" + "\traza mascota: " + raza + "\n"

            file.write(mensaje_temp)
            i += 1


mensage_inicial = "Base de datos para mascotas\n"
try:
    with open("persistencia_datos/mascotas.txt", 'r') as file:
        info_mascotas = file.read()
except:
    actualizar_db(mensage_inicial, 'persistencia_datos/mascotas.txt', mascotas)

while True:
    print("Clínica de mascotas ADSO")
    print("Seleccione la opoción que desea: ")
    print("1. Mostrar DB de mascotas")
    print("2. Ingresar una nueva mascota")
    print("3. Salir")
    opt = int(input("Opción = "))

    if opt == 1:
        datos = leer_db()
        print(datos)
    elif opt == 2:
        nombre = input('nombre: ')
        tipo = input('tipo: ')
        edad = input('edad: ')
        raza = input('raza: ')
        
        mascota_temp = {
            'nombre': nombre,
            'tipo': tipo,
            'edad': edad,
            'raza': raza
        }
        mascotas.append(mascota_temp)
        actualizar_db(mensage_inicial, 'persistencia_datos/mascotas.txt', mascotas)
        
    elif opt == 3:
        False
        break    
