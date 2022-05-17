n = float(input())
imposto = 0
if n <= 2000.00:
    print("Isento")
else:
    n -= 2000.00
    if n <= 0:
        print("R$ {:.2f}".format(imposto))
    else:
        if n > 1000:
            m = 1000
        else: 
            m = n
        imposto += (8/100)*m
        n -= 1000.00
        if n <= 0:
            print("R$ {:.2f}".format(imposto))
        else:
            if n > 1500:
                m = 1500
            else:
                m = n 
            imposto += (18/100)*m
            n -= 1500.00 
            if n > 0:
                imposto += (28/100)*n 
                print("R$ {:.2f}".format(imposto))
            else:
                print("R$ {:.2f}".format(imposto))
        
    

