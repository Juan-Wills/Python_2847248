class Usuario:
    def __init__(self, id, nombre, apellido, correo, residencia='', telefono='', afiliacion= False):
        self.id = id
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.residencia= residencia
        self.telefono= telefono
        self.afiliacion= afiliacion


    def __str__(self):
        return (
                "Detalles del Usuario:\n"
                f"ID: {self.id}\n"
                f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"Correo: {self.correo}\n"
                f"Telefono: {self.telefono}\n"
                f"Direccion de Residencia: {self.residencia}\n"
                f"Afiliacion: {'Afiliado' if self.afiliacion else 'No afiliado'}"
        )
        
    def to_dict(self):
        return vars(self)