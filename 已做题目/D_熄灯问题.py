import copy

def switch(x,y,matrix):
    matrix[x][y] = 1-matrix[x][y]
    return

def arrange(row):
    new_lights = copy.deepcopy(lights)
    opr = [[0 for _ in range(6)] for _ in range(5)]
    opr[0] = row
    for r in range(5):
        for c in range(6):
            if r :
                opr[r][c] = new_lights[r-1][c]
            if opr[r][c]:
                for x,y in [(r+1,c),(r-1,c),(r,c+1),(r,c-1),(r,c)]:
                    if x in range(5) and y in range(6):
                        switch(x,y,new_lights)
    for r in range(5):
        for c in range(6):
            if new_lights[r][c] :
                return
    for i in range(5):
        print(*opr[i])
    return

def press(col):
    if col == 6:
        #print(row1)
        arrange(row1)
        return
    for i in range(2):
        row1.append(i)
        press(col+1)
        row1.pop()

lights = [list(map(int,input().split())) for _ in range(5)]
row1 = []
press(0)