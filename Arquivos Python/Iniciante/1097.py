j = 5
j2 = j+1
j3 = j+2
for i in range(1,10):
    if i % 2 != 0:
        print("I={} J={}\nI={} J={}\nI={} J={}".format(i,j3,i,j2,i,j))
        j = j3
        j2 = j+1
        j3 = j+2