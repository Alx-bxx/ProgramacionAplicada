class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def ver_saldo(self):
        print(f"\nSaldo actual: ${self.saldo:.2f}")

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"\nHas depositado ${monto:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("\nEl monto a depositar debe ser mayor a cero.")

    def retirar(self, monto):
        if monto <= 0:
            print("\nEl monto debe ser mayor a cero.")
        elif monto > self.saldo:
            print("\nFondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"\nHas retirado ${monto:.2f}. Nuevo saldo: ${self.saldo:.2f}")