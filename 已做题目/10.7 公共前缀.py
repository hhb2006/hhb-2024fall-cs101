n = int(input())
strs = []
for i in range(n):
    strs.append(input())
def f(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    else:
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]
print(f(strs))