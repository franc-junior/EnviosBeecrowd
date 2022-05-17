matriz = []
somas = []
t = 6


for lin in range(t):
    linha = []
    for col in range(t):
        valores = float(input())
        linha.append(valores)
        if cont <= lin:
            somas.append(valores)
    matriz.append(linha)
