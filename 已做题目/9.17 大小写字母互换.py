s=input()
for i in s:
    if 'a'<= i <= 'z':
        print(i.upper(),end='')
    elif 'A'<= i <='Z':
        print(i.lower(),end='')
    else:
        print(i,end='')
'''
s=input()
for i in s:
    
    if i.isalpha():
        if i.islower():
            print(i.upper(),end='')
        else:
            print(i.lower(),end='')
    else:
        print(i,end='')
'''
