"""
Diseña una clase CuentaBancaria con:
· Atributos: titular, saldo, número de cuenta
· Métodos: depositar, retirar, consultar_saldo, transferir
· Validaciones apropiadas (no permitir saldos negativos)
"""

database = [{"titular": "Juan-Wills", "numero_cuenta": 795202589, "saldo": 120000}]
# keys= ['titular','numero_cuenta','saldo']


class CuentaBancaria:
    def __init__(self, titular: str, numero_cuenta: int, saldo: float = 0):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def __str__(self):
        return f"""
        Titular: {self.titular}
        Numero de Cuenta: {self.numero_cuenta}
        Saldo: {self.saldo}
        """

    def depositar(self, cantidad):
        if cantidad < 0:
            raise ValueError("No se pudo depositar el valor ingresado")

        self.saldo += cantidad

    def retirar(self, cantidad):
        if self.saldo - cantidad < 0:
            raise ValueError(
                f"No se permiten retirar menos del total del saldo disponible: {self.saldo}"
            )

        self.saldo -= cantidad

    def transferir(self, numero_cuenta, cantidad):
        if cantidad - self.saldo < 0:
            raise ValueError("Fondos insuficientes")

        existe_cuenta = False
        for i, cuentas in enumerate(database):
            if numero_cuenta == cuentas["numero_cuenta"]:
                existe_cuenta = True
                break

        if not existe_cuenta:
            raise ValueError("El numero de cuenta ingresado no existe")

        self.saldo -= cantidad
        database[i]["saldo"] += cantidad

    def consultar_saldo(self):
        return self.saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            raise ValueError("No se permiten valores negativos")

        self._saldo = saldo


def main():
    usuario = CuentaBancaria("Santi-Wills", 789654123, 50000)
    usuario.transferir(795202589, 50000)
    usuario.depositar(10000)
    usuario.retirar(5000)
    print(usuario.consultar_saldo)
    print(usuario)

if __name__ == "__main__":
    main()
