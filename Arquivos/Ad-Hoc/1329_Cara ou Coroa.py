def fun():
    n = int(input())
    if n == 0:
        return 
    else:
        jogos = input().split()
        print("Mary won {} times and John won {} times".format(jogos.count('0'),jogos.count('1')))
        return fun()     
fun()
