s = 0
for i in range(1,100):
    s += i + 1/i + 2
fim = s/100
print("{:.2f}".format(fim))