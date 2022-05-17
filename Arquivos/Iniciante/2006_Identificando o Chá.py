t = int(input())
l = input().split(' ')
soma = 0
for i in l:
    if int(i) == t:
        soma += 1
print(soma)