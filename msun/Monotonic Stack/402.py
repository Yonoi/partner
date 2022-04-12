from typing import List
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remainer = len(num) - k
        for s in num:
            while stack and stack[-1] > s and k:
                stack.pop()
                k -= 1
            stack.append(s)
        return ''.join(stack[:remainer]).lstrip('0') or '0'