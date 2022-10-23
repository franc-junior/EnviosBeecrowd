string = input().split()
t = len(string)
for i in range(t):
    print(string[i][1::2], end="")
    if i != t-1:
        print(end=" ")
print()