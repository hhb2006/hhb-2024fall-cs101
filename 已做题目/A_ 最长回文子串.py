class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        if len(s) == 1:
            return s
        res = ''
        for i in range(len(s)):
            odd = expand(s, i, i)
            if i < len(s)-1:
                even = expand(s, i, i+1) if s[i] == s[i+1] else ''
            else:
                even = ''
            res = odd if len(odd) > len(res) else res
            res = even if len(even) > len(res) else res
        return res

if __name__ == '__main__':
    s = input()
    print(Solution().longestPalindrome(s))
