cantidad = float ( input ("Introduzca una cantidad a invertir: ") )
num_interes = float( input ("Introduzca el interés anual: ") ) 
anios = int(input ("Introduzca el numero de años que va a durar la inversión: ") )


for i in range(1, anios + 1):

   # cantidad = cantidad * (1 + interes / 100)

   porcentaje_interés = ( ( (cantidad * num_interes) / 100 ) + cantidad )

total = 0
total = porcentaje_interés + total

print("Anio " + str(i) + " = " + str(round (total,2)) )