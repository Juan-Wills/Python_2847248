import re
import datetime
import json
from models.libro import Libro
from models.usuario import Usuario
from models.prestamo import Prestamo
from pathlib import Path


# Input validation
def validate_input_format(input, mode="simple_format", special_chars: str= None, optional=False):
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
):
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
def json_data_path(file_name):
    return (
        Path.cwd().joinpath(f"taller_final/Biblioteca/data/{file_name}.json")
        if "taller_final" not in str(Path.cwd())
        else Path.cwd().joinpath(f"Biblioteca/data/{file_name}.json")
    )


# Data manipulation
def retrieve_data(path, obj):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return convert_dict_to_object(json.load(file), globals()[obj.capitalize()])

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en {path}. Asegurese de que el archivo exista.")
        return None
    
    except json.JSONDecodeError:
        print(f"Error: El archivo en {path} esta vacio o tiene un formato invalido. Se ha ingresado una estructura valida.")
        if save(path, {"--header--": []}):  # Create an empty file if it doesn't exist
            return retrieve_data(path, obj)
        return None

def save(path, data: list):
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


def autoincrement(obj_name, data_file, pos=-1):
    result = None
    if isinstance(obj_name, str):
        if obj_name == 'prestamo' or obj_name == 'libro' or obj_name == 'usuario':
            obj_name = obj_name.lower()
        else:
            print("Error: El nombre del objeto debe ser 'prestamo', 'libro' o 'usuario'.")
            return False
    
    data = retrieve_data(data_file, obj_name)
    
    try:
        result = int(data[obj_name][pos].id) + 1
    except KeyError:
        result = "1"
    return str(result)


def convert_dict_to_object(data: dict, obj_type):
    objects = []
    header = list(data.keys())[0]
    for obj in data[header]:
        objects.append(obj_type(**obj))
    data[header]= objects
    return data


def get_feat(object: str, index : str):
    index = int(index) -1
    object= object.lower()

    if object == 'usuario':
        object = [
            "nombre",
            "apellido",
            "correo",
            "residencia",
            "telefono",
            "afiliacion",
        ]

    if object == 'libro':
        object = [
            "titulo",
            "autor",
            "genero",
            "editorial",
            "fecha_publicacion",
            "id",
        ]

    if object == 'prestamo':
        object= [
            "id",
            "libro",
            "usuario",
            "fecha_prestamo",
            "fecha_devolucion",
        ]

    try:
        return object[index]
    except (IndexError, ValueError):
        print(
            "Error: Opcion no valida, por favor ingrese un numero dentro del rango de opciones."
        )
        return False

# Define the path for libros.json
libro_path = json_data_path("libros")

# CRUD books
def add_book(libro: Libro):
    data = retrieve_data(libro_path, 'libro')
    if not data.get("libros", None):
        data = {"libros": []}
    data["libros"].append(libro)
    if save(libro_path, data):
        return True
    else: 
        print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
        return False

def find_book(filter_by: str, feature: str):
    data = retrieve_data(libro_path, 'libro')
    filtered_data = list(
        filter(lambda x: re.search(feature, getattr(x, filter_by), flags= re.I), data["libros"])
    )  # Filter books by the specified feature

    if len(filtered_data) == 0:
        return False

    return filtered_data


def upd_book(book: Libro):
    if del_book(book.id):
        data = retrieve_data(libro_path, 'libro')
        if isinstance(book, Libro):
            data["libros"].insert(int(book.id) - 1, book)   # Update the data with the new updated book                  
            if save(libro_path, data):
                return True
            else:
                print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
                return False
    print("Error al eliminar libro en base de datos")


def del_book(identification: str | list, mode="single", sort=False):
    rmd_book = None
    i = None
    
    data = retrieve_data(libro_path, 'libro')
    if mode == "multi":
        rmd_book = []
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
            book.id = autoincrement(i - 1)
            i += 1

        data["libros"].sort(key=lambda x: x.id)

    if rmd_book:
        if save(libro_path, data):
            return rmd_book
        else:
            print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
    return False



# Define the path for usuarios.json
usuario_path = json_data_path("usuarios")

# Add, search users
def add_user(user: Usuario):
    while True:
        print("Desea guardar el usuario?")
        print("1. Si\t2. No (Volver)")
        option = input("Ingresar opcion: ")

        if not validate_menu_options(option, type="dual"):
            continue

        if option == "1":
            data = retrieve_data(usuario_path, 'usuario')
            if not data.get("usuarios"):
                data = {"usuarios": []}
            data["usuarios"].append(user)
            if save(usuario_path, data):
                print("\nUsuario guardado exitosamente.")
                return True
            else:
                print("Error: No se pudieron guardar los cambios, verifique los datos ingresados e intentelo de nuevo")
            return False

def find_user(filter_by: str, feature: str):
    data = retrieve_data(usuario_path, 'usuario')
    filtered_data = list(
        filter(lambda x: re.search(feature, getattr(x, filter_by), flags= re.I), data["usuarios"])
    )  # Filter users by the specified feature

    if len(filtered_data) == 0:
        return False
    return filtered_data
