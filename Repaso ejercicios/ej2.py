suma=0
mayor=0
for i in range (1,10):
    num=int(input("pon un numero"))
    suma = suma + num
    if num > mayor:
        mayor=num
print ("la suma de los números es: ",suma)
print ("el número mayor es: ",mayor)
