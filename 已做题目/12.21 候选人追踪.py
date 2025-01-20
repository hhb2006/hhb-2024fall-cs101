from collections import defaultdict

n,k = map(int,input().split())
votes = list(map(int,input().split()))
s = list(map(int,input().split()))

ifs = defaultdict(int)
votes = [(votes[2*i],votes[2*i+1]) for i in range(n)]
votes.sort(key = lambda x:x[0])
states = defaultdict(list)
for vote in votes:
    states[vote[0]].append(vote[1])
for num in s:
    ifs[num] = 1
cnt = defaultdict(int)
sv = [(x,0) for x in s]
rv = [(x,0) for x in set([i for i in range(314160)])|set(s)]

for t,lis in states:
    for c in lis:
        if ifs[c]:
