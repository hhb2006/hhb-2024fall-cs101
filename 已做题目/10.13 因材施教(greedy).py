n,m = map(int,input().split())
stu = list(map(int,input().split()))
stu.sort()
gap,part,dif = [],[0],0

for i in range(len(stu)-1):
    gap.append([i,stu[i+1]-stu[i]])
gap.sort(key=lambda x:x[1],reverse = True)

for i in range(m-1):
    part.append(gap[i][0])
    part.append(gap[i][0]+1)
part.sort()
part.append(len(stu)-1)

for i in range(0,len(part),2):
    if part[i+1]-part[i] != 0:
        dif += (stu[part[i+1]]-stu[part[i]])
print(dif)