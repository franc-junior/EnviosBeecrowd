while True:
    try:
        h, m = map(int,input().split(":"))
        n =(((8-h)*60)-m)
        if n < 60:
            print("Atraso maximo:",60-n)
        else:
            print("Atraso maximo:",0)
    except EOFError:
        break