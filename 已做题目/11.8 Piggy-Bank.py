t = int(input())
for _ in range(t):
    e,f= map(int,input().split())
    volume = f-e
    n = int(input())
    coins = [list(map(int,input().split())) for _ in range(n)] # [value, weight]
    dp = [float('inf') for _ in range((volume+1))]
    dp[0] = 0
    for i in range(n):
        for j in range(coins[i][1],volume+1):
            dp[j] = min(dp[j], dp[j-coins[i][1]]+coins[i][0])
    if dp[-1] == float('inf'):
        print('This is impossible.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {dp[-1]}.')