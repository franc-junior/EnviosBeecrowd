n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    mdc = 1
    j = 2
    if a%j==0 and b%j==0:
        mdc = mdc*j

    while True:
        if a%j==0 and b%j==0:
            a = a/j
            b = b/j
        elif a <= 1 and b <= 1:
            break
        else:
            j+=1
            if a%j==0 and b%j==0:
                mdc = mdc*j
    print(mdc)