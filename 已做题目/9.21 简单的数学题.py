'''
def is_2n(num):
    return (num&(num-1)) == 0
'''

t=int(input())
for i in range(t):
    n=int(input())
    x=0
    add=n*(n+1)//2
    while n>=2:
        n/=2
        x+=1
    print(add-2*(2**(x+1)-1))


