import bisect
def cost(dic):
    total= sum(dic.values())
    total -= (total//300) * 50
    for i in range(m):
        if dic[i] > 0 and discount[i]:
            x = bisect.bisect(keys[i], dic[i])
            if x > 0:
                minus = max(discount[i][keys[i][k]] for k in range(0,x))
                total -= minus
    return total

def buy(x): # buy Item x+1
    global res
    if x == n :
        res = min(res, cost(record))
        #print(res,record,cost(record))
        return
    for i in range(m):
        if prices[i][x] > 0:
            record[i] += prices[i][x]
            buy(x+1)
            record[i] -= prices[i][x]
    return

n, m = map(int, input().split())  # n items , m stores
res = float('inf')
record = {i: 0 for i in range(m)}
prices = [[0 for _ in range(n)] for _ in range(m)]
#  prices[i][j] :  Store i+1 , Item j+1
discount = [{} for _ in range(m)]
keys = [[] for _ in range(m)]
for t in range(n):
    lis = list(map(str, input().split()))
    for l in lis:
        a, b = map(int, l.split(':'))
        prices[a - 1][t] = b
for t in range(m):
    lis = list(map(str, input().split()))
    for l in lis:
        a, b = map(int, l.split('-'))
        discount[t][a] = b  # a-b
        keys[t].append(a)

#print(prices)
#print(discount,keys)
buy(0)
print(res)