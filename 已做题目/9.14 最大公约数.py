import sys
import math


for line in sys.stdin:  # 从标准输入读取每一行
    if line.strip():  # 检查行是否为空
        a, b = map(int, line.split())  # 将输入的两个数字转换为整数
        print(math.gcd(a, b))  # 计算并打印最大公约数



