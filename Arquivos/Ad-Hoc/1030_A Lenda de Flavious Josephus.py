

# nc = int(input())
# for c in range(nc):
#     n, k = map(int,input().split())
#     lista_n = []
#     for i in range(n):
#         lista_n.append(i+1)
#     while len(lista_n)>1:
#         for i in range(k-1):
#             lista_n.append(lista_n.pop(0))
#         del lista_n[0]
#     print("Case {}: {}".format(c+1 ,lista_n[0]))

# nc = int(input())
# for c in range(nc):
#     n, k = map(int,input().split())
#     lista_n = list(range(1,n+1))
    
#     while len(lista_n)>1:
#         if len(lista_n)<=k:
#             for i in range(k-1):
#                 lista_n.append(lista_n.pop(0))
#             del lista_n[0]
#         else:
#             lista_n.extend(lista_n[:k-1])
#             del lista_n[:k]
        
#     print("Case {}: {}".format(c+1 ,lista_n[0]))

for i in range(int(input())):
    n, k = map(int, input().split())
    vivos = list(range(1,n+1))
    c = 0
    for i in range(1,n):
        remov = (k-1)+c
        if remov>len(vivos)-1:
            remov -= len(vivos)
            c -= len(vivos)
        del vivos[remov]
        c+=k-1
    print(vivos)

