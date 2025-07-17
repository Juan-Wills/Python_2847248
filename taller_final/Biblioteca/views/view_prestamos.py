from services.biblioteca_service import (
    add_loan,
    upd_loan,
    find_loan,
    del_loan,
    find_book,
    find_user,
    validate_input_format,
    validate_menu_options,
    autoincrement,
    get_feat,
)
from models.prestamo import Prestamo
from tests.test_views import test_mode

def gestion_prestamos():
    """
    if test_mode:
        print("Modo de prueba activado. No se guardaran cambios en los prestamos.")
        return
    """
    while True:
        try:
            print(
                (
                    "\nCrear Prestamo\n"
                    "    1. Crear prestamo\n"
                    "    2. Ver registro de prestamos\n"
                    "    3. Registrar devolucion\n\n"
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
                    print("\nCrear nuevo prestamo")
                    while True:
                        book_id = input("Ingrese el ID del libro: ").strip()
                        if validate_input_format(book_id):
                            continue

                        if book := find_book("id", book_id):
                            print(f"\Vista previa:\n{book}\n")
                            print("Es este el libro esperado?")
                            print("1. Confirmar    2. Rechazar")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", max_args=2, min_args=1
                            ):
                                continue

                            if option == "1":
                                break
                            else:
                                print("Operacion cancelada")
                                continue
                        else:
                            print(
                                "La referencia ingresada no se encuentra en la base de datos, por favor verifique la informacion."
                            )
                            continue

                    while True:
                        user_mail = input("Ingrese el correo del usuario: ").strip()
                        if validate_input_format(user_mail):
                            continue

                        if user := find_user("correo", user_mail):
                            print(f"\Vista previa:\n{user}\n")
                            print("Es este el usuario esperado?")
                            print("1. Confirmar    2. Rechazar")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", max_args=2, min_args=1
                            ):
                                continue

                            if option == "1":
                                break
                            else:
                                print("Operacion cancelada")
                                continue
                        else:
                            print(
                                "La referencia ingresada no se encuentra en la base de datos, por favor verifique la informacion."
                            )
                            continue

                    while True:
                        loan_date = input(
                            "Ingrese la fecha de prestamo (opcional): "
                        ).strip()
                        if validate_input_format(
                            loan_date, mode="date", optional=True
                        ):
                            continue

                        if len(loan_date) == 0:
                            loan_date = None
                        break

                    while True:
                        devolution_date = input(
                            "Ingrese la fecha de devolucion: "
                        ).strip()
                        if validate_input_format(devolution_date, mode="date"):
                            continue
                        break

                    new_prestamo = Prestamo(
                        autoincrement("prestamo", 'prestamos.json'),
                        book,
                        user,
                        loan_date,
                        devolution_date,
                    )
                    print(f"\nVista previa:\n{new_prestamo}")

                    while True:
                        print("Desea guardar el prestamo?")
                        print("1. Si\t2. No (Volver)")
                        option = input("Ingresar opcion: ")

                        if not validate_menu_options(option, type="dual"):
                            continue

                        if option == "2":
                            print("Operacion cancelada")
                            return
                        add_loan(new_prestamo)
                        print(f"\nPrestamo del libro '{new_prestamo.libro.titulo}' al usuario '{new_prestamo.usuario.correo}' agregado exitosamente.")
                        break
                    break


                case "2":
                    print("\nVer registro de prestamos")

                case "3":
                    print("\nRegistrar devolucion")

                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma cerrado forzosamente")
            return


def gestion_multas():
    while True:
        try:
            print(
                (
                    "\nGestionar Multas\n"
                    "    1. Pagar multa\n"
                    "    2. Ver registro de multas\n\n"
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
                    # Implementar logica para pagar multa
                    pass
                
                case "2":
                    # Implementar logica para ver multas
                    pass
                    
                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma cerrado forzosamente")
            return
        
if __name__ == "__main__":
    gestion_prestamos()
    gestion_multas()