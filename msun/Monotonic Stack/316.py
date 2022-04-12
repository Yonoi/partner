from typing import List
from collections import Counter 
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        dict_order = Counter(s)

        for ch in s:
            if ch not in stack:
                while stack and ch < stack[-1] and dict_order[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            dict_order[ch] -= 1
        return ''.join(stack)

