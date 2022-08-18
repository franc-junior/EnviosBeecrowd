from string import ascii_uppercase


beto = list(ascii_uppercase)
for i in range(int(input())):
    soma = 0
    for j in range(int(input())):
        string = list(input())
        for n, c in enumerate(string):
            soma += (n + j + beto.index(c))
    print(soma)
