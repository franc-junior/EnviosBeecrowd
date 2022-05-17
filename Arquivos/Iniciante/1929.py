def funcao(lista_f, x_f):
    cont = 0
    for i in lista_f:
        cont += i
    if cont > x_f:
        return "S"
    else:
        return "N"
        
cont = 0
lista = list(map(int, input().split()))
lista_2 = []

lista_2.append(max(lista))
lista.remove(max(lista))

x = max(lista)
lista_2.append(max(lista))
lista.remove(max(lista))

lista_2.append(max(lista))

x_2 = max(lista_2)
lista_2.remove(max(lista_2))

if funcao(lista, x) == "S":
    print("S")
else:
    print(funcao(lista_2, x_2))

