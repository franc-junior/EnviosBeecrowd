for i in range(int(input())):
    op = list(input().split())
    n1 = int(op[0]) 
    d1 = int(op[2])
    n2 = int(op[4]) 
    d2 = int(op[6])
    if op[3] == "+":
        n= n1*d2+n2*d1
        d=d1*d2
    elif op[3] == "-":
        n=n1*d2-n2*d1
        d=d1*d2
    elif op[3] == "*":
        n=n1*n2
        d=d1*d2
    else:
        n=n1*d2
        d=n2*d1

    j = abs(min(n,d))+1
    t = 1
    while t!=0 and j!=0:
        j-=1
        t = (n%j)+(d%j)

    n_s = n//j
    d_s = d//j

    print("{}/{} = {}/{}".format(n, d, n_s, d_s))