n,capacity = map(int,input().split())
prices = list(map(int,input().split()))
weights = list(map(int,input().split()))
items,dp = [],[[0]*(capacity+1) for _ in range(n)]

for x in range(n):
    items.append([prices[x],weights[x]])
items.sort(key = lambda e:e[1])

for _ in range(items[0][1],capacity+1):
    dp[0][_]=items[0][0]
for i in range(1,n):
    for j in range(items[0][1],capacity+1):
        if items[i][1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][1]]+items[i][0])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
