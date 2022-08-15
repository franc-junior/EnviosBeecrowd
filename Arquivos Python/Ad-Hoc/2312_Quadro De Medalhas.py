def nome(e):
    return e[0]
def ouro(e):
    return e[1]
def prata(e):
    return e[2]
def bronze(e):
    return e[3]

lista_paises = []
for i in range(int(input())): 
    nome_p, ouro_p, prata_p, bronze_p = input().split()
    ouro_p = int(ouro_p)
    prata_p = int(prata_p)
    bronze_p = int(bronze_p)
    lista_paises.append([nome_p, ouro_p, prata_p, bronze_p])

lista_paises.sort(key=nome)
lista_paises.sort(key=bronze, reverse=True)
lista_paises.sort(key=prata, reverse=True)
lista_paises.sort(key=ouro, reverse=True)

for i in lista_paises:
    print(i[0], i[1], i[2], i[3])