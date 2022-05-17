while True:
    h1, m1, h2, m2 = map(int,input().split())
    if h1+h2+m1+m2 == 0:
        break
    h = ((h2*60)+m2)-((h1*60)+m1)
    if h<0:
        h = (24*60)+h
    print(h)
        