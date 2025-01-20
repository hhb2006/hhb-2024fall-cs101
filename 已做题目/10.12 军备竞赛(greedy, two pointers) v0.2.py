def max_weapon_diff(p, costs):
    costs.sort()  # 按成本从小到大排序
    n = len(costs)
    left, right = 0, n - 1
    my_weapons = 0
    enemy_weapons = 0

    while left <= right:
        if p >= costs[left]:
            # 如果当前经费足够制作最便宜的武器，则制作
            p -= costs[left]
            my_weapons += 1
            left += 1
        else:
            # 如果经费不够制作最便宜的武器，尝试卖掉最贵的武器
            if right > left and my_weapons > enemy_weapons:
                p += costs[right]
                enemy_weapons += 1
                right -= 1
            else:
                break

    return my_weapons - enemy_weapons

p = int(input())
prices = (list(map(int, input().split())))
print(max_weapon_diff(p, prices))

'''
p = int(input())
prices = (list(map(int, input().split())))
prices.sort()
buy,sell,go= 0,0,1
while len(prices) > 0 and go:
    while p >= prices[0]:
        p -= prices[0]
        prices.pop(0)
        buy += 1
        #print(prices,p,buy,sell)
    go = 0
    # 买得起的都买完了
    if len(prices) > 2 and buy > sell:
        #print(1)
        n = len(prices)
        n1 = min((len(prices)-1)//2,buy-sell)
        cost,reap,go =prices[0],p,0
        for i in range(n1):
            cost += prices[i+1]
            reap += prices[-i-1]
            #print(2,cost,reap)
            if cost <= reap:
                sell += (i+1)
                buy += (i+2)
                p = (reap-cost)
                if 2 * (i + 1) + 1 == n:
                    prices = []
                else:
                    prices = prices[i + 2:n - i]
                go = 1
                #print(prices, p, buy, sell, '/')
                break

    else:
        break
print(buy-sell)
'''