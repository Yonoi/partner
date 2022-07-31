"647. Palindromic Substrings"
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if s[i] == s[j]:
                    if j - i <= 1:
                        ans += 1
                        dp[i][j] = True
                    else:
                        if dp[i+1][j-1]:
                            ans += 1
                            dp[i][j] = True
        return ans