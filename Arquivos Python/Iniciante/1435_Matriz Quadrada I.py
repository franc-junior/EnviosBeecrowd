while True:
    n = int(input())
    if n == 0:
        break
    matriz2 = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz2.append(linha)

    num = 1
    for i in range((n//2)+1):
        for j in range(i, n-i):
            matriz2[i][j] = num
            matriz2[(n-1)-i][(n-1)-j] = num
            matriz2[j][i] = num
            matriz2[(n-1)-j][(n-1)-i] = num
        num+=1

    for i in range(n):
        linha = ""
        for j in matriz2[i]:
            linha+="{:4d}".format(j)
        print(linha[1:])
    print()


