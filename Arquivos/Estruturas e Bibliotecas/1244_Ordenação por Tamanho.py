for i in range(int(input())):
    v = sorted(input().split(), key=len, reverse=True)
    for j in range(len(v)):
        print(v[j], end="")
        if j != len(v)-1:
            print(" ", end="")
    print()