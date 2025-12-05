a = [[4,3],[2,1]]
b = [[1,2],[3,4]]
result = [[0,0],[0,0]]
for i in range (len(a)):
    for j in range (len(b[0])):
        for k in range (len(b)):
            result[i][j] += a[i][k] * b[k][j]
            

#for i in range (len(a)):    #bucle para recorrer los elementos
    #for j in range (len(a[1])): #recorres los numeros de los elementos
        #print(a[i][j])


