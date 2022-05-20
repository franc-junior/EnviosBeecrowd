n = int(input())
hr = n // 3600 
mi = (n % 3600) // 60
se = n % 60
print("{}:{}:{}" .format(hr, mi, se))
