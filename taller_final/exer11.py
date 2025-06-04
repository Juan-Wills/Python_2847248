"""
Extiende la clase anterior creando CuentaAhorro y CuentaCorriente:
· CuentaAhorro: genera intereses mensuales
· CuentaCorriente: permite sobregiros hasta un límite
"""
from exer10 import CuentaBancaria

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, int_anual):
        pass



class CuentaCorriente(CuentaBancaria):
    def __init__(self):
        pass