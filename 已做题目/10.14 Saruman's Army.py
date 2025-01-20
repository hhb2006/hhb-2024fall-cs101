while True:
    r,n = map(int, input().split())
    if r == n == -1:
        break
    troops = list(map(int, input().split()))
    troops.sort()
    groups,count,head = [],0,0

    for i in range(len(troops)-1):
        if troops[i+1] - troops[i] > r:
            tail = i+1
            groups.append(troops[head:tail])
            head = tail
    groups.append(troops[head:])
    #print(groups)
    for g in groups:
        if len(g) <= 3:
            count += 1
        else:
            i,parts,j,k = 1,[[g[0],0,0]],0,0
            while i in range(1,len(g)):
                    if g[i]-parts[j][k] > r :
                        if k == 0:
                            parts[j][k+1] = g[i-1]
                            k += 1
                        elif k == 1:
                            parts[j][k+1] = g[i-1]
                            parts.append([0,0,0])
                            j += 1
                            k = 0
                            i += 1
                            parts[j][k] = g[i]
                    i += 1
            count += len(parts)
            #print(parts)
    print(count)