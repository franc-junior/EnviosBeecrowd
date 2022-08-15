caract = ["A","B","C","D","E"]
cont = 0
max_esp = 7
min_esp = 7
for i in range(9):
    if i < 5:
        if max_esp == min_esp:
            imprime = " "*max_esp + caract[cont]
        else:
            imprime = " "*min_esp + caract[cont] + " "*(max_esp-min_esp-1) + caract[cont]
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
        if max_esp == min_esp:
            imprime = " "*max_esp + caract[cont]
        else:
            imprime = " "*min_esp + caract[cont] + " "*(max_esp-min_esp-1) + caract[cont]
    print(imprime)

