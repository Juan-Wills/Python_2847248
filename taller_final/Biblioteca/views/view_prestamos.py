from datetime import datetime
from services.biblioteca_service import (
    add_loan,
    find_loan,
    upd_loan_devolution,
    find_book,
    find_fine,
    pay_fine,
    find_user,
    validate_input_format,
    validate_menu_options,
    autoincrement,
    get_feat,
)
from models.prestamo import Prestamo
from tests.test_views import test_mode

def gestion_prestamos():
    if test_mode:
        print("\nModo de prueba activado, no se guardaran los cambios realizados")
        # Add loan
        print("\nAgregar prestamo...")
        new_prestamo = Prestamo(
                        id= '1',
                        libro= 'Cien años de soledad',
                        usuario= 'Gabriel Garcia',
                        fecha_prestamo= datetime.strptime('2023-10-01', '%Y-%m-%d').date(),
                        fecha_devolucion= datetime.strptime('2023-10-15', '%Y-%m-%d').date()
                    )
        if add_loan(new_prestamo):
            print(f"\nNuevo prestamo agregado exitosamente:\n{new_prestamo}")
        else:
            print("Error al agregar el prestamo.")

        while True:
            # Find loans
            print("\nBuscar prestamos...")
            all_mode= input("Ver todos los registros? (si/no): ").strip().lower()
            if all_mode == 'si':
                all_mode = True
                filter_by = ''
                feature = ''
            else:
                all_mode = False
                categories= get_feat("prestamo", 0)
                print("\nCategorias disponibles:")
                print(categories)
                while True:
                    filter_by = input("Ingrese la categoria para filtrar: ").strip()
                    if filter_by in categories:
                        break
                    print(f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}")
                feature = input("Ingrese el atributo a filtrar: ").strip()
                print()

            if loans := find_loan(filter_by, feature, all= all_mode):
                for loan in loans:
                    print(loan)
                    print('-'*50)
            else:
                print("No se encontraron prestamos registrados.")

            # Update loan
            print("\nActualizar devolucion de prestamo...")
            try:
                if loans:= find_loan(filter_by, feature):
                    if len(loans) > 1:
                        print(f"Error, se encontro mas de un registro de prestamo con la busqueda proporcionada. Coincidencias: {len(loans)}")
                    else:
                        loan = loans[0]
                        print(f"\nPrestamo encontrado para actualizar:\n{loan}")
                        devolcion = input("\nIngrese la fecha de devolucion (opcional): ").title().strip()
                        if not devolcion:
                            devolcion = datetime.date.today()

                        setattr(loan, filter_by, devolcion)
                        if upd_loan_devolution(loan):
                            print(f"\nPrestamo actualizado exitosamente:\n{loan}")
                        else:
                            print("\nError al actualizar el prestamo.")
                else:
                    print("\nNo se encontraron prestamos.")
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
                            print(f"\nVista previa:\n{book}\n")
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
                            print(f"\nVista previa:\n{user}\n")
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
                    while True:
                        print("\nVer registros de prestamos")
                        print("Elegir categoria: ")
                        print(
                            "1. Libro    2. Usuario    3. Fecha de Prestamo    4. Fecha de Devolucion    5. ID    6. Deuda acumulada    7. Ver todos"
                        )
                        option = input("Ingresar opcion: ")

                        if option == "7":
                            for loan in find_loan('', '', all=True):
                                print(loan)
                                print('-'*20)
                            break

                        if not validate_menu_options(
                            option,
                            type="category",
                            max_args=7,
                            object_name= 'libro',
                        ):
                            continue
                        
                        attribute= get_feat("libro", option)
                        filter = input("Buscar: ").title().strip()

                        if loans := find_loan(attribute, filter):
                            for loan in loans:
                                print(loan)
                            break
                        print(
                            f"No se encontraron libros con la caracteristica {attribute.replace('_', ' de ').capitalize()}: {filter}.\n"
                        )
                        continue

                case "3":
                    while True:
                        print("\nRegistrar devolucion")
                        id_loan= input("Ingrese el ID del prestamo: ")

                        if loan:= find_loan("id", id_loan):
                            print(f"\nVista previa:\n{loan}")
                            print("Es este el prestamo esperado?")
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
                                devolution_date = input(
                                    "Ingrese la fecha de devolucion (opcional): "
                                ).strip()
                                if validate_input_format(devolution_date, mode="date", optional=True):
                                    continue

                                if len(devolution_date) == 0:
                                    devolution_date = datetime.date.today()

                                loan.fecha_devolucion = devolution_date

                                upd_loan_devolution(loan)
                                print(f"\nPrestamo del libro '{loan.libro.titulo}' al usuario '{loan.usuario.correo}' actualizado exitosamente.")
                                break
                case _:
                    print(
                        "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
                    )
        except (KeyboardInterrupt, EOFError):
            print("\nPrograma cerrado forzosamente")
            return


def gestion_multas():
    if test_mode:
        print("Modo de prueba activado. No se guardaran los cambios realizados")
        # Check fines logs 
        while True:
           # Find user
            print("Buscar prestamo...")
            all= input("Ver todos los registros? (si/no): ").strip().lower()
            if all == 'si':
                all = True
                filter_by = ''
                feature = ''
            else:
                all = False
                categories= get_feat("prestamo", 0)
                print("\nCategorias disponibles:")
                print(categories)
                while True:
                    filter_by = input("Ingrese la categoria para filtrar: ").strip()
                    if filter_by in categories:
                        break
                    print(f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}")
                feature = input("Ingrese el atributo a filtrar: ").strip()
                print()

            if prestamo := find_user(filter_by, feature, all= all):
                for fine in prestamo:
                    print(fine)
                    print('-'*50)
            else:
                print("No se encontraron multas registradas.")
        
            # Pay fine
            print("\nPagar multa pendiente...")
            try:
                if filter_by == 'id':
                    print("No se puede actualizar el Id de un libro.")
                else:
                    if loan:= find_book(filter_by, feature):
                        loan= loan[0]
                        print(f"Multa acumulada: ${loan.multa}")
                        to_pay= input("Ingrese el valor a pagar: ").strip()

                        if loan.pagar_multa(to_pay):
                            print(f"Multa pagada.")
                            print(f"Deuda actual: {loan.multa}")
                        else:
                            print(f"La multa no se pudo pagar por valor de pago insuficiente")
                    else:
                        print("No se encontraron prestamos con la caracteristica proporcionada.")
                        print("(Asegurese de no filtrar por todos los registros)")

            except AttributeError:
                    print("No se puede realizar esta accion con el filtro proporcionado.")
                    print("(Asegurese de no filtrar por todos los registros)")

            # End test mode
            if input("Terminar test? (si/no): ").strip().lower() == 'si':
                print("\nModo de prueba finalizado.")
                return
#---------------------------------------------------------------
    while True:
        try:
            print(
                (
                    "\nGestionar Multas\n"
                    "    1. Ver registro de multas\n\n"
                    "    2. Pagar multa\n"
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
                    while True:
                        print("\nPagar multa pendiente")
                        id_loan= input("Ingresa el ID del prestamo: ")

                        if loan:= find_loan("id", id_loan):
                            print(f"\nVista previa:\n{loan}")
                            print("Es este el prestamo esperado?")
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
                                valor = input("Ingrese el valor a pagar: ").strip()
                                if not valor.isdigit():
                                    print("El valor debe ser un numero entero.")
                                    continue

                                valor = int(valor)

                                if valor <= 0:
                                    print("El valor debe ser mayor a 0.")
                                    continue

                                if pay_fine(loan, valor):
                                    print(f"La multa ha sido pagada exitosamente.")
                                    print(f"Deuda actualizada: {loan.multa}")
                                break
                            break
                        else:
                            print(
                                "El ID de prestamo ingresado no se encuentra en la base de datos, por favor verifique la informacion."
                            )
                            continue
                
                case "1":
                    while True:
                        print("\nVer registro de multas")
                        print("Elegir categoria: ")
                        print(
                            "5. ID    6. Deuda acumulada    7. Ver todos"
                        )
                        option = input("Ingresar opcion: ")

                        if option == "7":
                            for loan in find_fine('', '', all=True):
                                print(loan)
                                print('-'*20)
                            break

                        if option == "6":
                            while True:
                                print("Se mostraran los prestamos con deuda menor o igual al valor a ingresar,\nDesea ver los resultados mayores o iguales?.")
                                print("1. Si    2. No")
                                greater_than= input("Ingresar opcion: ")

                                if not validate_menu_options(
                                    greater_than, mode="equal", max_args=2, min_args=1
                                ):
                                    continue

                                if greater_than == "1":
                                    greater_than = True
                                elif greater_than == "2":
                                    greater_than = False
                                break

                        if not validate_menu_options(
                            option,
                            type="category",
                            max_args=7,
                            object_name= 'libro',
                        ):
                            continue
                        
                        attribute= get_feat("libro", option)
                        filter = input("Buscar: ").title().strip()

                        if loans := find_fine(attribute, filter):
                            for loan in loans:
                                if attribute == "multa":
                                    if greater_than:
                                        if loan.multa >= int(filter):
                                            print(loan)
                                    else:
                                        if loan.multa <= int(filter):
                                            print(loan)
                                else:
                                    print(loan)
                            break
                        print(
                            f"No se encontraron libros con la caracteristica {attribute.replace('_', ' de ').capitalize()}: {filter}.\n"
                        )
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