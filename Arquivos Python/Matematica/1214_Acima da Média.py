for i in range(int(input())):
    cn = list(map(int, input().split()))
    
    media = sum(cn[1:]) / cn[0]
    acm = 0
    for j in cn[1:]:
        if j>media:
            acm+=1
    
    print("{:.3f}%".format((100*acm)/cn[0]))
    