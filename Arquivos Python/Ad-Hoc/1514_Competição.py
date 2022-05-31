while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    c1 = 1
    c2 = [0]*m
    c3 = 0
    c4 = 1
    cont = 0
    for i in range(n):
        c = input().split()
        if "0" not in c:
            c1 = 0
        if "1" not in c:
            c4 = 0 
        for j in range(m):
            if c[j] == "1":
                c2[j] += 1
    if 0 not in c2:
        cont+=1
    if c1 == 1:
        cont+=1
    if n not in c2:
        cont+=1
    if c4 == 1:
        cont+=1
    print(cont)

    
