for i in range(int(input())):
    nome = input()
    notas = list(map(float, input().split()))
    media = 0
    tam_notas = len(notas)
    if tam_notas == 4:
        del notas[notas.index(min(notas))]
        media = sum(notas)/3
    elif tam_notas == 3:
        media = sum(notas)/3
    else:
        media = sum(notas)/2
    print("{}: {:.1f}".format(nome, media))
    