import datetime
import json

"""
class Prestamo(Usuario, Libro):
    def __init__(self, fecha_prestamo, fecha_devolucion, correo, nombre,):
        super(Usuario).__init__(correo, nombre)
        self.fecha_prestamo= fecha_prestamo
        self.fecha_devolucion= fecha_devolucion

    
    def registrar_prestamo(self):
        pass
    
    def limite_entrega(self, usuario):
        dias_restantes= (datetime.date(self.fecha_devolucion) - datetime.date(self.fecha_prestamo)).days

        print("El prestamo ", end='')
        if dias_restantes > 0:
            print(f"expira en {dias_restantes} dias.")
            return
        elif dias_restantes == 0:
            print("expira hoy. Por favor, contactar al deudor.")
        else:
            print(f"expiro hace {abs(dias_restantes)} dias. Por favor, contactar urgentemente al deudor")
        print("\nDatos del usuario: ")
        print(f"Telefono: {usuario['telefono']}\tCorreo: {usuario['correo']}")

"""