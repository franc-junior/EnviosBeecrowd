n, m = map(int, input().split())
l = list(input().split())
lista_m = []
matriz = []
v=-1
for i in range(1,m+1):
    if str(i) in l[1:]:
        lista_m.append(True)
    else:
        lista_m.append(False)
for i in range(n):
    k = list(input().split())
    matriz.append(k[1:])
cont = 0
cont2 = 0
while cont != n*2:
    for i in matriz[cont2]:
        if lista_m[int(i)-1] == True:
            lista_m[int(i)-1] = False
        else:
            lista_m[int(i)-1] = True
    if not True in lista_m:
        v = cont+1
        break
    elif cont2 == n-1:
        cont2= -1
    cont2+=1
    cont+=1
print(v)
    
    
# 6 3
# 2 1 3
# 3 1 2 3
# 2 1 3
# 2 1 2
# 2 2 3
# 1 2
# 3 1 2 3