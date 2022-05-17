a = 1
r = 1
for i in range(3,40,2):
    a += a
    r+=(i/a)+0.0001
print(round(r))



