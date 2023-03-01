carlos = 0
r = "S"
for i in range(int(input())):
    nota = int(input())
    if i == 0:
        carlos = nota
    elif nota > carlos:
        r = "N"
print(r)
        