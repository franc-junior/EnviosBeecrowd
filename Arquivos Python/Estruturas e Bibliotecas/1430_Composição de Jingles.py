while True:
    notas = input().split("/")
    if notas[0] == "*":
        break
    certo = 0
    for i in notas:
        soma = 0
        for j in i:
            if j == "W":
                num = 1
            elif j == "H":
                num = 1/2
            elif j == "Q":
                num = 1/4
            elif j == "E":
                num = 1/8
            elif j == "S":
                num = 1/16
            elif j == "T":
                num = 1/32
            else:
                num = 1/64
            soma+=num
        if soma == 1:
            certo += 1
    print(certo)