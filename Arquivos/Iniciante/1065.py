quant = 0
for i in range(5):
    valor = int(input())
    if valor % 2 == 0:        
        quant += 1
print("{} valores pares".format(quant))