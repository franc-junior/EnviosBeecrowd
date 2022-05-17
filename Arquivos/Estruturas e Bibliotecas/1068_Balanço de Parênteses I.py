while True:
    
    try:
        cont = 0
        lista1 = []
        lista2 = []
       
        expre = list(input())
        for n, i in enumerate(expre):
            if i == '(':
                lista1.append(n)
            elif i == ')':
                lista2.append(n)
        print("lista1 =",lista1)
        print("lista2 =",lista2[::-1])


    except EOFError:
        break