p, n = map(int, input().split())
canos = input().split()
for i in range(n-1):
    x = (int(canos[i+1])-int(canos[i]))
    y = (int(canos[i]))-(int(canos[i+1]))
    if (x > p) or (y > p):
        print("GAME OVER")
        exit()
    else:
        pass
print("YOU WIN")