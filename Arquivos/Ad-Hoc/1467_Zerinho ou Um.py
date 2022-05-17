def pozi(num, lis):
    if lis.index(num) == 0:
        print("A")
    elif lis.index(num) == 1:
        print("B")
    else:
        print("C")
while True:
    try:
        pess = input().split()
        if pess[0] == pess[1] == pess[2]:
            print("*")
        else:
            if pess.count('0') == 1:
                pozi('0', pess)
            else:
                pozi('1', pess)
    except EOFError:
        break