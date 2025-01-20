prices = list(map(int,input().split(',')))
n,res = len(prices),float('-inf')
dp = [[0, 0] for _ in range(n + 1)]
for j in range(1,len(prices)+1):
    if j == 1:
        dp[j][0] = prices[0]
        dp[j][1] = float('-inf')
    else:
        dp[j][0] = max(dp[j-1][0] + prices[j-1],prices[j-1])
        dp[j][1] = max(dp[j-1][1] + prices[j-1],dp[j-1][0])
    res = max(res,dp[j][0],dp[j][1])
#print(dp)
print(res)