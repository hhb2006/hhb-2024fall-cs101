n = int(input())
stu = list(map(int, input().split()))
for i in range(n):
    stu[i] = [stu[i], str(i+1)]
stu.sort(key = lambda x: x[0])
for i in range(1,n):
    stu[i].append(sum(map(lambda x: x[0], stu[:i])))
print(' '.join(stu[i][1] for i in range(n)))
print("{:.2f}".format(sum(stu[i][2] for i in range(1,n))/n))