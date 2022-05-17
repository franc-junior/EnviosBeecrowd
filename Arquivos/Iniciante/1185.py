matriz = []
num = 12
o = input()

for i in range(num):
    linha = []
    for k in range(num):
        lin = float(input())
        linha.append(lin)
    matriz.append(linha)

cont = 0
soma = 0
for j in matriz:
    num -= 1
    for y in j[0:num]:
        soma += y
        cont += 1

if o == 'S':
    print(soma)
elif o == 'M':
    print("{:.1f}".format(soma/cont))