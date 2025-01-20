def descend(lis):
    lth = len(lis)
    for a in range(lth-1,-1,-1):
        for b in range(a):
                if int(lis[b]+lis[b+1]) < int(lis[b+1]+lis[b]):
                    lis[b],lis[b+1] = lis[b+1],lis[b]
    return

m = int(input())
n = int(input())
nums = list(map(str,input().split()))
nums.sort(reverse=True)
descend(nums)
dp = [0 for _ in range(m+1)]
for i in range(n):
    num = nums[i]
    for j in range(m,-1,-1):
        if j >= len(num):
            if dp[j-len(num)]:
                dp[j] = max(dp[j], int(str(dp[j-len(num)])+num), int(num+str(dp[j-len(num)])))
            else:
                dp[j] = max(dp[j], int(num),dp[len(num)])
for x in dp[::-1]:
    if x:
        print(x)
        break
else:
    print(dp[-1])