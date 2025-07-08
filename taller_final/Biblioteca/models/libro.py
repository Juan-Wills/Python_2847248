from services.biblioteca_service import libro_path, retrieve_data

class Libro:
    def __init__(
        self,
        titulo: str,
        genero: str,
        autor: str,
        editorial: str,
        fecha_publicacion: str,
        id= None,
    ):
        if id:
            self.id= id
        else:
            self.id= self.autoincrement()
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        

    def __str__(self):  # rich
        return f"""
    Id: {self.id}
    Titulo: {self.titulo}
    Genero: {self.genero}
    Autor: {self.autor}
    Fecha de Publicacion: {self.fecha_publicacion}
    Editorial: {self.editorial}
    """
    def autoincrement(self):
        data= retrieve_data(libro_path)
        try:
            self.id= int(data['libros'][-1]['id']) + 1
        except KeyError:
            self.id= "1"
        return str(self.id)