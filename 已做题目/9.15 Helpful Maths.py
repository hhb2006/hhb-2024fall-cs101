s=list(map(int,input().split('+')))
s.sort()
for i in range(len(s)-1):
    print(s[i],end='+')
print(s[-1])