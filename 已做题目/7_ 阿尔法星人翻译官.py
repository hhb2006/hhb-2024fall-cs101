alpha = ('zero, one, two, three, four, five, six, seven, eight, nine, '
         'ten, eleven, twelve, thirteen, fourteen, fifteen, '
         'sixteen, seventeen, eighteen, nineteen, twenty, '
         ' thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred').split(', ')
dic = {}
for i in range(21):
    dic[alpha[i]] = i
for i in range(30, 101, 10):
    dic[alpha[i//10+18]] = i
dic['thousand'],dic['million'] = 1000, 1000000

num_list = list(map(str,input().split()))
if num_list[0] == 'negative':
    print('-',end = '')
    num_list = num_list[1:]
n,a,h,t,m = 0,0,0,0,0
for i in num_list:
    if dic[i] < 100:
        a += dic[i]
    elif dic[i] == 100:
        h = a*100
        a = 0
    elif dic[i] == 1000:
        t = (h+a)*1000
        h,a = 0,0
    else:
        m = (t+h+a)*1000000
        t,h,a = 0,0,0
n = m+t+h+a
print(n)