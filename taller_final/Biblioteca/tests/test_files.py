import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import validation_and_dataManagement_service as vdm
import json
import pytest


# Read the existing data from the JSON file
def test_open_json_files():
    print("\nAbriendo archivos JSON para lectura y escritura...")
    with pytest.raises(TypeError):
        # Attempting to open a non-existent file
        assert open(vdm.json_data_path("data.json"), "r", encoding="utf-8")

        # Opening libros.json to read existing book data
        with open(vdm.json_data_path("libros.json"), "r", encoding="utf-8") as file:
            assert isinstance(
                json.load(file), dict
            ), "El archivo libros.json no contiene un diccionario válido."

        # Opening usuarios.json to read existing book data
        with open(vdm.json_data_path("usuarios.json"), "r", encoding="utf-8") as file:
            assert isinstance(
                json.load(file), dict
            ), "El archivo usuarios.json no contiene un diccionario válido."

        # Opening prestamos.json to read existing book data
        with open(vdm.json_data_path("prestamos.json"), "r", encoding="utf-8") as file:
            assert isinstance(
                json.load(file), dict
            ), "El archivo prestamos.json no contiene un diccionario válido."
