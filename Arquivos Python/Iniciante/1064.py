a = 0
soma = 0

for i in range(6):
    x = float(input())
    if x > 0:
        a += 1 
        soma += x 

print(a ,"valores positivos\n{:.1f}".format(soma/a))