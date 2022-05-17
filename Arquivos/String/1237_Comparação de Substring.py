# def compara(id1, str1, id2, str2):
#     cont = 0
#     i = 0
#     while str1[id1+i] == str2[id2+i]:
#         cont += 1
#         i+=1
#         if (i+id1 >= len(str1)) or (i+id2 >= len(str2)):
#             break
#     return cont
while True:
    try:
        string1 = input()
        string2 = input()
        cont = 0

        for id1 in range(len(string1)):
            for id2 in range(len(string2)):
                if string1[id1] == string2[id2]: 
                    
                    i1 = id1
                    i2 = id2
                    c = 0
                    while string1[i1] == string2[i2]:
                        c+=1
                        i1+=1
                        i2+=1
                    
                        if len(string1)==i1 or len(string2)==i2:
                            break
                        
                    if cont < c:
                        cont = c
        print(cont)
    except EOFError:
        break