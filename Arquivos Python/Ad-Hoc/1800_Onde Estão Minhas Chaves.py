q, e = map(int, input().split())
lista_e = list(map(int, input().split()))
for i in range(q):
    n_q = int(input())
    if n_q in lista_e:
        print("0")
    else:
        print("1")
        lista_e.append(n_q)