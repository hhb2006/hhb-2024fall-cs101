def liable(d):
    lp,rp,cnt = 0,1,0
    while True:
        if cnt >= c-1:
            return True
        if rp >= n:
            return False
        if pos[rp] - pos[lp] >= d:
            cnt += 1
            lp,rp = rp,rp+1
        else:
            rp += 1

n,c = map(int,input().split())
pos = [int(input()) for _ in range(n)]
pos.sort()
dist,left,right = pos[-1]//2,pos[0],pos[-1]
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