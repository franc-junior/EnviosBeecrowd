cont = 0
while True:

    try:
        cont += 1
        n = int(input())
        t = "0 "
        cont2 = 1

        for i in range(n+1):
            for j in range(i):
                i2 = str(i)+" "
                t += i2
                cont2 += 1
        
        if cont2 == 1:
            print("Caso {}: {} numero\n{}\n".format(cont,cont2,t[:-1]))
       
        else:
            print("Caso {}: {} numeros\n{}\n".format(cont,cont2,t[:-1]))
        cont2 = 1
    
    except EOFError:
        break