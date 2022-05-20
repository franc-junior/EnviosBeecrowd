fibo = [0,1]
for i in range(59):
    cont = fibo[len(fibo)-1] + fibo[len(fibo)-2]
    fibo.append(cont) 
n = int(input())
for i in range(n):
    x = int(input())
    print("Fib({}) = {}".format(x,fibo[x]))

