n = int(input())
for i in range(n):
    cont = 0
    x = int(input())
    for j in range(1, x+1):
        if x % j == 0:
            cont += 1
    if cont == 2:
        print(x, "eh primo")
    else:
        print(x, "nao eh primo")