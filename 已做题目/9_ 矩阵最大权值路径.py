def bfs(x,y):
    visited[x][y] = 1
    step,path = float('-inf'),[]
    if x == n-1 and y == m-1:
        return matrix[x][y],[[x+1, y+1]]

    for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=i<n and 0<=j<m and not visited[i][j] :
            visited[i][j] = 1
            b = bfs(i,j)
            if b[0] > step:
                step = b[0]
                path = b[1]
            visited[i][j] = 0
    return step+matrix[x][y],path+[[x+1,y+1]]


n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
res = bfs(0,0)
for pair in reversed(res[1]):
    print(pair[0],pair[1])