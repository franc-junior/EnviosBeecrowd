def func(lista, cont_max, cont_lis):  
    cont_lis2 = cont_lis 
    lista = lista[1:] 
    valor = lista[0]
    nvalor = valor
    cont = cont_lis
    if len(lista) == 1:
        return cont_max
    else:
        for i in lista:
            if i in nvalor:
                cont+=1
                nvalor = i

    if cont > cont_max:
        cont_max = cont
        cont_lis2 += 1
    a = func(lista, cont_max, cont_lis2)
    if a > 0:
        return a