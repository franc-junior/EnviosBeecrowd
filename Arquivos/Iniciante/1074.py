n = int(input())
for i in range(n):
    x = int(input())
    if x % 2 == 0 and x < 0:
        r = 'EVEN NEGATIVE'
    if x % 2 == 0 and x > 0:
        r = 'EVEN POSITIVE'
    if x % 2 != 0 and x > 0:
        r = 'ODD POSITIVE'
    if x % 2 != 0 and x < 0:
        r = 'ODD NEGATIVE'
    if x == 0:
        r = 'NULL'
    print(r)
