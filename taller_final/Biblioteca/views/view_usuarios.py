from services.biblioteca_service import (
    add_user,
    find_user,
    upd_user,
    del_user,
    validate_input_format,
    validate_menu_options,
    autoincrement,
    get_feat,
)
from models.usuario import Usuario
from tests.test_views import test_mode

def gestion_usuarios():
    if test_mode:
        print("\nModo de prueba activado, no se guardaran los cambios realizados")
        # Add user
        print("\nAgregar usuario...")
        new_user = Usuario(
                        id= '1',
                        nombre="Juan",
                        apellido="Wills",
                        correo="juan@gmail.com",
                        residencia="Dosquebradas, Risaralda, Colombia",
                        telefono="3225615099",
                        afiliacion=True,
                    )
        if add_user(new_user):
            print(f"\nNuevo usuario agregado exitosamente.\n{new_user}")
        else:
            print("Error al agregar el usuario.")

        while True:
            # Find user
            print("\nBuscar usuario...")
            all_mode= input("Ver todos los registros? (si/no): ").strip().lower()
            if all_mode == 'si':
                all_mode = True
                filter_by = ''
                feature = ''
            else:
                all_mode = False
                categories= get_feat("usuario", 0)
                print("\nCategorias disponibles:")
                print(categories)
                while True:
                    filter_by = input("Ingrese la categoria para filtrar: ").strip()
                    if filter_by in categories:
                        break
                    print(f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}")
                feature = input("Ingrese el atributo a filtrar: ").strip()
                print()

            if users := find_user(filter_by, feature, all= all_mode):
                for user in users:
                    print(user)
                    print('-'*50)
            else:
                print("No se encontraron usuarios registrados.")

            # Update user
            print("Actualizar usuario...")
            try:
                if users := find_user(filter_by, feature):
                    if len(users) > 1:
                        print(f"Error, se encontro mas de un usuario con la busqueda proporcionada. Coincidencias: {len(users)}")
                    else:
                        user = users[0]
                        print(f"\nUsuario encontrado para actualizar:\n{user}")
                        new_value = input(f"\nIngrese el nuevo valor para '{filter_by}': ").title().strip()
                        setattr(user, filter_by, new_value)
                        if user:= upd_user(user):
                            print(f"\nUsuario actualizado exitosamente: {user}")
                        else:
                            print("\nError al actualizar el usuario.")
                else:
                    print("\nNo se encontraron libros.")
                    print("(Asegurese de no filtrar por todos los registros)")

            except AttributeError:
                print("No se puede realizar esta accion con el filtro proporcionado.")
                print("(Asegurese de no filtrar por todos los registros)")
                
            # Delete user
            print("\nEliminar usuario...")
            try:
                if users := find_user(filter_by, feature):
                    user_ids = [user.id for user in users]
                    if del_users:= del_user(user_ids, sort=True):
                        print(f"\nUsuario/s eliminado exitosamente.")
                        print("Usuario eliminado:") 
                        for user in del_users:
                            print(user)
                    else:
                        print("\nError al eliminar el usuario.")
                else:
                    print("No se encontraron usuarios.")
                    print("(Asegurese de no filtrar por todos los registros)")

            except AttributeError:
                print("No se puede realizar esta accion con el filtro proporcionado.")
                print("(Asegurese de no filtrar por todos los registros)")


            # End test mode
            if input("\nTerminar test? (si/no): ").strip().lower() == 'si':
                print("\nModo de prueba finalizado.")
                return
#---------------------------------------------------------------
    while True:
        try:
            print(
                (
                    "\nGestionar Usuarios\n"
                    "    1. Agregar nuevo usuario\n"
                    "    2. Buscar usuario\n"
                    "    3. Actualizar usuario\n"
                    "    4. Eliminar usuario\n\n"
                    "    0. Volver\n"
                )
            )
            option = input("Ingresar opcion: ")

            if not validate_menu_options(option, max_args=2, min_args=0):
                continue

            match option:
                case "0":
                    return
                case "1":
                    while True:
                        print("\nAgregar nuevo usuario")
                        print("Ingrese los datos del usuario:")
                        while True:
                            nombre = input("Nombre/s: ").title().strip()
                            if validate_input_format(nombre):
                                break
                        while True:
                            apellido = input("Apellido/s: ").title().strip()
                            if validate_input_format(apellido):
                                break
                        while True:
                            correo = input("Correo: ").strip()
                            if validate_input_format(correo, mode="email"):
                                if find_user("correo", correo):
                                    print("Ya existe un usuario con ese correo.")
                                    continue
                                break
                        while True:
                            residencia = (
                                input("Direccion de residencia (opcional): ")
                                .title()
                                .strip()
                            )
                            if validate_input_format(
                                residencia, optional=True, special_chars="-,)("
                            ):
                                break

                        while True:
                            telefono = input("Telefono (opcional): ").strip()
                            if validate_input_format(
                                telefono, mode="phone", optional=True
                            ):
                                break

                        while True:
                            afiliacion = validate_input_format(
                                input("Es afiliado? (Si/No): ").strip().lower(),
                                mode="boolean",
                            )
                            break

                        new_user = Usuario(
                            autoincrement("usuario", 'usuarios.json'),
                            nombre,
                            apellido,
                            correo,
                            residencia,
                            telefono,
                            afiliacion,
                        )
                        print(f"\nVista previa:\n{new_user}")

                        while True:
                            print("Desea guardar el usuario?")
                            print("1. Si\t2. No (Volver)")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(option, type="dual"):
                                continue

                            if option == "2":
                                print("Operacion cancelada")
                                return
                            add_user(new_user)
                            print(f"\nUsuario '{new_user.nombre}' agregado exitosamente.")
                            break
                        break

                case "2":
                    while True:
                        print("\nBuscar usuario")
                        print("Ingrese el criterio de busqueda:")
                        print(
                            "1. Nombre    2. Apellido    3. Correo    4. Telefono    5. Afiliacion    6. ID    7. Ver todos"
                        )
                        option = input("Ingresar opcion: ")

                        if option == "7":
                            for user in find_user('', '', all=True):
                                print(user)
                                print('-'*20)
                            break

                        if not validate_menu_options(
                            option,
                            type="category",
                            object_name="usuario",
                            max_args=5,
                        ):
                            continue

                        attribute = get_feat("usuario", option)
                        feature = input("Buscar: ").strip()

                        if users := find_user(attribute, feature):
                            for user in users:
                                print(user)
                                print('-'*20)
                            break
                        else:
                            print(
                                f"No se encontraron libros con la caracteristica {attribute.replace('_', ' de ').capitalize()}: {filter}.\n"
                            )
                            continue
                case "3":
                     while True:
                        print("\nActualizar usuario")
                        print("Categorias de busqueda")
                        print("1. Correo\t6. Id")
                        menu_option = input("Ingresa opcion: ")

                        if not validate_menu_options(
                            menu_option, mode="equal", max_args=6, min_args=1
                        ):
                            continue

                        if menu_option == "1":
                            if not validate_input_format(menu_option, mode="email"):
                                continue

                        busqueda = input("Buscar: ")

                        user = find_user(get_feat("usuario", menu_option), busqueda)

                        if not user:
                            print(
                                "No se encontraron usuarios con la busqueda proporcionada. Por favor, verifique los datos e intente nuevamente."
                            )
                            continue

                        if len(user) > 1:
                            print(
                                "Error, se encontro mas de una coincidencia en la busqueda.\nIntente buscar por medio del Id."
                            )
                            continue

                        user = next(user)
                        print("Informacion original")
                        print(user)

                        while True:
                            print("Que informacion desea modificar:")
                            print(
                                "1. Nombre    2. Apellido    3. Correo    4. Residencia    5. Telefono    6. Afiliacion"
                            )
                            modificar = input("Ingresar opcion: ")

                            attribute = get_feat("usuario", modificar)

                            if not validate_menu_options(
                                modificar,
                                type="category",
                                max_args=6,
                                object_name= 'usuario',
                            ):
                                continue

                            print(
                                f"{attribute.capitalize()} anterior: {getattr(user, attribute)}"
                            )
                            new_info = input("Ingresar nuevo valor: ").title().strip()
                            setattr(user, attribute, new_info)

                            while True:
                                print(f"\nVista previa:\n{user}")
                                print("\nGuardar cambios?")
                                print("1. Si\t2. No")
                                save = input("Ingresar opcion: ")

                                if not validate_menu_options(
                                    save, mode="equal", min_args=1, max_args=2,
                                ):
                                    continue

                                if save == "2":
                                    print("Cambios descartados.")
                                    return

                                if upd_user(user):
                                    print(f"\nUsuario actualizado exitosamente.")
                                else:
                                    print(f"Se ha presentado un error al intentar guardar el usuario. Por favor intentelo de nuevo")
                                break
                            break
                        break

                case "4":
                     while True:
                        print("\nEliminar usuario")
                        id_user = (
                            input(
                                "Ingrese los Id de los usuarios a eliminar (separados por comas): "
                            )
                            .strip()
                            .split(",")
                        )

                        found_users = []
                        for id in id_user:
                            # If find_user returns None, it means no user was found
                            try:
                                for user in find_user("id", id.strip()):
                                    found_users.append(user)
                            except TypeError:
                                print(
                                    f"Error: No se encontro a algun usuario con el Id {id.strip()}."
                                )
                                return

                        print("\nVista previa de los usuarios a eliminar:")
                        for user in found_users:
                            print(user)
                            print('-'*20)

                        while True:
                            print("\nConfirme la eliminacion de los usuarios:")
                            print("1. Si\t2. No")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", min_args=1, max_args=2,
                            ):
                                continue

                            if option == "2":
                                print("Abortando eliminacion de usuarios...")
                                break

                            if del_user(id_user, mode="single", sort=True):
                                print(f"\nUsuario eliminado exitosamente.")
                                for user in found_users:
                                    print(user)
                            else:
                                print(f"\nError al eliminar los usuarios.")
                            break
                        break

                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma cerrado forzosamente")
            return
        
if __name__ == "__main__":
    gestion_usuarios()