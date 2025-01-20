n = int(input())
for i in range(n):
    t = 0
    a, b = map(int, input().split())
    t += (b-(a % b))*(a % b != 0)
    print(t)


