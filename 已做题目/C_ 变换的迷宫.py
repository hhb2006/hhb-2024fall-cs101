from collections import deque

def bfs(x1,y1,x2,y2):
    q = deque([(x1,y1,0)])
    while q:
        x,y,t = q.popleft()
        if x == x2 and y == y2:
            return t
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=nx<row and 0<=ny<col:
                if (maze[nx][ny] != '#' or (t+1)%k == 0) and not visited[nx][ny][(t+1)%k] :
                    visited[nx][ny][(t+1)%k] = 1
                    q.append((nx,ny,t+1))
    return -1

T = int(input())
for _ in range(T):
    row,col,k = map(int,input().split())
    maze,visited = [],[[[0 for _ in range(k)] for i in range(col)] for j in range(row)]
    sx,sy,ex,ey = 0, 0, 0, 0
    for i in range(row):
        lis = list(input())
        for j in range(col):
            if lis[j] == 'S':
                sx,sy = i,j
            elif lis[j] == 'E':
                ex,ey = i,j
        maze.append(lis)
    res = bfs(sx,sy,ex,ey)
    print(res if res != -1 else "Oop!")