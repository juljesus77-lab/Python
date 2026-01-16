dicc = {}
contador = 1
while contador==1:
    p = input("Introduzca las palabras en el siguientes formato  <palabra>:<traducción>: ")
    palabra = p.split(":")[0]
    traduccion = p.split(":")[1]
    dicc[palabra]=traduccion
    salir = input("Escriba 'exit' para salir del diccionario o pulse enter para continuar: ")
    if salir == "exit":
        break
print(dicc)

frase = input("Introduzca una frase y serán traducidas las palabras que anteriormente se definieron en el diccionario")


