k = int(input())
for _ in range(k):
    process,t = [],0
    n = int(input())
    for _ in range(n):
        process.append(list(map(int, input().split())))
    while len(process) > 1:
        process.sort(key=lambda x: x[0])
        last_head = process[-1]
        process.sort(key=lambda x: x[1])
        first_tail = process[0]
        if last_head[0] > first_tail[1] and last_head != first_tail:
            t += 2
        else:
            t += 1
            process = []
            break
        popped = []
        for i in range(len(process)):
            a = process[i]
            if a[0] > first_tail[1] and a[1] < last_head[0] and a!=last_head and a!=first_tail:
                popped.append(process[i])
        process = popped
    t += len(process)
    print(t)