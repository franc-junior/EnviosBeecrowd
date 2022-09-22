while True:
    n = int(input())
    if n == 0:
        break
    esta = []
    very = True
    cheg = input().split()
    said = input().split()
    movi = ""
    for vag in range(n):
        while very == True:
            if (cheg != []) and (cheg[0] == said[vag]):
                movi+="IR"
                del cheg[0]
                break
            else:
                if (esta != []) and esta[0] == said[vag]:
                    movi+="R"
                    del esta[0]
                    break
                elif cheg != []:
                    movi+="I"
                    esta.insert(0, cheg[0])
                    del cheg[0]
                else:
                    movi+=" Impossible"
                    very = False
                    break
    print(movi)



