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
    """
    if test_mode:
        print("\nModo de prueba activado, se usaran datos por defecto.")

        # Testing adding user
        nuevo_usuario = Usuario(
                        id= '1',
                        nombre="Juan",
                        apellido="Wills",
                        correo="juan@gmail.com",
                        residencia="Dosquebradas, Risaralda, Colombia",
                        telefono="3225615099",
                        afiliacion=True,
                    )
        add_user(nuevo_usuario)

        # Testing finding user
        users = find_user("correo", 'juan@gmail.com')
        print(f"\nUsuarios encontrados: {next(users)}")

        user= find_user()
    """

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
                            nombre = input("Nombre\s: ").title().strip()
                            if validate_input_format(nombre):
                                break
                        while True:
                            apellido = input("Apellido\s: ").title().strip()
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

                        nuevo_usuario = Usuario(
                            autoincrement("usuario", 'usuarios.json'),
                            nombre,
                            apellido,
                            correo,
                            residencia,
                            telefono,
                            afiliacion,
                        )
                        print(f"\nVista previa:\n{nuevo_usuario}")

                        while True:
                            print("Desea guardar el usuario?")
                            print("1. Si\t2. No (Volver)")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(option, type="dual"):
                                continue

                            if option == "2":
                                print("Operacion cancelada")
                                return
                            add_user(nuevo_usuario)
                            print(f"\nUsuario '{nuevo_usuario.nombre}' agregado exitosamente.")
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
                                    print(f"\Usuario actualizado exitosamente.")
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
                                continue

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

                            if len(id_user) == 1:
                                del_user(id_user[0], mode="single", sort=True)
                            else:
                                del_user(id_user, mode="multi", sort=True)

                            print(f"\nUsuarios eliminados exitosamente.")
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