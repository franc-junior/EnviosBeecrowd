cont = 1
n, q = map(int, input().split())
while n!=q!=0:  
    lista = []
    for i in range(n):
        lista.append(input())
    lista.sort()
    print("CASE# {}:".format(cont))
    for i in range(q):
        aqui = input()
        j = 0
        imprime = "not found"
        while j!=len(lista):
            if lista[j] == aqui:
                imprime = "found at "+str(j+1)
                break
            j+=1
        print(aqui, imprime)
    cont+=1
    n, q = map(int, input().split())