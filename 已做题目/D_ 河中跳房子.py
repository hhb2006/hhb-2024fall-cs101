def liable(d):
    lp,rp,cnt = 0,1,0
    while True:
        if cnt >= n-m+1:
            return True
        if rp >= n+2:
            return False
        if pos[rp] - pos[lp] >= d:
            cnt += 1
            lp,rp = rp,rp+1
        else:
            rp += 1

l,n,m = map(int,input().split())
pos = [0]+[int(input()) for _ in range(n)]+[l]
dist,left,right = l//2,0,l
while True:
    can = liable(dist)
    #print(dist,can)
    if right - left <= 1:
        print(dist if can else left)
        break
    if can:
        left = dist
        dist = (dist+right)//2
    else:
        right = dist
        dist = (left+dist)//2