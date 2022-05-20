while True:
    m, n = map(int,input().split())
    soma = m+n
    if soma == 0:
        break
    print(str(soma).replace("0",""))