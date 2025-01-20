n=int(input())
present,others=[],[]
absent,addition='',''
kids = list(map(int,input().split()))
for i in kids:
    if i in range(1,n+1):
        present.append(i)
for i in range(1,n+1):
    if i not in present:
        absent+=str(i)+' '
print(absent[:-1])
for i in kids:
    if i not in range(1,n+1):
        others.append(i)
        others.sort()
for i in others:
    addition+=str(i)+' '
print(addition[:-1])