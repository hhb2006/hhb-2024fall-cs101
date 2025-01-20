ox=list(map(int,input().split()))
ox.sort()
a,b,c=ox[0],ox[1],ox[2]
distance=abs(a-b)+abs(a-c)+abs(b-c)
for i in range(a,c+1):
    far=abs(i-a)+abs(i-b)+abs(i-c)
    distance=min(distance,far)
print(distance)