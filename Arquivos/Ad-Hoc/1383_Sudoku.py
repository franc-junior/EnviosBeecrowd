n = int(input())
for i in range(n):
    m1 = []
    m2 = []
    m3 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    soma = 0
    for matr in range(3):
        m1 = []
        m2 = []
        m3 = []
        for linha in range(3):
            d = list(map(int, input().split()))
            m1 += d[:3]
            m2 += d[3:6]
            m3 += d[6:]
            c1.append(d[0])
            c2.append(d[1])
            c3.append(d[2])
            c4.append(d[3])
            c5.append(d[4])
            c6.append(d[5])
            c7.append(d[6])
            c8.append(d[7])
            c9.append(d[8])
            # print(len(set(d)))
            soma+=len(set(d))
        # print(len(set(m1)))
        # print(len(set(m2)))
        # print(len(set(m3)))
        soma += len(set(m3)) + len(set(m2)) + len(set(m1))
    # print(len(set(c1)))
    # print(len(set(c2)))
    # print(len(set(c3)))
    # print(len(set(c4)))
    # print(len(set(c5)))
    # print(len(set(c6)))
    # print(len(set(c7)))
    # print(len(set(c8)))
    # print(len(set(c9)))
    soma += len(set(c1)) + len(set(c2)) + len(set(c3)) + len(set(c4)) + len(set(c5)) + len(set(c6)) + len(set(c7)) + len(set(c8)) + len(set(c9))
    print("Instancia", i+1)
    if soma == 243:
        print("SIM")
    else:
        print("NAO")
    print()

