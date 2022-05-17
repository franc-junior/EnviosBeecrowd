from string import ascii_lowercase

n = int(input())
for i in range(n):
    lista = ""
    cont = 0
    pala = input()
    for letra in ascii_lowercase:
        passa = pala.lower().count(letra)
        if passa>cont:
            lista = ""
            lista+=letra
            cont = passa
        elif passa==cont:
            lista+=letra
    print(lista)
