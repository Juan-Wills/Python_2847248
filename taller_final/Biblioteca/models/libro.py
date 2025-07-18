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
        return (
                "Detalles del Libro\n"
                f"Id: {self.id}\n"
                f"Titulo: {self.titulo}\n"
                f"Genero: {self.genero}\n"
                f"Autor: {self.autor}\n"
                f"Fecha de Publicacion: {self.fecha_publicacion}\n"
                f"Editorial: {self.editorial}"
        )

    def to_dict(self):
        return vars(self)

    