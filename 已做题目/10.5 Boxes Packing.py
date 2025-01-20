n = int(input())
a = list(map(int, input().split()))
b = list(set(a))
num = 0
for i in b:
    if a.count(i) > num:
        num = a.count(i)
print(num)