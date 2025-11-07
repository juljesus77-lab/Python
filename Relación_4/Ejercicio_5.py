cantidad = float ( input ("Introduzca una cantidad a invertir: ") )
interes = float( input ("Introduzca el interés anual: ") ) 
anios = int(input ("Introduzca el numero de años que va a durar la inversión: ") )


for i in range(1, anios + 1):

    cantidad = cantidad * (1 + interes / 100)
    print("Anio " + str(i) + " = " + str(round (cantidad,2)) )