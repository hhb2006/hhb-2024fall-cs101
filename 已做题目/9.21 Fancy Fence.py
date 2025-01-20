n = int(input())
angle = []
for i in range(n):
    angle.append(int(input()))
for a in angle:
    if 360 % (180-a) == 0:
        print('YES')
    else:
        print('NO')