n,m = map(int,input().split())
p,q = [],[]
for _ in range(n):
    p.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        a = str(p[0][j])
        b = str(p[i][-1])
        c = str(p[-1][j])
        d = str(p[i][0])
        q.append(p[i][j]*int(a+b+c+d))
q.sort()
print(q[-1])