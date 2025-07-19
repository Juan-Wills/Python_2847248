# Functions will be modified to not save data into the json files.
# Also, all the view files will use default data when using functions like add_user, add_book, etc.
import datetime
from models.prestamo import Prestamo
from models.usuario import Usuario
from models.libro import Libro
from services.biblioteca_service import (
    add_loan,
    find_loan,
    upd_loan_devolution,
    find_user,
    del_user,
    add_user,
    upd_user,
    del_book,
    add_book,
    find_book,
    upd_book,
    pay_fine,
    autoincrement,
)
from services.validation_and_dataManagement_service import (
    get_feat,

)

# Prestamos view
while True:
    # Add loan
    print("\nAgregar prestamo...")
    new_prestamo = Prestamo(
        id="1",
        libro= find_book("id", "1")[0],
        usuario= find_user("id", "1")[0],
        fecha_prestamo=datetime.strptime("2023-10-01", "%Y-%m-%d").date(),
        fecha_devolucion=datetime.strptime("2023-10-15", "%Y-%m-%d").date(),
    )

    if add_loan(new_prestamo):
        print(f"\nNuevo prestamo agregado exitosamente:\n{new_prestamo}")
    else:
        print("Error al agregar el prestamo.")

    while True:
        # Find loans
        print("\nBuscar prestamos...")
        # all_mode = input("Ver todos los registros? (si/no): ").strip().lower()
        all_mode= 'si'
        if all_mode == "si":
            all_mode = True
            filter_by = ""
            feature = ""
        else:
            all_mode = False
            categories = get_feat("prestamo", 0, all=True)
            print("\nCategorias disponibles:")
            print(categories)
            while True:
                filter_by = input("Ingrese la categoria para filtrar: ").strip()
                if filter_by in categories:
                    break
                print(
                    f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}"
                )
            feature = input("Ingrese el atributo a filtrar: ").strip()

        if loans := find_loan(filter_by, feature, all=all_mode):
            print()
            for loan in loans:
                print(loan)
                print("-" * 50)
        else:
            print("No se encontraron prestamos registrados.")

        # Update loan
        print("\nActualizar devolucion de prestamo...")
        try:
            if loans := find_loan(filter_by, feature):
                if len(loans) > 1:
                    print(
                        f"Error, se encontro mas de un registro de prestamo con la busqueda proporcionada. Coincidencias: {len(loans)}"
                    )
                else:
                    loan = loans[0]
                    print(f"\nPrestamo encontrado para actualizar:\n{loan}")
                    devolcion = (
                        input("\nIngrese la fecha de devolucion (opcional): ")
                        .title()
                        .strip()
                    )
                    if not devolcion:
                        devolcion = datetime.date.today()

                    setattr(loan, filter_by, devolcion)
                    if upd_loan_devolution(loan):
                        print(f"\nPrestamo actualizado exitosamente:\n{loan}")
                    else:
                        print("\nError al actualizar el prestamo.")
            else:
                print("No se encontraron prestamos registrados")

        except AttributeError:
            print("No se puede realizar esta accion con el filtro proporcionado.")
            print("(Asegurese de no filtrar por todos los registros)")

        # End test mode
        if input("\nTerminar test de la vista prestamos? (si/no): ").strip().lower() == "no":
            continue
        print("\nModo de prueba finalizado.")
        break
    break

# ---------------------------------------------------------------
# Usuarios view
while True:
    print("\nModo de prueba activado, no se guardaran los cambios realizados")
    # Add user
    print("\nAgregar usuario...")
    new_user = Usuario(
        id="1",
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
        all_mode = input("Ver todos los registros? (si/no): ").strip().lower()
        if all_mode == "si":
            all_mode = True
            filter_by = ""
            feature = ""
        else:
            all_mode = False
            categories = get_feat("usuario", 0, all=True)
            print("\nCategorias disponibles:")
            print(categories)
            while True:
                filter_by = input("Ingrese la categoria para filtrar: ").strip()
                if filter_by in categories:
                    break
                print(
                    f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}"
                )
            feature = input("Ingrese el atributo a filtrar: ").strip().lower()
            if filter_by == "afiliacion":
                if feature == "true":
                    feature = True
                elif feature == "false":
                    feature = False
                else:
                    print(
                        "Valor no valido para afiliacion, debe ser 'true' o 'false'."
                    )
                    continue

        if users := find_user(filter_by, feature, all=all_mode):
            print()
            for user in users:
                print(user)
                print("-" * 50)
        else:
            print("No se encontraron usuarios registrados.")

        # Update user
        print("\nActualizar usuario...")
        try:
            if users := find_user(filter_by, feature):
                if len(users) > 1:
                    print(
                        f"Error, se encontro mas de un usuario con la busqueda proporcionada. Coincidencias: {len(users)}"
                    )
                else:
                    user = users[0]
                    print(f"\nUsuario encontrado para actualizar:\n{user}")
                    while True:
                        new_value = (
                            input(f"\nIngrese el nuevo valor para '{filter_by}': ")
                            .title()
                            .strip()
                            .lower()
                        )
                        if filter_by == "afiliacion":
                            if new_value == "true" or new_value == "afiliado":
                                new_value = True
                            elif new_value == "false" or new_value == "no afiliado":
                                new_value = False
                            else:
                                print(
                                    "Valor no valido para afiliacion, debe ser 'true' o 'false'."
                                )
                                continue
                        break

                    setattr(user, filter_by, new_value)
                    if upd_user(user):
                        print(
                            f"\nUsuario actualizado exitosamente\nNuevo '{filter_by}': {getattr(user, filter_by)}"
                        )
                    else:
                        print("\nError al actualizar el usuario.")
            else:
                print("No se encontraron usuarios.")
                print("(Asegurese de no filtrar por todos los registros)")

        except AttributeError:
            print("No se puede realizar esta accion con el filtro proporcionado.")
            print("(Asegurese de no filtrar por todos los registros)")

        # Delete user
        print("\nEliminar usuario...")
        try:
            if users := find_user(filter_by, feature):
                user_ids = [user.id for user in users]

                if del_users := del_user(user_ids):
                    print("Usuario\s eliminado:")
                    for user in del_users:
                        print(user)
                        print("-" * 50)
                    print(f"\nUsuario/s eliminado exitosamente.")
                else:
                    print("\nError al eliminar el usuario.")
            else:
                print("No se encontraron usuarios.")
                print("(Asegurese de no filtrar por todos los registros)")

        except AttributeError:
            print("No se puede realizar esta accion con el filtro proporcionado.")
            print("(Asegurese de no filtrar por todos los registros)")

        # End test mode
        if input("\nTerminar test de la vista usuario? (si/no): ").strip().lower() == "no":
              continue
        print("\nModo de prueba finalizado.")
        break
    break

# ---------------------------------------------------------------
# Multas view
while True:
    # Find fines
    print("Buscar prestamo...")
    all = input("Ver todos los registros? (si/no): ").strip().lower()
    if all == "si":
        all = True
        filter_by = ""
        feature = ""
    else:
        all = False
        categories = get_feat("prestamo", 0)
        print("\nCategorias disponibles:")
        print(categories)
        while True:
            filter_by = input("Ingrese la categoria para filtrar: ").strip()
            if filter_by in categories:
                break
            print(
                f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}"
            )
        feature = input("Ingrese el atributo a filtrar: ").strip()
        print()

    if prestamo := find_user(filter_by, feature, all=all):
        for fine in prestamo:
            print(fine)
            print("-" * 50)
    else:
        print("No se encontraron multas registradas.")

    # Pay fine
    print("\nPagar multa pendiente...")
    try:
        if filter_by == "id":
            print("No se puede actualizar el Id de un libro.")
        else:
            if loan := find_book(filter_by, feature):
                loan = loan[0]
                print(f"Multa acumulada: ${loan.multa}")
                to_pay = input("Ingrese el valor a pagar: ").strip()

                if pay_fine(loan, to_pay):
                    print(f"Multa pagada.")
                    print(f"Deuda actual: {loan.multa}")
                else:
                    print(
                        f"La multa no se pudo pagar por valor de pago insuficiente"
                    )
            else:
                print(
                    "No se encontraron prestamos con la caracteristica proporcionada."
                )
                print("(Asegurese de no filtrar por todos los registros)")

    except AttributeError:
        print("No se puede realizar esta accion con el filtro proporcionado.")
        print("(Asegurese de no filtrar por todos los registros)")

        # End test mode
        if input("Terminar test de la vista multas? (si/no): ").strip().lower() == "no":
            print("\nModo de prueba finalizado.")
            continue
        print("\nModo de prueba finalizado.")
        break
    break

# ---------------------------------------------------------------
# Libros view
while True:
    print("\nAgregar libro...")
    new_libro = Libro(
        titulo="El Principito",
        genero="Ficcion",
        autor="Antoine de Saint-Exupery",
        editorial="Reynal & Hitchcock",
        fecha_publicacion="1943",
        id=autoincrement("libro", "libros.json"),
    )

    if add_book(new_libro):
        print(f"\nNuevo libro agregado exitosamente.\n\n{new_libro}")
    else:
        print("Error al agregar el libro.")

    while True:
        # Find book
        print("\nBuscar libro...")
        all_mode = input("Ver todos los registros? (si/no): ").strip().lower()
        if all_mode == "si":
            all_mode = True
            filter_by = ""
            feature = ""
        else:
            all_mode = False
            categories = get_feat("libro", 0, all=True)
            print("\nCategorias disponibles:")
            print(categories)
            while True:
                filter_by = input("Ingrese la categoria para filtrar: ").strip()
                if filter_by in categories:
                    break
                print(
                    f"Categoria '{filter_by}' no valida. Por favor, elija una de las siguientes: {categories}"
                )
            feature = input("Ingrese el atributo a filtrar: ").strip()

        if books := find_book(filter_by, feature, all=all_mode):
            print()
            for book in books:
                print(book)
                print("-" * 50)
        else:
            print("No se encontraron libros registrados.")

        # Update book
        print("\nActualizar libro...")
        try:
            if filter_by == "id":
                print("No se puede actualizar el Id de un libro.")
            else:
                if books := find_book(filter_by, feature):
                    if len(books) > 1:
                        print(
                            f"Error, se encontro mas de un libro con la busqueda proporcionada. Coincidencias: {len(books)}"
                        )
                    else:
                        book = books[0]
                        print(f"\nLibro encontrado para actualizar:\n{book}")
                        new_value = (
                            input(f"\nIngrese el nuevo valor para '{filter_by}': ")
                            .title()
                            .strip()
                        )
                        setattr(book, filter_by, new_value)
                        if upd_book(book):
                            print(
                                f"\nLibro actualizado exitosamente\nNuevo '{filter_by}': {getattr(book, filter_by)}"
                            )
                        else:
                            print("\nError al actualizar el libro.")
                else:
                    print("\nNo se encontraron libros.")
                    print("(Asegurese de no filtrar por todos los registros)")

        except AttributeError:
            print("No se puede realizar esta accion con el filtro proporcionado.")
            print("(Asegurese de no filtrar por todos los registros)")

        # Delete book
        print("\nEliminar libro...")
        try:
            if books := find_book(filter_by, feature):
                book_ids = [book.id for book in books]
                if del_books := del_book(book_ids):
                    print(f"\nLibro/s eliminado exitosamente.")
                    print("Libro eliminado:")
                    for book in del_books:
                        print(book)
                else:
                    print("\nError al eliminar el libro.")
            else:
                print("No se encontraron libros.")
                print("(Asegurese de no filtrar por todos los registros)")

        except AttributeError:
            print("No se puede realizar esta accion con el filtro proporcionado.")
            print("(Asegurese de no filtrar por todos los registros)")

        # End test mode
        if input("\nTerminar test de la vista libros? (si/no): ").strip().lower() == "no":
            print("\nModo de prueba finalizado.")
            continue
        print("\nModo de prueba finalizado.")
        break
    break

