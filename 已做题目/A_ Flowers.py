t,k = map(int,input().split())
dp = [0]*100001
add = [0]*100001
mod = 10**9+7
dp[0] = 1
for i in range(1,100001):
        if i >= k :
            dp[i] = (dp[i-1] + dp[i-k]) % mod
        else:
            dp[i] = 1
        add[i] = (dp[i] + add[i-1]) % mod

for _ in range(t):
    a,b = map(int,input().split())
    print((add[b]-add[a-1])%mod)