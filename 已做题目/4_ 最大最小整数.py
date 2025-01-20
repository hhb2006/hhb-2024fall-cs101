def max_sort(li):
    for a in range(len(li)-1):
        change = 0
        for b in range(a+1,len(li)):
            if int(str(li[a])+str(li[b])) < int(str(li[b])+str(li[a])):
                change = 1
                li[a],li[b] = li[b],li[a]
        if change == 0:
            return
    return

n = int(input())
nums = list(map(int, input().split()))
max_sort(nums)
print(int(''.join(map(str,nums))),int(''.join(map(str,nums[::-1]))))

'''
l = len(str(nums[-1]))
for i in range(n):
    num = int(str(nums[i])+ str(nums[i])[0] *(l-len(str(nums[i]))))
    nums_plus.append([num, nums[i]])
nums_plus.sort(key = lambda x:x[0])
for j in range(n):
    MIN += str(nums_plus[j][1])
    MAX += str(nums_plus[-j-1][1])
print(int(MAX),int(MIN))
'''