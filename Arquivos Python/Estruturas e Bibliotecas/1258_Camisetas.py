def nome_(e):
    return e[2]
def tamanho(e):
    return e[1]
def cor(e):
    return e[0]

c = False
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if c == False:
            c = True
        else:
            print()
    
    lista = []
    for i in range(n):
        nome = input()
        ct = input().split()
        lista.append([ct[0], ct[1], nome])
    lista.sort(key=nome_)
    lista.sort(key=tamanho, reverse=True)
    lista.sort(key=cor)
    for i in lista:
        print(i[0], i[1], i[2])
    
