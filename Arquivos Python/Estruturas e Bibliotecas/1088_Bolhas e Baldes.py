while True:
    nuns = list(map(int, input().split()))
    if nuns[0] == 0:
        break
    n = nuns[0]
    p = nuns[1:]
    cont = 0
    for i in range(n-1):
        end = p.index(i+1)
        del p[end]
        p.insert(i,i+1)
        cont+=(end-i)
    if cont%2 == 0:
        print("Carlos")
    else:
        print("Marcelo")

