n = int(input())
lados = {1:"N",2:"L",3:"S",4:"O"}
while n!=0:
    comandos = input()
    direcao = 1
    for i in range(n):
        if comandos[i] == "D":
            direcao+=1
            if direcao == 5:
                direcao=1
        else:
            direcao-=1
            if direcao == 0:
                direcao = 4
    print(lados[direcao])
    n = int(input())
    
        

