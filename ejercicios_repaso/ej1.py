def valor_futuro(capital,tipo_interes,num_anios):
    for i in range(1,num_anios + 1,1):
        vf = capital * (1 + tipo_interes)**i
        print ("Año " + str(i) + " " + str(vf))
    

parametro1 = float(input("Introduce un capital: "))
parametro2 = float(input("Introduce un tipo de interés: "))
parametro3 = int(input("Introduce un número de años: "))    
print(valor_futuro(parametro1,parametro2,parametro3))



