#Se quiser alerar a largura do quadro é só alterar o valor de 't' (a questão não exige essa ação)
    #Apenas números impares

def traco(t):
    return ("-"*t)

def x35(t, n):
    x = "|"
    stri = "x = 35"

    for i in range(3):
        if n == None:
            if i == 0:
                x += " "
            else:
                x += " "*((t-2)//2)
        elif i == n-1:
            if i == 2:
                x+=(" "+stri)
            else:
                x+=(stri+" ")
        else:
            x += " "*((t-9)//2)
    x+="|"
    return x

t = 39
print(traco(t))
cont = 1
for i in range(5):
    if (i%2) == 0:
        print(x35(t, cont))
        cont += 1
    else:
        print(x35(t, None))
print(traco(t)+"\n")


# tr = '---------------------------------------\n'
# um = '|x = 35                               |\n'
# va = '|                                     |\n'
# dois = '|                x = 35               |\n'
# tres = '|                               x = 35|\n'

# print(tr+ um+ va+ dois+ va+ tres+ tr)