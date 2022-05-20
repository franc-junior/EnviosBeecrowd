n = int(input())
dent = 0
fora = 0
for i in range(n):
    x = int(input())
    if x <= 20 and x >= 10:
        dent += 1
    else:
        fora += 1
print(dent, "in")
print(fora, "out")