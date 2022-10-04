while True:
    s = []
    try:
        while s == []:
            s = input().split() 
              
        for j in s:
            t = len(j)
            if j == '0':
                break
            elif t > 15:
                print(0)
            else:
                c = 1
                for i in range(t):
                    c = (i+1)*c
                print(c)
        if j=='0':
            break
    except EOFError:
        break
