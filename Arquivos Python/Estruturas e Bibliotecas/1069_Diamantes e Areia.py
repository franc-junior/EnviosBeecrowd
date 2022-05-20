n = int(input())
for i in range(n):
    peneira = input().replace(".", '')
    soma = 0
    cont = 0

    for p in peneira:
        if p == '<':
            cont += 1

        else:
            if cont > 0:
                soma += 1
                cont -= 1
            
    print(soma)
