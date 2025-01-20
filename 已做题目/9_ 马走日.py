cover, ways = 0, 0
def dfs(x,y):
    global cover,ways
    cover += 1
    visited[x][y] = 1
    #print(x,y)
    if cover == m*n:
        cover -= 1
        ways += 1
        return
    for i,j in [(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2)]:
        if 0<=i<n and 0<=j<m and not visited[i][j]:
            dfs(i,j)
            visited[i][j] = 0
    else:
        cover -= 1
    return

t = int(input())
for _ in range(t):
    n, m, x0, y0 = map(int, input().split())
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cover,ways = 0,0
    dfs(x0,y0)
    print(ways)