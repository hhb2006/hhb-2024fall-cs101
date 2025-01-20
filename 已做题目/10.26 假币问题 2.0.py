def operate(left_c, right_c, result, real_c):
    l,r,suspect_l,suspect_r = 0,0,[],[]
    for c in left_c:
        if c not in real_c:
            l += 1
            suspect_l.append(c)
    for c in suspect_l:
        coins[c] += 1 if result == 'up' else -1
    for c in right_c:
        if c not in real_c:
            l += 1
            suspect_r.append(c)
    for c in suspect_r:
        coins[c] -= 1 if result == 'up' else -1
    return


n = int(input())
for _ in range(n):
    uneven, real_coins, fake_coins, coins = [], [], [], dict()
    for x in 'ABCDEFGHIJKL':
        coins[x] = 0
    for _ in range(3):
        left, right, res = map(str, input().split())
        left_coins = [x for x in left]
        right_coins = [x for x in right]
        if res == 'even':
            even_coins = left_coins + right_coins
            real_coins.extend(even_coins)
            for x in even_coins:
                coins[x] = 0
        else:
            uneven.append((left_coins, right_coins, res))

    for event in uneven:
        operate(event[0], event[1], event[2], real_coins)
    sorted_coins = list(sorted(coins.items(), key=lambda item: abs(item[1]),reverse = True))
    status = 'light' if sorted_coins[0][1] < 0 else 'heavy'
    print(f'{sorted_coins[0][0]} is the counterfeit coin and it is {status}.')