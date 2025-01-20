n = int(input())
h = list(map(int,input().split()))
up = [1 for _ in range(n)]
down = [1 for _ in range(n)]
for i in range(1,n):
    for j in range(i):
        if h[i] > h[j]:
            up[i] = max(up[i],up[j]+1)
        if h[-i-1] > h[-j-1]:
            down[-i-1] = max(down[-i-1],down[-j-1]+1)
res = 0
for i in range(n):
    res = max(res,up[i]+down[i])
print(res-1)