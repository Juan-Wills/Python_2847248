nombre = input("Ingrese un nombre: ")

nombres_txt = open('nuevos_nombres.txt', mode='a+')
mensaje = nombre + " "
nombres_txt.write(mensaje)
nombres_txt.close()

lectura_archivo = open('nuevos_nombres.txt', 'r')
variable_1 = lectura_archivo.read()
lectura_archivo.close()

print(variable_1)