i = 0
while i != 22:
    for j in range(1, 3+1):
        x = i/10
        if (x % 2 == 0) or (x == 1.0):
            print("I={:.0f} J={:.0f}".format(x, j+x))
        else:
            print("I={:.1f} J={:.1f}".format(x, j+x))
    i += 2
    
           
