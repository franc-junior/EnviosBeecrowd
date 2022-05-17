k = int(input())
lista = [1, 3, 5, 10, 25, 50, 100]
i = 0
while True:
    if k<=lista[i]:
        print("Top",lista[i])
        break
    i+=1