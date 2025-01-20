class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, n, res = 0, s != '', len(s), 0
        while True:
            if j == n :
                break
            ss = s[i:j]
            if s[j] in ss:
                res = max(res, j-i)
                i = ss.find(s[j])+i+1
            j += 1
        res = max(res, j-i)
        return res

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(input()))