from  collections import defaultdict

n = int(input())
gifts = list(map(int,input().split()))
gifts = [g-520 for g in gifts]
pre = defaultdict(list)
ans,cur = 0,0
pre[0] = [-1]

for i in range(n):
    val = gifts[i]
    cur += val
    if pre[cur]:
        ans = max(ans,i-pre[cur][0])
    else:
        pre[cur].append(i)
print(ans*520)
