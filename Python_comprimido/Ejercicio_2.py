operador = input ("Introduzca la operacion que quiere realizar con el formato: + or - or * or / or ** " )
num1 = float( input ("Introduzca un número: ") )
num2 = float( input ("Introduzca un segundo número: ") )


suma = num1 + num2
resta= num1 - num2
producto= num1 * num2
division= num1 / num2
potencia= num1**num2

operador = "+" or "-" or "*" or "/" or "**"



if (operador == "+"):
    print ("num1 " + " + " + " num2 " + " = " + str(suma) )

elif (operador == "-"):
    print ("num1 " + " - " + " num2 " + " = " + str(resta) )

elif (operador == "*"):
    print ("num1 " + " * " + " num2 " + " = " + str(producto) )

elif (operador == "/"):
    print ("num1 " + " / " + " num2 " + " = " + str (division) )

elif (operador == "**"):
    print ("num1 " + "** " + " num2 " + " = " + str(potencia) )

