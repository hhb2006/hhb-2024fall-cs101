n,w = map(int,input().split())
v = 0
values = []
weight = []
v_and_w =  []
for i in range(n):
    a,b = map(int,input().split())
    c = a/b
    values.append(a)
    weight.append(b)
    v_and_w.append({'values':a,'weight':b,'value_per_weight':c})
v_and_w.sort(key=lambda x:x['value_per_weight'],reverse=True)
for i in range(n):
    if w > 0:
        if w >= v_and_w[i]['weight']:
            w -= v_and_w[i]['weight']
            v += v_and_w[i]['values']
        else:
            v += v_and_w[i]['values'] * w / v_and_w[i]['weight']
            w = 0
v=round(float(v),1)
print(v)

