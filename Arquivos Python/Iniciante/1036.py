a, b, c = map(float, input().split())

if a == 0 or (b ** 2 - 4 * a * c) < 0:
    print("Impossivel calcular")
else:
    delta = b ** 2 - 4 * a * c
    xi = (- b + (delta ** 0.5)) / (2 * a)
    xii = (- b - (delta ** 0.5)) / (2 * a) 
    print("R1 = {:.5f}\nR2 = {:.5f}".format(xi, xii))
