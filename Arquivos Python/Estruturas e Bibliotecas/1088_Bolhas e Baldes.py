nuns = input().split()
while nuns[0] != '0':
    p = nuns[1:]
    cont = 0
    for i in range(int(nuns[0])-1):
        if str(i+1) != p[i]: 
            end = p.index(str(i+1), i+1)
            del p[end]
            p.insert(i,str(i+1))
            cont+=(end-i)
    if cont%2 == 0:
        print("Carlos")
    else:
        print("Marcelo")
    nuns = input().split()

