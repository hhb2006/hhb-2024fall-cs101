n = int(input())
print(2**n-1)
def hanoi(t, a, b, c):
    if t == 1:
        print(a+'->'+c)
    else:
        hanoi(t - 1, a, c, b)
        print(a+'->'+c)
        hanoi(t - 1, b, a, c)
hanoi(n, 'A', 'B', 'C')