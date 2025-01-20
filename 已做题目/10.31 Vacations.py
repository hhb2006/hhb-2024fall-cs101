n = int(input())
events = [int(x) for x in input().split()]  # 0:neither  1:contest  2:sports  3:both
dp, rested = [0 for _ in range(n)], 0
dp[0] = 1 if events[0] else 0
for i in range(1,n):
    if events[i] == 0:
        dp[i] = dp[i-1]
    elif events[i] == 3:
        if events[i-1] == 1 or 2:
            dp[i] = dp[i-1] + 1
            events[i] = 3 - events[i-1]
        else:
            dp[i] = dp[i-1] + 1
    else:
        if events[i-1] == events[i] and not rested:
            dp[i] = dp[i-1]
            rested = 1
        else:
            dp[i] = dp[i-1] + 1
            rested = 0
#print(' '.join([str(x) for x in events]))
#print(' '.join([str(x) for x in dp]))
print(n-dp[-1])