d = int(input())
n = int(input())
bombs = {}
for _ in range(n):
    x,y,i = map(int,input().split())
    for j in range(max(0,x-d),min(1025,x+d+1)):
        for k in range(max(0,y-d),min(1025,y+d+1)):
                if (j,k) not in bombs.keys():
                    bombs[(j,k)] = i
                else:
                    bombs[(j,k)] += i
cleanup = list(bombs.values())
cleanup.sort(reverse=True)
print(cleanup.count(cleanup[0]),cleanup[0])
