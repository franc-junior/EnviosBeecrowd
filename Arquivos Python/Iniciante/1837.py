a, b = list(map(int,input().split()))
q = a//b
r = a % b
if r < 0:
    r+=3
    q = a//b
print("{:.0f} {}".format(q, r))