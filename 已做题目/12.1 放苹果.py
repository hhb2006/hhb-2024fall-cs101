t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    bag = m+n
    dp = [[0 for _ in range(n+1)] for _ in range(bag + 1)]
    for i in range(1, bag + 1): # i表示苹果个数
        for j in range(1, n+1): # j表示盘子个数
            if j > i:
                dp[i][j] = 0
            elif j == i or j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-j][j] + dp[i-1][j-1]
    print(dp[-1][-1])