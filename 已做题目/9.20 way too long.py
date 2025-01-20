n = int(input())
words=[]
for i in range(n):
    words.append(input())
for s in words:
    if len(s) > 10:
        print(f'{s[0]}{len(s)-2}{s[-1]}')
    else:
        print(s)

