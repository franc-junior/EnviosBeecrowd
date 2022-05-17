n = int(input())
consoantes = "bcdfghjklmnpqrstvwxyz"
for i in range(n):
    snome = input()
    cont = 0
    con2 = 0
    for j in snome.lower():
        if j in consoantes:
            cont += 1
            if cont == 3:
                con2 = 1
        else:
            cont = 0
    if con2 >= 1:
        print(snome, "nao eh facil")
    else:
        print(snome, "eh facil")

        