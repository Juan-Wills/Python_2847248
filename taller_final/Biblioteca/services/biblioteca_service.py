import re
from models.libro import Libro
from models.usuario import Usuario
from models.prestamo import Prestamo
from services.validation_and_dataManagement_service import (
    json_data_path,
    retrieve_data,
    save,
    autoincrement,
)
from tests.config import test_mode


# CRUD books
def add_book(libro: Libro) -> bool:
    if data:= retrieve_data("libros.json", "libro"):
        data["libros"].append(libro)

        if test_mode:
            print('\n'+'*'*50)
            print("Test mode on")
            print('*'*50)
            return True

        if save(json_data_path("libros.json"), data):
            return True
        else:
            print(
                "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
            )
            return False


def find_book(filter_by: str, feature: str, all=False) -> list | bool:
    if data:= retrieve_data("libros.json", "libro"):
        if all:
            if len(data["libros"]) == 0:
                return False
            return data["libros"]

        # Filter books by the specified feature
        filtered_data = list(
            filter(
                lambda x: re.search(feature, getattr(x, filter_by), flags=re.I),
                data["libros"],
            )
        )

        if len(filtered_data) == 0:
            return False

        return filtered_data


def upd_book(book: Libro) -> bool:
    if data:= retrieve_data("libros.json", "libro"):
        if isinstance(book, Libro):
            for i, b in enumerate(data["libros"]):
                if b.id == book.id:
                    data["libros"][i] = book
                    break

            if test_mode:
                print('\n'+'*'*50)
                print("Test mode on")
                print('*'*50)
                return True

            if save(json_data_path("libros.json"), data):
                return True
            else:
                print(
                    "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
                )
                return False


def del_book(identification: str | list, sort=False) -> list | bool:
    if data:= retrieve_data("libros.json", "libro"):
        i = None
        rmd_books = []
        try:

            for id in identification:
                for j, libro in enumerate(data["libros"]):
                    if libro.id == id.strip():
                        if i is None:
                            i = j
                        rmd_books.append(data["libros"].pop(j))
            if sort:
                try:
                    next_book = data["libros"][i]
                    next_book.id = int(autoincrement("libro", "libros.json", pos=i)) - 2
                    data["libros"][i] = next_book
                    id = int(next_book.id)

                    for book in data["libros"][i:]:
                        book.id = str(id + 1)
                        id = int(book.id)

                except IndexError:
                    pass

            if rmd_books:
                if test_mode:
                    print('\n'+'*'*50)
                    print("Test mode on")
                    print('*'*50)
                    return rmd_books

                if save(json_data_path("libros.json"), data):
                    return rmd_books
                else:
                    print("Error: No se pudo eliminar libro en la base de datos")
            return False

        except IndexError:
            print("Error: No se pudo eliminar el libro, verifique que el id sea correcto.")
            return False


# CRUD users
def add_user(user: Usuario) -> bool:
    if data:= retrieve_data("usuarios.json", "usuario"):
        data["usuarios"].append(user)

        if test_mode:
            print('\n'+'*'*50)
            print("Test mode on")
            print('*'*50)
            return True

        if save(json_data_path("usuarios.json"), data):
            return True
        else:
            print(
                "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
            )
        return False


def find_user(filter_by: str, feature: str | bool, all=False) -> list | bool:
    if data:= retrieve_data("usuarios.json", "usuario"):
        if all:
            if len(data["usuarios"]) == 0:
                return False
            return data["usuarios"]

        # Filter users by the specified feature
        if isinstance(feature, bool):
            filtered_data = list(
                filter(lambda x: getattr(x, filter_by) == feature, data["usuarios"])
            )
        else:
            filtered_data = list(
                filter(
                    lambda x: re.search(feature, getattr(x, filter_by), flags=re.I),
                    data["usuarios"],
                )
            )

        if len(filtered_data) == 0:
            return False
        return filtered_data


def upd_user(user: Usuario) -> bool:
    if data:= retrieve_data("usuarios.json", "usuario"):
        if isinstance(user, Usuario):
            for i, u in enumerate(data["usuarios"]):
                if u.id == user.id:
                    data["usuarios"][i] = user
                    break

            if test_mode:
                print('\n'+'*'*50)
                print("Test mode on")
                print('*'*50)
                return True

            if save(json_data_path("usuarios.json"), data):
                return True
            else:
                print(
                    "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
                )
                return False
            

def del_user(identification: list, sort=False) -> list | bool:
    if data:= retrieve_data("usuarios.json", "usuario"):
        i = None
        rmd_user = []

        try:
            for id in identification:
                for j, usuario in enumerate(data["usuarios"]):
                    if usuario.id == id.strip():
                        if i is None:
                            i = j
                        rmd_user.append(data["usuarios"].pop(j))

            if sort:
                next_user = data["usuarios"][i]
                next_user.id = int(autoincrement("usuario", "usuarios.json", pos=i)) - 2
                data["usuarios"][i] = next_user
                id = int(next_user.id)

                for user in data["usuarios"][i:]:
                    user.id = str(id + 1)
                    id = int(user.id)
                    i += 1

            if rmd_user:
                if test_mode:
                    print('\n'+'*'*50)
                    print("Test mode on")
                    print('*'*50)
                    return rmd_user

                if save(json_data_path("usuarios.json"), data):
                    return rmd_user
                else:
                    print("Error: No se pudo eliminar al usuario la base de datos")
                    return False
        except IndexError as e:
            print(
                f"Error: No se pudo eliminar el usuario, verifique que el id sea correcto.\n{e}"
            )
            return False


# CRUD loans
def add_loan(loan: Prestamo):
    if data:= retrieve_data("prestamos.json", "prestamo"):
        data["prestamos"].append(loan)

        if test_mode:
            print('\n'+'*'*50)
            print("Test mode on")
            print('*'*50)
            return True

        if save(json_data_path("prestamos.json"), data):
            return True
        print(
            "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
        )
        return False

def find_loan(filter_by: str, feature: str, all=False):
    if data:= retrieve_data("prestamos.json", "prestamo"):
        if all:
            if len(data["prestamos"]) == 0:
                return False
            return data["prestamos"]

        filtered_data = list(
            filter(
                lambda x: re.search(feature, getattr(x, filter_by), flags=re.I),
                data["prestamos"],
            )
        )  # Filter loans by the specified feature

        if len(filtered_data) == 0:
            return False
        return filtered_data


def upd_loan_devolution(loan: Prestamo):
    if data:= retrieve_data("prestamos.json", "prestamo"):
        if isinstance(loan, Prestamo):
            for i, l in enumerate(data["prestamos"]):
                if l.id == loan.id:
                    loan.multa = 0
                    loan.marcar_devuelto()
                    data["prestamos"][i] = loan
                    break

            if test_mode:
                print('\n'+'*'*50)
                print("Test mode on")
                print('*'*50)
                return True

            if save(json_data_path("prestamos.json"), data):
                return True
            else:
                print(
                    "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
                )
                return False


# Update and pay fines
def book_loaned(book_title) -> bool:
    if data:= retrieve_data("prestamos.json", "prestamo"):
        for loan in data["prestamos"]:
            if getattr(loan, 'libro') == book_title:
                return loan.usuario
        return False


def upd_fines():
    if data:= retrieve_data("prestamos.json", "prestamo"):
        for loan in data["prestamos"]:
            if loan.vencido():
                loan.actualizar_multa()

        if test_mode:
            print('\n'+'*'*50)
            print("Test mode on")
            print('*'*50)
            return True

        if save(json_data_path("prestamos.json"), data):
            return True
        else:
            print(
                "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
            )
            return False


def pay_fine(loan: Prestamo, to_pay: int) -> bool:
    if data:= retrieve_data("prestamos.json", "prestamo"):
        i= None
        id_found= False
        for i, loans in enumerate(data["prestamos"]):
            if loans.id == loan.id:
                id_found = True
                if not loan.vencido() and loan.multa != to_pay:
                    return False
                break

        if not id_found:
            print("Error: No se pudo encontrar el prestamo, verifique que el ID sea correcto.")
            return False

        loan.pagar_multa(to_pay)

        if loan.multa == 0:
            data["prestamos"][i] = loan

            if test_mode:
                print('\n'+'*'*50)
                print("Test mode on")
                print('*'*50)
                return True

            if save(json_data_path("prestamos.json"), data):
                return True
            else:
                print(
                    "Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo"
                )
            return False
        else:
            return False
