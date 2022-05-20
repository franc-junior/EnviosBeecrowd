n = int(input())
x = list(input().split())
menor = int(x[0])
posicao = 0

for i in range(n):
    x[i] = int(x[i])

    if x[i] < menor:
        menor = x[i]
        posicao = i

print("Menor valor: {}\nPosicao: {}".format(int(menor), int(posicao)))
        


    
    