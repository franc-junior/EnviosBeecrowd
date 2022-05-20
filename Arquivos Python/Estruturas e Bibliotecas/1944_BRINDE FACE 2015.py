n = int(input())
blocos = ['F A C E']
cont = 0
for i in range(n):
    new = input()
    end = blocos[len(blocos)-1]
    if new != end[::-1]:
        blocos.append(new)
    else:
        cont += 1
        if len(blocos) > 1:
            del(blocos[len(blocos)-1])
        
print(cont)


# >>> A.insert(0, "y")
# >>> A
# ["y", "a", "b", "c"]
# insert( <índice>, <objeto> )