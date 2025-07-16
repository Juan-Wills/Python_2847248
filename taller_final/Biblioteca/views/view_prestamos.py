from services.biblioteca_service import validate_input_format, validate_menu_options, add_user, find_user, get_feat
from models.usuario import Usuario

# Usar para pruebas
test_mode= False

def gestion_prestamos():
    while True:
        try:
            print((
                    "\nCrear Prestamo\n"
                    "    1. Crear prestamo\n"
                    "    2. Ver registro de prestamos\n"
                    "    3. Registrar devolucion\n"
                    "    0. Volver\n"
            ))

            option = input('Ingresar opcion: ')

            if not validate_menu_options(option, max_args=2, min_args=0):
                continue

            match option:
                case '0':
                    return
                case '1':
                    print("\nCrear nuevo prestamo")
                    while True:
                        libro = input('Ingrese el ID o Titulodel libro: ').strip()
                        if validate_input_format(libro, mode='id'):
                            break
                    print("Ingrese los datos del prestamo:")
                case '2':
                    print("\nVer registro de prestamos")
                case '3':
                    print("\nRegistrar devolucion")

        except (KeyboardInterrupt, EOFError):
            print('\nPrograma cerrado forzosamente')
            return
        

def gestion_multas():
    while True:
        try:
            print((
                    "\nGestionar Multas\n"
                    "    1. Pagar multa\n"
                    "    2. Ver registro de multas\n\n"
                    "    0. Volver\n"
                )
            )

            option = input('Ingresar opcion: ')

            if not validate_menu_options(option, max_args=2, min_args=0):
                continue

            match option:
                case '0':
                    return
                case '1':
                    # Implementar logica para pagar multa
                    pass
                case '2':
                    # Implementar logica para ver multas
                    pass

        except (KeyboardInterrupt, EOFError):
            print('\nPrograma cerrado forzosamente')
            return
            