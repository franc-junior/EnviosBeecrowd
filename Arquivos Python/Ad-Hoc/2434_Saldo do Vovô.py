ini = (input().split(" "))

saldo = int(ini[1])
menor = saldo
for i in range(int(ini[0])):
    saldo += int(input())
    if (saldo < menor):
        menor = saldo
print(menor)
