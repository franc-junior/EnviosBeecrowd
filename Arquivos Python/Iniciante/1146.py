
while True:
    x = int(input(""))
    e = ""
    if x == 0:
        break
    else:
        for i in range(1, x+1):
            i = str(i)     
            e = e + i + " "
        print(e[:-1])
            
