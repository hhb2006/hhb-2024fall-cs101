s = input()
num = [0]
n = 0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        n+=1
    num.append(n)
s0 = s.count('0')
m =int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(num[b-1]-num[a-1] )

