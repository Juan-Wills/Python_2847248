class Usuario:
    def __init__(self, nombre, apellido, correo, residencia='NA', telefono='NA', afiliacion= False):
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.residencia= residencia
        self.telefono= telefono
        self.afiliacion= afiliacion


    def __str__(self):
        print(f"""
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Correo: {self.correo}
    Telefono: {self.telefono}
    Direccion de Residencia: {self.residencia}
    Afiliacion: {'Afiliado' if self.afiliacion else 'No afiliado'}
    """)