s = input()
n = len(s)
m = 0
while n >= 2:
    n /= 2
    m += 1
l,r = 0,m
ns = ''
while l < r:
    ns += s[2**l-1]+s[2**r-1]
    l += 1
    r -= 1
if l == r:
    ns += s[2**l-1]
print(ns)