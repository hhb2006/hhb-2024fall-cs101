h = int(input())
m = int(input())
sc,progress = [],0
h = h*2 - m*0.5
for _ in range(m):
    s, c = map(float, input().split())#复习一门课程一小时预计提高的分数s和该课程的学分c
    #progress += 0.5*s*c
    sc.append([s, c])
sc.sort(key=lambda x: x[0]*x[1], reverse=True)
for subject in sc:
    if h >= 5/subject[0]:
        h -= 5/subject[0]
        progress += subject[1]*5
    else:
        progress += subject[1]*h*subject[0]
        break
print("%.1f" % progress)