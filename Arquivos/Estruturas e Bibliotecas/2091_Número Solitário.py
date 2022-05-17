n = int(input())
while n!=0:
    a = input().split()
    solitario = []
    for i in range(n):
        if a[i] in solitario:
            solitario.remove(a[i])
        else:
            solitario.append(a[i])
    print(solitario[0])
    n = int(input())