# while True:
#     try:
#         cont = 0
#         n, m = map(int, input().split())
#         for i in range(n,m+1):
#             t = False
#             for j in range(len(str(i))-1):
#                 for l in range(j+1,len(str(i))):
#                     if str(i)[j] == str(i)[l]:
#                         cont += 1
#                         t = True
#                         break
#                 if t == True:
#                     break       
#         print((m-n)-cont+1)
#     except EOFError:
#         break

# while True:
#     try:
#         cont = 0
#         n, m = map(int, input().split())
#         for i in range(n,m+1):
#             if len(str(i)) != len(set(str(i))):
#                 cont+=1
#         print((m-n)-cont+1)
                     
#     except EOFError:
#         break

while True:
    try:
        cont = 0
        n, m = map(int, input().split())
        for i in range(n,m+1):
            i = str(i)
            for j in i:
                if i.count(j)>1:
                    cont+=1
                    break
        print((m-n)-cont+1)
       
    except EOFError:
        break

