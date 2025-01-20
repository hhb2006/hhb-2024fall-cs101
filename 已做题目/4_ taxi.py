n = int(input())
kids = list(map(int, input().split()))
kids.sort()
c1,c2,c3,c4 = kids.count(1), kids.count(2), kids.count(3), kids.count(4)
cars = c4 + c3 + c2//2 + c2%2
if c1 > c3 + (c2%2)*2 :
    left = c1 - c3 - (c2%2)*2
    cars += left//4 + (left%4 != 0)
print(cars)