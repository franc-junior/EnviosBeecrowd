while True:
    try:
        n = int(input())
        l = list(map(int,input().split()))
        soma = sum(l)

        if (soma%n == 0):
            print(int(l[-1]-soma/n)+1)
        else:
            print(-1)
    except EOFError:
        break

