from collections import deque

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(x1, y1, x2, y2):
    q = deque([[0, None, (x1, y1)]])  # [seg,orient,(x,y)]
    visited = [[0]*(w+2) for _ in range(h+2)]

    while q:
        seg, orient, (x, y) = q.popleft()

        if x == x2 and y == y2:
            return seg

        for d in [z for z in dirs if z != orient]:
            new_seg, nx, ny = seg + 1, x, y
            while d is not None:
                nx += d[0]
                ny += d[1]
                if not (0<=nx<w+2 and 0<=ny<h+2) :
                    break
                if (field[ny][nx] != 'X' and not visited[ny][nx]) or (nx == x2 and ny == y2):
                    visited[ny][nx] = 1
                    q.append([new_seg, d, (nx, ny)])
                else:
                    break
    return 0

t = 0
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    t += 1
    print(f'Board #{t}:')
    field = [[' ']+list(input())+[' '] for _ in range(h)]
    field = [[' ']*(w+2)]+field+[[' ']*(w+2)]
    n = 0
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == y1 == x2 == y2 == 0:
            break
        n += 1
        res = bfs(x1, y1, x2, y2)
        print(f'Pair {n}: {res} segments.' if res else f'Pair {n}: impossible.')
    print()