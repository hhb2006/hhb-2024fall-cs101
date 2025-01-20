#二维布尔数组（/打表）
n,q = map(int,input().split())
bonds = {}
for _ in range(1,n+1):
    bonds[_] = []
for _ in range(q):
    a,b = map(int,input().split())
    bonds[a].append(b)
for i in range(1,len(bonds)+1):
    for j in bonds[i]:
        for k in bonds[j]:
            if i in bonds[k]:
                print('Yes')
                exit()
print('No')
'''
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    
    exists = [[False] * (n + 1) for _ in range(n + 1)]  # 初始化喜欢关系矩阵
    result = False  # 是否存在三方欢喜
    
    index = 2
    for _ in range(q):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        exists[a][b] = True  # 记录a喜欢b
        
        for c in range(1, n + 1):  # 遍历所有可能的c
            if c != a and c != b and exists[b][c] and exists[c][a]:  # 检查是否存在三方欢喜
                result = True
                break
    
    print("Yes" if result else "No")

if __name__ == "__main__":
    main()
    '''
