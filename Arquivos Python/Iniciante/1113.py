while 1 > 0:
    x, y = map(int, input().split())
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    else:
        break