q = int(input())
for _ in range(q):
    n = int(input())
    multiset = (list(map(int, input().split())))
    multiset.sort()
    if multiset.count(2048) :
        print('YES')
    elif sum(multiset) < 2048:
        print('NO')
    elif len(multiset) == len(set(list(multiset))):
        print('NO')
    else:
        for i in range(0,11):
            for j in range(multiset.count(2**i)//2):
                multiset.append(2**(i+1))
                #multiset.remove(2**i)
        if multiset.count(2048) :
            print('YES')
        else:
            print('NO')