lista = []
while True:
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    preg = int(input("Elige una opción: "))
    if preg == 9:
        break
    elif preg == 1:
        n = str(input("¿qué número quieres añadir?"))
        lista.append(n)
        print("Se ha añadido el número")
    elif preg == 8:
        for i in lista:
            print(i,end=" ")
        print("")
    elif preg == 3:
        c = len(lista)
        print (c)
    elif preg == 2:
        n = int(input("Introduce el número a añadir"))
        p = int(input("Introduce una posición"))
        p = p - 1
        lista.insert(p,n)
    elif preg == 4:
        lista.pop()
    elif preg == 7:
        n = int (input("¿Introduzca un número de la lista para hallar su posición?"))
        x = lista.index(n)
        print (x)
        

