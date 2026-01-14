Frutas =	{
  "Plátano": 1.35,
  "Manzana": 0.80,
  "Pera": 0.85,
  "Naranja": 0.70
}

p = float(input ("Elija una fruta: Plátano, Manzana, Pera o Naranja: "))
if p == "Plátano":
    k = float(input ("Introduzca el número de kilos que quiere de " + p + " "))
    operacion = Frutas["Plátano"] * k
    print (operacion)
elif p == "Manzana":
    k = float(input ("Introduzca el número de kilos que quiere de " + p + " "))
    operacion = Frutas["Manzana"] * k
    print (operacion)
elif p == "Pera":
    k = float(input ("Introduzca el número de kilos que quiere de " + p + " "))
    operacion = Frutas["Pera"] * k
    print (operacion)
elif p == "Naranja":
    k = float(input ("Introduzca el número de kilos que quiere de " + p + " "))
    operacion = Frutas["Naranja"] * k
    print (operacion)
else:
    print ("Esta fruta no se encuentra disponible")