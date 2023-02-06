while True:
    try:
        cp = input()

        b1 = 0
        b2 = 0
        for i in range(9):
            b1 += (i+1)*int(cp[i])
            b2 += (9-i)*int(cp[i])
        b1 = b1%11
        b2 = b2%11

        if b2 == 10:
            b2 = 0
        if b1 == 10:
            b1 = 0

        print(cp[0:3]+"."+cp[3:6]+"."+cp[6:]+"-"+str(b1)+str(b2))
    
    except EOFError:
        break
