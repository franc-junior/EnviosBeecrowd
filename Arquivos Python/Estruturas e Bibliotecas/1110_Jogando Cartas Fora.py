#Francisco da Cunha
#Joyce Teixeira

while True: #Laço de repetição que vai se repetir infinitamete até aja um 'break'
    cartas = [] #Lista onde será armazenada as cartas
    discart = [] #Lista onde será armazenada as cartas descartadas
    cont = True #Variavel booleana, ficará variando entre True e False
    n = int(input()) #Recebe uma variavel inteira na entrada padrão, nomeada como 'n'
    if n == 0: #Condicinal onde; se o 'n' for igual a 0 acontece a seguinte ação
        break #O laço de repetição é encerrado   
    for i in range(1,n+1): #Laço de repetição que vai se repetir 'n' vezes, mais 1, e a partir de 1
        cartas.append(i) #Adiciona ao final da lista 'cartas' o número referente a variavel 'i' do laço de repetição, (Gera a lista de cartas)
    e = 0 #Variavel inteira 'e' que vai funcionar como contador
    while e != (n*2)-2: #laço de repetição que vai se repetir enquanto a variavel 'e' é diferente da variavel 'n' multiplicada por 2 e com 2 subtraido. (Siginifica que o laço vai ser encerrado quando haver apenas uma carta sobrando)
        if cont == True: #Condicional onde; se variavel for igual True acontece a seguinte ação
            discart.append(cartas[e]) #O número na lista cartas com o index referenciado pela variavel 'e' é adicionado ao final da lista 'discart'
            cont = False #A variavel 'cont' agora passa a ser False
        else: #Se a condição acima não for verdadeira (variavel 'cont' igual a False) acontece a seguinte ação
            cartas.append(cartas[e]) #O número na lista cartas com o index referenciado pela variavel 'e' é adicionado novamente ao final da lista 'cartas'
            cont = True #A variavel 'cont' agora passa a ser True
        e+=1 #É somado 1 a variavel 'e'
    print("Discarded cards: {}\nRemaining card: {}".format(str(discart).replace("[","").replace("]",""), cartas[e])) #Imprime na saída padrão a lista 'discart' removendo com o metodo replace o '[' e o ']', e imprime o ultimo digito da lista cartas representando a ultima carta restante no baralho

