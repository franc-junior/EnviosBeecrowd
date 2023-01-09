n = int(input())
teste = 1
while n!=0:
    j1 = input()
    j2 = input()
    print("Teste", teste)
    for i in range(n):
        p1, p2 = map(int, input().split())
        if (p1+p2)%2 == 0:
            print(j1)
        else:
            print(j2)
    teste+=1
    print()
    n = int(input())