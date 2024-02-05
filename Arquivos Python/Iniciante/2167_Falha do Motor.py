n = int(input())
cont = 0

nuns = input().split()
menor = 0
ultimo = int(nuns[0])

while cont<n:
    if int(nuns[cont])<ultimo:
        menor = cont+1
        break
    ultimo = int(nuns[cont])
    cont+=1
print(menor)
    