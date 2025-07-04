from services import biblioteca_service as bs
from models.libro import Libro
import re
import datetime

def valid_input(input):
    if not re.fullmatch(r'[a-zA-Z0-9\s]+', input):
        print('Error: El valor ingresado es invalido, por favor evitar caracteres speciales como #$%@')
        return
    return True

def gestion_libros():
    print("""
    Gestionar libros:
        1. Buscar por categoria
        2. Ingresar nuevo libro
        3. Actualizar
        4. Eliminar
          
        0. Volver
    """)

    option= input('Ingresar opcion: ')
    filter_options= ['titulo', 'autor', 'genero', 'editorial', 'fecha_publicacion']

    match option:
        case '0':
            return
        
        case '1':
            while True:
                print("Filtrar libros")
                print('\nElegir categoria: ')
                print('1. Titulo\t2. Autor\t3. Genero\t4. Editorial\t5. Fecha')
                option= input('Ingresar opcion: ')
                index_option= filter_options[int(option)-1]
                if 1 > int(option) > 5:
                    print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')
                else:
                    print(f"\nHa elegido la categoria {(index_option if int(option)-1 != 4 else index_option.replace('_', ' de ')).capitalize()}.\n")
                    
                    if bs.find_book(index_option, input("Filtro: ").title()):
                        break

        case '2':
            print("Agregar nuevo libro")
            print("\nIngrese los datos del libro:")
            # Validacion de los input del usuario
            while True:
                titulo= input('Titulo: ').title()
                if valid_input(titulo):
                    break

            while True:
                genero= input('Genero: ').capitalize()
                if valid_input(genero):
                    break

            while True:
                autor= input('Autor: ').title()
                if valid_input(autor):
                    break

            while True:
                publicacion= input('Fecha de Publicacion: ')
                try: 
                    datetime.datetime.strptime(publicacion, '%d/-%m/%Y')
                except ValueError:
                    print("Error: La fecha no cumple con las reglas de formato, ingresar fecha con el siguiente formato 'DD/MM/YYYY'\nD: dia\tM: mes\tY: anio")
                else:
                    break

            while True:
                editorial= input('Editorial: ').title()
                if valid_input(editorial):
                    break

            bs.add_book(Libro(titulo, genero, autor, editorial, publicacion))

        case '3':
            print('Actualizar libro')
            print('\n')
        case '4':
            pass
        case _:
            print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')
            