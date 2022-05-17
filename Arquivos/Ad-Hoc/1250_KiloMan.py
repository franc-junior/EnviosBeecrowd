for i in range(int(input())):
    t = int(input())
    lista = list(map(int, input().split()))
    pulos = input()
    acerto = 0
    for j in range(t):
        if pulos[j] == "J":
            if lista[j] >2:
                acerto += 1
        else:
            if lista[j]<=2:
                acerto +=1
    print(acerto)