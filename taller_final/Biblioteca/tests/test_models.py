import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import datetime
from models.libro import Libro
from models.usuario import Usuario
from models.prestamo import Prestamo

# IMPORTANT: Do not execute this file with pytest, it will not work as expected, execute it as a script.


# Elegir modelo a testear
Test = "libro"  # Test= 'libro', 'usuario', 'prestamo'

# Modelo Prestamo
if Test == "prestamo":
    print("--- Testing Prestamo Class ---")
    # Create a two loan instances
    loan1 = Prestamo(
        "1", "Don quijote de la mancha", "santi@gmail.com", "20/07/2020", "20/08/2020"
    )
    loan2 = Prestamo(
        "2", "El samurai secreto", "juan@gmail.com", "14/06/2025", "21/04/2025"
    )

    print("--- Initial Loan 1 ---")
    print(loan1)
    print(f"Is Loan 1 overdue? {loan1.vencido()}")
    print("-" * 50)

    # Simulate a loan from the past to test overdue status
    past_date = datetime.date(2025, 6, 14)
    print("--- Initial Loan 2 (Past Date) ---")
    print(loan2)
    print(f"Is Loan 2 overdue? {loan2.vencido()}")
    print("-" * 50)

    # Mostrar, Aumentar, y pagar deuda de multa
    print("--- Initial Loan 2 (Multa) ---")
    print(f"Multa Actual: ${loan2.multa}")
    loan2.actualizar_multa()
    print(f"Multa de Actulizar: ${loan2.multa}")
    value = 2000
    loan2.pagar_multa(value)
    print(f"Pago invalido: ${loan2.multa}, Pago: ${value}")
    value = loan2.pagar_multa(loan2.multa)
    print(f"Multa Pagada: ${loan2.multa}, Pago: ${value}\n")

    # Mark loan1 as returned
    loan1.marcar_devuelto()
    print("\n--- Loan 1 After Marking as Returned ---")
    print(loan1)
    print("-" * 50)

    # Check loan2 again after some time (it should still be overdue if not returned)
    print("\n--- Loan 2 (After paid fine ) ---")
    print(loan2)
    print("-" * 50)

# Modelo Libro
if Test == "libro":
    print("--- Testing Libro Class ---")

    # Test Case 1: Create a new book instance and print its details
    print("\nTest Case 1: Creating a new book and printing its details.")
    book1 = Libro(
        id="B001",
        titulo="Cien años de soledad",
        genero="Realismo Mágico",
        autor="Gabriel García Márquez",
        editorial="Editorial Sudamericana",
        fecha_publicacion="1967-05-30",
    )
    print(book1)
    print("-" * 50)

    # Test Case 2: Create another book instance and convert it to a dictionary
    print("\nTest Case 2: Creating another book and converting it to a dictionary.")
    book2 = Libro(
        id="B002",
        titulo="Don Quijote de la Mancha",
        genero="Novela de caballerías",
        autor="Miguel de Cervantes",
        editorial="Francisco de Robles",
        fecha_publicacion="1605-01-16",
    )
    book2_dict = book2.to_dict()
    print(f"Book 2 as dictionary: {book2_dict}")
    print("-" * 50)

    # Test Case 3: Verify data types and access attributes directly
    print("\nTest Case 3: Verifying data types and direct attribute access.")
    print(f"Type of book1: {type(book1)}")
    print(f"Book1 ID: {book1.id}, Type: {type(book1.id)}")
    print(f"Book1 Title: {book1.titulo}, Type: {type(book1.titulo)}")
    print(
        f"Book1 Publication Date: {book1.fecha_publicacion}, Type: {type(book1.fecha_publicacion)}"
    )
    print("-" * 50)

    # Test Case 4: Check if the dictionary conversion is accurate
    print("\nTest Case 4: Checking accuracy of to_dict() method.")
    expected_dict = {
        "id": "B001",
        "titulo": "Cien años de soledad",
        "genero": "Realismo Mágico",
        "autor": "Gabriel García Márquez",
        "editorial": "Editorial Sudamericana",
        "fecha_publicacion": "1967-05-30",
    }
    if book1.to_dict() == expected_dict:
        print("to_dict() for book1 matches expected dictionary.")
    else:
        print("to_dict() for book1 does NOT match expected dictionary.")
    print("-" * 50)

    print("\n--- Libro Class Testing Complete ---")

# Modelo Usuario
if Test == "usuario":
    print("--- Testing Usuario Class ---")

    # Test Case 1: Create a new user instance with all parameters and print its details
    print(
        "\nTest Case 1: Creating a user with all its parameters and print its details."
    )
    user1 = Usuario(
        "1",
        "Alice",
        "Smith",
        "alice@gmail.com",
        "Barrio morena de la sal",
        "3220268742",
        afiliacion=True,
    )
    print(user1)
    print("-" * 50)

    # Test Case 2: Create another user instance with only required parameters (defaults for optional)
    print(
        "\nTest Case 2: Creating another user with only required parameters (defaults for optional)."
    )
    user2 = Usuario("2", "Bob", "Johnson", "bob@gmail.com", afiliacion=True)
    print(user2)
    print("-" * 50)

    # Test Case 3: Convert a user object to a dictionary
    print("\nTest Case 3: Converting a user object to a dictionary.")
    user1_dict = user1.to_dict()
    print(f"User 1 as dictionary: {user1_dict}")
    print("-" * 50)

    # Test Case 4: Verify data types and access attributes directly
    print("\nTest Case 4: Verifying data types and direct attribute access.")
    print(f"Type of user1: {type(user1)}")
    print(f"User1 Name: {user1.nombre}, Type: {type(user1.nombre)}")
    print(f"User1 Email: {user1.correo}, Type: {type(user1.correo)}")
    print(f"User1 Affiliation: {user1.afiliacion}, Type: {type(user1.afiliacion)}")
    print("-" * 50)

    # Test Case 5: Check if the dictionary conversion is accurate for user1
    print("\nTest Case 5: Checking accuracy of to_dict() method for user1.")
    expected_user1_dict = {
        "id": "1",
        "nombre": "Alice",
        "apellido": "Smith",
        "correo": "alice@gmail.com",
        "residencia": "Barrio morena de la sal",
        "telefono": "3220268742",
        "afiliacion": True,
    }
    if user1.to_dict() == expected_user1_dict:
        print("to_dict() for user1 matches expected dictionary.")
    else:
        print("to_dict() for user1 does NOT match expected dictionary.")
    print("-" * 50)

    # Test Case 6: Check if the dictionary conversion is accurate for user2 (with defaults)
    print(
        "\nTest Case 6: Checking accuracy of to_dict() method for user2 (with defaults)."
    )
    expected_user2_dict = {
        "id": "2",
        "nombre": "Bob",
        "apellido": "Johnson",
        "correo": "bob@gmail.com",
        "residencia": "",
        "telefono": "",
        "afiliacion": True,
    }

    if user2.to_dict() == expected_user2_dict:
        print("to_dict() for user2 matches expected dictionary.")
    else:
        print("to_dict() for user2 does NOT match expected dictionary.")
    print("-" * 50)

    print("\n--- Usuario Class Testing Complete ---")
