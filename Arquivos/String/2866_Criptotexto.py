c = int(input())
alfabeto ="abcdefghijklmnopqrstuvwxyzç"
for i in range(c):
    saida = ""
    cod = list(input())
    for j in range(len(cod)-1, -1, -1):
        if cod[j] in alfabeto:
            saida+=cod[j]
    print(saida)
print()