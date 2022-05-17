caw = 0
soma = 0
while caw < 3:
    entrada = input().replace('*','1').replace('-','0')
    if entrada == 'caw caw':
        print(soma)
        caw += 1
        soma = 0
    else:
        decim = int(entrada, 2)
        soma += decim
    

    