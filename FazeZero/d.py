pontos = [0]*5
for j in range(int(input())):
    certo = list(input())
    rodada = []
    lista = input().split()
    for i in range(5):
        c = 0
        palavra = list(lista[i])
        erros = 0
        while palavra != certo:
            try:
                if palavra[c] == certo[c]:
                    c+=1
                elif palavra[c] != certo[c]:
                    erros += 1
                    if palavra[c] not in certo[c:]:
                        if certo[c] not in palavra[c:]:      
                            palavra[c] = certo[c]
                            c+=1
                        else:
                            del palavra[c]
                    else:
                        palavra.insert(c,certo[c])
                        c+=1

            except IndexError:
                erros += 1
                if len(palavra) > len(certo):
                    del palavra[c]
                else:
                    palavra.append(certo[c])
                    c+=1

        rodada.append(erros)
    menor = min(rodada)
    if menor == 0:
        p = 1
    else:
        p = 0.5
    for i in range(5):
        if rodada[i] == menor:
            pontos[i] += p

maior = max(pontos)
print(maior)

venc = ""
for j in range(5):
    if pontos[j] == maior:
        venc += str(j+1)+" "
print(venc[:-1])

    
