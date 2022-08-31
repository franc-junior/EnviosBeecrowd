for i in range(int(input())):
    v = None
    for j in range(int(input())):
        indioma = input()
        if v == None:
            v = indioma
        elif v != indioma:
            v = "ingles"
    print(v)
