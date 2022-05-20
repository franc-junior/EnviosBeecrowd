n = int(input())
while n != 0:
    v = list(map(int, input().split()))
    v_ordenado = sorted(v, reverse=True)
    if len(v)<2:
        suspeito = v_ordenado[0]
    else:
        suspeito = v_ordenado[1]
    print(v.index(suspeito)+1)
    n = int(input())
    