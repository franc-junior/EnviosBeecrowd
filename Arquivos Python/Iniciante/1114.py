n = 2002
while True:
    senha = int(input())
    if senha != n:
        print("Senha Invalida")
    if senha == n:
        print("Acesso Permitido")
        break
