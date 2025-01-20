def prime(m):
    if m <= 1:
        return False
    return not any(m % k == 0 for k in range(2, int(m ** 0.5) + 1))
prime_list = []
for i in range(1000):
    if prime(i):
        prime_list.append(i)
def is_prime(x):
    for y in prime_list:
        if x%y == 0 and y!=x:
            return False
    return True
s = int(input())
if s%2 == 0:
    for i in range(s//2,2,-1):
        if is_prime(i) and is_prime(s-i):
            print(i*(s-i))
            break
else:
    print(2*(s-2))