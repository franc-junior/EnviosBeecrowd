while True:
    try:
        n, r = map(int, input().split())
        voltaro = list(map(int, input().split()))
        lista = list(range(1,n+1))
        for i in voltaro:
            lista.remove(i)
        if n == r:
            print('*')
        else:
            for i in lista:
                print(i, end=" ")
            print()
    except EOFError:
        break