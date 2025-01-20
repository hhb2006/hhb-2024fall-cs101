t = int(input())
for _ in range(t):
    n = int(input())
    dishes = []
    deliver = list(map(int, input().split()))
    pick = list(map(int, input().split()))
    pickup = sum(pick)
    for _ in range(n):
        dishes.append((deliver[_], pick[_]))
    if pickup <=  min(deliver):
        print(sum(pick))
    #elif max(deliver) <= min(pick):        print(max(deliver))
    else:
        printed = False
        dishes.sort(key = lambda x: x[0])
        time = pickup
        for i in range(n):
            pickup -= dishes[i][1]
            if max(dishes[i][0], pickup) >= time:
                print(time)
                printed = True
                break
            else:
                time = max(dishes[i][0], pickup)
        if not printed:
            print(time)

