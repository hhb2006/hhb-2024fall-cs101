n = 1
while True:
    p,e,i,d = map(int,input().split())
    if p==-1 and e==-1 and i==-1 and d==-1:
        exit()
    for day in range(1,21253):
        if (day+d-p)%23==0 and (day+d-e)%28==0 and (day+d-i)%33==0:
            print(f'Case {n}: the next triple peak occurs in {day} days.')
            break
    n+=1
