def judge_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
n=int(input())
if n%2!=0 or n<6 :
    print('Error!')
else:
    for i in range(2,n//2+1):
        if judge_prime(i) and judge_prime(n-i):
            s=str(n)+'='+str(i)+'+'+str(n-i)
            print(s)