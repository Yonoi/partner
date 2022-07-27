from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        res = [-1, -1]

        for x in intervals:
            if x[0] <= res[-2]:
                continue
            if x[0] > res[-1]:
                res.append(x[1])
        
        return len(res) - 2
