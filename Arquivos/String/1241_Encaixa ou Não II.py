n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    if b == a[len(a)-len(b):]:
        print("encaixa")
    else:
        print("nao encaixa")
   
