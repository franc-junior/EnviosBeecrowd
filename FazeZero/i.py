k = int(input())
l, r = map(int, input().split())
string = ""
cont=0
while len(string)<=((r+1)-l):
    string += str(l+cont)
    cont += 1
    print(string)
