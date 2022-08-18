while True:
    try:
        r = "CPF invalido"
        cpf = list(input())
        cpf_int = [int(cpf[0]),int(cpf[1]),int(cpf[2]),int(cpf[4]),int(cpf[5]),int(cpf[6]),int(cpf[8]),int(cpf[9]),int(cpf[10]),int(cpf[12]),int(cpf[13])] 
        soma1 = 0
        soma2 = 0
        i2 = 9
        for i in range(9):
            soma1 += (cpf_int[i]  * (i+1))
            soma2 += (cpf_int[i] * (i2))
            i2 -= 1
            
        a = soma1%11
        b = soma2%11

        if a == 10:
            a = 0
        if b == 10:
            b = 0

        if a == cpf_int[9] and b == cpf_int[10]:
            r = "CPF valido"
        print(r)    
            
    except EOFError:
        break 