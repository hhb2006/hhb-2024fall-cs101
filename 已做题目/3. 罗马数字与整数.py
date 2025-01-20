n = input()
num = [1,5,10,50,100,500,1000,4,9,40,90,400,900]
rome = ['I','V','X','L','C','D','M','IV','IX','XL','XC','CD','CM']
if n[0] in ['1','2','3','4','5','6','7','8','9']:
    m = ''
    n = int(n)
    m += 'M'*(n//1000)
    n %= 1000
    if n//100 == 4:
        m+='CD'
    elif n//100 == 9:
        m+='CM'
    elif 5 <=n//100 <= 8:
        m+='D'+'C'*(n//100-5)
    else:
        m+='C'*(n//100)
    n %= 100
    if n//10 == 4:
        m+='XL'
    elif n//10 == 9:
        m+='XC'
    elif 5 <=n//10 <= 8:
        m+='L'+'X'*(n//10-5)
    else:
        m+='X'*(n//10)
    n %= 10
    if n == 4:
        m += 'IV'
    elif n == 9:
        m += 'IX'
    elif 5 <= n <= 8:
        m += 'V' + 'I' * (n - 5)
    else:
        m += 'I' * n

else:
    m = 0
    while len(n) > 2:
        if n[0:2] in rome[7:] :
            m += num[rome.index(n[0:2])]
            n = n[2:]
        elif n[0] in rome[:7]:
            times=0
            for i in range(len(n)-1):
                if n[i]==n[0]:
                    m += num[rome.index(n[0])]
                    times += 1
                else:
                    break
            n = n[times:]
    if len(n)==2:
        if n[0:2] in rome[7:]:
            m += num[rome.index(n[0:2])]
        elif n[0] in rome[:7]:
            m += num[rome.index(n[0])]+ num[rome.index(n[1])]
    elif len(n)==1:
        m += num[rome.index(n[0])]
print(m)