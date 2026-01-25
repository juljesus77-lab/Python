meses= {"enero":31,
        "febrero":28,
        "marzo":31,
        "abril":30,
        "mayo":31,
        "junio":30,
        "julio":31,
        "agosto":31,
        "septiembre":30,
        "octubre":31,
        "noviembre":30,
        "diciembre":31}

dia = int(input("Indique el día: "))
mes = input("Indique el mes: ")
dias_anteriores = 0

for i in meses:
    if i == mes:
        break  # Detiene el bucle antes de sumar el mes actual
    dias_anteriores += meses[i]

numero = dias_anteriores + dia

print ("El día " + str(dia) + " de " + str(mes) + " es el día número " + str(numero) + " del año")




