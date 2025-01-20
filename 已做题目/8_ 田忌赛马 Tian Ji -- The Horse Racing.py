while True:
    n = int(input())
    if n == 0:
        exit()
    tj = sorted(list(map(int, input().split())))
    king = sorted(list(map(int, input().split())))

    win, il, ir, jl, jr = 0, 0, n-1, 0, n-1
    while il <= ir:
        if tj[il] > king[jl]:
            win += 1
            il += 1
            jl += 1
        elif tj[ir] > king[jr]:
            win += 1
            ir -= 1
            jr -= 1
        else:
            win -= (tj[il] < king[jr])
            il += 1
            jr -= 1
    print(win*200)