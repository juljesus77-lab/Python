nota1= float(input("Introduzca una nota "))
nota2= float(input("Introduzca la segunda nota "))
if (nota1 >=4 and nota2 >=4):
    media = (nota1 + nota2 ) / 2
    if (media >= 5):
        print ("El alumno ha aprobado")
    else:
        print ("El alumno ha suspendido")
else:
    print ("El alumno ha suspendido")
    if (nota1 < 4):
        print ("EL alumno tiene que repetir el primer parcial")
    elif (nota2 < 4):
        print ("El alumno tiene que repetir el segundo parcial")


