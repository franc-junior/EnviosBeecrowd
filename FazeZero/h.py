for i in range(int(input())):
    cartas = int(input())
    base = 1
    while cartas>3:
        cartas-=3*base+1
        base+=1
    print(base-1)

