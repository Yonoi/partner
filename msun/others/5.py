class Solution:
    def longestPalindrome(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch in stack: