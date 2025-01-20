n = int(input())
a = 0
for i in range(n,0,-1):
    for j in range(n,0,-1):
        for k in range(n,0,-1):
            if (i+j+k)%5 == 0 and (i+j)%3 == 0 and (j+k)%2 == 0 and i+j+k > a:
                a = i+j+k
print(a)