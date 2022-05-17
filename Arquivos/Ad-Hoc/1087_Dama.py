while True:
    x1, y1, x2, y2 = map(int,input().split())
    if x1+x2+y1+y2 == 0:
        break
    elif x2==x1 and y2==y1:
        print(0)
    elif x2==x1 or y2==y1:
        print(1)
    else:
        i = 1
        while True:
            dx1 = (x1-i)
            dy1 = (y1-i)

            dx2 = (x1-i)
            dy2 = (y1+i)

            dx3 = (x1+i)
            dy3 = (y1-i)

            dx4 = (x1+i)
            dy4 = (y1+i)

            i+=1

            if i > 8:
                print(2)
                break
            elif (x2 == dx1) and (y2 == dy1):
                print(1)
                break
            elif (x2 == dx2) and (y2 == dy2):
                print(1)
                break
            elif (x2 == dx3) and (y2 == dy3):
                print(1)
                break
            elif (x2 == dx4) and (y2 == dy4): 
                print(1)
                break 
    