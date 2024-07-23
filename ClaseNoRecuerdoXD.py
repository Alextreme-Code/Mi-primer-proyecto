def retirarDinero():
    dRetirado=int(input("¿Cuanto dinero desea retirar? Solo retirar maximo $500"))
    print("Muy bien, porfavor, ingrese su tarjeta.")
    int(input("Para ingresar su tarjeta, escriba cualquier numero."))
    print("Retirando $", dRetirado, "en Efectivo.")
    if dRetirado<501:
        print("Pago completado")
    else:
        print("Error: 2013")
        print("No se ha logrado completar el retiro.")

def reclamarSaldo():
    print("Bien, usted va a reclamar su saldo mesnual, por favor, escoga su trabajo:")
    print("Albañil: presione 1")
    print("Secretario: presione 3")
    print("Abogado: presione 3")
    print("Maestro: presione 4")
    print("Sin trabajo: presione 5")
    rSaldo=int(input("Ingrese el numero de su trabajo:"))
    if rSaldo==1:
        print("Retirando $100 en Efectivo.")
    if rSaldo==2:
        print("Retirando $190 en Efectivo.")
    if rSaldo==3:
        print("Retirando $1000 en Efectivo.")
    if rSaldo==4:
        print("Retirando $1250 en Efectivo.")
    if rSaldo==1:
        print("Retirando $0 en Efectivo.")


accion=int(input("Bienvenido al cajero automatico, si desea retirar dinero, escriba 1, si desea reclamar saldo, escriba 2."))
if accion==1:
    retirarDinero()
if accion==2:
    reclamarSaldo()
