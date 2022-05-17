n, m = map(int, input().split())
while n+m != 0:
    troco = m-n
    cont = 0
    if troco>=100:
        cont += troco//100
        troco = troco%100
    if troco>=50:
        cont += troco//50
        troco = troco%50
    if troco>=20:
        cont += troco//20
        troco = troco%20
    if troco>=10:
        cont += troco//10
        troco = troco%10
    if troco>=5:
        cont += troco//5
        troco = troco%5
    if troco>=2:
        cont += troco//2
        troco = troco%2
    if (troco == 0) and (cont==2):
        print("possible")
    else:
        print("impossible")
    n, m = map(int, input().split())
