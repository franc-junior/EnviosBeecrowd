for i in range(int(input())):
    x = 1
    for j in range(int(input())):
        x = x+x
    print("{:.0f} kg".format((x/12)//1000))