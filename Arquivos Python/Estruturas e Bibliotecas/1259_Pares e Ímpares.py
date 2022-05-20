n = int(input())
pares = []
impar = []
for i in range(n):
    num = int(input())
    if num%2 == 0:
        pares.append(num)
    else:
        impar.append(num)
pares.sort()
impar.sort(reverse=True)
for i in (pares+impar):
    print(i)