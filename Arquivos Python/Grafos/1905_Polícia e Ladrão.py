class Labirinto():
    def __init__(self, m) -> None:
        self.matriz = m
        self.save = []
        self.jafoi = []

    def verificaLinha(self, col, lin):

        self.jafoi.append([col, lin])
        #print(col, lin)
        #Final
        if lin == col == 4:
            return "COPS"
        
        elif self.matriz[col][lin] == 0:
            esquerda = baixo = direita = cima = 0

            #Verifica as possibilidades
            if (lin > 0) and (self.matriz[col][lin-1] == 0) and ([col,lin-1] not in self.jafoi):
                esquerda = 1
            if (col < 4) and (self.matriz[col+1][lin] == 0) and ([col+1, lin] not in self.jafoi):
                baixo = 1
            if (lin < 4) and (self.matriz[col][lin+1] == 0) and ([col, lin+1] not in self.jafoi):
                direita = 1
            if (col > 0) and (self.matriz[col-1][lin] == 0) and ([col-1, lin] not in self.jafoi):
                cima = 1

            #Se existir mais que uma possibilidade salva a posição
            if (esquerda + baixo + direita + cima) > 1:
                self.save.append([col,lin])

            #Movimenta para a poxima posição pela ordem de prioridade
            if esquerda == 1:
                return self.verificaLinha(col, lin-1)
            elif baixo == 1:
                return self.verificaLinha(col+1, lin)
            elif direita == 1:
                return self.verificaLinha(col, lin+1)
            elif cima == 1:
                return self.verificaLinha(col-1, lin)

            else:
                if self.save == []:
                    return "ROBBERS"

                #Se não tiver mais para onde ir, irá voltar para a ultima posição que tinha mais de um opção
                c = self.save[len(self.save)-1]
                del self.save[len(self.save)-1]
                return self.verificaLinha(c[0], c[1])
        else:
            return "ROBBERS"

for f in range(int(input())):
    matriz = []
    c = 0
    while c != 5:
        lista = input().split()
        if len(lista) == 5:
            matriz.append(list(map(int, lista)))
            c+=1

    labirinto = Labirinto(matriz)
    print(labirinto.verificaLinha(0, 0))