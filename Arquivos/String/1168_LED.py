n = int(input())
soma = 0
for i in range(n):
    v = input()
    dic = {'1': 2, '2': 5,'3': 5,'4': 4,'5': 5,'6': 6,'7': 3,'8': 7,'9': 6,'0': 6}
    for j in v:
        soma += dic[j]
    print(soma, "leds")
    soma = 0

