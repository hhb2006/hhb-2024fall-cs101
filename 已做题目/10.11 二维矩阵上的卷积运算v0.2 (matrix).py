m,n,p,q = map(int,input().split())
a,b,c = [],[],[]
for i in range(m):
    a.append(list(map(int,input().split())))
for i in range(p):
    b.append(list(map(int,input().split())))
for i in range(m-p+1):
    c.append([])
    for j in range(n-q+1):
        c[i].append(0)
        for k in range(p):
            for l in range(q):
                c[i][j] += a[i+k][j+l]*b[k][l]
for _ in range(m-p+1):
    print(*c[_])