while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    cont = 0
    lista = input().split()
    lista_set=set(lista)
    for i in lista_set:
        if lista.count(i)>=k:
            cont+=1
    print(cont)