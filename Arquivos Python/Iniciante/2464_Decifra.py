#Francisco da Cunha Júnior
 
alfa = list("abcdefghijklmnopqrstuvwxyz") 
alfa_cod = list(input())            
frase = list(input())               
frase_deco = []
for i in frase:
    letra = alfa_cod.index(i)
    frase_deco.append(alfa[letra])
for j in frase_deco:
    print(j, end="")  
print()