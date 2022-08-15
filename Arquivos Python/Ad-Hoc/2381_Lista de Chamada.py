n, k = map(int,input().split())
lista = []
for i in range(n):
    lista.append(input())
lista.sort()
print(lista[k-1])