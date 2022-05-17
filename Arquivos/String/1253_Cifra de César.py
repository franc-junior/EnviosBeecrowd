alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
for i in range(n):
    string = input()
    num = int(input())
    for j in string:
        letra = alfabeto.index(j)
        print(alfabeto[alfabeto.index(j)-num],end="")
    print()
