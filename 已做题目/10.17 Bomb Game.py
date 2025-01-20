a,b,k = map(int,input().split())
cover,miss,first = set(),set(),1
for _ in range(k):
    hit = set()
    r,s,p,t = map(int,input().split())
    d = p//2
    for i in range(r-d,r+d+1):
        for j in range(s-d,s+d+1):
            if 1 <= i <= a and 1 <= j <= b:
                hit.add((i,j))
    if t:
        if first:
            cover = hit
            first = 0
        else:
            cover &= hit
    else:
        miss |= hit
odds = cover-(cover & miss)
print(len(odds))
