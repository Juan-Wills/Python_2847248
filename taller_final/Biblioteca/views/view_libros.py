from services.biblioteca_service import (
    add_book,
    find_book,
    del_book,
    upd_book,
    retrieve_data,
    validate_input_format,
    validate_menu_options,
    autoincrement,
    get_feat,
    libro_path,
)
from models.libro import Libro


def gestion_libros():
    while True:
        try:
            print((
                    "\nGestionar libros:\n"
                    "    1. Buscar por categoria\n"
                    "    2. Ingresar nuevo libro\n"
                    "    3. Actualizar\n"
                    "    4. Eliminar\n\n"
                    "    0. Volver\n"
            ))

            option = input("Ingresar opcion: ")

            if not validate_menu_options(option, min_args= 0, max_args= 4,):
                continue

            match option:
                case "0":
                    return

                case "1":
                    while True:
                        print("\nFiltrar libros")
                        print("Elegir categoria: ")
                        print(
                            "1. Titulo    2. Autor    3. Genero    4. Editorial    5. Fecha    6. Id    7. Todo"
                        )
                        option = input("Ingresar opcion: ")

                        if option == "7":
                            data = retrieve_data(libro_path)
                            for book in data["libros"]:
                                print(book)
                            break

                        if not validate_menu_options(
                            option,
                            type="category",
                            max_args=7,
                            object_name= get_feat("libro", option),
                        ):
                            continue

                        filter = input("Buscar: ").title().strip()
                        if books := find_book(get_feat("libro", option), filter):
                            for book in books:
                                print(book)
                            break
                        print(
                            f"No se encontraron libros con la caracteristica {get_feat('libro', option).replace('_', ' de ').capitalize()}: {filter}.\n"
                        )
                        continue

                case "2":
                    print("\nAgregar nuevo libro")
                    print("Ingrese los datos del libro:")

                    # Usar para pruebas
                    test= False
                    
                    # Recolectar la informacion del libro
                    if not test:
                        while True:
                            titulo = input("Titulo: ").title().strip()
                            if validate_input_format(titulo):
                                break

                        while True:
                            genero = input("Genero: ").capitalize().strip()
                            if validate_input_format(genero):
                                break

                        while True:
                            autor = input("Autor: ").title()
                            if validate_input_format(autor):
                                break

                        while True:
                            publicacion = input("Fecha de Publicacion: ").strip()
                            if validate_input_format(publicacion):
                                break

                        while True:
                            editorial = input("Editorial: ").title().strip()
                            if validate_input_format(editorial):
                                break

                        new_libro = Libro(
                            titulo, genero, autor, editorial, publicacion, autoincrement()
                        )

                        while True:
                            print(f"\nVista previa:\n{new_libro}")
                            print("Desea guardar el libro?")
                            print("1. Si    2. No (Volver)")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(option, type="dual", min_args=1, max_args=2):
                                continue

                            if option == '2':
                                print("Abortando operacion...")
                                break

                            if option == "1":
                                if add_book(new_libro):
                                    print("\nLibro guardado exitosamente.")
                                else:  
                                    print("Abortando operacion...")
                                return
                        break

                    else:
                        new_libro = Libro(  # Test data
                            titulo="El Principito",
                            genero="Ficcion",
                            autor="Antoine de Saint-Exupery",
                            editorial="Reynal & Hitchcock",
                            fecha_publicacion="1943",
                            id=autoincrement(),
                        )

                        add_book(new_libro)

                case "3":
                    while True:
                        print("\nActualizar libro")
                        print("Categorias de busqueda")
                        print("1. Titulo de Obra\t6. Id")
                        menu_option = input("Ingresa opcion: ")

                        if not validate_menu_options(
                            menu_option, mode="equal", max_args=6, min_args=1
                        ):
                            continue

                        busqueda = input("Buscar: ")

                        book = find_book(get_feat("libro", menu_option), busqueda)

                        if not book:
                            print(
                                "No se encontraron libros con la busqueda proporcionada. Por favor, verifique los datos e intente nuevamente."
                            )
                            continue

                        if len(book) > 1:
                            print(
                                "Error, se encontro mas de una coincidencia en la busqueda.\nIntente buscar por medio del Id."
                            )
                            continue

                        book = book[0]
                        print("Informacion original")
                        print(book)

                        while True:
                            print("Que informacion desea modificar:")
                            print(
                                "1. Titulo\t2. Autor\t3. Genero\t4. Editorial\t5. Fecha de Publicacion"
                            )
                            modificar = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                modificar,
                                type="category",
                                max_args=5,
                                object_name= get_feat("libro", modificar),
                            ):
                                continue

                            attribute = get_feat("libro", modificar)
                            print(
                                f"{attribute.capitalize()} anterior: {getattr(book, attribute)}"
                            )
                            new_info = input("Ingresar nuevo valor: ").title().strip()
                            setattr(book, attribute, new_info)

                            while True:
                                print(f"\nVista previa:\n{book}")
                                print("\nDesea realizar mas cambios?")
                                print("1. Si\t2. No")
                                save = input("Ingresar opcion: ")

                                if not validate_menu_options(
                                    save, mode="equal", min_args=1, max_args=2,
                                ):
                                    continue

                                if save == "1":
                                    print()
                                    break

                                if upd_book(book):
                                    print(f"\nLibro actualizado exitosamente.")
                                else:
                                    print(f"Se ha presentado un error al intentar guardar el libro. Por favor intentelo de nuevo")
                                return

                case "4":
                    while True:
                        data = retrieve_data(libro_path)
                        print("\nEliminar libro")
                        id_book = (
                            input(
                                "Ingrese los Id de los libros a eliminar (separados por comas): "
                            )
                            .replace(" ", "")
                            .split(",")
                        )

                        found_books = []
                        try:
                            for id in id_book:
                                try:
                                    for book in find_book("id", id.strip()):
                                        found_books.append(book)
                                except TypeError:
                                    print(
                                        f"Error: No se encontro un libro con el Id {id.strip()}."
                                    )
                                    continue
                        except TypeError:
                            print(
                                "Error: Para eliminar varios libros, se deben ingresar los Id separados por comas."
                            )
                            continue

                        print("\nVista previa de los libros a eliminar:")
                        for book in found_books:
                            print(book)

                        while True:
                            print("\nConfirme la eliminacion de los libros:")
                            print("1. Si\t2. No")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", min_args=1, max_args=2,
                            ):
                                continue

                            if option == "2":
                                print("Abortando eliminacion de libros...")
                                break

                            if len(id_book) == 1:
                                del_book(id_book[0], mode="single", sort=True)

                            else:
                                del_book(id_book, mode="multi", sort=True)

                            print(f"\nLibros eliminado exitosamente.")
                            break
                        break

                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except KeyboardInterrupt:
            return print("\nSeccion cancelada por el usuario.")


if __name__ == "__main__":
    gestion_libros()
