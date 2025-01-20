nCases = int(input())
for _ in range(nCases):
    n, m, b = map(int, input().split())  # n代表技能的个数，m代表每一时刻可以使用最多m个技能，b代表怪兽初始的血量
    skills, time, t_max = [], [], 1
    for _ in range(n):
        t, x = map(int, input().split())
        skills.append([t, x])
        time.append(t)
        time = sorted(list(set(time)))
        skills.sort(key=lambda x: x[1],reverse=True)

    dic = {}
    for i in range(len(time)):
        dic[time[i]], turn = 0, 0
        for j in range(n):
            if skills[j][0] == time[i] and turn < m:
                dic[time[i]] += skills[j][1]
                turn += 1
            if turn >= m:
                break
    kill = 0
    for x in time:
        b -= dic[x]
        if b <= 0:
            print(x)
            break
    else:
        print('alive')