n,m = map(int,input().split())
tvs = list(map(int,input().split()))
want,reap = [],0
for tv in tvs:
    if tv < 0:
        want.append(tv)
want.sort()
buy = min(m,len(want))
for i in range(buy):
    reap += want[i]
print(abs(reap))