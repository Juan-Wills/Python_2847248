from datetime import datetime
from services.biblioteca_service import (
    add_loan,
    find_loan,
    upd_loan_devolution,
    book_loaned,
    upd_book,
    find_book,
    find_user,
)
from services.validation_and_dataManagement_service import (
    validate_input_format,
    validate_menu_options,
    autoincrement,
    get_feat,
)
from models.prestamo import Prestamo


def gestion_prestamos():
    while True:
        try:
            print(
                (
                    "\nCrear Prestamo\n"
                    "    1. Crear prestamo\n"
                    "    2. Ver registro de prestamos\n"
                    "    3. Registrar devolucion\n"
                    "    4. Reporte libros mas prestados\n\n"
                    "    0. Volver\n"
                )
            )

            option = input("Ingresar opcion: ").strip()

            if not validate_menu_options(option, max_args=4, min_args=0):
                continue

            match option:
                case "0":
                    return
                case "1":
                    print("\nCrear nuevo prestamo")
                    while True:
                        book_id = input("Ingrese el ID del libro: ").strip()

                        if not validate_input_format(book_id):
                            continue
                        
                        print("\nBuscando libro...")
                        if book := find_book("id", book_id):
                            book = book[0]
                            if not book.disponible:
                                print(
                                    f"El libro ya se encuentra prestado."
                                )
                                continue

                            print(f"\nVista previa:\n{book}\n")
                            print("Es este el libro esperado?")
                            print("1. Confirmar    2. Rechazar")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", max_args=2, min_args=1
                            ):
                                continue

                            if option == "1":
                                book = book.titulo
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
                        user_mail = input("\nIngrese el correo del usuario: ").strip()

                        if not validate_input_format(user_mail, mode="email"):
                            continue

                        print("\nBuscando usuario...")
                        if user := find_user("correo", user_mail):
                            user = user[0]
                            if user.afiliacion == False:
                                print(
                                    f"El usuario '{user.correo}' no esta afiliado a la biblioteca, por favor afiliarlo antes de continuar."
                                )
                                continue
                            
                            if loans:=find_loan("usuario", user.correo):
                                for loan in loans:
                                    if loan.multa:
                                        print(
                                            f"El usuario '{user.correo}' tiene una multa por prestamo pendiente, se debe pagar la multa antes de continuar."
                                        )
                                        continue

                            print(f"\nVista previa:\n{user}\n")
                            print("Es este el usuario esperado?")
                            print("1. Confirmar    2. Rechazar")
                            option = input("Ingresar opcion: ")

                            if not validate_menu_options(
                                option, mode="equal", max_args=2, min_args=1
                            ):
                                continue

                            if option == "1":
                                user = user.correo
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
                        loan_date = input("\nIngrese la fecha de prestamo (opcional): ").strip()

                        if not validate_input_format(loan_date, mode="date", optional=True):
                            continue

                        if len(loan_date) == 0:
                            loan_date = datetime.today().date()
                        else:
                            loan_date = datetime.strptime(loan_date, "%d/%m/%Y").date()

                            if loan_date < datetime.today().date():
                                print(
                                    "La fecha de prestamo no puede ser posterior a la fecha actual."
                                )
                                continue
                        break

                    while True:
                        devolution_date = input("\nIngrese la fecha de devolucion: ").strip()

                        if not validate_input_format(devolution_date, mode="date"):
                            continue

                        devolution_date = datetime.strptime(devolution_date, "%d/%m/%Y").date()

                        if devolution_date < loan_date:
                            print(
                                "La fecha de devolucion no puede ser anterior a la fecha de prestamo."
                            )
                            continue

                        loan_date = loan_date.strftime('%d/%m/%Y')
                        devolution_date = devolution_date.strftime('%d/%m/%Y')
                        break

                    new_prestamo = Prestamo(
                        id= autoincrement("prestamo", "prestamos.json"),
                        libro= book,
                        usuario= user,
                        fecha_prestamo= loan_date,
                        fecha_devolucion= devolution_date,
                        multa= None,
                    )
                    print(f"\nVista previa:\n{new_prestamo}")

                    while True:
                        print("\nDesea guardar el prestamo?")
                        print("1. Si\t2. No (Volver)")
                        option = input("Ingresar opcion: ")

                        if not validate_menu_options(option, type="dual"):
                            continue

                        if option == "2":
                            print("Operacion cancelada")
                            return

                        print("\nAgregando prestamo...")
                        # update book availability
                        book= find_book("id", book_id)[0]
                        book.disponible = False
                        upd_book(book)

                        # add new loan
                        if add_loan(new_prestamo):
                            print(
                                f"\nPrestamo del libro '{new_prestamo.libro}' al usuario '{new_prestamo.usuario}' agregado exitosamente."
                            )
                        break
                    break

                case "2":
                    print("\nBuscando en base de datos...")
                    if not find_loan("", "", all=True):
                        print(
                            "No hay prestamos registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue

                    while True:
                        print("\nVer registros de prestamos")
                        print("Elegir categoria: ")
                        print(
                            "1. Libro    2. Usuario    3. Fecha de Prestamo    4. Fecha de Devolucion\n" 
                            "5. ID    6. Deuda acumulada    7. Ver todos"
                        )
                        option = input("Ingresar opcion: ")

                        if option == "7":
                            print("\nBuscando prestamos...")
                            for loan in find_loan("", "", all=True):
                                print(loan)
                                print("-" * 50)
                            break

                        if not validate_menu_options(
                            option,
                            type="category",
                            max_args=7,
                            object_name="prestamo",
                        ):
                            continue

                        attribute = get_feat("prestamo", option)
                        filter = input("Buscar: ").title().strip()

                        print("\nBuscando prestamos...")
                        if loans := find_loan(attribute, filter):
                            for loan in loans:
                                print("-" * 50)
                                print(loan)
                            break
                        if attribute == "libro":
                            print(
                                f"No se encontraron libros con la caracteristica Titulo del libro: {filter}.\n"
                            )
                        elif attribute == "usuario":
                            print(
                                f"No se encontraron usuarios con la caracteristica Correo del usuario: {filter}.\n"
                            )
                        else:
                            print(
                                f"No se encontraron libros con la caracteristica {attribute.replace('_', ' de ').capitalize()}: {filter}.\n"
                            )
                        continue

                case "3":
                    print("\nBuscando en base de datos...")
                    if not find_loan("", "", all=True):
                        print(
                            "No hay prestamos registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue

                    while True:
                        print("\nRegistrar devolucion")
                        id_loan = input("Ingrese el ID del prestamo: ")

                        print("\nBuscando prestamos...")
                        if loan := find_loan("id", id_loan):
                            loan = loan[0]

                            if not book_loaned(loan.libro):
                                print(
                                    f"El libro '{loan.libro}' no se encuentra prestado."
                                )
                                continue
                            
                            if loan.estado == "Libro devuelto" or loan.estado == "Libro devuelto (Multa pagada)":
                                print(
                                    f"El libro '{loan.libro}' ya ha sido devuelto."
                                )
                                continue

                            if loan.multa:
                                print(
                                    f"El prestamo presenta una multa pendiente de ${loan.multa}. Pague la multa antes de continuar."
                                )
                                continue

                            print(f"\nPrestamo encontrado:\n{loan}")
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
                           
                            loan.fecha_devolucion =  datetime.today().strftime('%d/%m/%Y')
                            loan.marcar_devuelto()

                            print("\nActualizando prestamo...")
                            # update book availability
                            if book:= find_book("titulo", loan.libro):
                                book = book[0]
                                book.disponible = True
                                upd_book(book)

                                # update loan
                                upd_loan_devolution(loan)
                                print(
                                    f"\nPrestamo del libro '{loan.libro}' al usuario '{loan.usuario}' actualizado exitosamente.\nEstado del prestamo: {loan.estado}."
                                )
                                break
                            else:
                                print(
                                    f"No se encontro el libro '{loan.libro}' en la base de datos."
                                )
                                continue
                        else:
                            print("No se encontraron prestamos registrados.")

                case "4":
                    print("\nBuscando en base de datos...")
                    if not find_loan("", "", all=True):
                        print(
                            "No hay prestamos registrados en la base de datos, por favor ingrese un libro antes de intentar buscar."
                        )
                        continue

                    print("\nReporte de libros mas prestados")
                    list_loans = []
                    count_loans = []
                    count= 0

                    print("\nBuscando prestamos...")
                    for loan in find_loan("", "", all=True):
                        list_loans.append(loan.to_dict()["libro"])

                    count_loans = list(list_loans.count(loans) for loans in set(list_loans)) 

                    list_loans = sorted(dict(zip(list_loans, count_loans)).items(), key=lambda x: x[1], reverse=True)

                    print("\nLibros mas prestados:")
                    for libro, count in list_loans:
                        print(f"{libro} - {count} veces")
                    print("\nCantidad total de prestamos:", sum(count_loans))

                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            return print("\nSeccion cancelada por el usuario.")


if __name__ == "__main__":
    gestion_prestamos()
