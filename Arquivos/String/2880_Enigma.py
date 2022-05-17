palavra = list(input())
crib = input()
cont = 0
for i in range(len(palavra)-len(crib)+1):
    char = 0
    while crib[char] != palavra[char]:
        if char == len(crib)-1:
            cont += 1
            break
        char+=1
    del palavra[0]
print(cont)

   


