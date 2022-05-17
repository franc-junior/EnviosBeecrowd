a, b = map(int, input().split())
while a+b!=0:
    
    xP = input().split()
    yP = input().split()
    x = set(xP)
    y = set(yP)

    for i in min(xP, yP):
        if (i in x) and (i in y):
            x.remove(i)
            y.remove(i)
                
    print(min(len(x),len(y)))
    a, b = map(int, input().split()) 


