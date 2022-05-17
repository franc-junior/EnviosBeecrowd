n = int(input())

totalC = 0
totalS = 0
totalR = 0

for i in range(1, n+1): 

    quant, tipo = input().split(' ')
    quant = int(quant)
    tipo = str(tipo)
    
    if tipo == 'C':
        totalC += quant
    if tipo == 'R':
        totalR += quant
    if tipo == 'S':
        totalS += quant
    
    total = totalC + totalR + totalS
    pcC = totalC * 100 / total
    pcR = totalR * 100 / total
    pcS = totalS * 100 / total

print("Total:", total, "cobaias")        
print("Total de coelhos:", totalC)
print("Total de ratos:", totalR)
print("Total de sapos:", totalS)

print("Percentual de coelhos: {:.2f} %".format(pcC))
print("Percentual de ratos: {:.2f} %".format(pcR))
print("Percentual de sapos: {:.2f} %".format(pcS))
    
    
   