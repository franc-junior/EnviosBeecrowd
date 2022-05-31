import math

n_cidade = 1
while True:
    n = int(input())
    if n == 0:
        break
    elif n_cidade != 1:
        print()

    listaCasa = []
    somaPessoas = 0
    somaAgua = 0

    for i in range(n):
        x, y = map(int, input().split())
        somaPessoas += x
        somaAgua += y
        media_redonda = math.floor(y/x)
        
        if listaCasa == []:
            listaCasa.append("{}-{}".format(x,media_redonda))

        else:
            for i in range(len(listaCasa)):
                person ,media_estavel = map(int,listaCasa[i].split("-"))
                
                if media_redonda==media_estavel:
                    listaCasa[i] = "{}-{}".format(person+x,media_redonda)
                    break

                elif media_redonda<media_estavel:
                    listaCasa.insert(i, "{}-{}".format(x,media_redonda))
                    break

                elif i == len(listaCasa)-1:
                    listaCasa.append("{}-{}".format(x,media_redonda))

    print("Cidade# {}:".format(n_cidade))
    string = ""
    for i in listaCasa:
        string += i+' '
    print(string[:-1])
    print("Consumo medio: {:.2f} m3.".format(somaAgua/somaPessoas-0.0049))
    n_cidade+=1

    
    