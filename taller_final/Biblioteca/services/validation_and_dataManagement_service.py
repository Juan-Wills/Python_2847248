import re 
import json
import datetime
from pathlib import Path
# Importing classes for attribute and name use
from models.libro import Libro
from models.usuario import Usuario 
from models.prestamo import Prestamo

# Input validation
def validate_input_format(
    input, mode="simple_format", special_chars: str = None, optional=False
) -> bool:
    if mode == "simple_format":
        if optional and input == "":
            return True

        if isinstance(special_chars, str):
            pass
        elif not (special_chars is None):
            print(
                "Error: El argumento special_chars debe ser una cadena de caracteres."
            )
            print("Por lo tanto, puede que el resultado no sea el esperado.")

        escaped_special_chars = re.escape(special_chars) if special_chars else ""

        if re.fullmatch(rf"[a-zA-Z0-9\s{escaped_special_chars}]+", input):
            return True
        print(
            "Error: El valor ingresado es invalido, por favor evitar caracteres speciales como #$%@."
        )
        return False

    if mode == "date":
        if optional and input == "":
            return True
        try:
            if datetime.datetime.strptime(input, "%d/%m/%Y"):
                return True
        except ValueError:
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

        if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", input):
            return True
        print(
            "Error: El formato de correo es invalido, por favor ingresar un correo valido."
        )
        return False

    if mode == "phone":
        if optional and input == "":
            return True

        if re.fullmatch(
            r"\+?\d{1,3}[-\s]?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,9}", input
        ):
            return True
        print(
            "Error: El formato de telefono es invalido, por favor ingresar un telefono valido."
        )
        return False

    print(
        "Error Final de Funcion: No se aplico ningun filtro por un error en los parametros, asegurece que esten bien asignados."
    )
    return False


def validate_menu_options(
    option, min_args=1, max_args=5, type=None, mode=None, object_name=None
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
            if (
                object_name == "usuario"
                or object_name == "libro"
                or object_name == "prestamo"
            ):
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
    if not re.search(r"[.json]$", file_name):
        file_name += ".json"

    path = str(Path.cwd().joinpath(f"Biblioteca/data/{file_name}"))
    if "taller_final" not in str(Path.cwd()):
        path = "taller_final/" + path
    try:
        # Just to check if the file exists
        with open(path, "r", encoding="utf-8"):
            pass
    except FileNotFoundError:
        return None
    return path


# Data manipulation
def retrieve_data(file_name, obj_name) -> dict:
    path = json_data_path(file_name)

    try:
        with open(path, "r", encoding="utf-8") as file:
            return convert_dict_to_obj(
                json.load(file), globals()[obj_name.capitalize()]
            )

    except FileNotFoundError:
        print(
            f"Error: No se pudo encontrar el archivo en {path}. Asegurese de que el archivo exista."
        )

    except json.JSONDecodeError:
        save(
            path, {obj_name + "s": []}
        )  # Create an valid structure if it doesn't exist
        return None


def save(path, data: list) -> bool:
    try:
        header = list(data.keys())[0]
        with open(path, "w", encoding="utf-8") as file:
            data = {header: [element.to_dict() for element in data[header]]}
            json.dump(data, file, indent=2)
            return True
    except FileNotFoundError:
        print(
            f"Error: No se pudo encontrar el archivo, Asegurese de que el archivo exista"
        )


def autoincrement(obj_name, data_file_name, pos=-1) -> str | None:
    result = None
    if isinstance(obj_name, str):
        obj_name = obj_name.lower()

        if not (obj_name == "prestamo" or obj_name == "libro" or obj_name == "usuario"):
            print(
                "Error: El nombre del objeto debe ser 'prestamo', 'libro' o 'usuario'."
            )
            return None
    else:
        print(
            "Error: El nombre del objeto debe ser una cadena de caracteres, por favor ingrese un nombre valido."
        )
        return None

    data = retrieve_data(data_file_name, obj_name)

    if not data:
        print(
            f"Error: los argumentos no son validos, verifique que el nombre del archivo {data_file_name} sea valido, y que el nombre del objeto este bien escrito."
        )
        return None

    obj_name = obj_name + "s"  # Convert to plural form for the key

    try:
        result = int(data[obj_name][-1].id) + 1
    except KeyError:
        result = "1"

    except IndexError:
        if len(data[obj_name]) == 0:
            result = "1"
        else:
            print(
                f"Error: No se pudo encontrar el ultimo '{obj_name}' en el archivo '{data_file_name}'."
            )
            return None
    return str(result)


def convert_dict_to_obj(data: dict, obj_type) -> dict:
    try:
        objects = []
        header = list(data.keys())[0]
        for obj in data[header]:
            objects.append(obj_type(**obj))
        data[header] = objects
        return data
    except TypeError as e:
        print(
            f"Error: No se pudo convertir el diccionario a objetos de tipo {obj_type.__name__}. Detalles: {e}"
        )
        return None


def get_feat(object_name: str, index: str, all= False) -> str | bool:
    try:
        index = int(index) - 1
    except ValueError:
        print(
            "Error: El valor ingresado no es un numero, por favor ingrese un numero que corresponda a las opciones del menu de navegacion."
        )
        return False

    object_name = object_name.lower()

    if object_name == "usuario":
        object_name = [
            "nombre",
            "apellido",
            "correo",
            "residencia",
            "telefono",
            "afiliacion",
            "id",
        ]

    if object_name == "libro":
        object_name = [
            "titulo",
            "autor",
            "genero",
            "editorial",
            "fecha_publicacion",
            "id",
            "disponible",
        ]

    if object_name == "prestamo":
        object_name = [
            "libro",
            "usuario",
            "fecha_prestamo",
            "fecha_devolucion",
            "id",
            "multa",
        ]

    try:
        if all:
            return object_name
        return object_name[index]
    except (IndexError, ValueError):
        print(
            "Error: Opcion no valida, por favor ingrese un numero dentro del rango de opciones."
        )
        return False
