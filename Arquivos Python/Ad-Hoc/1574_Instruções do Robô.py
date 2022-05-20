for i in range(int(input())):
    pos = 0
    history = []
    for j in range(int(input())):
        comando = input().split()
        coman = comando[0]
        if comando[0] == "SAME":
            coman = history[int(comando[2])-1]
        if coman == "LEFT":
            pos-=1
            history.append("LEFT")
        else:
            pos+=1
            history.append("RIGHT")
    print(pos)