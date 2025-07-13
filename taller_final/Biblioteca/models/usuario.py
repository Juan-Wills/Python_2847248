class Usuario:
    def __init__(self, nombre, apellido, correo, residencia='', telefono='', afiliacion= False):
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.residencia= residencia
        self.telefono= telefono
        self.afiliacion= afiliacion


    def __str__(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Correo: {self.correo}
        Telefono: {self.telefono}
        Direccion de Residencia: {self.residencia}
        Afiliacion: {'Afiliado' if self.afiliacion else 'No afiliado'}
        """
        
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'residencia': self.residencia,
            'telefono': self.telefono,
            'afiliacion': self.afiliacion
        }