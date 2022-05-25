while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    t = "yes"
    lista = [True]*n
    for i in range(d):
        caso = input().split()
        for j in range(n):
            if caso[j] == '0':
                lista[j] = False
    if True not in lista:
        t = "no"
    print(t)

        

        


    
        

    

    
    


