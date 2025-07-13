import sys
sys.path.append('C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/')
from services import biblioteca_service as bs
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
