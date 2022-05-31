import math

class Cidade():
    def __init__(self, n) -> None:
        self.listaCasa = []
        self.somaPessoas = 0
        self.somaAgua = 0
        self.n = n
        self.calculo()

    def calculo(self):
        for i in range(self.n):
            x, y = map(int, input().split())
            self.somaPessoas += x
            self.somaAgua += y
            media_redonda = math.floor(y/x)
            
            if self.listaCasa == []:
                self.listaCasa.append("{}-{}".format(x,media_redonda))

            else:
                for i in range(len(self.listaCasa)):
                    media_estavel = int(self.listaCasa[i].split("-")[1])
                    
                    if media_redonda==media_estavel:
                        self.listaCasa[i] = "{}-{}".format(int(self.listaCasa[i].split("-")[0])+x,media_redonda)
                        break

                    elif media_redonda<media_estavel:
                        self.listaCasa.insert(i, "{}-{}".format(x,media_redonda))
                        break

                    elif i == len(self.listaCasa)-1:
                        self.listaCasa.append("{}-{}".format(x,media_redonda))

    def imprime_lista(self):
        string = ""
        for i in self.listaCasa:
            string += i+' '
        print(string[:-1])
        

    def imprime_media(self):
        return self.somaAgua/self.somaPessoas
   
n_cidade = 1
while True:
    n = int(input())
    cidade = Cidade(n)
    if n == 0:
        break
    elif n_cidade != 1:
        print()
    print("Cidade# {}:".format(n_cidade))
    cidade.imprime_lista()
    print("Consumo medio: {:.2f} m3.".format(cidade.imprime_media()-0.0049))
    n_cidade+=1

    
    