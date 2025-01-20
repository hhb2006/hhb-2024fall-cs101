n = int(input())
potions = list(map(int, input().split()))
res,max_life,neg_list,remain = 0,0,[],[0 for _ in range(n)]
for i in range(n):
    if potions[i] >= 0:
        max_life += potions[i]
        res += 1
    else:
        neg_list.append((i,potions[i]))
    remain[i] = max_life
neg_list.sort(key=lambda ele: abs(ele[1]))

if res == 0 or res == n:
    print(res)
else:
    m = len(neg_list)
    for x in range(m):
        if min(remain[neg_list[x][0]:])+neg_list[x][1] >= 0:
            res += 1
            for y in range(neg_list[x][0],n):
                remain[y] += neg_list[x][1]
    print(res)
