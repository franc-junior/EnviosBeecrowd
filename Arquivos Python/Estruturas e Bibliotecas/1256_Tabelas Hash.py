import math

n = int(input())
for i in range(n):
    m, c = map(int, input().split())
    matriz = []
    for num in range(m):
        matriz.append("")
    
    lista = list(map(int, input().split()))
    for num in range(c):
        ende = (math.floor(lista[num]/m) * m)
        matriz[lista[num]-ende] += str(lista[num])+" "

    for num in range(m):
        string = str(num)+" ->"
        for j in matriz[num].split():
            string += " "+str(j)+" ->"
        string += " \\"
        print(string)
    if i != n-1:
        print()

        
