import heapq

def dijkstra(sx, sy, ex, ey):
    if field[sx][sy] == '#' or field[ex][ey] == '#':
        return -1

    q = [(0, sx, sy)]
    centered = [[0 for _ in range(n)] for _ in range(m)]
    min_dist = [[float('inf') for _ in range(n)] for _ in range(m)]
    min_dist[sx][sy] = 0

    while q:
        d, x, y = heapq.heappop(q)
        if x == ex and y == ey:
            return d
        if centered[x][y]:
            continue
        centered[x][y] = 1
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < m and 0 <= ny < n:
                if not centered[nx][ny] and field[nx][ny] != '#':
                    nd = abs(int(field[nx][ny]) - int(field[x][y])) + d
                    min_dist[nx][ny] = min(min_dist[nx][ny], nd)
                    heapq.heappush(q, (min_dist[nx][ny], nx, ny))
    return -1


m, n, p = map(int, input().split())
field = [list(map(str, input().split())) for _ in range(m)]
for _ in range(p):
    x0, y0, x1, y1 = map(int, input().split())
    res = dijkstra(x0, y0, x1, y1)
    print(res if res != -1 else 'NO')