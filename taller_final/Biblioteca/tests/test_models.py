import sys
sys.path.append('C:/Users/juand/Documents/Python/Python_2847248/taller_final/Biblioteca/')
from models.libro import Libro

def test_model_libro():
    text_to_print= """
    Id: 1
    Titulo: Cien Anios De Soledad
    Genero: Novela
    Autor: Gabriel Garcia Marquez
    Fecha de Publicacion: 27/05/1967
    Editorial: Casa Penguiene
    """
    # Test data type
    type(Libro('Cien anios de soledad', 'Novela', 'Gabriel Garcia Marquez', 'Casa penguiene', '27/05/1967')) == Libro

    # Test printing
    print(Libro('Cien anios de soledad', 'Novela', 'Gabriel Garcia Marquez', 'Casa penguiene', '27/05/1967')) == text_to_print

def test_():
    pass
def test_():
    pass

print(Libro('Cien anios de soledad', 'Novela', 'Gabriel Garcia Marquez', 'Casa penguiene', '27/05/1967').__dict__)