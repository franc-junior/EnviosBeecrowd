n = int(input())
while n!=0:

    lista = [0,0,0,0,0,0,0,0,0]
    
    for i in range(n):
        q = input().split()
        if q[0] == "um":
            if q[1] == "circulo":
                lista[0]+=1

            elif q[1] == "quadrado":
                lista[1]+=1

            else:
                lista[2]+=1

        elif q[0] == "dois":
            if q[1] == "circulos":
                lista[3]+=1

            elif q[1] == "quadrados":
                lista[4]+=1

            else:
                lista[5]+=1

        else:
            if q[1] == "circulos":
                lista[6]+=1

            elif q[1] == "quadrados":
                lista[7]+=1

            else:
                lista[8]+=1

    cont = 0
    if lista[0]>=3:
        cont += lista[0]//3
        lista[0] = lista[0]%3
    if lista[3]>=3:
        cont += lista[3]//3
        lista[3] = lista[3]%3
    if lista[6]>=3:
        cont += lista[6]//3
        lista[6] = lista[6]%3
    if lista[0]>=1 and lista[3]>=1 and lista[6]>=1:
        v = min(lista[0], lista[3], lista[6])
        cont += v
        lista[0]-=v
        lista[3]-=v
        lista[6]-=v

    if lista[1]>=3:
        cont += lista[1]//3
        lista[1] = lista[1]%3
    if lista[4]>=3:
        cont += lista[4]//3
        lista[4] = lista[4]%3
    if lista[7]>=3:
        cont += lista[7]//3
        lista[7] = lista[7]%3
    if lista[1]>=1 and lista[4]>= 1 and lista[7]>=1:
        v = min(lista[1], lista[4], lista[7])
        cont +=v
        lista[1]-=v
        lista[4]-=v
        lista[7]-=v

    if lista[2]>=3:
        cont += lista[2]//3
        lista[2] = lista[2]%3
    if lista[5]>=3:
        cont += lista[5]//3
        lista[5] = lista[5]%3
    if lista[8]>=3:
        cont += lista[8]//3
        lista[8] = lista[8]%3
    if lista[2]>=1 and lista[5]>=1 and lista[8]>=1:
        v = min(lista[2], lista[5], lista[8])
        cont +=v
        lista[2]-=v
        lista[5]-=v
        lista[8]-=v

    if lista[0]>=1 and lista[4]>=1 and lista[8]>=1:
        v = min(lista[0], lista[4], lista[8])
        cont+=v
        lista[0]-=v
        lista[4]-=v
        lista[8]-=v
    if lista[0]>=1 and lista[5]>=1 and lista[7]>=1:
        v = min(lista[0], lista[5], lista[7])
        cont+=v
        lista[0]-=v
        lista[5]-=v
        lista[7]-=v

    if lista[1]>=1 and lista[3]>=1 and lista[8]>=1:
        v = min(lista[1], lista[3], lista[8])
        cont+=v
        lista[1]-=v
        lista[3]-=v
        lista[8]-=v
    if lista[1]>=1 and lista[5]>=1 and lista[6]>=1:
        v = min(lista[1], lista[5], lista[6])
        cont+=v
        lista[1]-=v
        lista[5]-=v
        lista[6]-=v

    if lista[2]>=1 and lista[3]>=1 and lista[7]>=1:
        v = min(lista[2], lista[3], lista[7])
        cont+=v
        lista[2]-=v
        lista[3]-=v
        lista[7]-=v
    if lista[2]>=1 and lista[4]>=1 and lista[6]>=1:
        v = min(lista[2], lista[4], lista[6])
        cont+=v
        lista[2]-=v
        lista[4]-=v
        lista[6]-=v
    if lista[0]+lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]>=5:
        cont+=1
    
    print(cont)
    
    n = int(input())
    

        