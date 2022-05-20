for i in range(int(input())):
    n = int(input())
    carneiros = input().split()
    distintos = []
    for j in range(n):
        if carneiros[j] not in distintos:
            distintos.append(carneiros[j])
    print(len(distintos))
    
