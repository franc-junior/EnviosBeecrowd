while True:
    try:
        lista = []
        cont = 0
        n = int(input())
        for i in range(n):
            lista.append(input())
        lista.sort()
        
        tel = lista[0]
        for i in range(n-1):
            tel2 = lista[i+1]

            for num, j in enumerate(tel):
                if j == tel2[num]:
                    cont += 1
                else:
                    tel = tel2
                    break
        print(cont)

    except EOFError:
        break