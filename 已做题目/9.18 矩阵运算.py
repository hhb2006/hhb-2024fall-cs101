row1,col1 = map(int,input().split())
matrix1 = []
for i in range(row1):
    matrix1.append(list(map(int,input().split())))

row2,col2 = map(int,input().split())
matrix2 = []
for i in range(row2):
    matrix2.append(list(map(int,input().split())))

row3,col3 = map(int,input().split())
matrix3 = []
for i in range(row3):
    matrix3.append(list(map(int,input().split())))

c = []
try:
    if col1 == row2 and row1 == row3 and col2 == col3:
        for i in range(row1):
            c.append([])
            for j in range(col2):
                c[i].append(0)
        for i in range(row1):
            for j in range(col2):
                for k in range(row2):
                    c[i][j] += matrix1[i][k]*matrix2[k][j]
                c[i][j] += matrix3[i][j]
        for u in range(row1):
            for v in range(col2):
                print(c[u][v],end=" ")
            print()
    else:
        print("Error!")
except Exception as e:
    print("Error!")



