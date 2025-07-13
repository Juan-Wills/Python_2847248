import re
import datetime
import json
from models.libro import Libro
from pathlib import Path

libro_path = Path.cwd().joinpath('taller_final/Biblioteca/data/libros.json') if 'taller_final' not in str(Path.cwd()) else Path.cwd().joinpath('Biblioteca/data/libros.json')

# Input validation
def validate_input_format(input):
    try:
        datetime.datetime.strptime(input, '%d/%m/%Y')
        return True
    except ValueError:
        if re.fullmatch(r'[a-zA-Z0-9\s]+', input):
            return True
        print('Error: El valor ingresado es invalido, por favor evitar caracteres speciales como #$%@.')
        print("Si esta ingresando una fecha, ingresarla con el siguiente formato 'DD/MM/YYYY'\nD: dia\tM: mes\tY: anio")

def validate_menu_options(option, input= None,  min_args=0, max_args=6, type= None, mode=None):
    try:
        option= int(option)
    except ValueError:
        print('Error: El valor ingresado no es un numero, por favor ingrese un numero que corresponda a las opciones del menu de navegacion.')
        return False
    
    condition= max_args > option > min_args

    if mode == 'inclusive':
        condition= max_args >= option >= min_args

    if mode == 'equal':
        condition= max_args == option or min_args == option

    if condition:
        if type == 'category':
            print(f"\nHa elegido la categoria {input.replace('_', ' de ').capitalize()}.\n")
        return True
    else:
        print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')

# Data manipulation
def retrieve_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return from_dict_to_libro(json.load(file))
    
def save(data: list):
    try:
        with open(libro_path, 'w', encoding='utf-8') as file:
            data= {'libros': [libro.to_dict() for libro in data['libros']]}
            json.dump(data, file, indent= 2)
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo libros.json. Asegurese de que el archivo exista")

def autoincrement(pos= -1):
    result= None
    data= retrieve_data(libro_path)
    try:
        result= int(data['libros'][pos].id) + 1
    except KeyError:
        result= "1"
    return str(result)

def from_dict_to_libro(data):
    libros= []
    for libro in data['libros']:
        libros.append(
                    Libro(
                        id=libro['id'],
                        titulo=libro['titulo'],
                        genero=libro['genero'],
                        autor=libro['autor'],
                        editorial=libro['editorial'],
                        fecha_publicacion=libro['fecha_publicacion']
                    )
        )
    return {'libros': libros}

# CRUD books
def add_book(libro: Libro):
    while True:
        print("Desea guardar el libro?")
        print("1. Si\t2. No (Volver)")
        option= input("Ingresar opcion: ")

        if not validate_menu_options(option, type= 'dual'):
            continue

        if option == '1':
            data= retrieve_data(libro_path)
            data['libros'].append(libro)
            save(data)
            print("\nLibro guardado exitosamente.")
            return True

        print("Abortando operacion...")
        return


def find_book(filter_by: str, feature: str):
    data= retrieve_data(libro_path)
    filtered_data= list(filter(lambda x: re.search(feature, getattr(x, filter_by)), data['libros'])) # Filter books by the specified feature

    if len(filtered_data) == 0:
        print(f'No se encontraron resultados con la caracteristica {filter_by.replace('_', ' de ').capitalize()}: {feature}.\n')
        return

    return filtered_data

def upd_book(book):
    del_book(book.id)  # Remove the old book entry
    data= retrieve_data(libro_path)
    data['libros'].insert(int(book.id)-1, book)   # Update the book attribute in the data
    save(data)   # Save the updated data
    print(f"\nLibro actualizado exitosamente.")
    return True


def del_book(identification: str | list, mode= 'single', sort= False):
    rm_book= None
    i= None
    data= retrieve_data(libro_path)
    if mode == 'multi':
        rm_book= []
        for id in identification:
            for j, libro in enumerate(data['libros']):
                if libro.id == id:
                    if i is None:
                        i= j         
                    rm_book.append(data['libros'].pop(j))

    if mode == 'single':
        for i, book in enumerate(data['libros']):
            if book.id == identification:
                rm_book= data['libros'].pop(i)
                break

    if sort:
        for book in data['libros'][i:]:
            book.id= autoincrement(i-1)
            i += 1

        data['libros'].sort(key=lambda x: x.id)

    save(data)
    return rm_book
        
            

