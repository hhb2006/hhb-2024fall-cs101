n, k = map(int, input().split())
t = list(map(int, input().split()))
t.sort(reverse = True)
total_time,p = sum(t),k

for i in range(n):
    if t[i] > total_time/p:
        total_time -= t[i]
        p -= 1
    else:
        break

print(f"{total_time/p:.3f}")