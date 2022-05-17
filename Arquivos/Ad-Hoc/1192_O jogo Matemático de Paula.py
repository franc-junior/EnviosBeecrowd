from string import ascii_uppercase, ascii_lowercase

n = int(input())
for i in range(n):
    entr = list(input())
    if entr[0] == entr[2]:
        s = int(entr[0])*int(entr[2])
    elif entr[1] in ascii_uppercase:
        s = (int(entr[2])-int(entr[0]))
    elif entr[1] in ascii_lowercase:
        s = int(entr[0])+int(entr[2])
    print(s)