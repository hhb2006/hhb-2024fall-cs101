m,n = map(int, input().split())
bonds = []
for i in range(n):
    love = list(map(int, input().split()))
    love.sort()
    bonds.append(int(str(love[0])+str(love[1])))
bonds = list(set(bonds))
print('Yes' if len(bonds) != n else 'No')


