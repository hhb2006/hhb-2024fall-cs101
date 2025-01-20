def dfs(x, y):
    visited[x][y] = 1
    step = float('inf')
    if field[x][y] == 1:
        return 0
    for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=i<m and 0<=j<n and (visited[i][j] == field[i][j] == 0 or field[i][j] == 1):
            visited[i][j] = 1
            step = min(step, 1 + dfs(i, j))
            visited[i][j] = 0
    return step

m,n = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
res = dfs(0, 0)
print(res if res != float('inf') else 'NO')