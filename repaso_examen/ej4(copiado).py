while True:
    limiteInf = int(input("Introduce el límite inferior: "))
    limiteSup = int(input("Introduce el límite superior: "))

    if limiteInf > limiteSup:
        print ("El limite superior no puede ser mayor que el superior")
        break

    sumaDentro = 0
    cantidadFuera = 0
    tocaLimite = False

    print("Introduce números (0 para terminar), Intervalo abierto ({limiteInf},{limiteSup}): ")

    while True:
        numero = int(input("Numeros: "))
        if numero == 0:
            break
        if limiteInf < numero < limiteSup:
            sumaDentro += numero
        elif numero == limiteInf or numero == limiteSup:
            tocaLimite = True
            cantidadFuera += 1
        else:
            cantidadFuera += 1

    print ("\n-----Resultados-----")
    print (f"la suma de números dentro del intervalo {sumaDentro}")
    print (f"Cantidad de numeros fuera del intervalo {cantidadFuera}")