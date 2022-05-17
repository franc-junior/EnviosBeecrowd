for i in range(int(input())):
    m = int(input())
    fila = list(map(int,input().split()))
    cont=0
    inverso = sorted(fila,reverse=True)
    for j in range(m):
        if fila[j] == inverso[j]:
            cont+=1
    print(cont)
