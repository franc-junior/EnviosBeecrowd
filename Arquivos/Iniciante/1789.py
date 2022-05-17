while True:
    try:
        l = int(input())
        lista = list(map(int,input().split()))
        maior = lista[0]
        for i in range(l):
            if lista[i] > maior:
                maior = lista[i]
        if maior < 10:
            print("1")
        elif (maior >= 10) and (maior < 20):
            print("2")
        else:
            print("3") 
    except EOFError:
        break