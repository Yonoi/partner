class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp0, dp1, dp2 = 1, 10, 0
        if n == 0:
            return dp0
        if n == 1:
            return dp1
        
        for i in range(2, n):
            dp2 = dp1 + (dp1 - dp0) * (11 - i)
            dp1, dp0 = dp2, dp1
        
        return dp2