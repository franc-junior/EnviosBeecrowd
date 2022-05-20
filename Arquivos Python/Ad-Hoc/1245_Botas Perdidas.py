while True:
    try:
        n = int(input())
        l_m = []
        l_l = []
        cont = 0
        for i in range(n):
            m, l = input().split()
            if m in l_m:
                if l_l[l_m.index(m)] != l:
                    cont+=1
                    del l_l[l_m.index(m)] 
                    del l_m[l_m.index(m)] 
                else:
                    l_m.append(m)
                    l_l.append(l)  
            else:
                l_m.append(m)
                l_l.append(l)
        print(cont)
    except EOFError:
        break