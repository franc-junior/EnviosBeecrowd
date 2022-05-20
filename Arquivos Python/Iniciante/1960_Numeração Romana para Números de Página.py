n = list(input())
numero = ""
cont = len(n)

def roma(x,r5,r4,r1,r9):
    num = ''
    while x != 0:
        if (x >= 5) and (x <= 8):
            num += r5
            x -= 5
        elif x < 5:
            if x == 4:
                num += r4
                x -= 4
            else:
                num += r1
                x -= 1
        elif x >= 9:
            if x == 9:
                num += r9
                x -= 9
    return num

for i in range(len(n)):
    x = int(n[i])
    if cont >= 3:
        numero += roma(x,'D','CD','C','CM')
        cont -= 1
    elif cont == 2:
        numero += roma(x,'L','XL','X','XC')
        cont -= 1
    elif cont == 1:
        numero += roma(x,'V','IV','I','IX')
             
print(numero)