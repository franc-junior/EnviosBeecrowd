n = int(input())
dic = {'1001': 1.50, '1002': 2.50, '1003': 3.50, '1004': 4.50, '1005': 5.50}
soma = 0
for i in range(n):
    prod, q = input().split()
    q = int(q)
    soma += (dic[prod]*q)
print("{:.2f}".format(soma))