'''days1 = {'1':30,'2':28, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
days2 = {'1':30,'2':29, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31, '9':30, '10':31, '11':30, '12':31}
Y,M,D = map(int,input().split('-'))
if (y%4==0 and y%100!=0) or y%400==0 and y%3200!=0:
    year=1  #闰年
else:
    year=0'''
from datetime import datetime, timedelta

date_input = input().strip('-')
days_to_add = int(input())
date_object = datetime.strptime(date_input, "%Y-%m-%d")
new_date_object = date_object + timedelta(days=days_to_add)
print(new_date_object.strftime("%Y-%m-%d"))

