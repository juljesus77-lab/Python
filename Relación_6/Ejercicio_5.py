creditos = {'Matemáticas': 6, 
            'Física': 4, 
            'Química': 5}

print ( creditos[0] + " tiene " + str(creditos["Matemáticas"]) + " créditos.")
print ( creditos[1] + " tiene " + str(creditos["Física"]) + " créditos.")
print ( creditos[2] + "Química tiene " + str(creditos["Química"]) + " créditos.")

suma_creditos = creditos["Matemáticas"] + creditos["Física"] + creditos["Química"]
print ("Total de créditos: " + str(suma_creditos) )
