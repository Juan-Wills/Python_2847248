from services import biblioteca_service as bs
from models.libro import Libro
from services.biblioteca_service import validate_input_format, validate_menu_options
from textwrap import dedent
# import rich

       
def gestion_libros():
    print(dedent("""
    Gestionar libros:
        1. Buscar por categoria
        2. Ingresar nuevo libro
        3. Actualizar
        4. Eliminar
          
        0. Volver
    """))
    option= input('Ingresar opcion: ')

    match option:
        case '0':
            return
        
        case '1':
            while True:
                print("\nFiltrar libros")
                print('Elegir categoria: ')
                print('1. Titulo\t2. Autor\t3. Genero\t4. Editorial\t5. Fecha\t6. Id')
                option= input('Ingresar opcion: ')

                if not validate_menu_options(option, type='category', max_args=7):
                    continue

                filter= input("Buscar: ").title()
                if books:= bs.find_book(option, filter):
                    for book in books:
                        print(dedent(f"""
                                Id: {book['id']}
                                Titulo: {book['titulo']}
                                Genero: {book['genero']}
                                Autor: {book['autor']}
                                Editorial: {book['editorial']}
                                Fecha de Publicacion: {book['fecha_publicacion']}
                            """))
                    break

        case '2':
            print("\nAgregar nuevo libro")
            print("Ingrese los datos del libro:")
    
            while True:
                titulo= input('Titulo: ').title()
                if validate_input_format(titulo):
                    break

            while True:
                genero= input('Genero: ').capitalize()
                if validate_input_format(genero):
                    break

            while True:
                autor= input('Autor: ').title()
                if validate_input_format(autor):
                    break

            while True:
                publicacion= input('Fecha de Publicacion: ').strip()
                if validate_input_format(publicacion):
                    break

            while True:
                editorial= input('Editorial: ').title()
                if validate_input_format(editorial):
                    break
                
            new_libro= Libro(titulo, genero, autor, editorial, publicacion)
            print(f"\nVista previa:\n{new_libro}")
            bs.add_book(new_libro)

        case '3':
            while True:
                print('\nActualizar libro')
                print("Categorias de busqueda")
                print("1. Titulo de Obra\t6. Id")
                menu_option= input('Ingresa opcion: ')
                if not validate_menu_options(menu_option, mode='equal'): 
                    continue

                busqueda= input("Buscar: ")

                book= bs.find_book(menu_option, busqueda)
                if len(book) > 1:
                    print("Error, se encontro mas de una coincidencia en la busqueda.\nIntente buscar por medio del Id.")
                    continue

                book= book[0]
                book= Libro(book['titulo'], book['genero'], book['autor'], book['editorial'], book['fecha_publicacion'], id= book['id'])
                print('Informacion original')
                print(book)

                bs.upd_book(book)
                break

        case '4':
            pass
        case _:
            print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')
            