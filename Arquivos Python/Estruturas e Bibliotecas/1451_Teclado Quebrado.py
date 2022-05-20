texto = input()
texto_limpo = ""
id1 = 0
id2 = 0
for i in range(len(texto)):
    if (texto[i] == '[') and (id1 == -1):
        id1 = i
    elif (texto[i] == ']') and (id2 == -1):
        id2 = i
