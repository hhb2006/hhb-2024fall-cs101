def vert(i,lis):
    new_lis=[int(lis[i]),int(0-int(lis[i]))]
    return new_lis

def cal(lis):
    count=0
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    if vert(0,lis)[a]+vert(1,lis)[b]+vert(2,lis)[c]+vert(3,lis)[d]==24:
                        count+=1
    if count==0:
        return 'NO'
    else:
        return 'YES'

lis=[]
num_lis=[]
num=''
count=input()
u=0
for x in range(int(count)):
    s=input()
    s+=' '
    lis.append(str(s))
for group in lis:
    for y in range(len(group)) :
        if group[y]==' ':
            for z in range(u,y):
                num+=group[z]
            num_lis.append(int(num))
            u=y+1
            num=''
    print(cal(num_lis))
    u=0
    num_lis=[]

