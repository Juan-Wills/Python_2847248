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
        self._fecha_creacion = datetime.date.today()

    def __str__(self):
        return f"""{super().__str__()}
        Interes Anual: {float(self.int_anual)} %
        Interes Mensual: $ {self.interes_mensual():,.2f}
        """

    def interes_mensual(self):
        return round((self.int_anual / 12) * self.saldo)

    def acumulado(self, fecha=datetime.date.today()):
        if isinstance(fecha, datetime.date):
            months_acum = round((fecha - self._fecha_creacion).days / 12)

            if months_acum == 0:
                return 0

            self.int_acum+= months_acum * self.interes_mensual()
            return (months_acum, self.int_acum)



class CuentaCorriente(x.CuentaBancaria):
    def __init__(self, titular, numero_cuenta, saldo, limite= 500_000):
        super().__init__(titular, numero_cuenta, saldo)
        self.limite = limite
        self._fecha_creacion = datetime.date.today()

    def retirar(self, cantidad):
        operation= self.saldo - cantidad
        if operation < 0 and abs(operation) > self.limite:
            raise OverflowError(f"La cantidad a retirar sobrepasa el limite de sobregiro {self.limite}")
            
        self.saldo-= cantidad

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo= saldo

