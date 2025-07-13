from services.biblioteca_service import validate_input_format, validate_menu_options, add_user, find_user, get_feat
from models.usuario import Usuario
from textwrap import dedent

def gestion_usuarios():
    while True:
        try:
            print(dedent("""
            Gestionar libros:
                1. Agregar nuevo usuario
                2. Buscar usuario

                0. Volver
            """))
            option= input('Ingresar opcion: ')

            if not validate_menu_options(option, mode='equal', max_args=2, min_args=1):
                continue

            match option:
                case '0':
                    return
                case '1':
                    while True:
                        print("\nAgregar nuevo usuario")
                        print("Ingrese los datos del usuario:")

                        # Usar para pruebas
                        test= False

                        # Recolectar la informacion del usuario
                        if not test:
                            while True:
                                nombre = input('Nombre\s: ').title().strip()
                                if validate_input_format(nombre):
                                    break
                            while True:
                                apellido = input('Apellido\s: ').title().strip()
                                if validate_input_format(apellido):
                                    break
                            while True:
                                correo = input('Correo: ').strip()
                                if validate_input_format(correo, mode='email'):
                                    if find_user('correo', correo):
                                        print("Ya existe un usuario con ese correo.")
                                        continue
                                    break
                            while True:
                                residencia = input('Direccion de residencia (opcional): ').title().strip()
                                if validate_input_format(residencia, optional=True, special_chars= '-,)('):
                                    break
                            
                            while True:
                                telefono = input('Telefono (opcional): ').strip()
                                if validate_input_format(telefono, mode='phone', optional=True):
                                    break
                            while True:

                                afiliacion = validate_input_format(input('Es afiliado? (Si/No): ').strip().lower(), mode= 'boolean')
                                break
                            nuevo_usuario= Usuario(nombre, apellido, correo, residencia, telefono, afiliacion)
                        else:
                            nuevo_usuario = Usuario(  # Test data
                                nombre="Juan",
                                apellido="Wills",
                                correo="juan@gmail.com",
                                residencia="Dosquebradas, Risaralda, Colombia",
                                telefono="3225615099",
                                afiliacion=True
                            )

                        print(f"\nVista previa:\n{nuevo_usuario}")
                        add_user(nuevo_usuario)
                        break

                case '2':
                    while True:
                        print("\nBuscar usuario")
                        print("Ingrese el criterio de busqueda:")
                        print("1. Nombre    2. Apellido    3. Correo")
                        option= input('Ingresar opcion: ')

                        if not validate_menu_options(option, type='category', object_name= 'usuario', max_args=4):
                            continue

                        feature = input("Buscar: ").strip()
                        if users := find_user(get_feat("usuario", option), feature):
                            for user in users:
                                print(user)
                            break
                        else:
                            print("No se encontraron usuarios con ese criterio.")
                            continue

                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            print('\nPrograma cerrado forzosamente')
            return