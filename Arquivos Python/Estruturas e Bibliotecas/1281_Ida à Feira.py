for i in range(int(input())):
    soma = 0 
    fruta = []
    preco = []
    for j in range(int(input())):
        k = input().split()
        fruta.append(k[0])
        preco.append(k[1])
    for j in range(int(input())):
        k = input().split()
        soma+=float(preco[fruta.index(k[0])])*int(k[1])
    print("R$ {:.2f}".format(soma))