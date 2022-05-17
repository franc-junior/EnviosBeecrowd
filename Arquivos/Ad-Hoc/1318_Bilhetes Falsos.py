n, m = map(int, input().split())
while n+m != 0:
    t = input().split()
    cont = 0
    real = []
    falso = []
    for i in t:
        if i in real:
            if not i in falso:
                cont += 1
                falso.append(i)
        else:
            real.append(i)
    print(cont)
    n, m = map(int, input().split())