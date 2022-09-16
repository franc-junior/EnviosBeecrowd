n = int(input())
p, c, q = input().split()
p = int(p)
q = int(q)
if c == "*":
    r = p*q
else:
    r = p+q
if r>n:
    print("OVERFLOW")
else:
    print("OK")