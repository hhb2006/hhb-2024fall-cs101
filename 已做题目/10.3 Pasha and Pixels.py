#使用集合避免重复运算
n, m, k = map(int, input().split())
a = set()
for i in range(k):
    x, y = map(int, input().split())
    if ((x - 1, y) in a and (x, y - 1) in a and (x - 1, y - 1) in a) or \
       ((x + 1, y) in a and (x, y - 1) in a and (x + 1, y - 1) in a) or \
       ((x - 1, y) in a and (x, y + 1) in a and (x - 1, y + 1) in a) or \
       ((x + 1, y) in a and (x, y + 1) in a and (x + 1, y + 1) in a):
        print(i + 1)
        exit()
    a.add((x, y))
print(0)