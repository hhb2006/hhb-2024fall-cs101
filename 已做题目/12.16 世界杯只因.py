n = int(input())
cov = list(map(int, input().split()))

for i in range(n):
    cov[i] = [max(0,i-cov[i]),i+cov[i]-max(0,i-cov[i])]
cov.sort(key = lambda ele:ele[0])

leap = [0 for _ in range(n)]
x, d = cov[0][0], cov[0][1]
leap[x] = d
for i in range(1,n):
    if cov[i][0] == x:
        leap[x] = max(leap[x],cov[i][1])
    else:
        x, d = cov[i][0], cov[i][1]
        leap[x] = max(leap[x],d)
#上面是预处理

#下面才是真正开始区间覆盖问题
cnt,cur_range,next_range = 1,leap[0],0
for i in range(1,n):
    next_range = max(leap[i] + i,next_range)
    if i > cur_range:
        cnt += 1
        cur_range = next_range
#print(*leap)
print(cnt)