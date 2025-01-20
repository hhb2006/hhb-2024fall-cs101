from  typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        stack, rain, preh = [0], 0, 0
        for i in range(1,len(height)):
            while True:
                if not stack:
                    break
                if height[stack[-1]]> height[i]:
                    rain += (height[i] - preh) * (i - stack[-1] - 1)
                    break
                pos = stack.pop()
                h = height[pos]
                rain += (i - pos - 1) * (h - preh)
                preh = h if stack else 0
            stack.append(i)
        return rain

if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))