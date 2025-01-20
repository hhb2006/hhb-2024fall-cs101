a,b = map(int,input().split())
s = ''
for i in range(a,b+1):
    if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
        s+=str(i)+' '
if s=='':
    print('NO')
else:
    print(s[:-1])
