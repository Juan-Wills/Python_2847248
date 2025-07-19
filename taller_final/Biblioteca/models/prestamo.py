import datetime

class Prestamo:
    def __init__(self, id, libro, usuario, fecha_prestamo, fecha_devolucion, multa= None):
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo if not (fecha_prestamo is None) else datetime.date.today().strftime('%d/%m/%Y')
        self.fecha_devolucion = fecha_devolucion
        self.multa= multa if not (multa is None) else 0

    def marcar_devuelto(self):
        self.fecha_devolucion = datetime.date.today().strftime('%d/%m/%Y')

    def vencido(self):
        if datetime.datetime.strptime(self.fecha_devolucion, '%d/%m/%Y').date() < datetime.datetime.today().date():
            return True
        return False
    
    def actualizar_multa(self):
        aumento= 0
        today= datetime.datetime.today().date()
        self.fecha_devolucion = datetime.datetime.strptime(self.fecha_devolucion, '%d/%m/%Y').date()
        if self.fecha_devolucion < today:
            days_difference= abs((self.fecha_devolucion - today).days)
            for _ in range(days_difference):
                aumento+= 2000

            if self.multa != aumento:
                self.multa= aumento - self.multa 

        elif self.fecha_devolucion >= today:
            self.multa= 0
        
        self.fecha_devolucion = self.fecha_devolucion.strftime('%d/%m/%Y')


    def pagar_multa(self, valor):
        if (self.multa - valor) == 0:
            self.multa-= valor
        return self.multa
    
    def to_dict(self):
        return vars(self)

    def __str__(self):
        return (f"Detalles de Prestamo\n"
                f"  Libro ID: {self.libro}\n"
                f"  Correo del Usuario: {self.usuario}\n"
                f"  Fecha del Prestamo: {self.fecha_prestamo}\n"
                f"  Fecha de Devolucion: {self.fecha_devolucion}"
                )