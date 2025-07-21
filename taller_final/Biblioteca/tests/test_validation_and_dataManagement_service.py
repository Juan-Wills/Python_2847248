import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import validation_and_dataManagement_service as vdm
from models.usuario import Usuario
from pathlib import WindowsPath
from tests.config import test_mode


if test_mode:

    def test_get_feat():
        # Test getting a feature by index
        assert vdm.get_feat("libro", 1) == "titulo"
        assert vdm.get_feat("libro", 3) == "genero"

        # Test getting a feature with an invalid index
        assert (
            vdm.get_feat("libro", 10) is False
        )  # Assuming it returns False for invalid index

    def test_save():
        # Test saving a book to a file
        usuario = Usuario(
            "nombre", "apellido", "correo", "residencia", "telefono", True
        )
        vdm.save(
            r"C:\\Users\\juand\\Documents\\Python\\Python_2847248\\taller_final\\Biblioteca\\data\\usuarios.json",
            {"usuarios": [usuario]},
        )

    def test_retrieve_data():
        # Test retrieving data from a file
        data = vdm.retrieve_data("usuarios.json", "usuario")
        assert data is not None
        assert isinstance(data, dict)
        assert "usuarios" in data

        # Test retrieving data from a non-existing file
        data = vdm.retrieve_data("non_existing_file.json", "usuario")
        assert data is None  # Assuming it returns None for non-existing files

    def test_autoincrement():
        # Test autoincrement function
        current_id = vdm.autoincrement("prestamo", "prestamos.json")
        assert isinstance(current_id, str)
        assert int(current_id) > 0  # Assuming IDs start from 1

    def test_json_data_path():
        # Test json_data_path function
        path = vdm.json_data_path("usuarios.json")
        assert isinstance(path, WindowsPath)
        path = str(path)
        assert path.endswith("usuarios.json")

        # Test with a file that does not exist
        path = vdm.json_data_path("non_existing_file.json")
        assert path == None

else:
    print(
        "Se necesita activar el modo de prueba para ejecutar este archivo, edite el archivo 'config.py' y cambie 'test_mode' a True."
    )
