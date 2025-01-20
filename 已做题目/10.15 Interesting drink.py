n = int(input())
prices = list(map(int, input().split()))
q = int(input())
coins = [int(input()) for _ in range(q)]
prices.sort()
for coin in coins:
    if coin >= prices[-1]:
        print(n)
    elif coin < prices[0]:
        print(0)
    else:
        i, head, tail = (n-1)//2, 0, n-1
        while tail-head > 1:
            #print(i, head, tail,coin)
            if coin >= prices[i]:
                head = i
            else:
                tail = i
            i = (head+tail)//2
        print(i+1)
'''
n = int(input())
prices = list(map(int, input().split()))
q = int(input())
coins = [int(input()) for _ in range(q)]
prices.sort()
for coin in coins:
    if coin >= prices[-1]:
        print(n)
    elif coin < prices[0]:
        print(0)
    else:
        head, tail =  0, n-1
        while head < tail:
            i = (head + tail) // 2
            if prices[i] <= coin:
                head = i + 1
            else:
                tail = i
        print(head)
'''