n = int(input())
for i in range(n):
    num = 0
    s = int(input())
    len_a = int(input())
    a = list(map(int, input().split()))
    len_b = int(input())
    b = list(map(int, input().split()))
    for j in range(len_b):
        num += a.count(s-b[j])
    print(num)