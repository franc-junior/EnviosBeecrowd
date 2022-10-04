m, n = map(int, input().split())
colunas = [0]*(n+1)
for i in range(m):
    linha = list(map(int, input().split()))
    soma_linha = sum(linha)
    if soma_linha > colunas[n]:
        colunas[n] = soma_linha
    for j in range(n):
        colunas[j] += linha[j]
print(max(colunas))