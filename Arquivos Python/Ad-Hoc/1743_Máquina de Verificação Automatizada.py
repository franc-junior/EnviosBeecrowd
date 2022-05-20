x = input().split()
y = input().split()
t = "Y"
for i in range(5):
    if x[i] == y[i]:
        t = "N"
print(t)
