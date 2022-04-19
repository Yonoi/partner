# 821. Shortest Distance to a Character
from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        location = []

        for idx, ch in enumerate(s):
            if ch == c:
                location.append(idx)

        for idx in range(n):
            ans[idx] = min([abs(each - idx) for each in location])
        
        return ans