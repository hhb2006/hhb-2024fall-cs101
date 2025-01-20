l, a, b, c = map(int, input().split())
num = sorted([a,b,c])
dp = [[0 for _ in range(l+1)] for _ in range(3)]

for i in range(num[0],l+1):
    if i%num[0] == 0:
        dp[0][i] = i//num[0]
for i in range(1,3):
    for j in range(num[0],l+1):
            for p in range(1,i+1):
                k,cut = 0,0
                while j-k*num[i] > 0:
                    if dp[i-p][j-k*num[i]] != 0:
                        dp[i][j] = max(dp[i-p][j-k*num[i]]+k, dp[i][j])
                        cut = 1
                        break
                    k += 1
                if j-k*num[i] == 0 and not cut:
                    dp[i][j] = max(j//num[i], dp[i][j])
print(dp[-1][-1])
