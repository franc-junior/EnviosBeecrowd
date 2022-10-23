while True:
    try:
        otos = []
        n, g = map(int,input().split())
        pontos = 0
        for i in range(n):
            s, r = map(int, input().split())
            if (s == r):
                if (g>=1):
                    g-=1
                    pontos+=3
                else:
                    pontos+=1
            elif s>r:
                pontos+=3
            else:
                otos.append((r-s))
        otos.sort()
        for j in otos:
            if g>j:
                g-=j+1
                pontos+=3
            elif g==j:
                pontos+=1
                g-=j
            else:
                break
        print(pontos)
    except EOFError:
        break
