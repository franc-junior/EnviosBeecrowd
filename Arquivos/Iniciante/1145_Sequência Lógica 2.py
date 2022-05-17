x, y = map(int, input().split())
fim = ''
cont = 0

while True:
    for i in range(x):
        cont += 1
        fim += str(cont)

        if cont == y:
            if i == x-1:
                pass
            else:
                fim += " "
            print(fim)
            exit()
            
        elif i == x-1:
            fim += "\n"
        
        else:
            fim += " "

    