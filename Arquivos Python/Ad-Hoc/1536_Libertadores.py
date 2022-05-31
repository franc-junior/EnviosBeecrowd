class Time():
    def __init__(self):
        self.pontos = 0
        self.gols = 0
        self.gols_ad = 0
    def add_pontos(self, quant):
        self.pontos+=quant
    def add_gols(self, quant_gols, lugar):
        self.gols+=quant_gols
        if lugar == 1:
            self.gols_ad+=quant_gols
    def get_pontos(self):
        return self.pontos
    def get_gols(self):
        return self.gols
    def get_ad(self):
        return self.gols_ad

def sets(m, v, a, b):
    if m == v:
        a.add_pontos(1)
        b.add_pontos(1)
        
    elif m > v:
        a.add_pontos(3)
    else:
        b.add_pontos(3)

    a.add_gols(m, 0)
    b.add_gols(v, 1)

for i in range(int(input())):
    t1 = Time()
    t2 = Time()
    
    #Primeira Partida
    m, v = map(int, input().split(" x "))
    sets(m, v, t1, t2)

    #Segunda Partida
    m, v = map(int, input().split(" x "))
    sets(m, v, t2, t1)

    #Vencedor
    if t1.get_pontos() > t2.get_pontos():
        print("Time 1")
    elif t2.get_pontos() > t1.get_pontos():
        print("Time 2")
    else:
        if t1.get_gols() > t2.get_gols():
            print("Time 1")
        elif t2.get_gols() > t1.get_gols():
            print("Time 2")
        else:
            if t1.get_ad() > t2.get_ad():
                print("Time 1")
            elif t2.get_ad() > t1.get_ad():
                print("Time 2")
            else:
                print("Penaltis")

    # print("T1\npontos", t1.get_pontos(), "\ngols", t1.get_gols(),"\ngols fora", t1.get_ad())
    # print("T2\npontos", t2.get_pontos(), "\ngols", t2.get_gols(),"\ngols fora", t2.get_ad())
