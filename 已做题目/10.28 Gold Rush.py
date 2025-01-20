class PileTree:
  def __init__(self, data):
    self.data = int(data)
    self.large = data*2//3 if data%3 == 0 else None
    self.small = data//3 if data%3 == 0 else None

t = int(input())
for _ in range(t):
    n,m = map(int, input().split()) # 原始数n，目标数m
    if n < m or (n%3 != 0 and n != m):
        print('NO')
    elif n == m:
        print('YES')
    else:
        piles,printed = [n],0
        while n != m and len(piles) > 0:
            new_piles = []
            for p in piles:
                if p == m:
                    print('YES')
                    printed = 1
                    break
                if p is not None:
                    new_piles.extend([PileTree(p).large,PileTree(p).small])
            piles = list(set(new_piles))
        if not printed:
            print('NO')