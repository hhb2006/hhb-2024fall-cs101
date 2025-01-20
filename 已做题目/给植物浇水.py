n,A,B = map(int,input().split())
plants = list(map(int,input().split()))
l, r, cnt = 0, n-1, 0
a,b = A,B
while l < r:
    if a >= plants[l]:
        a -= plants[l]
    else:
        a = A - plants[l]
        cnt += 1
    if b >= plants[r]:
        b -= plants[r]
    else:
        b = B - plants[r]
        cnt += 1
    l += 1
    r -= 1
if l == r:
    if max(a,b) < plants[l]:
        cnt += 1
print(cnt)