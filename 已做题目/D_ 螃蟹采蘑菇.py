from collections import deque

def bfs(field):
    origin,visited = [],[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if field[i][j] == 5:
                origin.append(i)
                origin.append(j)
    x1,y1,x2,y2 = origin
    q = deque([(x1,y1,x2,y2)])

    while q:
        crab = q.pop() #(x1,y1,x2,y2)
        #print(crab)
        visited[crab[0]][crab[1]],visited[crab[2]][crab[3]] = 1,1
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx1,ny1,nx2,ny2 = crab[0]+dx,crab[1]+dy,crab[2]+dx,crab[3]+dy
            #print(nx1,ny1,nx2,ny2)
            if 0<=nx1<n and 0<=ny1<n and 0<=nx2<n and 0<=ny2<n and (not visited[nx1][ny1] or not visited[nx2][ny2]):
                if field[nx1][ny1] != 1 and field[nx2][ny2] != 1:
                    if field[nx1][ny1] == 9 or field[nx2][ny2] == 9:
                        return 'yes'
                    else:
                        q.append((nx1,ny1,nx2,ny2))
    return 'no'

n = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]
print(bfs(maze))
