
class Labirinto():
    def __init__(self, m) -> None:
        self.matriz = m
        self.save = []
        self.jafoi = []
    def verificaLinha(self, col, lin):

        i = col
        j = lin
    

        self.jafoi.append([i, j])
        if self.matriz[i][j] == 0:

            #Esquerda
            if (j > 0) and (self.matriz[i][j-1] == 0) and ([i,j-1] not in self.jafoi):
                if ((j < 4) and (self.matriz[i][j+1] == 0) and ([i, j+1] not in self.jafoi)) or ((i < 4) and (self.matriz[i+1][j] == 0) and ([i+1, j] not in self.jafoi)):
                    self.save.append([i, j])
                return self.verificaLinha(i, j-1)

            #Baixo
            elif (i < 4) and (self.matriz[i+1][j] == 0) and ([i+1, j] not in self.jafoi):
                if ((j > 0) and (self.matriz[i][j-1] == 0)) or ((j < 4 and self.matriz[i][j+1] == 0) and ([i, j+1] not in self.jafoi)):
                    self.save.append([i+1, j])
                return self.verificaLinha(i+1, j)
        
            #Direira
            elif (j < 4) and (self.matriz[i][j+1] == 0) and ([i, j+1] not in self.jafoi):
                if ((i < 4) and (self.matriz[i+1][j] == 0)) or ((j > 0) and (self.matriz[i][j-1] == 0)):
                    self.save.append([i, j+1])
                return self.verificaLinha(i, j+1)
            
            else:
                if j == i == 4:
                    print("Valeu o Boi")
                    return "Valeu o boi"
                elif self.save == []:
                    return "Não valeu o boi"
                    
                c = self.save[len(self.save)-1]
                del self.save[len(self.save)-1]
                print(c[0], c[1])
                return self.verificaLinha(c[0], c[1])
          
                


matriz = []
labirinto = Labirinto(matriz)
for i in range(5):
    matriz.append(list(map(int, input().split())))

labirinto = Labirinto(matriz)
print(labirinto.verificaLinha(0, 0))