n, d = map(int, input().split())
lista = []

for i in range(d):
    lista.append(input().split())
for i in range(n):
    res = 2
    for j in range(n):
        r = "yes"
        if res == 2:
            res = lista[j][i]
        elif res != lista[j][i]:
            res = "no"
    if r == "yes":
        print(r)
    
        

    

    
    


