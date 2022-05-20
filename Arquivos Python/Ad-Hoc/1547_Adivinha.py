# for i in range(int(input())):
#     qt, s = map(int, input().split())

#     lista = list(map(int,input().split()))
#     i=0
#     j=0
#     while True:
#         if lista[j] == s+i:
#             print(j+1)
#             break
#         else:
#             j+=1
#             if j == qt:
#                 i+=1
#                 j=0

# n = int(input())
# for i in range(n):
#     qt, s = map(int, input().split())
#     lista = list(map(int, input().split()))
#     if s in lista:
#         print(lista.index(s)+1)
#     else:
#         i = 0
#         while True:
#             i+=1
#             if s+i in lista:
#                 print(lista.index(s+i)+1)
#                 break
#             elif s-i in lista:
#                 print(lista.index(s-i)+1)
#                 break
            
# n = int(input())
# for i in range(n):
#     qt, s = map(int, input().split())
#     lista = list(map(int, input().split()))
#     if s in lista:
#         print(lista.index(s)+1)
#     else:
#         i = 0
#         while True:
#             i+=1
#             if s+i in lista:
#                 print(lista.index(s+i)+1)
#                 break
#             elif s-i in lista:
#                 print(lista.index(s-i)+1)
#                 break

n = int(input())
for i in range(n):
    qt, s = map(int, input().split())
    lista = list(map(int, input().split()))
    cont = 101
    id = 0
    for j in lista:
        if abs(s-j) < cont:
            id = lista.index(j)
            cont = abs(s-j)
    print(id+1)
        