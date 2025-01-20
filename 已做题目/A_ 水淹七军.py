from collections import deque
import sys

def bfs(x1, y1, x2, y2):
    hm = field[x1][y1]
    visited = [[0] * n for _ in range(m)]
    q = deque([[x1,y1]])
    visited[x1][y1] = 1
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        else:
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if 0<=i<m and 0<=j<n and not visited[i][j] and field[i][j] < hm:
                    visited[i][j] = 1
                    q.append([i,j])
    return 0

data = sys.stdin.read().split()
k = int(data[0])
d = 1
ans = []

for _ in range(k):
    m, n = int(data[d]),int(data[d + 1])
    d += 2
    field = [list(map(int, data[d + i * n:d + (i + 1) * n])) for i in range(m)]
    d += m * n
    a,b = int(data[d]) - 1, int(data[d + 1]) - 1
    d += 2
    p = int(data[d])
    d += 1
    pos = [(int(data[d + i * 2]) - 1, int(data[d + i * 2 + 1]) - 1) for i in range(p)]
    d += p * 2
    result = any(bfs(x,y,a,b)for x,y in pos)
    ans.append("Yes" if result else "No")

sys.stdout.write("\n".join(ans)+"\n")
