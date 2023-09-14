from logica.Cuenta import Cuenta

if __name__ == '__main__':
    saldoInicial = float(input("Ingrese el saldo incial: "))
    cuenta = Cuenta(saldoInicial)weakref
    cuenta.interes()
    cuenta.imprimirSaldo()