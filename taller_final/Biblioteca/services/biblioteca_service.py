import re
import datetime
import json
from models.libro import Libro
from models.usuario import Usuario
from models.prestamo import Prestamo
from tests.test_views import test_mode
from pathlib import Path

# Input validation
def validate_input_format(input, mode="simple_format", special_chars: str= None, optional=False) -> bool:
    if mode == "simple_format":
        if optional and input == "":
            return True
        
        if isinstance(special_chars, str):
            pass
        elif not (special_chars is None):
            print("Error: El argumento special_chars debe ser una cadena de caracteres.")
            print("Por lo tanto, puede que el resultado no sea el esperado.")

        escaped_special_chars = re.escape(special_chars) if special_chars else ''

        if re.fullmatch(rf"[a-zA-Z0-9\s{escaped_special_chars}]+",  input):
            return True
        print(
            "Error: El valor ingresado es invalido, por favor evitar caracteres speciales como #$%@."
        )
        return False

    if mode == "date":
        if optional and input == "":
            return True

        if datetime.datetime.strptime(input, "%d/%m/%Y"):
            return True
        print(
            'Error: El formato de fecha es invalido, por favor ingresar la fecha con el siguiente formato "DD/MM/YYYY"'
        )
        return False

    if mode == "boolean":
        if optional and input == "":
            return True

        if input.lower() == "si":
            return True
        print('Error: El valor ingresado no es valido, por favor ingresar "Si" o "No".')
        return False

    if mode == "email": 
        if optional and input == "":
            return True
        
        if re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', input):  
            return True
        print("Error: El formato de correo es invalido, por favor ingresar un correo valido.")
        return False
    
    if mode == "phone":
        if optional and input == "":
            return True 
            
        if re.fullmatch(r'\+?\d{1,3}[-\s]?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,9}', input):
            return True
        print("Error: El formato de telefono es invalido, por favor ingresar un telefono valido.")
        return False

    print("Error Final de Funcion: No se aplico ningun filtro por un error en los parametros, asegurece que esten bien asignados.")
    return False
    
def validate_menu_options(
    option, min_args=1, max_args=5, type=None, mode=None, object_name= None
) -> bool:
    try:
        option = int(option)
    except ValueError:
        print(
            "Error: El valor ingresado no es un numero, por favor ingrese un numero que corresponda a las opciones del menu de navegacion."
        )
        return False

    condition = max_args >= option >= min_args

    if mode == "exclusive":
        condition = max_args > option > min_args

    if mode == "equal":
        condition = max_args == option or min_args == option

    if condition:
        if type == "category":
            if object_name == 'usuario' or object_name == 'libro' or object_name == 'prestamo':
                print(
                    f"\nHa elegido la categoria {get_feat(object_name, option).replace('_', ' de ').capitalize()}.\n"
                )
            else:
                print("\nHa elegido una categoria valida.")
        return True
    else:
        print(
            "Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion."
        )
        return False


# Path management
def json_data_path(file_name) -> str:
    if not re.search(r'[.json]$', file_name):
        file_name += '.json'

    path= str(Path.cwd().joinpath(f"Biblioteca/data/{file_name}"))

    if "taller_final" not in str(Path.cwd()):
        path= "taller_final/" + path  

    try:
        # Just to check if the file exists
        with open(path, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        return None  
    return path


# Data manipulation
def retrieve_data(file_name, obj) -> dict:
    path= json_data_path(file_name)

    try:
        with open(path, "r", encoding="utf-8") as file:
            return convert_dict_to_object(json.load(file), globals()[obj.capitalize()])

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en {path}. Asegurese de que el archivo exista.")
        return None
    
    except json.JSONDecodeError:
        if save(path, {"--header--": []}):  # Create an valid structure if it doesn't exist
            return retrieve_data(file_name, obj)
        return None

def save(path, data: list) -> bool:
    try:
        header= list(data.keys())[0]
        with open(path, "w", encoding="utf-8") as file:
            data = {header: [element.to_dict() for element in data[header]]}
            json.dump(data, file, indent=2)
            return True
    except FileNotFoundError:
        print(
            f"Error: No se pudo encontrar el archivo libros.json. Asegurese de que el archivo exista"
        )


def autoincrement(obj_name, data_file_name, pos=-1) -> str | None:
    result = None
    if isinstance(obj_name, str):
        obj_name = obj_name.lower()

        if not (obj_name == 'prestamo' or obj_name == 'libro' or obj_name == 'usuario'):
            print("Error: El nombre del objeto debe ser 'prestamo', 'libro' o 'usuario'.")
            return None
    
    data = retrieve_data(data_file_name, obj_name)

    if not data:
        print(f"Error: los argumentos no son validos, verifique que el nombre del archivo {data_file_name} sea valido, y que el nombre del objeto este bien escrito.")
        return None
    
    try:
        result = int(data[obj_name][pos].id) + 1
    except KeyError:
        result = "1"
    return str(result)


def convert_dict_to_object(data: dict, obj_type) -> dict:
    objects = []
    header = list(data.keys())[0]
    for obj in data[header]:
        objects.append(obj_type(**obj))
    data[header]= objects
    return data


def get_feat(object_name: str, index : str) -> str | bool:
    index = int(index) -1
    object_name= object_name.lower()

    if object_name == 'usuario':
        object_name = [
            "nombre",
            "apellido",
            "correo",
            "residencia",
            "telefono",
            "afiliacion",
            "id",
        ]

    if object_name == 'libro':
        object_name = [
            "titulo",
            "autor",
            "genero",
            "editorial",
            "fecha_publicacion",
            "id",
        ]

    if object_name == 'prestamo':
        object_name= [
            "libro",
            "usuario",
            "fecha_prestamo",
            "fecha_devolucion",
            "id",
            "multa",
        ]

    try:
        return object_name[index]
    except (IndexError, ValueError):
        print(
            "Error: Opcion no valida, por favor ingrese un numero dentro del rango de opciones."
        )
        return False

# --------------------------------------------------------------------------------------------------- #
# Books data from json file
data= retrieve_data('libros.json', 'libro')

# CRUD books
def add_book(libro: Libro) -> bool:
    if not data.get("libros", None):
        data = {"libros": []}
    data["libros"].append(libro)

    if test_mode:
        return True
        
    if save(json_data_path('libros.json'), data):
        return True
    else: 
        print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
        return False


def find_book(filter_by: str, feature: str, all=False) -> list | bool:
    if all:
        return data["libros"]

    # Filter books by the specified feature
    filtered_data= list(
        filter(lambda x: re.search(feature, getattr(x, filter_by), flags= re.I), data["libros"])
    ) 

    if len(filtered_data) == 0:
        return False

    return filtered_data


def upd_book(book: Libro) -> bool:
    if isinstance(book, Libro):
        for i, b in enumerate(data["libros"]):
            if b.id == book.id:
                data["libros"][i] = book
                break

        if test_mode:
            return True             

        if save(json_data_path('libros.json'), data):
            return True
        else:
            print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
            return False


def del_book(identification: str | list, mode="single", sort=False) -> list | bool:
    rmd_book = [] 

    if mode == "multi":
        for id in identification:
            for j, libro in enumerate(data["libros"]):
                if libro.id == id:
                    if i is None:
                        i = j
                    rmd_book.append(data["libros"].pop(j))

    if mode == "single":
        for i, book in enumerate(data["libros"]):
            if book.id == identification:
                rmd_book = data["libros"].pop(i)
                break

    if sort:
        for book in data["libros"][i:]:
            book.id = autoincrement("libro", 'libros.json', pos= i - 1)
            i += 1

        data["libros"].sort(key=lambda x: x.id)

    if rmd_book:
        if test_mode:
            return rmd_book
        
        if save(json_data_path('libros.json'), data):
            return rmd_book
        else:
            print("Error: No se pudo eliminar libro en la base de datos")
    return False

# Users data from json fil
data= retrieve_data('libros.json', 'libro')

# CRUD users
def add_user(user: Usuario) -> bool:
    if not data.get("usuarios"):
        data = {"usuarios": []}
    data["usuarios"].append(user)

    if test_mode:
        return True

    if save(json_data_path('usuarios.json'), data):
        print("\nUsuario guardado exitosamente.")
        return True
    else:
        print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
    return False


def find_user(filter_by: str, feature: str, all=False) -> list | bool:
    if all:
        return data["usuarios"]
    
    # Filter users by the specified feature
    filtered_data= list(
        filter(lambda x: re.search(feature, getattr(x, filter_by), flags= re.I), data["usuarios"])
    )

    if len(filtered_data) == 0:
        return False
    return filtered_data

def upd_user(user: Usuario) -> bool:
    if isinstance(user, Usuario):
        for i, u in enumerate(data["usuarios"]):
            if u.id == user.id:
                data["usuarios"][i] = user
                break

            if test_mode:
                return True

            if save(json_data_path('usuarios.json'), data):
                return True
            else:
                print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
                return False


def del_user(identification: str | list, mode="single", sort=False) -> list | bool:
    rmd_user = [] 
    
    if mode == "multi":
        for id in identification:
            for j, usuario in enumerate(data["usuarios"]):
                if usuario.id == id:
                    if i is None:
                        i = j
                    rmd_user.append(data["usuarios"].pop(j))

    if mode == "single":
        for i, book in enumerate(data["usuarios"]):
            if book.id == identification:
                rmd_user = data["usuarios"].pop(i)
                break

    if sort:
        for book in data["usuarios"][i:]:
            book.id = autoincrement("usuario", 'usuarios.json', pos= i - 1)
            i += 1

        data["usuarios"].sort(key=lambda x: x.id)

    if rmd_user:

        if test_mode:
            return rmd_user

        if save(json_data_path('usuarios.json'), data):
            return rmd_user
        else:
            print("Error: No se pudo eliminar al usuario la base de datos")
    return False

# Loans data from json file
data= retrieve_data('prestamos.json', 'prestamo')

# CRUD loans
def add_loan(loan: Prestamo):
    data["prestamos"].append(loan)

    if test_mode:
        return True

    if save(json_data_path('prestamos'), data):
        return True
    print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
    return False


def find_loan(filter_by: str, feature: str, all=False):
    if all:
        return data["prestamos"]
    
    filtered_data= list(
        filter(lambda x: re.search(feature, getattr(x, filter_by), flags= re.I), data["prestamos"])
    )  # Filter loans by the specified feature

    if len(filtered_data) == 0:
        return False
    return filtered_data


def upd_loan_devolution(loan: Prestamo):
    if isinstance(loan, Prestamo):
        for i, l in enumerate(data["prestamos"]):
            if l.id == loan.id:
                loan.multa = 0
                data["prestamos"][i] = loan
                break

        if test_mode:
            return True

        if save(json_data_path('prestamos.json'), data):
            return True
        else:
            print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
            return False

# Search and update fines
def find_fine(filter_by: str, feature: str, all= False):
    if all:
        return data["prestamos"]
    
    filtered_data= list(
        filter(lambda x: re.search(feature, getattr(x, filter_by), flags= re.I), data["prestamos"])
    )  # Filter loans by the specified feature

    if len(filtered_data) == 0:
        return False
    
    for loan in filtered_data:
        if loan.vencido():
            print(f"El prestamo del libro '{loan.libro.titulo}' al usuario '{loan.usuario.nombre}' esta vencido.")
            loan.actualizar_multa()
        else:
            print(f"El prestamo del libro '{loan.libro.titulo}' al usuario '{loan.usuario.nombre}' no tiene multa pendiente.")
    return filtered_data


def pay_fine(loan: Prestamo, to_pay: int) -> bool:
    for i, loan in enumerate(data["prestamos"]):

        if loan.id == loan.id:

            if loan.vencido():
                
                if loan.pagar_multa(to_pay) != 0:
                    print("Valor insuficiente para pagar multa, por favor ingrese el valor exacto.")
                    print(f"Valor de multa pendiente: ${loan.multa}")
                    return False
                break
            else:
                print(f"El prestamo del libro '{loan.libro.titulo}' no tiene multa pendiente.")
                return False

        data["prestamos"][i] = loan

        return True
                
        if test_mode:
            return True
        
        if save(json_data_path('prestamos.json'), data):
            return True
        else:
            print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
            return False
        
