
contador = 1
thisdict = {}
total_precio = 0
while contador==1:
    articulo = input("introduzca el articulo que desea añadir: ")
    precio = float(input("introduzca su precio: "))
    thisdict[articulo]= precio
    total_precio = precio + total_precio
    salir = input("Escriba 'exit' para salir del diccionario o pulse enter para continuar: ")
    if salir == "exit":
        break

print(thisdict)
print ("Total: " + str(total_precio) )
