verifica = 2
cont = 0
for i in range(int(input())):
    n = int(input())
    if n != verifica:
        cont+=1
        verifica = n
print(cont)
    