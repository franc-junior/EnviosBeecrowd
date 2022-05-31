while True:
    try:
        n = int(input())%12
        if n == 0 or n == 6:
            print("Y")
        else:
            print("N")
    except EOFError:
        break