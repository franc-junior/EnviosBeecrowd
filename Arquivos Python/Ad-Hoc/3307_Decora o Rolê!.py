for i in range(int(input())):
    a = int(input())
    r = (a/(3.14*4))**0.5
    if r<=12:
        print("vermelho = R$ {:.2f}".format(a*0.09))
    elif r<= 15:
        print("azul = R$ {:.2f}".format(a*0.07))
    else:
        print("amarelo = R$ {:.2f}".format(a*0.05))