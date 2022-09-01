while True:
    try:
        lista = []
        for i in range(int(input())):
            lista.append(input())
        lista.sort()
        for i in lista:
            print(i)
    except EOFError:
        break