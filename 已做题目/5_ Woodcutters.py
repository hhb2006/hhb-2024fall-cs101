n = int(input())
trees,occupied,fallen = [],[],1+(n>1)
for _ in range(n):
  tree = list(map(int, input().split()))
  occupied.append([tree[0]])
  trees.append(tree)  # 第 z 棵树的坐标和高度
trees.sort(key=lambda x: x[0])  # 按照坐标排序
for i in range(1,n-1):
    if trees[i][0] - occupied[i-1][-1] > trees[i][1]: #可以向左倒
        fallen += 1
    elif trees[i+1][0] - trees[i][0] > trees[i][1]: #可以向右倒
        fallen += 1
        occupied[i].append(trees[i][0]+trees[i][1])
print(fallen)