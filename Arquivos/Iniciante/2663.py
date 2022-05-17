classificados = []
n = int(input())
k = int(input())
cont = 0

for i in range(n):
    pontuacao = int(input())
    classificados.append(pontuacao)

for j in range(k):
    if k > cont:
        x = max(classificados)
        y = classificados.count(x)

        if y > 1:
            for q in range(y):
                cont += 1
                classificados.remove(x)
        else:
            cont += 1
            classificados.remove(x)
    else:
        print(cont)
        exit()
    
print(cont)
    


