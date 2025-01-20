x=0
n=int(input())
for i in range(n):
    operation=input()
    if '++' in operation:
        x+=1
    elif '--' in operation:
        x-=1
print(x)