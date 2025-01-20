def dfs(x,y):
    cnt = 1
    field[x][y] = '.'
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0<=x+i<len(field) and 0<=y+j<len(field[0]) and field[x+i][y+j] == 'W':
                cnt += dfs(x+i,y+j)
    return cnt

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    field = [list(input()) for _ in range(n)]
    area = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 'W':
                area = max(area, dfs(i, j))
    print(area)