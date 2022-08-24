n = int(input())

cont = 7
for i in range(n):
    if i+1 <= 10:
        pass
    elif i+1 <= 30:
        cont += 1
    elif i+1 <= 100:
        cont += 2
    else:
        cont += 5
print(cont)
