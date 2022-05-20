def fim(lista):
    soma = 0
    for i in lista:
        if i <= 0:
            soma += 0
        else:
            soma += i
    return soma

n = int(input())
x = list(map(int, input().split()))
num = 0
star = 0
while n != star:
    
    if x[num] % 2 != 0:
        x[num] -= 1
        num += 1
        star += 1
    else:
        x[num] -= 1
        if num == 0:
            star += 1
            break
        else:
            num -= 1
print(star, fim(x))
