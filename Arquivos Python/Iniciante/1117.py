vali = 0
media = 0
while True:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        vali += 1
        media += nota
        if vali == 2:
            print("media = {:.2f}".format(media/2))
            break
    elif nota < 0 or nota > 10:
        print("nota invalida") 
        
