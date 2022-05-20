# >>> ord('a')
# 97
# >>> chr(97)
# 'a'
alfabeto = "abcdefghijklmnopqrstuvwxyzçABCDEFGHIJKLMNOPQRSTUVWXYZÇ"
n = int(input())
for i in range(n):
    p1 = ''
    m = input()
    for j in range(len(m)):
        if m[j] in alfabeto:
            p1+=chr(ord(m[j])+3)
        else:
            p1+=m[j]
    p2 = ''.join(reversed(p1))
    p3 = list(p2)
    metade = len(p2)//2
    for j in range(metade,len(p2)):
        p3[j] = chr(ord(p3[j])-1)
    for j in p3:
        print(j,end="")
    print()
    
    
       