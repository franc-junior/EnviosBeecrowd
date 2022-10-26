while True:
    try:
        mn = input().split()
        s = 0
        for i in mn[1]:
            s += int(i)
        if s%3 == 0:
            print(s, "sim")
        else:
            print(s, "nao")
    except EOFError:
        break