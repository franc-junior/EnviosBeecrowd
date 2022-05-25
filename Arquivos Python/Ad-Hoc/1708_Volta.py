x, y = map(int, input().split())
sx = x
sy = y
cont = 1
while sy<sx+y:
    sx+=x
    sy+=y
    cont+=1
print(cont)
