
def suma(num1, num2): 
    """"
    Metodo que recibe dos numero y retorna la suma de ellos 
    """
    return num1+num2


def multiplicacion(num1, num2):
    return num1*num2


def division(num1, num2):
    if(num2 != 0):
        return num1/num2
    else:
        print("Error de división, el denominador no puede ser 0")


def guardar_resultado(tipo_operacion, num1, num2, resultado):

    try:
        with open("resultados_matematica.txt", "r") as archivo:
            mensaje = archivo.read()

            nuevo_mensaje = mensaje + "\n" "la " + tipo_operacion + " de " + str(num1) + " con " + str(num2) + " es " + str(resultado)    
            
            with open("resultados_matematica.txt", "w") as archivo2:
                archivo2.write(nuevo_mensaje)
            
    except:
        with open("resultados_matematica.txt", "w") as archivo:
            mensaje = "la " + tipo_operacion + " de " + str(num1) + " con " + str(num2) + " es " + str(resultado)
            archivo.write(mensaje)

