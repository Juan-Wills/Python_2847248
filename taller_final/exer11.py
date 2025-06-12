"""
Extiende la clase anterior creando CuentaAhorro y CuentaCorriente:
· CuentaAhorro: genera intereses mensuales
· CuentaCorriente: permite sobregiros hasta un límite
"""

import exer10 as x
import datetime

db = x.database


class CuentaAhorro(x.CuentaBancaria):

    def __init__(self, titular, numero_cuenta, saldo, int_anual):
        super().__init__(titular, numero_cuenta, saldo)
        self.int_anual = int_anual
        self.int_acum = 0
        self.fecha_creacion = None

    def __str__(self):
        return f"""{super().__str__()}
        Interes Anual: {float(self.int_anual)} %
        Interes Mensual: $ {self.interes_mensual():,.2f}
        """

    def interes_mensual(self):
        return (self.int_anual / 12) * self.saldo

    def cobro_ints(self, fecha=datetime.date.today()):
        if isinstance(fecha, datetime):
            months_acum = round((fecha - self.fecha_creacion) * 30.4167)

            if months_acum == 0:
                return 0

            self.int_acum+= months_acum * self.interes_mensual()
            return self.int_acum

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @fecha_creacion.setter
    def fecha_creacion(self, fecha_creacion):
        if fecha_creacion:
            self._fecha_creacion= fecha_creacion
            return

        raise PermissionError("This attribute cannot be change.")


class CuentaCorriente(x.CuentaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite


cuentaA = CuentaAhorro("Diego", 123456789, 1_000_000, 2)
print(cuentaA.interes_mensual())

cuentaC = CuentaCorriente("Felipe", 1_000_000, 500_000)
