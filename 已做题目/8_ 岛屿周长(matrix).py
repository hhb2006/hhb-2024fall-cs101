def circ(x,y,n,m,matrix):
    c = 0
    if matrix[x][y]:
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            if x-i in range(n) and y-j in range(m):
                if matrix[x-i][y-j] :
                    c += 1
        c = 4-c
    return c

n,m = map(int,input().split())
matrix,res = [],0
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
for i in range(n):
    for j in range(m):
        res += circ(i,j,n,m,matrix)
print(res)