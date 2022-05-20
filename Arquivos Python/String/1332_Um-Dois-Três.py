n = int(input())
for i in range(n):
    string=input()
    if len(string) > 3:
        valor = 3
    else:
        if (string[0] == 'o' and string[2] == 'e') or (string[0] == 'o' and string[1] == 'n') or (string[1] == 'n' and string[2] == 'e'):
            valor = 1
        else:
            valor = 2
    print(valor)