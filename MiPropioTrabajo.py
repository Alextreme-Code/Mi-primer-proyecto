preguntacero=int(input("Este juego se responde con 1=SI y 0=NO, ¿Desea jugar?"))
if preguntacero==1:
    print("Reloj: 6:00 AM")
    primerapregunta=int(input("Acabas de despertar, ¿Deseas desayunar?"))
if primerapregunta==1:
                   
    prancia1=int(input("¿Desea comer cereal"))
    if prancia1==1:
        preguntados=int(input("Bien,¿Desea ir a la escuela?"))
        if preguntados==1:
            print("Usted se ha convertido en un buen estudiante")
            print("GANASTE")
    if prancia1==0:
        print("Tu mamá ha dicho que esta harta de que sigas reprobando y te castiga el celular")
        print("GAME OVER")
if primerapregunta==0:
    print("Usted ha decidido quedarse a dormir en la cama")
    print("Reloj: 9:00 AM")
    print("Tu mamá ha dicho que esta harta de seguir cuidandote a los 18 años y te saca de la casa")
    print("GAME OVER")
    
if preguntacero==0:
    print("Ok,adios")
