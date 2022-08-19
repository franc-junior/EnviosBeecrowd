from string import ascii_lowercase, ascii_uppercase

while True:
    try:
        n_mai = False
        n_min = False
        n_num = False
        invali = False

        s = input()
        if len(s) <= 32 and len(s) >= 6:
            for i in s:
                if i in ascii_uppercase:
                    n_mai=True
                elif i in ascii_lowercase:
                    n_min=True
                elif i.isnumeric():
                    n_num=True
                else:
                    invali = True
                    break
        if invali == True:
            print("Senha invalida.")
        elif n_mai == n_min == n_num == True:
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break