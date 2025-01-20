def win(a, b):
    if a//b >= 2 or a%b == 0:
        return 1
    else:
        return 1 - win(b, a - b)

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    m, n = max(m, n), min(m, n)
    if win(m, n):
        print("win")
    else:
        print("lose")