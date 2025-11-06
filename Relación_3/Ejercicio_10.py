pedido = input ("Elija entre las dos posibles opciones de pizza (vegetariana, no vegetariana): ")

pedido_mayusculas = pedido.upper()

if (pedido_mayusculas == "VEGETARIANA"):

    v = input ("Elija un ingrediente entre estos: pimiento y tofu: ")

    print ( "Ha elegido una pizza vegetariana: " + "\n" +
        v + "\n" +
               "mozarella" + "\n" +
                "tomate"  )

        

elif (pedido_mayusculas == "NO VEGETARIANA"):

    nv = input ("Elija un ingrediente entre estos: peperoni, jamón, salmón: ")    

    print ( "Ha elegido una pizza no vegetariana: " + "\n" +
        nv + "\n" +
               "mozarella" + "\n" +
                "tomate"  )