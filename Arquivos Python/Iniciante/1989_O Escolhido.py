n = int(input())
nota_maior = 0
m_maior = 0

for i in range(n):
    m, nota = input().split()
    m = int(m)
    nota = float(nota)
    if nota >= 8:
        if nota > nota_maior:
            nota_maior = nota
            m_maior = m
if nota_maior == 0:
    print("Minimum note not reached")
else:
    print(m_maior)

