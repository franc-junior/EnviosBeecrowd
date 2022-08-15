def func(cont, max, min):
    caract = ["A","B","C","D","E"]
    if max == min:
        imprime = " "*max + caract[cont]
    else:
        imprime = " "*min + caract[cont] + " "*(max-min-1) + caract[cont]
    return imprime
cont = 0
max_esp = 7
min_esp = 7
for i in range(9):
    if i < 5:
        print(func(cont, max_esp, min_esp))
        cont+=1
        max_esp+=1
        min_esp-=1
    else:
        cont-=1
        max_esp-=1
        min_esp+=1
        if i == 5:
            cont-=1
            max_esp-=1
            min_esp+=1
        print(func(cont, max_esp, min_esp))