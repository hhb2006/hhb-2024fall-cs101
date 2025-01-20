import copy
def capture(x,y,board):
    new_board = copy.deepcopy(board)
    new_board[x] = ['1' for _ in range(8)]
    for i in range(8):
        new_board[i][y] = '1'
        if i+y-x in range(8):
            new_board[i][i+y-x] = '1'
        if y+x-i in range(8):
            new_board[i][y+x-i] = '1'
    new_board[x][y] = '2'
    return new_board

def set_queen(r,s,board):
    a = []
    for c in range(8):
        if board[r][c] == '0':
            new_board = capture(r, c, board)
            new_s = str(s)+str(c+1)
            a.append([new_s,new_board])
    return a

def all_perm(m,board):
    if m == 1:
        a = []
        for x in range(8):
            a.append([str(x+1),capture(0,x,board)])
        return a
    else:
        all_perm(m-1,board)
        a = []
        for perm in all_perm(m-1,board):
            a.extend(set_queen(m-1,int(perm[0]),perm[1]))
        return a

chessboard = [['0' for _ in range(8)] for _ in range(8)]
n = int(input())
a = all_perm(8,chessboard)
for _ in range(n):
    b = int(input())
    print(a[b-1][0])