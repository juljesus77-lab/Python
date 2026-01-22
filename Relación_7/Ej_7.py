def my_function(lista):
  lista2 = []
  for i in lista:
    cuadrado = i ** 2
    lista2.append(cuadrado)
  return lista2  

numeros = [1, 2, 3]
print(my_function(numeros))