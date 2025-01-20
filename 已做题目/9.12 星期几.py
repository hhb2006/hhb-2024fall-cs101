n=int(input())
week=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for i in range(n):
    s=input()
    cy=int(s[0:4])
    c=int(s[0:2])
    y=int(s[2:4])
    m=int(s[4:6])
    if m==1 or m==2:
        m+=12
        cy-=1
        c=int(cy//100)
        y=int(cy%100)
    d=int(s[6:8])
    w=int((y+(y//4)+(c//4)-2*c+(26*(m+1))//10+d-1)%7)
    print(week[w])