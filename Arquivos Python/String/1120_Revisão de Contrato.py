while True:
    d, n = map(str, input().split())
    if d+n == "00":
        break
    n.replace(d,"")
    try:
        print(int(n.replace(d,"")))
    except ValueError:
        print(0)