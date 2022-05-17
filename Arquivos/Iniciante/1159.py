x = 1
while x != 0:
    soma = 0
    x = int(input())
    if x == 0:
        break
    for i in range(x,x+10):
        if i % 2 == 0:
            soma += i
    print(soma)
    