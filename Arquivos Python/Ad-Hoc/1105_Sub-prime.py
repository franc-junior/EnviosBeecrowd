while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    list_banc = list(map(int, input().split()))

    for i in range(n):
        d, c, v = map(int, input().split())
        list_banc[c-1] += v 
        list_banc[d-1] -= v

    r = "S"
    for i in list_banc:
        if i<0:
            r = "N"
            break
    print(r)