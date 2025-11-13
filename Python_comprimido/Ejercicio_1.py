va = float ( input("Introduzca un capital: ") )
interes = float ( input("Introduzca un tipo de interés: ") )
n = int ( input("Introduzca un número a de años: ") )

#mostrar valor de futuro cada año 

vf = va * (1 + interes)**n
incremento_anual = 0

for i in range (1, n+1, 1):

    incremento_anual = vf + incremento_anual

    print (i)