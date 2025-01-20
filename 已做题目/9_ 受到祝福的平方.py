import math

def is_square_number1(x):
    if not x :
        return False
    sqrt_x = math.sqrt(x)
    return sqrt_x.is_integer()

def dfs(x,a):
    blessed = 0
    if x == len(a):
        return 1
    for i in range(x+1,len(a)+1):
        if is_square_number1(int(a[x:i])):
            b = dfs(i,a)
            blessed += b
    return blessed

a = str(input())
res = dfs(0,a)
print('Yes' if res else 'No')