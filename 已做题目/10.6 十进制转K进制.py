n,k = map(int,input().split())
m = ''
while n >= 1:
    m += str(n%k)if n%k<10 else chr(n%k+55)
    n //= k
print(m[-1::-1])
