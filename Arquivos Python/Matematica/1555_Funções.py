for i in range(int(input())):
    x, y = map(int,input().split())
    raf =  (3*x)**2 + (y**2) # (3x)² + y²
    bet = 2*(x**2) + (5*y)**2 # 2(x²) + (5y)²
    car = (-100*x) + y**3 #  -100x + y³

    if max(raf, bet, car) == raf:   
        g = "Rafael"
    elif max(raf, bet, car) == bet:
        g = "Beto"
    elif max(raf, bet, car) == car:
        g = "Carlos"

    print(g, "ganhou")