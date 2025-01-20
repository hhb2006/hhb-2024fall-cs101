n = int(input())
nums = list(map(int,input().split()))
nums.sort()
nums.append(float('inf'))
count,static,points = 1,{},0
for i in range(n):
    if nums[i] == nums[i+1]:
        count += 1
    else:
        static[nums[i]] = count
        count = 1
key_list = list(static.keys())
m = len(static)
#print(key_list,static)
dp = [0 for _ in range(m+1)]
dp[1] = key_list[0]*static[key_list[0]]
for i in range(2,m+1):
    if key_list[i-1] > key_list[i-2]+1:
        dp[i] = key_list[i-1]*static[key_list[i-1]] + dp[i-1]
    else:
        dp[i] = max(dp[i-1], dp[i-2]+key_list[i-1]*static[key_list[i-1]])
print(dp[-1])