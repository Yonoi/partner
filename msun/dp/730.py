"730. Count Different Palindromic Subsequences"
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp[i][j] = [[0] * n for _ in range(n)]
        ans = 0

        # init_state
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1]

        ans = dp[0][n-1]
        return ans % int(10**9 + 7)