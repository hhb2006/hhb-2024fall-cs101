class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1,l2 = len(text1),len(text2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        #for x in dp:
        #    print(x)
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence("abcde","ace")) #3