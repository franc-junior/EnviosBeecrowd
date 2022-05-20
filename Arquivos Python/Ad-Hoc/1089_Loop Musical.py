n=int(input())
while n!=0:
    cont = 0
    torf = 2
    notas = list(map(int, input().split()))
    ant = notas[0]
    for i in range(1,n):
        if notas[i] > ant:
            if torf != True:
                torf = True
                cont+=1
        else:
            if torf != False:
                torf = False
                cont += 1 
        ant = notas[i]

    if notas[0]<notas[1]:
        inicial = False
    else:
        inicial = True
    if torf != inicial:
        cont+=1
    print(cont)
    n=int(input())
