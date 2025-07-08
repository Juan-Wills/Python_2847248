import re
import datetime
import json
from pathlib import Path

libro_path = Path.cwd().joinpath('taller_final/Biblioteca/data/libros.json')

book_features= ['titulo', 'autor', 'genero', 'editorial', 'fecha_publicacion', 'id']

# Input validation
def validate_input_format(input):
    try:
        datetime.datetime.strptime(input, '%d/%m/%Y')
        return True
    except ValueError:
        if re.fullmatch(r'[a-zA-Z0-9\s]+', input):
            return True
        print('Error: El valor ingresado es invalido, por favor evitar caracteres speciales como #$%@')
        print("Si esta ingresando una fecha, ingresarla con el siguiente formato 'DD/MM/YYYY'\nD: dia\tM: mes\tY: anio")

def validate_menu_options(input, type= None, mode=None, max_args=6, min_args=0):
    try:
        input= int(input)
    except ValueError:
        print('No se ingreso ningun valor.')
    else:
        condition= max_args > input > min_args

        if mode == 'dual':
            max_args= 2

        if mode == 'inclusive':
            condition= max_args >= input >= min_args

        if mode == 'equal':
            condition= max_args == input or min_args == input

        if condition:
            if type == 'category':
                index= book_features[input-1]
                print(f"\nHa elegido la categoria {index.replace('_', ' de ').capitalize()}.\n")

            return True
        else:
            print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')

# Data manipulation
def retrieve_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_data(data, book= None):
    with open(libro_path, 'w', encoding='utf-8') as file:
        if book:
            data['libros'].append(vars(book))
        json.dump(data, file, indent= 2)

# CRUD books
def add_book(libro):
    while True:
        print("Desea guardar el libro?")
        print("1. Si\t2. No (Volver)")
        option= input("Ingresar opcion: ")

        if not validate_menu_options(option, type= 'dual'):
            continue

        if option == '1':
            save_data(retrieve_data(libro_path), book= libro)
            print("\nLibro guardado exitosamente.")
            return True

        print("Abortando operacion...")
        return


def find_book(filter_by: str, feature: str):
    filter_by= book_features[int(filter_by)-1]
    data= retrieve_data(libro_path)
    filtered_data= list(filter(lambda x: re.search(feature, x[filter_by]), data['libros']))

    if len(filtered_data) == 0:
        print(f'No se encontraron resultados con la caracteristica {filter_by.replace('_', ' de ').capitalize()}: {feature}.\n')
        return

    return filtered_data

def upd_book(book):
    while True:
        print('Que informacion desea modificar:')
        print('1. Titulo\t2. Autor\t3. Genero\t4. Editorial\t5. Fecha de Publicacion')
        modificar= input('Ingresar opcion: ')

        if not validate_menu_options(modificar, type= 'category'):
            continue

        attribute= book_features[int(modificar)-1]
        print(f"{attribute.capitalize()} anterior: {getattr(book, attribute)}")
        new_info= input('Ingresar nuevo valor: ')

        if new_info:
            setattr(book, attribute, new_info.title())

        while True:
            print(f"\nVista previa:\n{book}")
            print('Desea realizar mas cambios?')
            print("1. Si\t2. No")
            save= input("Ingresar opcion: ") 
            print('\n')

            if not validate_menu_options(save, type= 'dual'):
                continue

            match save:
                case '1':
                    break

            del_book(book.id)
            print(f"\nVista previa:\n{book}")

            if add_book(book):
                return True
            
def del_book(identification, mode= None):
    rm_book= None
    data= retrieve_data(libro_path)
    if mode == 'multi':
        pass
    for i, book in enumerate(data['libros']):
        if book['id'] == identification:
            rm_book= data['libros'].pop(i)
            save_data(data)
            break
    return rm_book
        
            

