lista = list(map(int,input().split()))
cont = None
v = None
for i in lista:
    if cont == None:
        cont = i
    elif i>cont:
        if v == "D":
            v = "N"
            break
        else:
            v = "C"        
    elif i<cont:
        if v == "C":
            v = "N"
            break
        else:
            v = "D"
    cont = i
print(v)
