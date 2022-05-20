x = int(input())
z = x-1
while x >= z:
    z = int(input())
    if z > x:
        num = x
        contador = 1
        while x <= z:
            contador += 1
            num += 1
            x += num  
        print(contador)
        break
            
       
