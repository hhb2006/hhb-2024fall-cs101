n = int(input())
pell = [1,2]
for i in range(1000000):
    ai = pell[-2] + 2 * pell[-1]
    pell.append(ai)
print(pell[-1])
#for _ in range(n):
