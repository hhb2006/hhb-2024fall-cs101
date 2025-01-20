import sys

opes = sys.stdin.read().split()
pigs = []
min_w = []
for ope in opes:
    if ope == 'pop':
        if pigs:
            pigs.pop()
            min_w.pop()
    elif ope == 'min':
        if pigs:
            print(min_w[-1])
    elif ope == 'push':
        continue
    else:
        num = int(ope)
        pigs.append(num)
        min_w.append(min(min_w[-1], num) if min_w else num)