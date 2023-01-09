caso = 1
while True:
    try:
        n1 = input()
        n2 = input()
        t_n1 = len(n1)
        i = 0
        ultimo = 0
        q = 0
        while True:
            try:
                end = n2.index(n1[0],i)
                if n2[end:end+t_n1] == n1:
                    ultimo = end
                    q+=1
                i=end+1
                
            except ValueError:
                print("Caso #{}:".format(caso))
                if q == 0:
                    print("Nao existe subsequencia\n")
                else:
                        print("Qtd.Subsequencias: {}\n"
                        "Pos: {}\n".format(q, ultimo+1))
                caso+=1
                break
        
    except EOFError:
        break