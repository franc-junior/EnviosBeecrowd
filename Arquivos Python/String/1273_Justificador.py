c = False
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if c == False:
            c = True
        else:
            print()
    palavras = []
    m = 0
    
    for i in range(n):
        palavra = input()
        t = len(palavra)
        if t > m:
            m = t
        palavras.append(palavra)
    for i in palavras:
        print("{:>{}}".format(i, m))
    