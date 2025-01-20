def arrange(i):
    if i == 1:
        return [str(i)]
    else:
        arrange(i-1)
        all_s = [s[:j]+str(i)+s[j:] for j in range(i) for s in arrange(i-1)]
    return all_s

n = int(input())
a = arrange(n)
a.sort(key = lambda x: int(x))
for s in a:
    print(' '.join(s))