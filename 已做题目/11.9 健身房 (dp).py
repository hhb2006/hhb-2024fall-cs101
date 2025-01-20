t,n = map(int,input().split())
time,progress = [],[]
for _ in range(n):
    ti,wi = map(int,input().split())
    time.append(ti)
    progress.append(wi)
dp = [0 for _ in range(t+1)]
for i in range(n):
    for j in range(t,time[i]-1,-1):
        if j == time[i] or dp[j-time[i]]:
            dp[j] = max(dp[j], dp[j-time[i]] + progress[i])
        else:
            dp[j] = max(dp[j],0)
print(dp[-1] if dp[-1] else -1)