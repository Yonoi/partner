"5. Longest Palindromic Substring"
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_length = 0
        ans = ''

        for i in range(n - 1, -1, -1):
            for j in range(i, n, 1):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        if dp[i + 1][j - 1]:
                            dp[i][j] = True
                    if dp[i][j] and max_length <= j - i:
                        max_length = j - i
                        ans = s[i:j+1]
                    
        return ans if len(ans) != 0 else s
