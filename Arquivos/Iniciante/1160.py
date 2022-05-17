t = int(input())

for i in range(t):
    pa, pb, ga, gb = input().split()
    pa = int(pa)
    pb = int(pb)
    ga = float(ga)
    gb = float(gb)

    aumento = 0

    while pb >= pa:
        aumento += 1

        cresA = (pa * ga) // 100
        cresB = (pb * gb) // 100

        pa += cresA
        pb += cresB
        
        if aumento > 100:
            print("Mais de 1 seculo.")
            break

    if aumento <= 100:
        print(aumento, "anos.")