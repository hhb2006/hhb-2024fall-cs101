n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(n-1):
    if a[i] > a[i+1]:
        count+=1
if count == 0:
    print("YES")
else:
    print("NO")