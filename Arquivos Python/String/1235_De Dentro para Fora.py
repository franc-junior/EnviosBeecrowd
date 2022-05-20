n = int(input())
for i in range(n):
    string = input()
    tamanho = (len(string)//2)
    str1 = string[:tamanho]
    str2 = string[tamanho:]
    print("{}{}".format(str1[::-1], str2[::-1]))