import datetime

class Prestamo:
    def __init__(self, id, libro, usuario, fecha_devolucion, fecha_prestamo=None):
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo if fecha_prestamo is not None else datetime.date.today()
        self.fecha_devolucion = fecha_devolucion
        self.multa= 0

    def marcar_devuelto(self):
        self.fecha_devolucion = datetime.date.today()
        print(f"Prestamo del libro '{self.libro.titulo}' entregado a '{self.usuario.nombre}' ha sido marcado como devuelto el dia {self.fecha_devolucion}.")

    def vencido(self):
        if self.fecha_devolucion < datetime.date.today():
            return True
        return False
    
    def aumentar_multa(self):
        aumento= 0
        today= datetime.date.today()
        if self.fecha_devolucion < today:
            days_difference= abs((self.fecha_devolucion - today).days)
            for _ in range(days_difference):
                aumento+= 2000
        self.multa= aumento - self.multa


    def pagar_multa(self, valor):
        if (self.multa - valor) == 0:
            self.multa-= valor
            return self.multa
        return False

    def __str__(self):
        return (f"Detalles de Prestamo:\n"
                f"  Libro: {self.libro.titulo}\n"
                f"  Usuario: {self.usuario.nombre}\n"
                f"  Fecha del Prestamo: {self.fecha_prestamo.strftime('%Y/%m/%d')}\n"
                f"  Fecha de Devolucion: {self.fecha_devolucion.strftime('%Y/%m/%d')}"
                )