n = int(input())
cont = 18
while True:
    lista = list(range(2, n+1))
    ordem = [1]
    for i in range(n):
        ordem.append(lista.pop(cont))
        lista.extend(lista)
        cont+=cont-1
        
        
        


        
        
        



