n = int(input())
lista = list(input().split())
dois = 0
tres = 0
quatro = 0
cinco = 0

for i in range(n):
    lista[i] = int(lista[i])  
    if lista[i] % 2 == 0:
        dois += 1
    if lista[i] % 3 == 0:
        tres += 1
    if lista[i] % 4 == 0:
        quatro += 1
    if lista[i] % 5 == 0:
        cinco += 1
print("{} Multiplo(s) de 2\n{} Multiplo(s) de 3\n{} Multiplo(s) de 4\n{} Multiplo(s) de 5".format(dois,tres,quatro,cinco))
