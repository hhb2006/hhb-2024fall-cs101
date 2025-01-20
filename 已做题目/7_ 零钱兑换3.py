n,m = map(int, input().split())
coins = sorted(list(map(int, input().split())))
dp = [float('inf') for _ in range(m+1)]
dp[0] = 0
i = -1
for j in range(coins[0],m+1):
    if j == coins[min(i+1,n-1)]:
        dp[j] = 1
        i += 1
    else:
        dp[j] = min(dp[j-coins[k]]+1 for k in range(i+1) if j-coins[k] >= 0)
num = dp[-1]
print(num if num != float('inf') else -1)