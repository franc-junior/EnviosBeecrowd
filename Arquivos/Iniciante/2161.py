n = int(input())
matriz = []
for i in range(n+1):
    linha = input().split()
    matriz.append(linha)

resposta = []
for l in range(n):
    lim = []
    for c in range(n-0):
        cont = 0

        if matriz[l][c] == '1':
            cont += 1
        if matriz[l][c+1] == '1':
            cont += 1
        if matriz[l+1][c] == '1':
            cont += 1
        if matriz[l+1][c+1] == '1':
            cont += 1
        
        if cont >= 2:
            lim.append("S")
        else:
            lim.append("U")
    resposta.append(lim)
for lr in range(n):
    for cr in range(n):
        print("{}".format(resposta[lr][cr]), end="")
    print()

# dia 28
         