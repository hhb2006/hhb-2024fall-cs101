def prime(m):
    if m <= 1:
        return False
    return not any(m % k == 0 for k in range(2, int(m ** 0.5) + 1))

prime_list = []
for i in range(1000):
    if prime(i):
        prime_list.append(i)

def prime_plus(x):
    for y in prime_list:
        if x%y == 0 and y!=x:
            return False
    return True

n = int(input())
num_list = list(map(int,input().split()))
for num in num_list:
    if num == 1:
        print('NO')
    elif num**0.5 == int(num**0.5) :
        if prime_plus(int(num**0.5)):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


