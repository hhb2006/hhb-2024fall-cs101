import heapq as hp
from  collections import  defaultdict

q = int(input())
lhp,rhp = [],[]
ldict, rdict = defaultdict(int),defaultdict(int)
for _ in range(q):
    opr = input()
    l, r = map(int, opr[1:].split())
    if opr[0] == '+':
        ldict[-l] += 1
        rdict[r] += 1
        hp.heappush(lhp, -l)
        hp.heappush(rhp, r)
    else:
        ldict[-l] -= 1
        rdict[r] -= 1
        while len(lhp) > 0:
            if ldict[lhp[0]] <= 0:
                hp.heappop(lhp)
            else:
                break
        while len(rhp) > 0:
            if rdict[rhp[0]] <= 0:
                hp.heappop(rhp)
            else:
                break
    #print(lhp,rhp,ldict[lhp[0]],rdict[rhp[0]])
    if lhp and rhp:
        print('YES' if lhp[0] + rhp[0] < 0 else 'NO')
    else:
        print('NO')