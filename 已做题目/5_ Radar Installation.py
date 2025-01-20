from math import sqrt
def distance(x, y, d):
    dx = sqrt(d ** 2 - y ** 2)
    return [x - dx, x + dx]
t = 0
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        exit()
    islands, num, radar = [], 1, []
    t += 1

    for _ in range(n):
        x, y = map(int, input().split())
        if y > d:
            num = -1
            continue
        interval = distance(x, y, d)
        islands.append(interval)
    islands.sort(key = lambda a: a[0])

    if num != -1:
        radar = [islands[0]]
        for i in range(1, n):
            if radar[-1][-1] < islands[i][0]:
                num += 1
                radar.append(islands[i])
            else:
                radar[-1] = [islands[i][0], min(radar[-1][-1],islands[i][-1])]
    print(f"Case {t}: {num}")
    input()