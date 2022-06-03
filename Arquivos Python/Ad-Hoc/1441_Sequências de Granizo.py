while True:
    h = int(input())
    if h == 0:
        break
    maior = 0
    if h == 1:
        maior = 1
    while h > 1:
        if h>maior:
            maior=h
        if h%2 == 0:
            h = h//2
        else:
            h = (h*3)+1
    print(maior)