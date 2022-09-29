def countt(e):
    return e[1]
def asccc(e):
    return e[0]
c = False
while True:
    try:
        lista = []
        strings = list(input())
        if c == False:
            c = True
        else:
            print()
        string2 = set(strings)
        for i in string2:
            lista.append([ord(i),strings.count(i)])
        lista.sort(key=asccc, reverse=True)
        lista.sort(key=countt)
        for i in lista:
            print(i[0],i[1])
        
    except EOFError:
        break