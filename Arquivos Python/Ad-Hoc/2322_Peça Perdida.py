n = int(input())
nuns = input().split()
for i in range(1,n+1):
    if str(i) not in nuns:
        print(i)
        break
