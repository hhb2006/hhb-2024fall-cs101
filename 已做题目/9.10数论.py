def pFactors(n):
    #Finds the prime factors of 'n'
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(int(check))
            num /= check
    if num > 1:
        pFact.append(int(num))
    return pFact

def myu(n):
    c=1
    lis=pFactors(int(n))
    for i in lis:
        ci=lis.count(i)
        if ci==2:
            break

    if ci==2:
        return 2
    else:
        if len(list(set(lis)))%2==0:
            return 1
        else:
            return -1
n=input()
print(pFactors(int(n)))
print(myu(n))