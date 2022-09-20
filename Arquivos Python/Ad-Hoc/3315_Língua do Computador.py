m = 0
for i in range(4):
    semana = list(map(int, input().split()))
    soma = sum(semana)
    if soma>m:
        m = soma

decimall = m
binary = ""
while decimall > 0:
    
    if decimall%2 == 0:
        binary+="0"
    else:
        binary+="1"
    decimall = decimall//2
print(m,"=",binary[::-1])
    