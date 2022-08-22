import math

while True:
    try:
        n = int(input())
       
        quadrado = (n/2)**0.5
        #print(quadrado)

        x1 = math.floor(quadrado)
        x2 = math.ceil(quadrado)
        #print(x1)
        #print(x2)

        if (x1**2)+(x2**2) == n:
            print("YES")
        else:
            print("NO")
        
    except EOFError:
        break
    