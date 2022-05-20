n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    soma = 0
    for j in range(x,x+y*2):  
        if j % 2 != 0:
            soma += j
    print(soma)   