n = int(input())
a = list(map(int, input().split())) #所有事件的列表
crime_list =[]  #所有的位置
crime_left = 0
#crime_all = a.count(-1)
for i in range(n):
    crime_left += a[i]
    crime_list.append(crime_left)
crime_list.sort()
if crime_list[0] <= 0:
    print(abs(crime_list[0]))
else:
    print(0)
