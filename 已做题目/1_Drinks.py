bottle=int(input())
portion=input()
p=list(portion.split())
n=0
for i in range(bottle):
    n+=int(p[i])
k=n/bottle
print(k)