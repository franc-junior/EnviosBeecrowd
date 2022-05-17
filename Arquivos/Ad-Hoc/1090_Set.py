n = int(input())
while n!=0:

    lista = [0,0,0,0,0,0,0,0,0]
    
    for i in range(n):
        q = input().split()
        if q[0] == "um":
            if q[1] == "circulo":
                #um_circulo+=1
                lista[0]+=1

            elif q[1] == "quadrado":
                #um_quadrado+=1
                lista[1]+=1

            else:
                #um_triangulo+=1
                lista[2]+=1

        elif q[0] == "dois":
            if q[1] == "circulos":
                #dois_circulo+=1
                lista[3]+=1

            elif q[1] == "quadrados":
                #dois_quadrado+=1
                lista[4]+=1

            else:
                #dois_triangulo+=1
                lista[5]+=1

        else:
            if q[1] == "circulos":
                #tres_circulo+=1
                lista[6]+=1

            elif q[1] == "quadrados":
                #tres_quadrado+=1
                lista[7]+=1

            else:
                #tres_triangulo+=1
                lista[8]+=1

    um_circulo = lista[0]
    dois_circulo = lista[3]
    tres_circulo = lista[6]
    um_quadrado = lista[1]
    dois_quadrado = lista[4]
    tres_quadrado = lista[7]
    um_triangulo = lista[2]
    dois_triangulo = lista[5]
    tres_triangulo = lista[8]

    cont = 0
    if um_circulo>=3:
        cont += um_circulo//3
        um_circulo = um_circulo%3
    if dois_circulo>=3:
        cont += dois_circulo//3
        dois_circulo = dois_circulo%3
    if tres_circulo>=3:
        cont += tres_circulo//3
        tres_circulo = tres_circulo%3
    if um_circulo>=1 and dois_circulo>=1 and tres_circulo>=1:
        v = min(um_circulo, dois_circulo, tres_circulo)
        cont += v
        um_circulo-=v
        dois_circulo-=v
        tres_circulo-=v


    if um_quadrado>=3:
        cont += um_quadrado//3
        um_quadrado = um_quadrado%3
    if dois_quadrado>=3:
        cont += dois_quadrado//3
        dois_quadrado = dois_quadrado%3
    if tres_quadrado>=3:
        cont += tres_quadrado//3
        tres_quadrado = tres_quadrado%3
    if um_quadrado>=1 and dois_quadrado>= 1 and tres_quadrado>=1:
        v = min(um_quadrado, dois_quadrado, tres_quadrado)
        cont +=v
        um_quadrado-=v
        dois_quadrado-=v
        tres_quadrado-=v


    if um_triangulo>=3:
        cont += um_triangulo//3
        um_triangulo = um_triangulo%3
    if dois_triangulo>=3:
        cont += dois_triangulo//3
        dois_triangulo = dois_triangulo%3
    if tres_triangulo>=3:
        cont += tres_triangulo//3
        tres_triangulo = tres_triangulo%3
    if um_triangulo>=1 and dois_triangulo>=1 and tres_triangulo>=1:
        v = min(um_triangulo, dois_triangulo, tres_triangulo)
        cont +=v
        um_triangulo-=v
        dois_triangulo-=v
        tres_triangulo-=v

#######################################################################

    if um_circulo>=1 and dois_quadrado>=1 and tres_triangulo>=1:
        v = min(um_circulo, dois_quadrado, tres_triangulo)
        cont+=v
        um_circulo-=v
        dois_quadrado-=v
        tres_triangulo-=v
    if um_circulo>=1 and dois_triangulo>=1 and tres_quadrado>=1:
        v = min(um_circulo, dois_triangulo, tres_quadrado)
        cont+=v
        um_circulo-=v
        dois_triangulo-=v
        tres_quadrado-=v

    if um_quadrado>=1 and dois_circulo>=1 and tres_triangulo>=1:
        v = min(um_quadrado, dois_circulo, tres_triangulo)
        cont+=v
        um_quadrado-=v
        dois_circulo-=v
        tres_triangulo-=v
    if um_quadrado>=1 and dois_triangulo>=1 and tres_circulo>=1:
        v = min(um_quadrado, dois_triangulo, tres_circulo)
        cont+=v
        um_quadrado-=v
        dois_triangulo-=v
        tres_circulo-=v

    if um_triangulo>=1 and dois_circulo>=1 and tres_quadrado>=1:
        v = min(um_triangulo, dois_circulo, tres_quadrado)
        cont+=v
        um_triangulo-=v
        dois_circulo-=v
        tres_quadrado-=v
    if um_triangulo>=1 and dois_quadrado>=1 and tres_circulo>=1:
        v = min(um_triangulo, dois_quadrado, tres_circulo)
        cont+=v
        um_triangulo-=v
        dois_quadrado-=v
        tres_circulo-=v
    if um_circulo+um_quadrado+um_triangulo+dois_circulo+dois_quadrado+dois_triangulo+tres_circulo+tres_quadrado+tres_triangulo>=5:
        cont+=1
    
    print(cont)
    #Não consigo essa brucuta
    
    # print("um_circulo =", um_circulo,
    # "\ndois_circulo =", dois_circulo,
    # "\ntres_circulo =", tres_circulo,
    # "\num_quadrado =", um_quadrado,
    # "\ndois_quadrado =", dois_quadrado,
    # "\ntres_quadrado =", tres_quadrado,
    # "\num_triangulo =", um_triangulo,
    # "\ndois_triangulo =", dois_triangulo,
    # "\ntres_triangulo =", tres_triangulo 
    # )
    n = int(input())
    

        