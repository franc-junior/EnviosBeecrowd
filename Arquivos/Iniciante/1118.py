nota_f = 0
soma = 0
perg = 1
while perg == 1:
    nota = float(input())

    if nota > 10 or nota < 0:
        print("nota invalida")

    else:
        nota_f += nota
        soma += 1

        if soma == 2:
            nota_f /= 2
            print(("media = {:.2f}").format(nota_f))
            soma = 0
            nota_f = 0
            perg = int(input("novo calculo (1-sim 2-nao)\n"))

            while perg != 1 and perg != 2:
                perg = int(input("novo calculo (1-sim 2-nao)\n"))
                if perg == 1:
                    continue
                elif perg == 2:
                    break
                

           
            
                

    

    

