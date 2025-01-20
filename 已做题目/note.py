"""
#打表  #!边界条件 #!看清题目 #!列表的同步复制机制, 深拷贝！！
注意数据类型 if hashable
'%.2f'% a  #保留两位小数
print(*c[_])
x,y,z=map(int,input().split())
money=list(map(int,input().split()))
i.isalpha()
i.islower()
import sys
from typing import List

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


for line in sys.stdin:  # 从标准输入读取每一行
    if line.strip():  # 检查行是否为空
        a, b = map(int, line.split())  # 将输入的两个数字转换为整数
        print(math.gcd(a, b))  # 计算并打印最大公约数

"""

"""
def pFactors(n):
    #Finds the prime factors of 'n'
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(int(check))
            num /= check
    if num > 1:
        pFact.append(int(num))
    return pFact

def myu(n):
    c=1
    lis=pFactors(int(n))
    for i in lis:
        ci=lis.count(i)
        if ci==2:
            break

    if ci==2:
        return 2
    else:
        return (-1)**len(list(set(lis)))

n=input()
print(pFactors(int(n)))
print(myu(n))
"""