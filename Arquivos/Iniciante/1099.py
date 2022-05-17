n = int(input())
for i in range(1, n+1):
    a, b = map(int, input().split())
    y = max(a,b)
    x = min(a,b)
    soma = 0
    for e in range(x+1, y):
        if e % 2 != 0:
            soma += e
    print(soma)