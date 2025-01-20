n,m=map(int,input().split())
button=[]
count=0
for i in range(n):
    a=list(map(int,input().split()))
    button.extend(a[1:])
for j in range(1,m+1):
    if j in button:
        count+=1
if count==m:
    print("YES")
else:
    print("NO")
