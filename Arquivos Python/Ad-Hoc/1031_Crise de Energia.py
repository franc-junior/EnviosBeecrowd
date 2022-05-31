while True:
    n = int(input())
    if n == 0:
        break
    num = 0
    lista=0
    while lista != [13]:
        lista = list(range(1,n+1))
        cont = 0
        for i in range(n-1):
            while cont>=len(lista):
                cont -= len(lista)
            if lista[cont] == 13:
                break
            del lista[cont]
            cont += num
        num += 1
    print(num)
        # if lista == [13]:
        #     break


# 1,6,11,16,5,12,2,9,17,10,4,15,14,3,8,13,7