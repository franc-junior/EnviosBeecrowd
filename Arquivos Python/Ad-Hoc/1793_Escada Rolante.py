while(True):
    n = int(input())
    if n == 0:
        break
    t = input().split(" ")
    soma = 10
    ant = int(t[-1])

    for j in range(n, 0, -1):
        calc = ant-int(t[j-1])

        if calc >= 10:
            soma+=10
        else:
            soma+=calc
        ant = int(t[j-1])
    print(soma)
    
        