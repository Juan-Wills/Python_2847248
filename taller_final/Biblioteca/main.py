import sys
from views.view_libros import gestion_libros
from views.view_usuarios import gestion_usuarios
from views.view_prestamos import gestion_prestamos
from views.view_multas import gestion_multas


def main():
    try:
        while True:
            print(
                (
                    "\n   Sistema Gestor para Bibliotecas\n\n"
                    "1. Libros\n"
                    "2. Usuarios\n"
                    "3. Prestamos y Devoluciones\n"
                    "4. Multas\n\n"
                    "0. Salir del Programa\n"
                )
            )
            menu_option = input("Ingresar respuesta: ")

            match menu_option:
                case "0":
                    sys.exit("Gracias por utilizar nuestros servicios!")
                case "1":
                    gestion_libros()
                case "2":
                    gestion_usuarios()
                case "3":
                    gestion_prestamos()
                case "4":
                    gestion_multas()
                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma cerrado forzosamente")


if __name__ == "__main__":
    main()
