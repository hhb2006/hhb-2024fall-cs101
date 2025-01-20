n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse = True)
all_value,my_value = sum(coins), 0
for i in range(n):
    my_value += coins[i]
    if my_value > all_value - my_value:
        print(i + 1)
        break
