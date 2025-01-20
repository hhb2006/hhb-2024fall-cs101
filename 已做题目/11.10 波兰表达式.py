def operate(lis):
    node = lis.pop(0)
    try:
        node = float(node)
        return node
    except ValueError:
        node_left = operate(lis)
        node_right = operate(lis)
        if node == '+':
            return node_left + node_right
        elif node == '-':
            return node_left - node_right
        elif node == '*':
            return node_left * node_right
        elif node == '/':
            return node_left / node_right

s = list(map(str, input().split()))
print('%f'% operate(s))