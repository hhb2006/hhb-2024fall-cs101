from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack,res = [-1,0],0
        heights.append(0)
        for i in range(1,len(heights)):
            while stack[1:]:
                if heights[i] > heights[stack[-1]]:
                    break
                h = heights[stack.pop()]
                s = h*(i-stack[-1]-1)
                res = max(s,res)
            stack.append(i)
        return res

if __name__ == '__main__':
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))