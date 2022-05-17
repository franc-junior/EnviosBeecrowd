n = int(input())
for i in range(n):
    p1, p2 = map(str,input().split())
    saida = ""
    j = 0
    while True:
        saida+=p1[j]
        saida+=p2[j]
        if len(p1)-1==j or len(p2)-1==j:
            if len(p1)-1==j:
                saida+=p2[j+1:]
            else:
                saida+=p1[j+1:]
            print(saida)
            break
        else:
            j+=1
