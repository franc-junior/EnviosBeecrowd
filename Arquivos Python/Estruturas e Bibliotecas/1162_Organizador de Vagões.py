for i in range(int(input())):
    n = int(input())
    vag = list(map(int, input().split()))
    mov = 0
    for j in range(n):
        if j+1 != vag[j]:
            indice = vag.index(j+1)
            mov += (indice) - j
            del vag[indice]
            vag.insert(j, j+1)
    print("Optimal train swapping takes {} swaps.".format(mov))
    