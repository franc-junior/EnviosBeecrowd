n = int(input())
matriz = []
for i in range(n):
    matriz.append(list(map(int, input().split())))
borboletas = []
q = 0
for i in range(n*2):
    x, y = map(int, input().split())
    if matriz[x-1][y-1] not in borboletas:
        borboletas.append(matriz[x-1][y-1])
        q+=1
print(q)
    
