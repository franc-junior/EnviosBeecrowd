j, r = map(int, input().split())
jogadores = [0]*j
partidas = list(map(int, input().split()))
cont = 0

maior_p = 0
maior_j = 0

for i in range(r):
    for u in range(j):
        jogadores[u] += partidas[cont]
        if jogadores[u] >= maior_p:
            maior_p = jogadores[u]
            maior_j = u
        cont += 1
print(maior_j+1)