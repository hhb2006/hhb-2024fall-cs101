n=int(input())
while n>1:
    if n % 2 == 0:
        m=n//2
        print(f'{n}/2={m}')
        n=m
    else:
        m=n*3+1
        print(f'{n}*3+1={m}')
        n=m