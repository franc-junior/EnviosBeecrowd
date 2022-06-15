for i in range(int(input())):
    c = float(input())
    cont = 0
    while c>1:
        c /= 2
        cont += 1
    print(cont, "dias")