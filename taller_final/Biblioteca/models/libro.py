class Libro:
    def __init__(
        self,
        titulo: str,
        genero: str,
        autor: str,
        editorial: str,
        fecha_publicacion: str,
    ):
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        

    def __str__(self):  # rich
        return f"""
    Titulo: {self.titulo}
    Genero: {self.genero}
    Autor: {self.autor}
    Fecha de Publicacion: {self.fecha_publicacion}
    Editorial: {self.editorial}
    """
