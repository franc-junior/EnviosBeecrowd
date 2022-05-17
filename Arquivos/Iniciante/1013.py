a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
ab = (a + b + abs(int(a) - b)) / 2
abc = (ab + c + abs(int(ab) - c)) / 2
print("{:.0f} eh o maior".format(abc))
