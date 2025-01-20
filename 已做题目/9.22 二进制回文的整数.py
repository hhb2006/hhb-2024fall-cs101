x = int(input())
y = bin(x)[2:]
if y == y[::-1]:
    print('Yes')
else:
    print('No')