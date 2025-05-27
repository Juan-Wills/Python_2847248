# Crea una función que reciba tres parámetros: nombre (string), edad (entero) y salario (float).
# La función debe retornar un diccionario con esta información y calcular el salario anual.

def main():
    nombre= input("Ingresar nombre completo: ")
    edad= int(input("Ingresar edad: "))
    salario= float(input("Ingresar salario mensual: "))
    informacion= crear_perfil_empleado(nombre, edad, salario)
    print(informacion)

def crear_perfil_empleado(n, e, sm):
    return {'Nombre': n, 'Edad': e, 'Salario': f'{sm:,.2f}', 'Salario anual': f'{sm*12:,.2f}'}

if __name__== '__main__':
    main()