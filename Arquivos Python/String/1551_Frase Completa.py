from string import ascii_lowercase


for i in range(int(input())):
    alfabeto = list(ascii_lowercase)
    for j in input():
        if j in alfabeto:
            alfabeto.remove(j)
    tam = len(alfabeto)
    if tam == 0:
        print("frase completa")
    elif tam <= (26/2):
        print("frase quase completa")
    else:
        print("frase mal elaborada")
