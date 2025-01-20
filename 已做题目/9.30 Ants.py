case = int(input())
for i in range(case):
    t_max = 0
    l,n = map(int,input().split())
    ants = list(map(int,input().split()))
    ants.sort(key=lambda x:abs(x-l/2))
    t_min = abs(ants[0]-l)

    print(t_min,t_max)