n = 1
while(n != 0):
    n = int(input())
    sentenca = []
    for i in range(n):
        str0 = input()
        str1  = ''
        espaco = False
        for j in str0:
            if j != ' ':
                str1 += j
                espaco = True
            elif espaco:
                str1 += ' '
                espaco = False
        if str1[-1] == ' ':
            sentenca.append(str1[:-1])
        else:
            sentenca.append(str1)
        
    maxv = max(sentenca, key=lambda x: len(x))
    for i in range(n):
        dif = len(maxv) - len(sentenca[i])
        print(dif*' ', end="")
        print(sentenca[i])
