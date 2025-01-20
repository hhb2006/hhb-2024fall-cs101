num=input()
a,b,c=0,0,0
for i in num:
    if i != '4' and i != '7':
        a+=1
if a == 0:
    print('YES')
else:
    luckynum=[]
    for u in range(4,int(num)):
        for v in range(len(str(u))):
            if str(u)[v] != '4' and str(u)[v] != '7':
                b+=1
        if b == 0:
            luckynum.append(u)
        else:
            b=0
    for x in luckynum:
        if int(num)%x == 0:
            c+=1
    if c == 0:
        print('NO')
    else:
        print('YES')


