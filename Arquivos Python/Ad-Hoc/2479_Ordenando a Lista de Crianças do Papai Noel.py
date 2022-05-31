bem = 0
mal = 0
lista = []
for i in range(int(input())):
    s, n = input().split()
    lista.append(n)
    if s == "+":
        bem+=1
    else:
        mal+=1
lista.sort()
for i in lista:
    print(i)
print("Se comportaram: {} | Nao se comportaram: {}".format(bem, mal))
    