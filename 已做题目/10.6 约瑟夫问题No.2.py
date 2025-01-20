while True:
    n,p,m = map(int,input().split())
    if n == 0 and p == 0 and m == 0:
        break
    kids = list(range(1,n+1))
    out = ''
    p -= 1
    while len(kids) >= 1:
        p = (p+m-1)%len(kids)
        out += str(kids[p]) + ','
        kids.pop(p)
    print(out[:-1])