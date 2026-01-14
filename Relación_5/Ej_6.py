asignaturas = ['Matemáticas','Física','Química','Historia','Lengua']

m = int(input ("Matemáticas"))
f = int(input ("Física"))
q = int(input ("Química"))
h = int(input ("Historia"))
l = int(input ("Lengua"))


for i in range (0,4,1):
    if asignaturas[i] >=5:
        print (asignaturas[i])
    else:
        asignaturas.remove [i]

