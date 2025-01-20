turn=int(input())
all=[]
add=0
for i in range(turn):
    all.append(list(map(int,input().split())))
for each in all:
    if each[1]+each[2]+each[0]>1:
        add+=1
print(add)