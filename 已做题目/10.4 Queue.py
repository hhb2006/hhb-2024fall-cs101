n = int(input())
queue = list(map(int,input().split()))
queue.sort()
time,num = 0,0
for i in range(n):
    if queue[i] >= time:
        time += queue[i]
        num += 1
    else:
        queue.append(queue[i])
print(num)
