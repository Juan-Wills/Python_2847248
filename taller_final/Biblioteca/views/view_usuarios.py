from services.biblioteca_service import (
    add_user,
    find_user,
    upd_user,
    del_user,
)
from services.validation_and_dataManagement_service import (
    validate_input_format,
    validate_menu_options,
    autoincrement,
    get_feat,
)
import re
from models.usuario import Usuario


def gestion_usuarios():
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

            if not validate_menu_options(option, max_args=4, min_args=0):
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
                                print("\nValidando correo...")
                                if find_user("correo", correo):
                                    print("Ya existe un usuario con ese correo.")
                                    continue
                                print("Correo valido.\n")
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
                                input("Esta afiliado? (Si/No): ").strip().lower(),
                                mode="boolean",
                            )
                            break

                        new_user = Usuario(
                            autoincrement("usuario", "usuarios.json"),
                            nombre,
                            apellido,
                            correo,
                            residencia,
                            telefono,
                            afiliacion,
                        )
                        print(f"\nVista previa:\n{new_user}")

                        while True:
                            print("\nDesea guardar el usuario?")
                            print("1. Si\t2. No (Volver)")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(option, type="dual"):
                                continue

                            if option == "2":
                                print("Operacion cancelada")
                                return
                            
                            print("\nAgregando usuario...")
                            if add_user(new_user):
                                print(
                                    f"\nUsuario agregado exitosamente."
                                )
                            break
                        break

                case "2":
                    print("\nBuscando en base de datos...")
                    if not find_user("", "", all=True):
                        print(
                            "No hay usuarios registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue

                    while True:
                        print("\nBuscar usuario")
                        print("Ingrese el criterio de busqueda:")
                        print(
                            "1. Nombre    2. Apellido    3. Correo    4. Residencia\n" 
                            "5. Telefono    6. Afiliacion    7. ID    8. Ver todos" 
                        )
                        option = input("Ingresar opcion: ")


                        if option == "8":
                            print("\nBuscando usuarios...")
                            for user in find_user("", "", all=True):
                                print(user)
                                print("-" * 50)
                            break

                        if not validate_menu_options(
                            option,
                            type="category",
                            object_name="usuario",
                            max_args=8,
                        ):
                            continue

                        attribute = get_feat("usuario", option)
                        feature = input("Buscar: ").strip()

                        print("\nBuscando usuarios...")
                        if users := find_user(attribute, feature):
                            for user in users:
                                print(user)
                                print("-" * 20)
                            break
                        else:
                            print(
                                f"No se encontraron libros con la caracteristica {attribute.replace('_', ' de ').capitalize()}: {filter}.\n"
                            )
                            continue
                case "3":
                    print("\nBuscando en base de datos...")
                    if not find_user("", "", all=True):
                        print(
                            "No hay usuarios registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue

                    while True:
                        print("\nActualizar usuario")
                        print("Categorias de busqueda")
                        print("3. Correo\t6. Id")
                        menu_option = input("Ingresa opcion: ")

                        if not validate_menu_options(
                            menu_option, mode="equal", max_args=6, min_args=3
                        ):
                            continue


                        busqueda = input("Buscar: ")
                        
                        if menu_option == "3":
                            if not validate_input_format(busqueda, mode="email"):
                                continue

                        print("\nBuscando usuario...")
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

                        user = user[0]
                        print("\nInformacion original")
                        print(user)

                        while True:
                            print("\nQue informacion desea modificar:")
                            print(
                                "1. Nombre    2. Apellido    3. Correo    4. Residencia    5. Telefono    6. Afiliacion"
                            )
                            modificar = input("Ingresar opcion: ").strip()

                            attribute = get_feat("usuario", modificar)

                            if not validate_menu_options(
                                modificar,
                                type="category",
                                max_args=6,
                                object_name="usuario",
                            ):
                                continue
                                
                            print(
                                f"{attribute.capitalize()} anterior: ",
                                end= ''
                            )

                            if modificar == "6":
                                print(
                                    f"{'Afiliado' if user.afiliacion else 'No afiliado'}"
                                )
                            else:
                                print(getattr(user, attribute))

                            new_info = input("Ingresar nuevo valor: ").title().strip()

                            if modificar == "6":
                                if new_info == "Afiliado" or  new_info == "True":
                                    new_info = True
                                elif new_info == "No Afiliado" or new_info == "False":
                                    new_info = False

                            setattr(user, attribute, new_info)

                            while True:
                                print(f"\nVista previa:\n{user}")
                                print("\nGuardar cambios?")
                                print("1. Si\t2. No")
                                save = input("Ingresar opcion: ")

                                if not validate_menu_options(
                                    save,
                                    mode="equal",
                                    min_args=1,
                                    max_args=2,
                                ):
                                    continue

                                if save == "2":
                                    print("Cambios descartados.")
                                    return

                                print("\nActualizando usuario...")
                                if upd_user(user):
                                    print(f"\nUsuario actualizado exitosamente.")
                                else:
                                    print(
                                        f"Se ha presentado un error al intentar guardar el usuario. Por favor intentelo de nuevo"
                                    )
                                break
                            break
                        break

                case "4":
                    print("\nBuscando en base de datos...")
                    if not find_user("", "", all=True):
                        print(
                            "No hay usuarios registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue
                      
                    while True:
                        print("\nEliminar usuario")
                        id_user = (
                            input(
                                "Ingrese los Id de los usuarios a eliminar: "
                            )
                            .strip()
                            .split(",")
                        )

                        if len(id_user) == 1 and not id_user[0].isnumeric():
                            if re.fullmatch(r"\d[,]+\s*?\d", id_user[0]) is None:
                                print("Error: Ingrese los id's separados por comas.")
                                continue

                        found_users = []
                        # If find_user returns None, it means no user was found
                        print("\nBuscando usuarios...")
                        for id in id_user:
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
                            print("-" * 50)

                        while True:
                            print("\nConfirme la eliminacion de los usuarios:")
                            print("1. Si\t2. No")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option,
                                mode="equal",
                                max_args=2,
                            ):
                                continue

                            if option == "2":
                                print("Abortando eliminacion de usuarios...")
                                break

                            print("\nEliminando usuario...")
                            if del_user(id_user, sort=True):
                                print(f"\nUsuario eliminado exitosamente.")
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
