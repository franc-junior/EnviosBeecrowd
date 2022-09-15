while True:
    n = int(input())
    if n == 0:
        break
    while True:
        saida = list(map(int, input().split()))
        if saida[0] == 0:
            print()
            break
        trens = list(range(1, n+1))
        estacao = [0]
        num = 1
        r = "Yes"
        for said in saida:
            while r != "No":
                if said == num:
                    num += 1
                    break
                elif estacao[0] == said:
                    del estacao[0]
                    break
                elif (said != num) and (num <= n):
                    estacao.insert(0, num)
                    num += 1
                else:
                    r = "No"
        print(r)
