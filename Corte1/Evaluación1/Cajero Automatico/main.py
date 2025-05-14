from Cuenta import CuentaBancaria # type: ignore
from Menu import mostrar_menu # type: ignore

def ejecutar_cajero():
    cuenta = CuentaBancaria("Alejandro", 70000)  # Puedes cambiar el titular y el saldo

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción (1-4): "))

            if opcion == 1:
                cuenta.ver_saldo()

            elif opcion == 2:
                monto = float(input("Ingrese el monto a depositar: "))
                cuenta.depositar(monto)

            elif opcion == 3:
                monto = float(input("Ingrese el monto a retirar: "))
                cuenta.retirar(monto)

            elif opcion == 4:
                print("\nGracias por usar el cajero. Hasta pronto.")
                break

            else:
                print("\nOpción no válida. Intenta nuevamente.")

        except ValueError:
            print("\nEntrada no válida. Por favor, ingresa números.")

# Ejecutar
if __name__ == "__main__":
    ejecutar_cajero()