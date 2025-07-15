from services.biblioteca_service import validate_input_format, validate_menu_options, add_user, find_user, get_feat
from models.usuario import Usuario

# Usar para pruebas
test_mode= False

def gestion_usuarios():
    while True:
        try:
            print((
                    "\nGestionar Usuarios\n"
                    "    1. Agregar nuevo usuario\n"
                    "    2. Buscar usuario\n\n"
                    "    0. Volver\n"
            ))
            option= input('Ingresar opcion: ')

            if not validate_menu_options(option, max_args=2, min_args=0):
                continue

            match option:
                case '0':
                    return
                case '1':
                    while True:
                        print("\nAgregar nuevo usuario")
                        print("Ingrese los datos del usuario:")

                        # Recolectar la informacion del usuario
                        if not test_mode:
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
                    if not test_mode:
                        while True:
                            print("\nBuscar usuario")
                            print("Ingrese el criterio de busqueda:")
                            print("1. Nombre    2. Apellido    3. Correo    4. Telefono    5. Afiliacion")
                            option= input('Ingresar opcion: ')

                            if not validate_menu_options(option, type='category', object_name= 'usuario', max_args=5):
                                continue

                            feature = input("Buscar: ").strip()
                            if users := find_user(get_feat("usuario", option), feature):
                                for user in users:
                                    print(user)
                                break
                            else:
                                print("No se encontraron usuarios con ese criterio.")
                                continue
                    else:
                        for user in find_user('Correo', 'juan@gmail.com'):
                            print(user)
                        print()

                        for user in find_user('nombre', 'juan'):
                            print(user)
                        print()

                        for user in find_user('apellido', 'wills'):
                            print(user)
                        print()

                        if users := find_user('correo', 'brayan@gmail.com'):
                            for user in users:
                                print(user)
                        else:
                            print("No se encontraron usuarios este criterio (Correo).\n")
                        
                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            print('\nPrograma cerrado forzosamente')
            return