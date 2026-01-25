total_saldo = 0
Ingresos = []
Reintegros = []
while True:
    print ("¿Qué desea hacer?")
    print ("1- Ingreso")
    print ("2- Reintegro")
    opcion = int(input("Elige una opción (pulse 3 para finalizar): "))
    if opcion == 3:
     print ("Actualmente tiene un saldo de " + str(total_saldo))
     print ("Transacciones realizadas:")
     print ("Ingresos: " + str(Ingresos))
     print ("Reintegros: " + str(Reintegros))
     break
    elif opcion == 1:
        ingreso = float(input("¿Qué cantidad desea ingresar?: "))
        Ingresos.append(ingreso)
        total_saldo = total_saldo + ingreso
        print (total_saldo)
    elif opcion == 2:
       reintegro = float(input("¿Qué cantidad desea extraer?: "))
       if reintegro > total_saldo:
          print  ("No dispone de suficiente saldo,por favor, introduzca otra cantidad: ")
       else:
            total_saldo = total_saldo - reintegro
            Reintegros.append(reintegro)
            print (total_saldo)