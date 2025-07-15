if __name__ == "__main__":
    import sys
    import datetime
    from models.libro import Libro
    from models.usuario import Usuario
    from models.prestamo import Prestamo
    sys.path.append('C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/')

    # Elegir modelo
    Test= 'prestamo'.lower()

    # Testear Prestamo
    if Test == 'prestamo':
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

    if Test == 'libro':
        print(Libro('Cien anios de soledad', 'Novela', 'Gabriel Garcia Marquez', 'Casa penguiene', '27/05/1967').__dict__)