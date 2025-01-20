def spellable(s,x,used_lis):
    if x ==len(s):
        return 1
    res = 0
    for i in range(4):
        if i not in used_lis and s[x] in blocks[i]:
            used_lis.append(i)
            res += spellable(s,x+1,used_lis)
            used_lis.pop()
    return res

n = int(input())
blocks = []
for _ in range(4):
    blocks.append(set(list(input())))
for _ in range(n):
    ans = spellable(input(),0,blocks)
    print('YES' if ans else 'NO')