class Libro:
    def __init__(
        self,
        titulo: str,
        genero: str,
        autor: str,
        editorial: str,
        fecha_publicacion: str,
        id: str,
    ):
        self.id= id
        self.titulo = titulo
        self.genero = genero
        self.autor = autor
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        

    def __str__(self):
        return f"""
    Id: {self.id}
    Titulo: {self.titulo}
    Genero: {self.genero}
    Autor: {self.autor}
    Fecha de Publicacion: {self.fecha_publicacion}
    Editorial: {self.editorial}
    """

    def to_dict(self):
        return vars(self)

    