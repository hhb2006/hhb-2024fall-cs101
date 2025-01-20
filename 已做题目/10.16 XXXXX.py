t = int(input())    #如果a可以通过从开头删除几个（可能为零或全部）元素和从末尾删除几个（可能为零或全部）元素来获得b，则数组 b 是数组 a 的子数组。
for _ in range(t):
    n, x = map(int, input().split())
    num = list(map(int, input().split()))
    add = sum(num)
    if add % x != 0:
        print(n)
    else:
        mod = [k % x for k in num]
        if set(mod) == {0}:
            print(-1)
        else:
            left, right = 0, n - 1
            while left < right:
                if mod[left] == mod[right] == 0:
                    left += 1
                    right -= 1
                else:
                    break
            print(n-left-1)