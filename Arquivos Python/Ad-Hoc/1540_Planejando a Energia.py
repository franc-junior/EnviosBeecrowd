for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    print(str("{:.3f}".format((d-b)/(c-a))).replace(".",",")[:-1])