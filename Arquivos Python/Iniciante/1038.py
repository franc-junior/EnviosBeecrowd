a, b = map(int, input().split())
if a == 1:
    c = b * 4.00
if a == 2:
    c = b * 4.50
if a == 3:
    c = b * 5.00
if a == 4:
    c = b * 2.00  
if a == 5:
    c = b * 1.50  
print("Total: R$ {:.2f}".format(c))

