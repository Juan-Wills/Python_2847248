import sys
# import rich
from views.view_libros import gestion_libros

def main():
    try:
        while True:
            print("""
                Sistema Gestor de Bibliotecas
        1. Libros
        2. Usuarios
        3. Prestamos y Devoluciones
        4. Multas

        0. Salir del Programa
            """)  # rich
            menu_option= input("Ingresar respuesta: ")

            match menu_option:
                case '0':
                    sys.exit('Gracias por utilizar nuestros servicios!')
                case '1':
                    gestion_libros()
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case _:
                    print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')
    except (KeyboardInterrupt, EOFError):
        print('\nPrograma cerrado forzosamente')

if __name__=='__main__':
    main()