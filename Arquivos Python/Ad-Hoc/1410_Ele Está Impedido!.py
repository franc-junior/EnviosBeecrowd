while True:
    at, de = map(int, input().split())
    if at == de == 0:
        break
    d_at = list(map(int, input().split()))
    d_de = list(map(int, input().split()))

    for i in range(at):
        frente = 0
        igual = 0
        r = "N"

        for j in range(de):
            if d_at[i] > d_de[j]:
                frente+=1
            elif d_at[i] == d_de[j]:
                igual+=1
        if igual < 2 and frente < 2 and (igual+frente)!=2:
            r = "Y"
            break
    print(r)
        
