a, b, c = map(float, input().split())
if (a < b + c) & (b < a + c) & (c < a + b):
    x = a + b + c
    print("Perimetro = {:.1f}".format(x))
else:
    x = ((a + b) * c) / 2
    print("Area = {:.1f}".format(x))
    
