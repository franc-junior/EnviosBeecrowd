flavio = input().split()
sorteio = input().split()
r = "azar"
cont = 0
for i in flavio:
    if i in sorteio:
        cont += 1
if cont == 3:
    r = "terno"
elif cont == 4:
    r = "quadra"
elif cont == 5:
    r = "quina"
elif cont == 6:
    r = "sena"
print(r)