import math
t_list = []
d = 4.5 * 3600
while True:
    n = int(input())
    if n == 0:
        break

    riders = []
    for _ in range(n):
        v, t = map(int, input().split())

        if t >= 0:
            arrival_time = t + d / v
            riders.append((v, t, arrival_time))

    riders.sort(key=lambda x: x[2])

    v0, t0, _ = riders[0]
    t = riders[0][2]

    for i in range(1, len(riders)):
        vi, ti, arrival_time = riders[i]
        if vi > v0 and arrival_time < t:
            v0 = vi
            t = arrival_time

    t_list.append(math.ceil(t))
for i in t_list:
    print(i)

'''import math
d = 4.5*3600 #总折合里程数
t_list = []
while True:
    n = int(input())
    if n != 0:
        riders = []
        s, t = 0, 0
        for i in range(n):
            v,time = map(int,input().split('\t'))
            #riders.append({'v':v,'t':t})
            if time >= 0:
                riders.append({'v':v,'t':time})
        #riders.sort(key=lambda x:x['t'])
        riders.sort(key=lambda x:x['t'])
        v0 = riders[0]['v']
        riders = list(filter(lambda x:x['v'] > v0,riders))
        if riders :
            a = 1
            riders.sort(key=lambda x:x['t']*v0/(x['v']-v0))
            t0 = riders[0]['t']*v0/(riders[0]['v']-v0)+riders[0]['t']
        else:
            t0 = (d-s)/v0
            a = 0

        while s+t0*v0 < d and a:
            s += t0*v0
            t += t0
            v0 = riders[0]['v']
            riders = list(filter(lambda x:x['v'] > v0,riders))
            if riders :
                riders.sort(key = lambda x: x['t'] * v0 / (x['v'] - v0))
                t0 = riders[0]['t']*v0/(riders[0]['v']-v0)-t
            else:
                t0 = (d-s)/v0
                break
        t += (d-s)/v0
        t_list.append(math.ceil(t))
    else:
        break
for i in t_list:
    print(i)
'''
