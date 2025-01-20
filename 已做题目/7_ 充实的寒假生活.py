def select(lis,tail):
    new_lis = []
    for x in lis:
        if x[0] > tail:
            new_lis.append(x)
    return new_lis
n = int(input())
l,events,num = 61,[],0
for _ in range(n):
    start,end = map(int,input().split())
    if end <= 60:
        events.append([start,end])
while events:
    num += 1
    events.sort(key=lambda x: x[1])
    event = events[0]
    events = select(events,event[1])
print(num)