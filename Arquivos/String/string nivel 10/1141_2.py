class Strings:
    def __init__(self, string, lista):
        self.string = string
        self.lista = lista

    def fucao(self):

        def func(lista, cont_max, cont_lis):  
            cont_lis2 = cont_lis 
            lista = lista[1:] 
            if len(lista)==0:
                return cont_max
            valor = lista[0]
            nvalor = valor
            cont = cont_lis
            if len(lista) == 1:
                return cont_max
            else:
                for i in lista:
                    if i in nvalor:
                        cont+=1
                        nvalor = i

            if cont > cont_max:
                cont_max = cont
                cont_lis2 += 1
            a = func(lista, cont_max, cont_lis2)
            if a > 0:
                return a
    


        lista_ordem = []
        
        for i in self.lista:
            if i in self.string:
                lista_ordem.append(i)

        lista_ordem.sort(key=len, reverse=True)
        
        
        return func(lista_ordem, 0, 1)
      

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