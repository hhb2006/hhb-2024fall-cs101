def ski(x,y):
    h,go = field[x][y],0
    visited[x][y] = 1
    for nx,ny in [(x,y+1),(x,y-1),(x+1,y),(x-1,y)]:
        if 0<=nx<r and 0<=ny<c:
            nh = field[nx][ny]
            if nh < h:
                go = 1
                if visited[nx][ny]:
                    dp[x][y] = max(dp[x][y],dp[nx][ny]+1)
                else:
                    if nh < h:
                        dp[x][y] = max(dp[x][y],ski(nx,ny)+1)
    if go:
        return dp[x][y]
    else:
        return 1

r,c = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(r)]
dp = [[1 for _ in range(c)] for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
res = float('-inf')
for i in range(r):
    for j in range(c):
        res = max(res,ski(i,j))
print(res)