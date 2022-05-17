for i in range(int(input())):
    qt, s = map(int, input().split())
    lista = list(map(int, input().split()))
    if s in lista:
        print(lista.index(s)+1)
    else:
        i = 0
        while True:
            i+=1
            if s+i in lista:
                if s-i in lista:
                    if lista.index(s+i)+1 < lista.index(s-i)+1:
                        print(lista.index(s+i)+1)
                        break
                    else:
                        print(lista.index(s-i)+1)
                        break
                else:
                    print(lista.index(s+i)+1)
                    break
            elif s-i in lista:
                print(lista.index(s-i)+1)
                break