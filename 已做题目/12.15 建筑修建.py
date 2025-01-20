n,m = map(int,input().split())
bld = [list(map(int,input().split())) for _ in range(n)]  # [xi,yi]
# for each xi, yi, [head,tail) : head [max(0,xi-yi+1),xi], tail [xi+1,min(n,xi+yi)]
t = 0
cnt = 0

while bld:
    bld.sort(key = lambda x: (max(t, x[0] - x[1] + 1) + x[1]))
    t = max(t, bld[0][0] - bld[0][1] + 1) + bld[0][1]
    #print(t)
    if t <= m:
        cnt += 1
    else:
        break
    new_bld = []
    for i in range(1, len(bld)):
        if bld[i][0] >= t:
            new_bld.append(bld[i])
    bld = new_bld

print(cnt)
'''
for i in range(1,n):
    if bld[i][0]-bld[i][1]+1 >= t:
        t = bld[i][0]+1
'''