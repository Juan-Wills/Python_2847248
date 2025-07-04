import re
import json

libro_path= 'C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/data/libros.json'

def retrieve_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Libros CRUD
def add_book(libro):
    print(f"\nVista previa:\n{libro}")
    while True:
        print("Desea guardar el libro?")
        print("1. Si\t2. No (Volver)")
        option= input("Ingresar opcion: ")
        if option == '1':
            data= retrieve_data(libro_path)
            with open(libro_path, 'w', encoding='utf-8') as file:
                data['libros'].append(vars(libro))
                json.dump(data, file, indent= 2)
            print("\nLibro guardado exitosamente.")
            return
        elif option == '2':
            print("Abortando operacion...")
            return
        else:
            print('Valor ingresado no valido, ingrese un valor que corresponda a las opciones del menu de navegacion.')


def find_book(filter_by: str, feature: str):
    data= retrieve_data(libro_path)
    filtered_data= list(filter(lambda x: re.search(feature, x[filter_by]), data['libros']))
    if len(filtered_data) == 0:
        print(f'No se encontraron resultados con la caracteristica {filter_by.replace('_', ' de ').capitalize()}: {feature}.\n')
        return

    for i, book in enumerate(filtered_data):
        print(f"""
        {i+1}.
        Titulo: {book['titulo']}
        Genero: {book['genero']}
        Autor: {book['autor']}
        Fecha de Publicacion: {book['fecha_publicacion']}
        Editorial: {book['editorial']}
        """)
    return True

def upd_book():
    pass


def del_book():
    pass