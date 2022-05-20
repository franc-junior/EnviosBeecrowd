def traco():
    for i in range(39):
        print("-",end="")
    

def espaco(pos, tipo, tipo2):    
    lista = []
    for i in range(5):
        lista.append("               ")

    lista[pos] = tipo
    lista[0] = tipo2
    lista[4] = tipo2
    lista[1] += " "

    for j in lista:
        print(j,end="")
    print()

a = "x = 35"
a2 = "      "
b = " "
c = "|" 

traco()
print()
espaco(1,a2,b)
espaco(1,a,c)
espaco(1,a2,b)
espaco(1,a2,c)
espaco(1,a2,b)
espaco(2,a,c)
espaco(1,a2,b)
espaco(1,a2,c)
espaco(1,a2,b)
espaco(3,a,c)
espaco(1,a2,b)
traco()




