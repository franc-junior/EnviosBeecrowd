for i in range(int(input())):
    Ax, Ay, Bx, By, Cx, Cy, Dx, Dy, Rx, Ry = map(int, input().split())
      
    # if ((Cx - Ax)<=1  or (Cy - Ay)<=1): 
    #     print(0)
    # else:    
    if ((Rx >= Ax) and (Rx <= Cx)) and ((Ry >= Ay) and (Ry <= Cy)) and (Ay==By and Bx==Cx and Cy==Dy and Dx==Ax):
        print(1)
    else:
        print(0)