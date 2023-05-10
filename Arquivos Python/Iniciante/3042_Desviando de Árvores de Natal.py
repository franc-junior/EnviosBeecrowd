while True:
    m = int(input())
    if m == 0:
        break
    atual = 1
    cont = 0
    for i in range(m):
        lcr = input().split()
        if lcr[atual] == '1':
            if lcr[0] == '0':
                cont += abs(atual-0)
                atual=0
            elif lcr[1] == '0':
                v = abs(atual-1)
                cont += abs(atual-1)
                atual=1
            else:
                cont += abs(atual-2)
                atual=2
    print(cont)
