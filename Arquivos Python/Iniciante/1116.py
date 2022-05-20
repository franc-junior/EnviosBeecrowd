n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if y != 0:
        div = x / y
        print("{:.1f}".format(div))
    if y == 0:
        print("divisao impossivel")
      

