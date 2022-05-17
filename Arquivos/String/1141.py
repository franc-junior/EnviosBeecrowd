class Strings:
    def __init__(self, string, lista):
        self.string = string
        self.lista = lista

    def fucao(self):

        lista_ordem = []
        
        for i in self.lista:
            if i in self.string:
                lista_ordem.append(i)

        lista_ordem.sort(key=len, reverse=True)
        maior = lista_ordem[0]
        cont = 0
        cont2= 0 
        for i in lista_ordem:
            if i in maior:
                maior=i
                cont+=1
        
        return max(cont,cont2)

while True:           
    lista_str = []
    maior_valor=0
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        palavra = input()
        lista_str.append(palavra)
    for i in range(n):
        strin = Strings(lista_str[i], lista_str)
        valor = strin.fucao()
        if valor > maior_valor:
            maior_valor=valor

    print(maior_valor)