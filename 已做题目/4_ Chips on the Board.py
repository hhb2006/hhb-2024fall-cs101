t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_min,b_min,a_sum,b_sum = min(a),min(b),sum(a),sum(b)
    print(min(a_min*n+b_sum,b_min*n+a_sum))