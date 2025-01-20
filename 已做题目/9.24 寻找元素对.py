n=int(input())
seq=list(map(int,input().split()))
k=int(input())
num=0
seq=list(set(seq))
seq.sort()
for i in range(n):
    for j in range(i+1,n):
        if seq[i]+seq[j]==k:
            num+=1
print(num)
#方法二：排序+双指针
'''
seq.sort()
left=0
    
right=n-1
while left<right:
    if seq[left]+seq[right]==k:
        print(seq[left],seq[right])
        break
    elif seq[left]+seq[right]>k:
        right-=1
    else:
        left+=1
'''
#方法三：哈希表
# hashset=set()
# for i in range(n):
#     if k-seq[i] in hashset:
#         print(k-seq[i],seq[i])
#     else:
#         hashset.add(seq[i])
#方法四：二分查找
# for i in range(n):
#     left=i+1
#     right=n-1
#     while left<right:
#         if seq[left]+seq[right]==k:
#             print(seq[left],seq[right])
#             break
#         elif seq[left]+seq[right]>k:
#             right-=1
#         else:
#             left+=1
#方法五：排序+二分查找
# seq.sort()
# for i in range(n):
#     left=i+1
#     right=n-1
#     while left<right:
#         if seq[left]+seq[right]==k:
#             print(seq[left],seq[right])
#             break
#         elif seq[left]+seq[right]>k:
#             right-=1
#         else:
#             left+=1
#方法六：排序+二分查找+哈希表