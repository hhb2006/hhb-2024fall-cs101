from bisect import bisect


def size(s):
    num,unit = float(s[:-1]),s[-1]
    if unit == 'M':
        return num
    else:
        return 1000*num

n = int(input())
models = dict()
for _ in range(n):
    name,para = map(str,input().split('-'))
    if name in models.keys():
        sizes = [size(x) for x in models[name]]
        i = bisect(sizes,size(para))
        if i == n:
            models[name].append(para)
        else:
            models[name].insert(i,para)
    else:
        models[name] = [para]
for k in sorted(list(models.keys())):
    print(f'{k}:',', '.join(models[k]))