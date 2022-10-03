num = int(input())
for i in range(num):
    matriz = []
    m = int(input())
    maior = [0]*m
    for lin in range(m):
        linha = input().split()
        l = []
        for col in range(m):
            n = int(linha[col])
            quadr = str(n*n)
            if maior[col] < len(quadr):
                maior[col] = len(quadr)
            l.append(quadr)
        matriz.append(l)
    
    print("Quadrado da matriz #{}:".format(i+4))
    for lin in matriz:
        for col in range(m):
            if col == 0:
                print("{:>{}}".format(lin[col], maior[col]), end="")
            else:
                print("{:>{}}".format(lin[col], maior[col]+1), end="")
        print()
    if i != num-1:
        print()
