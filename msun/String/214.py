"214. Shortest Palindrome"
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rs = s[::-1]
        ans = ''

        i = 0
        while True:
            if rs[i:] == s[:n - i]:
                break
            i += 1