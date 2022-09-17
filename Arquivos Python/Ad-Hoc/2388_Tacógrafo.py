soma = 0
for i in range(int(input())):
    t, v = map(int, input().split())
    soma+= t*v
print(soma)