p, j1, j2, r, a = map(int,input().split())
if (j1+j2) % 2 == 0:
    n = 1
else:
    n = 0
if p == n:
    if r == 0:
        if a == 1:
            venc = 1
        if a == 0:
            venc = 1
    else:
        if a == 1:
            venc = 2
        else:
            venc = 1
elif p != n:
    if r == 1:
        if a == 1:
            venc = 2
        else:
            venc = 1
    else:
        if a == 1:
            venc = 1
        else:
            venc = 2
if venc == 1:
    print("Jogador 1 ganha!")    
else:
    print("Jogador 2 ganha!")
