if __name__ == "__main__":
    import sys
    import datetime
    from models.libro import Libro
    from models.usuario import Usuario
    from models.prestamo import Prestamo
    sys.path.append('C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/')

    # Elegir modelo
    Test= 'prestamo'.lower()

    # Modelo Prestamo
    if Test == 'prestamo':
        print("--- Testing Prestamo Class ---")

        book1 = Libro("The Great Gatsby", "Fantasia", "F. Scott Fitzgerald", "Wonderlands", datetime.date.today(), '1')
        book2 = Libro("1984", "Novela", "George Orwell", "Books and more", datetime.date.today(), '2')
        user1 = Usuario("Alice", "Smith", "alice@gmail.com", afiliacion= True)
        user2 = Usuario("Bob", "Johnson", "bob@gmail.com", afiliacion= True)

        # Create a new loan
        loan1 = Prestamo(book1, user1, datetime.date(2025, 8, 15))
        print("--- Initial Loan 1 ---")
        print(loan1)
        print(f"Is Loan 1 overdue? {loan1.vencido()}")
        print("-" * 20)

        # Simulate a loan from the past to test overdue status
        past_date = datetime.date(2025, 6, 14)
        loan2 = Prestamo(book2, user2, datetime.date(2025, 7, 12), fecha_prestamo=past_date)
        print("--- Initial Loan 2 (Past Date) ---")
        print(loan2)
        print(f"Is Loan 2 overdue? {loan2.vencido()}")
        print("-" * 20)


        # Mostrar, Aumentar, y pagar deuda de multa
        print("--- Initial Loan 2 (Multa) ---")
        print(f"Multa Actual: ${loan2.multa}")
        loan2.aumentar_multa()
        print(f"Multa Despues: ${loan2.multa}")
        loan2.pagar_multa(2000)
        print(f"Pago invalido: ${loan2.multa}")
        loan2.pagar_multa(loan2.multa)
        print(f"Multa Pagada: ${loan2.multa}\n")

        # Mark loan1 as returned
        loan1.marcar_devuelto()
        print("\n--- Loan 1 After Marking as Returned ---")
        print(loan1)
        print(f"Is Loan 1 overdue? {loan1.vencido()}")
        print("-" * 20)

        # Check loan2 again after some time (it should still be overdue if not returned)
        print("\n--- Loan 2 (Still Overdue) ---")
        print(loan2)
        print(f"Is Loan 2 overdue? {loan2.vencido()}")
        print("-" * 20)

    # Modelo Libro
    if Test == 'libro':
        print("--- Testing Libro Class ---")

        # Test Case 1: Create a new book instance and print its details
        print("\nTest Case 1: Creating a new book and printing its details.")
        book1 = Libro(
            id="B001",
            titulo="Cien años de soledad",
            genero="Realismo Mágico",
            autor="Gabriel García Márquez",
            editorial="Editorial Sudamericana",
            fecha_publicacion="1967-05-30"
        )
        print(book1)
        print("-" * 30)

        # Test Case 2: Create another book instance and convert it to a dictionary
        print("\nTest Case 2: Creating another book and converting it to a dictionary.")
        book2 = Libro(
            id="B002",
            titulo="Don Quijote de la Mancha",
            genero="Novela de caballerías",
            autor="Miguel de Cervantes",
            editorial="Francisco de Robles",
            fecha_publicacion="1605-01-16"
        )
        book2_dict = book2.to_dict()
        print(f"Book 2 as dictionary: {book2_dict}")
        print("-" * 30)

        # Test Case 3: Verify data types and access attributes directly
        print("\nTest Case 3: Verifying data types and direct attribute access.")
        print(f"Type of book1: {type(book1)}")
        print(f"Book1 ID: {book1.id}, Type: {type(book1.id)}")
        print(f"Book1 Title: {book1.titulo}, Type: {type(book1.titulo)}")
        print(f"Book1 Publication Date: {book1.fecha_publicacion}, Type: {type(book1.fecha_publicacion)}")
        print("-" * 30)

        # Test Case 4: Check if the dictionary conversion is accurate
        print("\nTest Case 4: Checking accuracy of to_dict() method.")
        expected_dict = {
            'id': 'B001',
            'titulo': 'Cien años de soledad',
            'genero': 'Realismo Mágico',
            'autor': 'Gabriel García Márquez',
            'editorial': 'Editorial Sudamericana',
            'fecha_publicacion': '1967-05-30'
        }
        if book1.to_dict() == expected_dict:
            print("to_dict() for book1 matches expected dictionary.")
        else:
            print("to_dict() for book1 does NOT match expected dictionary.")
        print("-" * 30)

        print("\n--- Libro Class Testing Complete ---")

    # Modelo Usuario
    if Test == 'usuario':
        print("--- Testing Usuario Class ---")

        # Test Case 1: Create a new user instance with all parameters and print its details
        print("\nTest Case 1: Creating a new user with all parameters and printing its details.")
        user1 = Usuario(
            nombre="Ana",
            apellido="García",
            correo="ana.garcia@example.com",
            residencia="Calle Falsa 123, Ciudad",
            telefono="555-1234",
            afiliacion=True
        )
        print(user1)
        print("-" * 30)

        # Test Case 2: Create another user instance with only required parameters (defaults for optional)
        print("\nTest Case 2: Creating another user with only required parameters (defaults for optional).")
        user2 = Usuario(
            nombre="Juan",
            apellido="Pérez",
            correo="juan.perez@example.com"
        )
        print(user2)
        print("-" * 30)

        # Test Case 3: Convert a user object to a dictionary
        print("\nTest Case 3: Converting a user object to a dictionary.")
        user1_dict = user1.to_dict()
        print(f"User 1 as dictionary: {user1_dict}")
        print("-" * 30)

        # Test Case 4: Verify data types and access attributes directly
        print("\nTest Case 4: Verifying data types and direct attribute access.")
        print(f"Type of user1: {type(user1)}")
        print(f"User1 Name: {user1.nombre}, Type: {type(user1.nombre)}")
        print(f"User1 Email: {user1.correo}, Type: {type(user1.correo)}")
        print(f"User1 Affiliation: {user1.afiliacion}, Type: {type(user1.afiliacion)}")
        print("-" * 30)

        # Test Case 5: Check if the dictionary conversion is accurate for user1
        print("\nTest Case 5: Checking accuracy of to_dict() method for user1.")
        expected_user1_dict = {
            'nombre': 'Ana',
            'apellido': 'García',
            'correo': 'ana.garcia@example.com',
            'residencia': 'Calle Falsa 123, Ciudad',
            'telefono': '555-1234',
            'afiliacion': True
        }
        if user1.to_dict() == expected_user1_dict:
            print("to_dict() for user1 matches expected dictionary.")
        else:
            print("to_dict() for user1 does NOT match expected dictionary.")
        print("-" * 30)

        # Test Case 6: Check if the dictionary conversion is accurate for user2 (with defaults)
        print("\nTest Case 6: Checking accuracy of to_dict() method for user2 (with defaults).")
        expected_user2_dict = {
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'correo': 'juan.perez@example.com',
            'residencia': '',
            'telefono': '',
            'afiliacion': False
        }
        if user2.to_dict() == expected_user2_dict:
            print("to_dict() for user2 matches expected dictionary.")
        else:
            print("to_dict() for user2 does NOT match expected dictionary.")
        print("-" * 30)

        print("\n--- Usuario Class Testing Complete ---")
