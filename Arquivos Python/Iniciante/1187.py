o = input()
m = []
t = 12
for col in range(t):
    linha = []
    for lin in range(t):
        valor = float(input())
        linha.append(valor)
    m.append(linha)

cont = len(m[0])
soma = 0

for i in range(t):
    somador = m[i][i+1:cont-1]
    cont -= 1
    for j in somador:
        soma += j
    
if o == 'S':
     print("{:.1f}".format(soma))
elif o == 'M':
    print("{:.1f}".format(soma/30)) 


