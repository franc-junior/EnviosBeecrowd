h1, h2 = map(int, input().split())
if h2 <= 2:
    print("nova")
elif h1 < h2 and h2 <= 96:
    print("crescente")
elif h1 > h2 and h2 <= 96: 
    print("minguante")
else:
    print("cheia")
