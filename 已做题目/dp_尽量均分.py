nums = list(map(int, input().split())) # 输入数组
nums.sort() # 降序排序
num_sum = sum(nums)
target = num_sum//2
dp = [0 for _ in range(target+1)] # dp数组
for i in range(len(nums)):
    for j in range(int(target), nums[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
print(dp)
print(num_sum-2*dp[-1]) # 输出结果