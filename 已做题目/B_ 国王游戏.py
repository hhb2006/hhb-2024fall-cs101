def multiply(index):
    m = kl
    for x in range(index):
        m *= q[x][0]
    return m

n = int(input())
kl,kr = map(int,input().split())
q,res = [],0
for _ in range(n):
    l,r = map(int,input().split())
    q.append([l,r])
q.sort(key = lambda x:x[1])
q.sort(key = lambda x:x[0])

for i in range(1,n):
    curl,curr = q[i]
    for j in range(i-1,-1,-1):
        jl,jr = q[j]
        if max(multiply(j+1)//curr,multiply(j)//jr) > max(multiply(j)//curr,((multiply(j+1)//jl)*curl)//jr):
            q[j+1],q[j] = q[j],q[j+1]
        else:
            break
    print(q)
for i in range(n):
    res = max(res, multiply(i)//q[i][1])
print(res)