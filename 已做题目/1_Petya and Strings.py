a=input().upper()
b=input().upper()
for i in range(len(a)):
    if a[i]>b[i]:
        print(1)
        break
    if a[i]<b[i]:
        print(-1)
        break
    if i==len(a)-1:
        print(0)
