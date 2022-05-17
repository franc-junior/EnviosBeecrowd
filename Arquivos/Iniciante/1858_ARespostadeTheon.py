n = int(input())
lista = input().split()
menor = lista[0]
index = 0
for i in range(n):
    if  lista[i] < menor:
        menor = lista[i]
        index = i
print(index+1)