while True:
    try:
        n = int(input())
        largada = input().split()
        chegada = input().split()
        contador = 0
        
        ultrapass = 0
        for i in range(n):
            if largada[i] != chegada[i]:
                for j in range(i, n):
                    if largada[i] == chegada[j]:
                        contador+=(j-i)
                        break
        print(contador)

    except EOFError:
        break
