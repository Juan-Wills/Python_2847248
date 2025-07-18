import json
import pytest
from Biblioteca.services.biblioteca_service import json_data_path, retrieve_data, save

# Read the existing data from the JSON file
def test_open_json_files():
    print("\nAbriendo archivos JSON para lectura y escritura...")
    with pytest.raises(FileNotFoundError):
        # Attempting to open a non-existent file
        with open(json_data_path('data.json'), 'r', encoding='utf-8'):
            pass

        # Opening libros.json to read existing book data
        with open(json_data_path('libros.json'), 'r', encoding='utf-8') as file:
            assert isinstance(json.load(file), dict), "El archivo libros.json no contiene un diccionario válido."

        # Opening usuarios.json to read existing book data
        with open(json_data_path('usuarios.json'), 'w', encoding='utf-8') as file:
            assert isinstance(json.load(file), dict), "El archivo usuarios.json no contiene un diccionario válido."

        # Opening prestamos.json to read existing book data
        with open(json_data_path('prestamos.json'), 'w', encoding='utf-8') as file:
            assert isinstance(json.load(file), dict), "El archivo prestamos.json no contiene un diccionario válido."

# Test retrieving data from JSON files
def test_retrieve_data():
    print("\nProbando la funcion retrieve_data...")
    # Test retrieving data from libros.json
    libros = retrieve_data('libros.json', 'libros')
    assert isinstance(libros, dict), "La funcion retrieve_data no devolvio un diccionario valido para libros."

    if not libros:
        assert libros == {'libros', []}, "Se creo una estructura valida para guardar la informacion."

# Test saving data to JSON files
def test_save_data():
    print("\nProbando la funcion save..")
    # Test saving data to libros.json
    libros = {'libros': [{'titulo': 'Libro de prueba', 'autor': 'Autor de prueba', 'anio_publicacion': 2023}]}
    assert save('libros.json', libros) == True, "La funcion save guardo los datos correctamente en libros.json."


    libros = {'titulo': 'Libro de prueba', 'autor': 'Autor de prueba', 'anio_publicacion': 2023}
    assert save('libros.json', libros) == False, "La estructura de datos es invalida."


    