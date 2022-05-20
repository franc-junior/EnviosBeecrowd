n = int(input())
la, lb = map(int, input().split())
sa, sb = map(int, input().split())
if n in range(la, lb+1) and n in range(sa, sb+1):
    print("possivel")
else:
    print("impossivel")