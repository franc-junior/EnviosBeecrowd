q = input()
v = input().split()
if v.count("0")<=len(v)- v.count("0"):
    print("N")
else:
    print("Y")