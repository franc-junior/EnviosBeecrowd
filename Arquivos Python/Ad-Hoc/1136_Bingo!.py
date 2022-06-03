while True:
    try:
        n, b = map(int, input().split())
        if n == b == 0:
            break
        lista = list(map(int,input().split()))
        lista_set = set()
        r = "N"
        for i in range(b-1):
            for j in range(i+1, b):
                lista_set.add(abs(lista[i]-lista[j]))
            if len(lista_set) >= n:
                r = "Y"
                break
    except EOFError:
        break
    print(r)

