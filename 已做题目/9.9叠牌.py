while True:
    s=input()
    set_len=float(s)
    if(set_len==0.00):
        break
    real_len = 0
    i = 2
    num = 0
    while real_len < set_len:  # 当实际长度小于设定长度时，继续叠牌
        real_len += 1 / i
        i += 1
        num += 1
    out=str(num)+' card(s)'
    print(out)

