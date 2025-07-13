import sys
sys.path.append('C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/')
from services import biblioteca_service as bs
from models.libro import Libro
from models.usuario import Usuario

def test_find_book():
    # Test finding a book by title
    result = bs.find_book('titulo', 'Cien Años de Soledad')
    assert len(result) == 1
    assert result[0].titulo == 'Cien Años de Soledad'

    # Test finding a book by author
    result = bs.find_book('autor', 'Gabriel Garcia Marquez')
    assert len(result) == 1
    assert result[0].autor == 'Gabriel Garcia Marquez'

    # Test finding a book by genre
    result = bs.find_book('genero', 'Ficción')
    assert len(result) == 1
    assert result[0].genero == 'Ficción'

    # Test finding a book by non-existing feature
    result = bs.find_book('genero', 'Non-Existing Genre')
    assert result is None

def test_del_book():
    # Test deleting a book by ID
    book_id = '1'  # Assuming this ID exists in the test data
    result = bs.del_book(book_id)
    print(result)
    # assert result is True  # Assuming del_book returns True on success

    # # Test deleting a non-existing book
    # result = bs.del_book('999')  # Assuming this ID does not exist
    # assert result is False  # Assuming del_book returns False on failure

def test_get_feat():
    # Test getting a feature by index
    object_like = Libro('titulo', 'autor', 'genero', 'editorial', 'fecha', 'id')
    assert bs.get_feat(object_like, 1) == 'titulo'
    assert bs.get_feat(object_like, 3) == 'genero'

    # Test getting a feature with an invalid index
    assert bs.get_feat(object_like, 10) is False  # Assuming it returns False for invalid index

def test_save():
    # Test saving a book to a file
    usuario = Usuario('nombre', 'apellido', 'correo', 'residencia', 'telefono', True)
    bs.save(r'C:\\Users\\juand\\Documents\\Python\\Python_2847248\\taller_final\\Biblioteca\\data\\usuarios.json', {'usuarios': [usuario.to_dict()]})

    # Verify the file was created and contains the book data
    with open('test_libros.json', 'r') as f:
        data = f.read()
        assert '"titulo": "titulo"' in data
        assert '"autor": "autor"' in data

def test_retrieve_data():
    # Test retrieving data from a file
    data = bs.retrieve_data(r'C:\\Users\\juand\\Documents\\Python\\Python_2847248\\taller_final\\Biblioteca\\data\\usuarios.json')
    assert data is not None
    assert isinstance(data, dict)
    assert 'usuarios' in data

    # Test retrieving data from a non-existing file
    data = bs.retrieve_data('non_existing_file.json')
    assert data is None  # Assuming it returns None for non-existing files