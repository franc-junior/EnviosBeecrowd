string = input()
vogais = ""
for i in string:
    if i in "aeiou":
        vogais+=i
if vogais == vogais[::-1]:
    print("S")
else:
    print("N")