o = input()
m = []
t = 3
for col in range(t):
    linha = []
    for lin in range(t):
        valor = float(input())
        linha.append(valor)
    m.append(linha)
r = 1
b = t-1
soma = 0
mult = 0
for i in range(t-1, (t//2)-1, -1):
    
    for j in m[i][r:b]:
        soma += j
        mult += 1
    r+=1
    b-=1
if o == 'S':
    print("{:.1f}".format(soma))
else: 
    print("{:.1f}".format(soma/mult))  

print(m)    
    
 