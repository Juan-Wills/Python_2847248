from services.validation_and_dataManagement_service import validate_menu_options, get_feat
from services.biblioteca_service import find_loan, pay_fine, upd_fines

def gestion_multas():
    try:
        print("\nBuscando si existen prestamos registrados...")
        if len(find_loan("", "", all=True)) == 0:
            print(
                "No hay prestamos registrados en la base de datos, por favor ingrese un prestamo antes de intentar buscar."
            )
            return
        print("Prestamos encontrados, continuando con la gestion de multas...")
    except Exception as e:
        print(f"Error al buscar prestamos: {e}")
        return
    
    while True:
        try:
            print(
                (
                    "\nGestionar Multas\n"
                    "    1. Ver registro de multas\n"
                    "    2. Pagar multa\n\n"
                    "    0. Volver\n"
                )
            )
            option = input("Ingresar opcion: ")

            if not validate_menu_options(option, max_args=2, min_args=0):
                continue
            
            match option:
                case "0":
                    return
                case "2":
                    print("\nBuscando en base de datos...")
                    if not find_loan("", "", all=True):
                        print(
                            "No hay prestamos registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue
                    
                    # Update loan's fine records
                    upd_fines()
                    while True:
                        print("\nPagar multa pendiente")
                        id_loan = input("Ingresa el ID del prestamo: ")

                        print("\nBuscando prestamo...")
                        if loan := find_loan("id", id_loan):
                            loan= loan[0]
                            if not loan.vencido() and loan.multa == 0:
                                print(
                                    f"El prestamo no tiene multa pendiente."
                                )
                                continue

                            print(f"\n{loan}\n  Multa acumulada: ${loan.multa}")
                            print("\nEs este el prestamo esperado?")
                            print("1. Confirmar    2. Rechazar")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", max_args=2, min_args=1
                            ):
                                continue

                            if option == "2":
                                print("Operacion cancelada")
                                continue

                            while True:
                                valor = input("\nIngrese el valor a pagar: ").strip()
                                if not valor.isdigit():
                                    print("El valor debe ser un numero entero.")
                                    continue

                                valor = int(valor)

                                if valor <= 0:
                                    print("El valor debe ser mayor a 0.")
                                    continue
                                
                                print("\nActualizando prestamos...")
                                if pay_fine(loan, valor):
                                    print(f"\nLa multa ha sido pagada exitosamente.")
                                else:
                                    print(
                                        "Valor insuficiente para pagar multa, por favor ingrese el valor exacto."
                                    )
                                    print(f"Valor de multa pendiente: ${loan.multa}")
                                    continue
                                break
                            break
                        else:
                            print(
                                "El ID de prestamo ingresado no se encuentra en la base de datos, por favor verifique la informacion."
                            )
                            continue

                case "1":
                    print("\nBuscando en base de datos...")
                    if not find_loan("", "", all=True):
                        print(
                            "No hay prestamos registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue

                    # Update loan's fine records
                    upd_fines()
                    while True:

                        print("\nVer registro de multas")
                        print("Elegir categoria: ")
                        print("5. ID    7. Ver todos")
                        option = input("Ingresar opcion: ")

                        if not validate_menu_options(
                            option,
                            mode= "equal",
                            min_args=5,
                            max_args=7,
                        ):
                            continue

                        if option == "7":
                            while True:
                                print(
                                    "\nSe mostraran las multas de manera ascendente.\nDesea ver los resultados descendentemente?."
                                )
                                print("1. Asc    2. Desc    0. Sin organizar")
                                greater_than = input("Ingresar opcion: ")

                                if not validate_menu_options(
                                    greater_than, max_args=2, min_args=0
                                ):
                                    continue

                                loans = find_loan("", "", all=True)

                                if greater_than == "0":
                                    print("\nPrestamos sin organizar:")

                                if greater_than == "1":
                                    loans.sort(key=lambda x: x.multa)

                                if greater_than == "2":
                                    loans.sort(key=lambda x: x.multa, reverse=True)

                                for loan in loans:
                                    print(loan)
                                    print(f"  Multa pendiente: ${loan.multa}")
                                    print("-" * 50)
                                break

                        else:
                            attribute = get_feat("prestamo", option)
                            filter = input("Buscar: ").title().strip()

                            print("\nBuscando prestamos...")
                            if loans := find_loan(attribute, filter):
                                for loan in loans:
                                    print(loan)
                                    print(f"  Multa pendiente: ${loan.multa}")
                                    print("-" * 50)
                                break
                            else:
                                print(
                                    f"No se encontraron libros con la caracteristica {attribute.replace('_', ' de ').capitalize()}: {filter}.\n"
                                )
                        break
                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )

        except (KeyboardInterrupt, EOFError):
            return print("\nSeccion cancelada por el usuario.")

        

if __name__ == "__main__":
    gestion_multas()