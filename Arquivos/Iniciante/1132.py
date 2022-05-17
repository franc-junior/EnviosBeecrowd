a = int(input())
b = int(input())
x = min(a, b)
y = max(a, b)
soma = 0
for i in range(x, y+1):
    if i % 13 != 0:
        soma += i
print(soma)
