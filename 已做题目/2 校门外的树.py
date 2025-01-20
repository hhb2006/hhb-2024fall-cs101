l,m = map(int,input().split())
trees = l+1
metro = []
for i in range(m):
    head,tail = map(int,input().split())
    metro.append({'head':head,'tail':tail})
metro.sort(key=lambda x:x['head'])
trees -= (metro[0]['tail']-metro[0]['head']+1)
for i in range(1,m):
    if metro[i-1]['tail'] < metro[i]['head'] :
        trees -= (metro[i]['tail']-metro[i]['head']+1)
    elif metro[i-1]['tail'] < metro[i]['tail']:
        trees -= (metro[i]['tail']-metro[i-1]['tail'])
    else:
        metro[i]['tail']=metro[i-1]['tail']
print(trees)

