grena = 1
inter = 0
gremi = 0
empat = 0
while True:
    x, y = map(int, input().split())
    if x > y:
        inter += 1
    elif x < y:
        gremi += 1
    else:
        empat += 1

    if inter > gremi:
        vence = 'Inter venceu mais'
    elif inter < gremi:
        vence = 'Gremio venceu mais'
    else:
        vence = 'Nao houve vencedor'

    res = int(input("Novo grenal (1-sim 2-nao)\n"))

    if res == 1:
        grena += 1
        continue
    if res == 2:
        print(grena, "grenais")
        print("Inter:{}\nGremio:{}\nEmpates:{}\n{}".format(inter, gremi, empat, vence))
        break
    
