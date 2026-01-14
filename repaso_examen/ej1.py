while True:
    print ("Elija entre las siguientes opciones e introduzca el numero para ejecutar: ")
    print ("1.contar palabras de una frase")
    print ("2.mostrar las palabras de una frase en lineas distintas")
    print ("3.mostrar la frase con todas sus letras en mayúsculas")
    print ("4.salir")
    opcion = input ("selecciona una opción")
    if (opcion == "1"):
        o1=input ("Introduzca una frase")
        dividir= o1.split(" ")
        num= len(dividir)
        print ("su frase tiene "+ str(num) +" elementos")
    elif (opcion == "2"):
        o2= input ("Introduzca una frase")
        dividir = o2.split(" ")
        num= len(dividir)
        for i in range (1, num -1, 1):
            print(dividir)
    elif (opcion == "3"):
        o3 = input ("Introduzca una frase")
        mayus = o3.upper()
        print (mayus)
    elif (opcion == "4"):
        break



