s = input()
ss = ''
for i in range(len(s)):
    if s[i] not in "aeiouyAEIOUY":
        ss += f'.{s[i]}'
        ss = ss.lower()
print(ss)