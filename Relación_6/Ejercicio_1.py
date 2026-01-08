dic = {'Euro':'€','Dollar':'$', 'Yen':'¥'}
d = input("Introduzca una divisa")
if d in dic:
    print (dic[d])
else:
    print ("La divisa no se encuentra en un diccionario")