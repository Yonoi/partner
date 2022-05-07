# 433. Minimum Genetic Mutation
from typing import List
from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            if end in bank:
                return 0
            else:
                return -1
        bank = set(bank)
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            for i, x in enumerate(cur):
                for y in "AGCT":
                    if y != x:
                        nxt = cur[:i] + y + cur[i+1:]
                        if nxt in bank:
                            if nxt == end:
                                return step + 1
                            bank.remove(nxt)
                            q.append((nxt, step + 1))
        return -1
        