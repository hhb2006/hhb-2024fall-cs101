n=int(input())
money=list(map(int,input().split()))
day,maximum=1,1
for i in range(1,n):
    if money[i] >= money[i-1]:
        day+=1
    else:
        maximum=max(maximum,day)
        day=1
if day>maximum:
    print(day)
else:
    print(maximum)