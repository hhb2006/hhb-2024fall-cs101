def neighbor(i, j, matrix):
    add = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i][j - 1] + matrix[i][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
    return add
def update(a, b, mat):
    matr = [x for x in mat]
    r = [0 for _ in range(b + 2)]
    matr = [r] + matr + [r]
    for x in range(1, a + 1):
        matr[x] = [0] + matr[x] + [0]
    for i in range(0, a):
        for j in range(0,b):
            if mat[i][j]==1:
                if neighbor(i+1,j+1, matr) == 2 or neighbor(i+1,j+1, matr) == 3:
                    mat[i][j]= '1'
                else:
                    mat[i][j]= '0'
            else:
                if neighbor(i+1,j+1, matr) == 3:
                    mat[i][j]= '1'
                else:
                    mat[i][j]= '0'
    return
n,m = map(int,input().split())
ma=[]
for _ in range(n):
    row = list(map(int,input().split()))
    ma.append(row)
update(n,m,ma)
for y in range(n):
    print(' '.join(map(str,ma[y])))