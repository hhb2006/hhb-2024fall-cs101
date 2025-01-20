num = input()
length,l = 1,1
for i in range(len(num)-1):
    if num[i] != num[i+1]:
        l += 1
    else:
        length = max(length,l)
        l = 1
length = max(length,l)
print(length)