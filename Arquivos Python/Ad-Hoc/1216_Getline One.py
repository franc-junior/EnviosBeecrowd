distancia = 0
divisor = 0
while True:
    try:
        nome=input()
        distancia += int(input())
        divisor+=1
    except EOFError:
        print("{:.1f}".format(distancia/divisor))
        break