def len_sk(k):
    k = int(k)
    l = len(str(k))
    l_sk = ((10**l) * (9*l-10) +10 + (k - 10**(l-1) + 1)*l*9) // 9
    return l_sk
def find_k(n):
    k,l = 1,1
    while True:
        k += 1
        if l + len_sk(k) >= n:
            break
        l += len_sk(k)
    return [l,k-1]

def find_digit(n):
    pos = find_k(n)
    n -= pos[0]
    bit = 0
    while True:
        if n - bit*9*10**(bit-1) < 0:
            break
        n -= bit*9*10**(bit-1)
        bit += 1
    digit = n//bit + 10**(bit-1) - 1
    return  digit

t = int(input())
for _ in range(t):
    i = int(input())
    num = find_digit(i)
    print(num)