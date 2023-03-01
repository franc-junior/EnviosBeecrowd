class City():
    def __init__(self, n, m, c) -> None:
        self.barruada = []
        self.dboa = 0
        self.p_veiculo = c
        self.vertical = n
        self.horizont = m
        
    def movimento(self):
        print(self.p_veiculo)
        for i in range(len(self.p_veiculo)):
            #print(self.p_veiculo[i][2])
            if self.p_veiculo[i][2] == "N":
                self.p_veiculo[i][0]-=1
                if self.p_veiculo[i][0] == 0:
                    self.p_veiculo[i][2] = "1"
                    
            elif self.p_veiculo[i][2] == "S":
                self.p_veiculo[i][0]+=1
                if self.p_veiculo[i][0] == self.vertical:
                    self.p_veiculo[i][2] = "1"
                
            elif self.p_veiculo[i][2] == "L":
                self.p_veiculo[i][1]+=1
                if self.p_veiculo[i][1] == 0:
                    self.p_veiculo[i][2] = "1"
                    
            else: #i[2] == "O"
                self.p_veiculo[i][1]-=1
                if self.p_veiculo[i][1] == self.horizont:
                    self.p_veiculo[i][2] == "1"
                    
            self.movimento()
    
    def posicao(self):
        t = len(self.p_veiculo)
        
        for i in range(t):
            for j in range(i, t):
                if (self.p_veiculo[j][0] == self.p_veiculo[i][0]) and (self.p_veiculo[j][1] == self.p_veiculo[i][1]):
                    
             
        
n, m, c = map(int, input().split())
carros = []
for i in range(c):
    a, b, d = input().split()
    a = int(a)
    b = int(b)
    carros.append([a, b, d])
    
city = City(n, m, carros)
city.movimento()