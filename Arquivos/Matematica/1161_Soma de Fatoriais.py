while True:
    try:
        m, n = map(int, input().split())
        sm = 1
        sn = 1
        for i in range(m, 1, -1):
            sm *= i
        for i in range(n, 1, -1):
            sn *= i
        print(sm+sn)
    except EOFError:
        break
