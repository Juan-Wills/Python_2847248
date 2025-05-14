import mis_librerias.matematica as operaciones

numero_1 = int(input("Ingrese el número 1: "))
numero_2 = int(input("Ingrese el número 2: "))

suma = operaciones.suma(numero_1, numero_2)
print(f"la suma de {numero_1} con {numero_2} es igual a {suma}")

producto = operaciones.multiplicacion(numero_1, numero_2)
print(f"la multiplicación de {numero_1} con {numero_2} es igual a {producto}")

