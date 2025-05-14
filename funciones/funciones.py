# Funciones:
# Bloque de código que puede ser reutilizable
# Características:
# 1. Recibe parámetros (que pueden ser de acuerdo al objetivo de la función)
# 2. Pueden tener un retorno

# En Python la estructura de una función es:
def nombre_de_la_funcion(parametros):
    pass

# Ejemplo:
def saludar(parametro1: str) -> str:
    print(f"\nHola {nombre}, esto es un saludo de función\n")

nombre = "Juana"
saludar(nombre)

# Ejemplo 2:
frutas = ["najanas", "peras", "moras", 2, 10, 50]

def imprimir_frutas(lista_frutas):
    i=3
    for fruta in lista_frutas:
        print(f"\nFruta: {fruta}, cantidad: {lista_frutas[i]}")
        i+=1
        if(i==6):
            break

imprimir_frutas(frutas)


# # Ejemplo 3:
# def contar_vocales(texto):
#     """
#     Función para contar vocales de una palabra
#     """
#     vocales = 0
#     for caracter in texto:
#         if(caracter in "aeiou"):
#             vocales += 1

#     return vocales


# palabra = input("Introducir una palabra: ")
# numero_vocales = contar_vocales(palabra)

# print("El número de vocales en {} es {}".format(palabra, numero_vocales))


# Ejercicio:
# Generar un función que determine los números primos
# de una lista aleatoria de datos
# Guardar el resultado utilizando una función para guardar
# información que ustedes hayan creado.

def numeros_primos(numeros):

    nums_primos = []
    for num in numeros:
        cont = 0
        for i in range(1, num+1):
            if(num%i == 0):
                cont+=1                
        
        if(cont == 2):
            nums_primos.append(num)

    return nums_primos


lista_numeros = [12, 45, 2, 1, 89, 90, 35]
primos = numeros_primos(lista_numeros)
print("*"*64)
print(f"Lista original = {lista_numeros}")
print(f"Números primos = {primos}")


# Funciones de múltiple retorno:
def pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if(n%2 == 0):
            pares.append(n)
        else:
            impares.append(n)
    
    return pares, impares

lista_numeros = [12, 45, 2, 1, 89, 90, 35]
nums_pares, nums_impares = pares_impares(lista_numeros)

print("*"*64)
print(f"Lista de números = {lista_numeros}")
print(f"Numeros pares = {nums_pares}")
print(f"Numeros impares = {nums_impares}")

# Paso de parámetros por posción:
def suma(num1: int, num2: float, texto: str) -> float:
    """
    Función que recibe dos número y los suma.

    Args:
        num1 (int): Número entero
        num2 (float): Número decimal
        texto (str): Aviso de función

    Returns:
        float: Resultado de la suma.
    """
    result = num1 + num2
    print(f"Estoy escribiendo {texto} desde la función")
    
    return result

print("\n")
x = suma(20, 10, "HOLA")
print(f"El resultado de la suma x es = {x}")

# Paso de parámetros por referencia:
y = suma(texto="HOLA", num1=20, num2=10)
print(f"El resultado de la suma y es = {y}")

# Función como argumento de otra función:

def squares(number_list):
    square_numbers = [x*x for x in number_list]
    
    return square_numbers

def calculate(func, num):
    x = func(num)
    
    return x

n = [2, 10, 15, 287]
square_numbers = calculate(squares, n)
print(f"El cuadrado de {n} es = {square_numbers}")

# Función que agrupa funciones:
def operaciones_matematicas():
    
    # Métodos de la función:
    def sumar(num1, num2, num3):
        return num1 + num2 + num3

    def restar(num1, num2):
        return num1 - num2
    
    def multiplicar(num1, num2, num3):
        return num1 * num2 * num3
    

x = 40
y = 10
z = 2 

suma_nums = operaciones_matematicas.sumar(x, y, z)
