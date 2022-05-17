n = int(input())
for i in range(n):
    soma = 0
    x = int(input())
    for j in range(1,x):
        if x % j == 0:
            soma += j
    if x == soma:
        print(x, "eh perfeito")
    else:
        print(x, "nao eh perfeito")