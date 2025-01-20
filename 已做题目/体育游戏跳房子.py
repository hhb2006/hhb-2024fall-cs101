from collections import deque

def leap(s,e):
    q = deque([[s,'']])
    visited = set([s])
    while q:
        x,path = q.popleft()
        #print(x,path)
        if x == e:
            return len(path),path
        for nx in (x*3,x//2):
            if nx > 0 and nx not in visited:
                visited.add(nx)
                if nx == x//2:
                    q.append([nx,path+'O'])
                else:
                    q.append([nx,path+'H'])


while True:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    res = leap(a,b)
    print(res[0])
    print(res[1])