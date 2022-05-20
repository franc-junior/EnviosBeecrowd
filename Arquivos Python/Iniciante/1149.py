lista = list(map(int, input().split()))
v = 1
soma = 0
a = lista[0]
n = lista[v]
while n <= 0:
    n = lista[v]
    v += 1
for i in range(n):
    soma += a + i
print(soma)


