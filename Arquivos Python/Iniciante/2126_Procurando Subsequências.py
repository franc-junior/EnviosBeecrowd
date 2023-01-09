caso = 1
while True:
    try:
        subs = input()
        strin = input()

        subsI = subs[::-1]
        strinI = strin[::-1]
        q = strin.count(subs)

        print("Caso #{}".format(caso))
        if q>=1:
            print("Qtd.Subsequencias: {}\nPos: {}".format(q, ((strin.index(subs))+len(strin))-len(subs)+1))
        else:
            print("Nao existe subsequencia")
        caso+=1
        print()

    except EOFError:
        break