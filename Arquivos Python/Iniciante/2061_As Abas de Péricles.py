n, m = map(int, input().split())
for i in range(m):
    t = input()
    if t == "fechou":
        n+=1
    else:
        n-=1
print(n)