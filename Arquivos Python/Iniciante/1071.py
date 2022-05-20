x = int(input())
y = int(input())
a = min(x,y)
b = max(x,y)
soma = 0
if a == b:
    soma = 0
for i in range(a+1, b):
    if i % 2 != 0: 
        soma = soma + i
print(soma)
