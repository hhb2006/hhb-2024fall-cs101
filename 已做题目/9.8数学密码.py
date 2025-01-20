input()
q=0
for i in range(int(input())):
    for j in range(i-1,int(input())):
        for k in range(j-1,int(input())):
            for n in range(i):
                if n%i==0 and n%j==0 and n%k==0 and n>q:
                    q=n
print(q)