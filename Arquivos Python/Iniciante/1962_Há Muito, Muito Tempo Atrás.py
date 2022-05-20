n = int(input())
for i in range(n):
    a = int(input())
    t = 2015-a
    if t <= 0:
        t = t*(-1)+1
        print(t, "A.C.")
    else:
        print(t, "D.C.")