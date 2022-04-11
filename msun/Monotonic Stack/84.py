from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        ans = 0
        heights = [0] + heights + [0]

        stack = [0]
        length += 2
        for i in range(1, length):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_weight = i - stack[-1] - 1
                ans = max(ans, cur_height * cur_weight)
            stack.append(i)
        return ans