menor = 101
meno = 0
oscaba = ["Otavio", "Bruno", "Ian", "Empate"]
migs = list(map(float, input().split()))
for i in range(3):
    if migs[i] < menor:
        menor = migs[i]
        meno = i
    elif migs[i] == menor:
        menor = migs[i]
        meno = 3
print(oscaba[meno])