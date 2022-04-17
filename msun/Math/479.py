# 479. Largest Palindrome Product
class Solution:
    def largestPalindrome(self, n: int) -> int:
        modulo = 1337

        ans = 0
        if n == 1:
            return 9
        upper = 10 ** n - 1

        for left in range(upper, upper // 10, -1):
            p, x = left, left
            while x:
                p = p * 10 + x % 10
                x = x // 10
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % modulo
                x -= 1


        return ans % modulo