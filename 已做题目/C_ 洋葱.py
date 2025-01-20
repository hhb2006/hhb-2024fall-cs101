def find_max_layer(N, matrix):
    x0,y0,l,res = 0,0,N,0
    for t in range(0, (N + 1) // 2):  #t表示层数
        sum_layer = 0
        for i in range(x0, x0+l):
            if i == x0 or i == x0+l-1:
                sum_layer += sum(matrix[i][y0:y0+l])
            else:
                sum_layer += matrix[i][y0] + matrix[i][y0+l-1]
        res = max(res,sum_layer)
        x0 += 1
        y0 += 1
        l -= 2
    return res

n = int(input())
onion = [list(map(int, input().split())) for _ in range(n)]
print(find_max_layer(n, onion))