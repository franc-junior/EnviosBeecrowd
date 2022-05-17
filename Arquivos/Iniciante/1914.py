qt = int(input())
for i in range(qt):
    j1, d1, j2, d2 = input().split()
    n, m = map(int, input().split())
    soma = n + m
    if soma % 2 == 0:
        res = "PAR"
    else:
        res = "IMPAR"
    if res == d1:
        print(j1)
    else:
        print(j2)
    