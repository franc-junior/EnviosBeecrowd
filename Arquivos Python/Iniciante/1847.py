a,b,c = map(int, input().split())
if a > b:
    if b <= c or (b-a) < (c-b):
        print(":)")
    elif (b-a) >= (c-b):
        print(":(")
elif b > a:
    if b >= c or (b-a) > (c-b):
        print(":(")
    elif (b-a) <= (c-b):
        print(":)")
elif a == b:
    if b < c:
        print(":)")
    else:
        print(":(")
