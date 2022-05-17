import math
while True:
    valores = list(map(int,input().split()))
    if valores[0] == 0:
        break
    v = math.floor((valores[0]*valores[2])*(valores[1]/(valores[2]-valores[0])))
    if v == 1:
        print(v, "pagina")
    else:
        print(v, "paginas")
    #q = valores[0]
    #d = valores[1]
    #p = valores[2]
    #q, d, p = map(int, input().split())
    #print("{:.0f} paginas".format(math.floor((q*p)*(d/(p-q)))))
