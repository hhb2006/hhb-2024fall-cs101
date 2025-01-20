n = int(input())
height, targets = list(map(int, input().split())), []
targets.append((n-1,height[-1],1))
for i in range(n-2,-1,-1):
    h,potential = height[i],1
    for j in range(n-i-1):
        if h >= targets[j][1]:
            potential += targets[j][2]
            break
    targets.append((i,h,potential))
    targets.sort(key=lambda x:x[2],reverse=True)
print(targets[0][2])
# 倒着遍历，优先队列 dp (随时排序)