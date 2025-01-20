def compute_f(k):
    total = 0
    d = 1
    while True:
        L = max(1, 10**(d-1))
        R = min(k, 10**d -1)
        if L > R:
            break
        count = R - L +1
        sum_n = (R * (R +1)) //2 - ((L-1)*L)//2
        total += d * ((k+1)*count - sum_n)
        d +=1
    return total

def find_k(i):
    low =1
    high = 1000000  # sufficiently high
    while low < high:
        mid = (low + high)//2
        f = compute_f(mid)
        if f >=i:
            high = mid
        else:
            low = mid +1
    return low

def find_digit_in_sk(k, pos):
    d =1
    while True:
        L = max(1, 10**(d-1))
        R = min(k, 10**d -1)
        if L > R:
            break
        count = R - L +1
        total_digits = count *d
        if pos <= total_digits:
            num_index = (pos-1) //d
            digit_index = (pos-1) %d
            number = L + num_index
            return str(number)[digit_index]
        pos -= total_digits
        d +=1
    return '0'  # default, should not reach here

'''
import sys
import sys
t_and_cases = sys.stdin.read().split()
t = int(t_and_cases[0])
cases = list(map(int, t_and_cases[1:t+1]))
'''
t = int(input())
for _ in range(t):
    i = int(input())
    k = find_k(i)
    f_k_minus_1 = compute_f(k-1)
    pos = i - f_k_minus_1
    digit = find_digit_in_sk(k, pos)
    print(digit)

'''
def bit(m):
    m,bits = int(m),0
    for k in range(1,m+1):
        for j in range(1, len(str(k))):
            bits += (10 ** j - 1) * j
        bits += (k-10**(len(str(k))-1)+1)*len(str(k))
    return bits

def decide_bit(m):
    m, bits,k,b = int(m), 0 ,1,0
    while bits < m:
        b = bits
        bits += k*9*len(str(k))
        k *= 10
    return [len(str(k))-1,b]

t = int(input())
s,x,max_x,bit_dic = '',1,1,{1:1}
for _ in range(t):
    n = int(input())
    if n > bit_dic[max_x]:
        while bit_dic[max_x] < n:
            max_x += 1
            bit_dic[max_x] = bit(max_x)
        x = max_x
    else:
        for i in range(1, max_x + 1):
            if bit_dic[i] >= n:
                x = i
                break
    if n == bit_dic[x]:
        print(x)
    else:
        r = n - bit_dic[x-1]
        db = decide_bit(r)
        num = (r-db[1])//db[0] + 10**db[0]
        print(str(num)[(r-db[1])%db[0]-1])
'''
